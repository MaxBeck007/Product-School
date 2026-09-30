# Agent Spec: Weekly Insight Report (P8L2)

> **This is an extension spec.** A Friday weekly workflow already exists as
> `skills/friday-status.md` (P7L2), which derives Shipped / In progress /
> Blocked from the workspace and applies the stakeholder tone rules in
> `skills/weekly-status.md`. This file adds the 3-2-1 compression, the
> versioned `reports/` output, and the Slack delivery P8L2 asks for.
>
> **Read `skills/friday-status.md` first.** Its derivation rules, its
> "not derivable from the workspace" honesty section, and its
> never-invent-a-metric rule all still apply.
>
> **Built:** P8L2, 2026-09-29.

---

## 1. The relationship between this and `skills/friday-status.md`

**One derivation, two lengths. This report is the compression, not a second
analysis.**

| | `skills/friday-status.md` | This agent |
| --- | --- | --- |
| Audience | Raj and Lena (team), Marcus (leadership) | Anyone scanning Slack, including Max next month |
| Length | Up to a page per version | Six bullets |
| Structure | Shipped / In progress / Blocked | Done 3 / Changed 2 / Watch 1 |
| Output | `status/friday-<date>.md` | `reports/<date>.md` + Slack post |
| Derivation | Reads the workspace directly | **Reads the friday-status output for the same week** |

**Why this ordering matters.** Two weekly reports that independently read the
same workspace will disagree within a month, and then nobody trusts either.
This agent runs *after* `friday-status.md` and compresses its output. If
`friday-status.md` has not run for the current week, this agent stops and says
so rather than deriving the buckets itself.

**The one thing it adds beyond compression:** the *Changed* section. Neither
`friday-status.md` nor `weekly-status.md` currently asks "what number or user
signal moved this week," as distinct from "what did we finish." That is the
section worth having, and §3 is about why it is also the hardest to fill
honestly.

## 2. Sources, and what each one can actually support

P8L2 names three sources. Two of them do not mean what the prompt assumes in
this workspace. Flagging that up front rather than writing a spec that quietly
fabricates a weekly cadence.

**Source 1, retention metrics from `data/`.** `data/metric-findings.md`,
`data/metric-diagnosis.md`, `data/experiment-design.md`.
**Constraint: these are static analyses, not a feed.** They were computed once
against five CSVs that are **no longer in this workspace**
(`workspace-audit.md` G4). Nothing in `data/` will change week over week until
the source is restored and `agents/monday_retention.py` runs for real. Until
then, the *Changed* section cannot cite a moved metric, and must say so.

**Source 2, sprint completions from `change_log.md`.**
**Constraint: `change_log.md` is a session log, not a sprint log.** Entries 1
through 5 are all dated 2026-09-28, one day of course work covering P3 through
P7. It records what artifacts were produced and what was corrected, which is
genuinely useful, but it does not carry sprint boundaries, ticket IDs, or
estimates. "Sprint completions this week" maps to "change_log entries added
since the last report" and nothing more.

**Source 3, top NPS themes from `research/nps-analysis.md`.**
**Constraint: this is not a weekly feed either.** `research/nps-analysis.md`
states its source plainly: 10 raw NPS comments provided in the P2L2 exercise.
There is no incoming NPS stream, so "top NPS themes this week" will return the
same four themes every week, indefinitely.

**Consequence for the spec:** the report pulls NPS themes only when
`research/nps-analysis.md` has changed since the last run, and otherwise omits
the line. A report that restates the same "top theme" for twelve weeks running
trains its reader to skip it. `skills/research-pulse.md` (P7L2) is the file
that would pick up genuinely new research input if any arrived.

## 3. Trigger prompt

```
Run the weekly insight report: agents/weekly-insight.md
```

## 4. Steps the agent runs

1. **Find this week's friday-status output** in `status/`. If absent, stop and
   say: "friday-status has not run for week of <date>. Run
   `skills/friday-status.md` first." Do not derive the buckets independently.
2. **Compress Shipped into three Done bullets.** Each names the file it landed
   in. More than three shipped items means picking the three that a reader
   outside the triad would care about, and saying how many were omitted.
3. **Fill Changed from evidence of movement, not activity.** Two bullets, each
   one either a metric that moved or a user signal that moved. Sources in
   priority order: a real run of `agents/monday_retention.py`, a new
   `change_log.md` correction that changed a previously stated number, or a new
   research artifact.
   **If neither bullet can be filled from evidence, write "Nothing moved this
   week" and leave it at that.** Do not promote a Done item into Changed. That
   substitution is the specific failure mode this section exists to prevent:
   work happening is not the same as the number moving.
4. **Pick one Watch bullet.** The single item most likely to matter next week.
   Default source: the topmost unresolved item in `CLAUDE.md` Known gaps, or a
   carry-forward open item in `change_log.md` that is newly time-pressured.
   One bullet, not a list.
