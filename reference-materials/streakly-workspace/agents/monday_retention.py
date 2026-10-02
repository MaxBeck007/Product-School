#!/usr/bin/env python3
"""Monday Retention Digest, Streakly.

Spec: agents/monday-retention.md

Reads the five Streakly CSVs from data/raw/ with DuckDB and prints a
three-part Slack digest: one headline number, one signal to watch, one
suggested action.

Design rules this script follows deliberately:
  * If a source file is missing, it exits non-zero and names the file. It
    never estimates, interpolates, or reports a partial number.
  * Deltas inside +/-3 percentage points are reported as "no meaningful
    change", not as a direction. Arm sizes are ~50/variant.
  * It prints the Slack text. It does not post it. See spec section 6.

Usage:
    python monday_retention.py --week 5 --compare-week 4
    python monday_retention.py --week 5 --compare-week 4 --save

Dependencies: duckdb
"""

from __future__ import annotations

import argparse
import sys
from datetime import date
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
RAW = REPO / "data" / "raw"
OUT = REPO / "agents" / "output"

REQUIRED = [
    "nudge_users.csv",
    "nudge_sessions.csv",
    "nudge_retention.csv",
    "nudge_weekly_summary_sends.csv",
]

# Escalation trigger from data/metric-diagnosis.md, cited in
# data/experiment-design.md Step 6.
BREAK_RATE_HIGH_WATER = 56.5
FLAT_BAND_PTS = 3.0


def fail(msg: str) -> "NoReturn":  # noqa: F821
    print(f"ERROR: {msg}", file=sys.stderr)
    sys.exit(1)


def check_sources() -> None:
    """Fail loudly and completely. Never run on a partial source set."""
    if not RAW.is_dir():
        fail(
            f"{RAW} does not exist. The five Streakly CSVs are not in this "
            "workspace (see workspace-audit.md G4). Restore them before "
            "running. No number is produced without them."
        )
    missing = [f for f in REQUIRED if not (RAW / f).is_file()]
    if missing:
        fail(
            "missing source file(s) in data/raw/: "
            + ", ".join(missing)
            + ". Refusing to report a partial result."
        )


def connect():
    try:
        import duckdb
    except ImportError:
        fail("duckdb is not installed. pip install duckdb")
    con = duckdb.connect()
    for f in REQUIRED:
        table = f.removesuffix(".csv")
        con.execute(
            f"CREATE VIEW {table} AS SELECT * FROM read_csv_auto('{(RAW / f).as_posix()}')"
        )
    return con


def scalar(con, sql: str, params: list):
    row = con.execute(sql, params).fetchone()
    return None if row is None else row[0]


def day7_by_variant(con, week: int) -> dict:
    """Day-7 retention by variant for one cohort week.

    Mirrors data/metric-findings.md Q3 exactly so results stay comparable.
    Pre-launch weeks carry variant = '' and are returned under 'all'.
    """
    rows = con.execute(
        """
        -- Pre-launch weeks carry variant = '', which read_csv_auto may load as
        -- NULL, so both cases have to collapse to 'all'.
        SELECT CASE WHEN u.variant IS NULL OR u.variant = '' THEN 'all'
                    ELSE u.variant END AS arm,
               COUNT(*) AS n,
               ROUND(AVG(r.day_7::INT) * 100, 1) AS day7_pct
        FROM nudge_users u
        JOIN nudge_retention r ON u.user_id = r.user_id
        WHERE u.cohort_week = ?
        GROUP BY 1
        """,
        [week],
    ).fetchall()
    return {arm: {"n": n, "day7": pct} for arm, n, pct in rows}


def break_rate(con, week: int):
    """Break rate among starters: day_1 active, day_7 not.

    PROXY, not a real streak-break event. See data/metric-findings.md Q2.
    """
    return scalar(
        con,
        """
        SELECT ROUND(
                 100.0 * SUM(CASE WHEN day_1 AND NOT day_7 THEN 1 ELSE 0 END)
                 / NULLIF(SUM(CASE WHEN day_1 THEN 1 ELSE 0 END), 0), 1)
        FROM nudge_retention
        WHERE cohort_week = ?
        """,
        [week],
    )


def sessions_per_user(con, week: int):
    return scalar(
        con,
        """
        SELECT ROUND(COUNT(s.session_id) * 1.0 / NULLIF(COUNT(DISTINCT u.user_id), 0), 2)
        FROM nudge_users u
        LEFT JOIN nudge_sessions s ON s.user_id = u.user_id
        WHERE u.cohort_week = ?
        """,
        [week],
    )


def open_rate(con, week: int, variant: str):
    # NOTE: the real CSV uses `send_number`, not `week_number` as the course's
    # schema note stated. Column renamed here to match the actual file,
    # not the assumed schema. See change_log.md Entry 16.
    return scalar(
        con,
        """
        SELECT ROUND(AVG(opened::INT) * 100, 1)
        FROM nudge_weekly_summary_sends
        WHERE send_number = ? AND variant = ?
        """,
        [week, variant],
    )


