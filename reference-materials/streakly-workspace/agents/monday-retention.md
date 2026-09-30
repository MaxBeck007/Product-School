# Agent Spec: Monday Retention Digest

> **Built:** P7L3, 2026-09-28.
> **What this is:** Max's own reading tool, run before standup. It is not an
> engineering ask, not a production job, and nothing in it is direction to the
> team. It answers one question: what changed in the retention picture since
> last Monday, and what should I look at this week.
> **Blocking dependency, stated up front:** the five source CSVs
> (`nudge_users`, `nudge_sessions`, `nudge_retention`, `nudge_nudges`,
> `nudge_weekly_summary_sends`) are cited by `data/metric-findings.md` but are
> **not in this workspace** (`workspace-audit.md` G4). The script below cannot
> produce a number until they are restored to `data/raw/` or the connection is
> repointed. It is written to fail loudly rather than fill the gap.

---

## 1. What it reports, and why only three things

| Slot | Metric | Why this one |
| --- | --- | --- |
| Headline | Day-7 retention, treatment arm, this week vs last | The core metric (`CLAUDE.md`). One number, so there is no ambiguity about what "it" is. |
| Signal to watch | Biggest week-over-week mover across break rate, sessions/user, and comeback open rate | `data/experiment-design.md` Step 6 names exactly these three as the leading indicators worth watching weekly instead of waiting out the full test. |
| Suggested action | One thing to look at this week | A digest that reports without pointing somewhere gets skimmed and forgotten. |

Deliberately excluded: Day-30 retention (too slow to move week over week and
invites over-reading noise), and anything from the pre-launch cohorts 1-4
(that trend is history, not news).

## 2. Thresholds, and the honesty rule

The script computes deltas. It does **not** decide whether a delta is real.
With arms of roughly 50 users, a few percentage points is noise, and the
digest has to say so rather than narrate a story.

- **Flat** if the delta is within ±3 percentage points. Reported as "no
  meaningful change," not as a direction.
- **Mover** outside ±3pts. Reported with the caveat that arm sizes are small.
- **Watch** if the same metric moves the same direction three weeks running.
  A persistent drift matters more than a single large jump at this sample size.
- **Break-rate high-water mark:** flag explicitly if break rate among starters
  passes cohort 4's 56.5% (`data/metric-diagnosis.md`), the escalation trigger
  already named in `data/experiment-design.md` Step 6.

## 3. The script

Saved as `agents/monday_retention.py`. Reads CSVs from `data/raw/` with DuckDB,
the same engine used for `data/metric-findings.md`, so numbers stay comparable.
Writes a dated digest to `agents/output/` and prints the Slack text to stdout.

**Dependencies:** `duckdb`. **No Slack posting in v1**, see section 6.

**Verified 2026-09-28:** compiles on Python 3.10, and step 1 below (empty
`data/raw/`) exits non-zero naming the missing files. Query logic was then
smoke-tested against **synthetic CSVs built to the schema described in
`data/metric-findings.md`**, not the real data, which is not in the workspace.
That run reproduced 76.0% treatment vs 46.0% control and correctly refused the
week-4 comparison as not like for like. It also surfaced one real bug, now
fixed: DuckDB loads the pre-launch `variant = ''` values as NULL, so the
previous week's figure was silently dropped. **This is a logic check, not
evidence the numbers are right.** Step 2 below is still required against the
real CSVs.

## 4. Run it manually first, in this order

Do not schedule anything until all four pass.

1. **Dry run with no data.** Run it with `data/raw/` empty. Expected: it names
   every missing file and exits non-zero. If it prints a number instead, stop,
   the script is inventing data.
2. **Reproduce a known result.** With the CSVs restored, run
   `--week 5 --compare-week 4`. Expected: treatment Day-7 = 76.0%, control =
   46.0% (`data/metric-findings.md` Q3). If those two numbers do not match
   exactly, the query is wrong and nothing downstream can be trusted.
3. **Check the flat case.** Run it against two weeks you know are similar.
   Expected: "no meaningful change," not a fabricated narrative.
4. **Read the Slack text out loud.** If you would not say that sentence to Raj
   at standup, the template is wrong, not the data.

Only after all four: run it manually every Monday for three weeks. Schedule it
only once you have stopped finding surprises in the output.

## 5. Slack message template

Plain English, no dashboard vocabulary. Numbers only where a number exists.

```
*Streakly retention, Monday <date>*

*Day-7 retention (treatment):* <x>% vs <y>% last week (<+/-z>pts)
<one-line read, or "No meaningful change, within noise for arm sizes this small.">

*Watching:* <metric> moved from <a> to <b>.
<why it matters in one line, tied to Day-7 retention>

*Worth a look this week:* <one specific thing>

_Auto-generated from data/raw/ · arm sizes ~50/variant, treat small moves as
noise · open questions live in CLAUDE.md_
```

**Worked example** using the one week where real figures exist
(`data/metric-findings.md`, week 5 vs week 4, cohort-level, **illustrative,
not a live run**):

```
*Streakly retention, Monday 2026-09-28*

*Day-7 retention (treatment):* 76.0% vs 44.0% last week (+32pts)
Week 4 is a pre-launch cohort with no treatment arm, so this is not a
like-for-like comparison. The clean comparison is treatment 76.0% vs control
46.0% in the same week.

*Watching:* comeback open rate in the treatment arm, 52% to 56% across the
last two sends, while control stayed at 4-6%.
Rising engagement over repeated exposure is the durability signal, a fading
spike would weaken the case for scaling.

*Worth a look this week:* the weekly count of streak-break events. It is still
the missing input that blocks committing to a test duration
(data/experiment-design.md Step 4).

_Auto-generated from data/raw/ · arm sizes ~50/variant, treat small moves as
noise · open questions live in CLAUDE.md_
```

Note what the example does: it refuses the flattering +32pt headline because
the comparison is invalid. That behavior is the point of the template.

## 6. Scheduling, and what is deliberately not automated

In the real world this runs via cron, Windows Task Scheduler, n8n, or a hosted
timer. For now: **run manually**, Monday morning.

**Posting to Slack is not automated in v1.** The script prints the message; you
paste it. Reason: an agent that posts unreviewed numbers into a team channel
can be wrong in public, and at ~50 users per arm it will sometimes be wrong.
Auto-post is worth revisiting once section 4 step 2 has passed for several
consecutive weeks and the thresholds have proven themselves.

## 7. Open questions

1. Which source becomes the real one when this stops being a course exercise,
   product analytics, the warehouse, or an export? That choice decides whether
   the CSV path survives.
2. Is there a genuine streak-break event log anywhere? Every break-rate figure
   in this workspace is the day-1-active / day-7-inactive proxy
   (`data/metric-findings.md` Q2), and the proxy is doing a lot of work.
3. Should the digest go to a channel or stay a DM to Max? A channel post makes
   it a team artifact and raises the accuracy bar considerably.