5. **Check the labels.** Any figure quoted from a Framing B document
   (`data/*`, `docs/recommendation-memo.md`, `docs/one-pager.md`) carries the
   exercise-dataset caveat, per `CLAUDE.md` "What is actually real." A 3-2-1
   report is short enough to be forwarded, which is exactly when an unlabeled
   pilot figure does damage.
6. **Prompt Max to save**, then write `reports/<YYYY-MM-DD>.md`.
7. **Print the Slack text.** Do not post it, see §7.

## 5. Output format

````
# Streakly Weekly Insight, <weekday> <date>

**Done this week**
- <bullet, naming the artifact or file>
- <bullet>
- <bullet>
<"+N more, see status/friday-<date>.md" if anything was omitted>

**Changed this week**
- <a metric or user signal that moved, with its source file>
- <second one>
<or: "Nothing moved this week. <one line on why, e.g. no data source connected.>">

**Watch next week**
- <the one thing most likely to matter>

---
Derived from status/friday-<date>.md · sources: data/, change_log.md,
research/nps-analysis.md · <label any exercise-dataset figures quoted above>
````

## 6. Sample output

**Built from the actual state of this workspace as of 2026-09-29.
Verified against `change_log.md` entries 4-5 and `CLAUDE.md` Known gaps.
This is a real compression of real workspace state, not an invented example,
except that `status/` does not yet contain a friday-status file, so step 1 would
in fact stop before reaching this point. Shown as the output it would produce
once that file exists.**

```
📋 Streakly Weekly Insight, Tue 2026-09-29

Done this week:
• P7 workspace formalization: CLAUDE.md rewritten with a file map, precedence
  rule, and metric definitions; audit in workspace-audit.md (8 gaps, 9 reorg
  options)
• Three one-command workflows saved to skills/ (friday-status, research-pulse,
  competitive-pulse) plus a working Monday digest script, agents/monday_retention.py
• Capstone fixes F1-F3 landed: the shipped-vs-not contradiction is now named in
  CLAUDE.md, PRD Open Question 8 added, five unreal artifacts tagged
  (change_log.md entry 5)

Changed this week:
• Nothing moved in the metrics. The five source CSVs are absent
  (workspace-audit.md G4), so no retention figure has been recomputed and
  agents/monday_retention.py has never produced a real number.
• One stated number did change: a real bug in monday_retention.py was dropping
  the previous week's Day-7 figure, because DuckDB loads pre-launch variant = ''
  as NULL. Found by smoke test against synthetic CSVs, fixed (change_log.md
  entry 4). The digest previously said "no comparable figure" when one existed.

Watch next week:
• The weekly eligible-user volume. It is still unconfirmed
  (data/experiment-design.md Step 4) and it blocks committing to a duration for
  the confirmatory test, which is the actual recommendation on the table.

---
Derived from change_log.md entries 4-5 and CLAUDE.md Known gaps · no figures
from the P5 exercise dataset quoted above
```

**What the sample does that matters.** Its *Changed* section says nothing
moved, in a week with three substantial Done bullets. That is the honest read:
P7 produced a lot of artifacts and moved zero metrics. A report that dressed
the artifacts up as movement would be the more flattering one and the less
useful one.

## 7. Delivery, scheduling, and what stays manual

**Save:** `reports/<YYYY-MM-DD>.md`. One file per week, never overwritten, so a
later report can diff against an earlier one.

**Note the two-folder split, on purpose:** `status/` holds the long
friday-status output, `reports/` holds the short weekly insight. Same week,
two files, two lengths. If that proves annoying in practice, collapse them,
but collapse them deliberately rather than letting one quietly stop running.

**Slack: print, do not post, in v1.** Same reasoning as
`agents/monday-retention.md` §6 and `agents/metric-pulse.md` §5. This report is
six bullets that a reader will take at face value and forward, which raises
rather than lowers the accuracy bar.

**Real-world wiring, as context not direction.** Friday 4pm via cron, Windows
Task Scheduler, n8n, or a scheduled job owned by engineering. Same three
options and the same trade-offs as `agents/metric-pulse.md` §4. The prerequisite
is the same too: do not schedule a report that has never run correctly by hand.

**Run it manually for three weeks first.** Specifically, check whether the
*Changed* section ever fills. If it stays empty for three weeks, the report is
not broken, it is telling you the workspace has no live data source, and that
is the finding.

## 8. Open questions

1. **Should `status/` and `reports/` be one folder?** Two weekly files invites
   drift. Collapsing them means one audience loses its length.
2. **What becomes the real NPS input?** §2 source 3 has no feed. Without one,
   the report's user-signal half is permanently empty.
3. **Does anyone other than Max read this?** If it goes to a channel it needs
   the Framing A / Framing B warning inline every week, not just when a pilot
   figure appears. `agents/monday-retention.md` §7 question 3 is the same
   question about the Monday digest, and both should be answered the same way.