def delta(now, prev):
    if now is None or prev is None:
        return None
    return round(now - prev, 1)


def read_delta(d, unit="pts"):
    """Turn a delta into an honest sentence, or refuse to."""
    if d is None:
        return "Not comparable, one of the two weeks has no value for this metric."
    if abs(d) <= FLAT_BAND_PTS:
        return (
            f"No meaningful change ({d:+.1f}{unit}), within noise for arm sizes "
            "this small."
        )
    return f"Moved {d:+.1f}{unit}. Arm sizes are ~50/variant, so treat with care."


def biggest_mover(candidates: dict):
    """candidates: label -> (now, prev, delta). Returns label or None."""
    scored = {k: v for k, v in candidates.items() if v[2] is not None}
    if not scored:
        return None
    return max(scored, key=lambda k: abs(scored[k][2]))


def build(con, week: int, prev_week: int) -> str:
    now_arms = day7_by_variant(con, week)
    prev_arms = day7_by_variant(con, prev_week)

    if not now_arms:
        fail(f"no users found for cohort_week = {week}.")

    treat_key = "comeback" if "comeback" in now_arms else "all"
    now_d7 = now_arms[treat_key]["day7"]
    prev_key = "comeback" if "comeback" in prev_arms else "all"
    prev_d7 = prev_arms.get(prev_key, {}).get("day7")
    d7_delta = delta(now_d7, prev_d7)

    # Honesty guard: a treatment-vs-pre-launch comparison is not like for like.
    not_like_for_like = treat_key == "comeback" and prev_key == "all"

    br_now, br_prev = break_rate(con, week), break_rate(con, prev_week)
    sp_now, sp_prev = sessions_per_user(con, week), sessions_per_user(con, prev_week)
    or_now, or_prev = open_rate(con, week, "comeback"), open_rate(con, prev_week, "comeback")

    movers = {
        "break rate among starters": (br_now, br_prev, delta(br_now, br_prev)),
        "sessions per user": (sp_now, sp_prev, delta(sp_now, sp_prev)),
        "comeback open rate (treatment)": (or_now, or_prev, delta(or_now, or_prev)),
    }
    mover = biggest_mover(movers)

    lines = [f"*Streakly retention, Monday {date.today().isoformat()}*", ""]

    # ---- Headline
    arm_label = "treatment" if treat_key == "comeback" else "all users"
    head = f"*Day-7 retention ({arm_label}):* {now_d7}%"
    if prev_d7 is not None:
        head += f" vs {prev_d7}% last week ({d7_delta:+.1f}pts)"
    else:
        head += " (no comparable figure for last week)"
    lines += [head]

    if not_like_for_like:
        ctrl = now_arms.get("control", {}).get("day7")
        lines += [
            f"Week {prev_week} is a pre-launch cohort with no treatment arm, so "
            "this is not a like-for-like comparison."
            + (
                f" The clean comparison is treatment {now_d7}% vs control {ctrl}% "
                f"in week {week}."
                if ctrl is not None
                else ""
            )
        ]
    else:
        lines += [read_delta(d7_delta)]

    # ---- Signal
    lines += [""]
    if mover is None:
        lines += ["*Watching:* no metric had a comparable week-over-week value."]
    else:
        n, p, d = movers[mover]
        lines += [f"*Watching:* {mover}, {p} to {n} ({d:+.1f}).", read_delta(d)]

    if br_now is not None and br_now > BREAK_RATE_HIGH_WATER:
        lines += [
            f"Break rate among starters is {br_now}%, past cohort 4's "
            f"{BREAK_RATE_HIGH_WATER}% high-water mark. This is the escalation "
            "trigger named in data/experiment-design.md Step 6."
        ]

    # ---- Action
    lines += [
        "",
        "*Worth a look this week:* the weekly count of streak-break events. It is "
        "still the missing input that blocks committing to a test duration "
        "(data/experiment-design.md Step 4).",
        "",
        "_Auto-generated from data/raw/ · break rate is a day-1-active / "
        "day-7-inactive proxy, not a real streak-break event · arm sizes "
        "~50/variant, treat small moves as noise · open questions live in "
        "CLAUDE.md_",
    ]
    return "\n".join(lines)


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--week", type=int, required=True, help="cohort week to report")
    ap.add_argument("--compare-week", type=int, required=True, help="baseline week")
    ap.add_argument("--save", action="store_true", help="also write to agents/output/")
    args = ap.parse_args()

    check_sources()
    con = connect()
    msg = build(con, args.week, args.compare_week)
    print(msg)

    if args.save:
        OUT.mkdir(parents=True, exist_ok=True)
        path = OUT / f"digest-{date.today().isoformat()}.md"
        path.write_text(msg + "\n", encoding="utf-8")
        print(f"\n[saved] {path}", file=sys.stderr)


if __name__ == "__main__":
    main()
