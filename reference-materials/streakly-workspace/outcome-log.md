# Outcome Log: Anomaly Diagnoses and Their Results

> **Created:** P8L3/P8L4, 2026-09-29. **Currently empty, and that is accurate.**
> The Anomaly-to-Hypothesis Agent (`agents/anomaly-diagnosis.md`) has never
> run, because the five source CSVs are absent from this workspace
> (`workspace-audit.md` G4).
>
> **What this file is for:** every run of the anomaly agent appends a row,
> including every run that **stopped** before producing a diagnosis. The stops
> matter as much as the diagnoses, they are the record of the agent declining
> to guess, and they are how you find out whether the gates are set too tight.
>
> **What makes it work:** the `what_actually_happened` column. It is written by
> a human, later, once the answer is known. Nothing else in the stack can fill
> it. If it stays blank, the learning loop (`agents/registry.md` §4) has nothing
> to grade and the agent stack stops compounding while still looking busy.

---

## How to read a row

| Field | Written by | When |
| --- | --- | --- |
| `date`, `trigger`, `stopped_at`, `stop_reason` | agent | at run time |
| `drivers`, `hypotheses`, `top_confidence`, `sql_issued` | agent | at run time |
| `what_actually_happened` | **a human** | when the answer is known |
| `grade` (hit / partial / miss) | learning loop | weekly grading pass |

Grading definitions are in `agents/registry.md` §4 step 2. A row blank for more
than three weeks gets reported by the learning loop as an unclosed diagnosis,
not silently ignored.

---

## Rows

*No entries. The agent has not run.*

<!--
Template. Copy below this comment for each run.

### Row <n>, <YYYY-MM-DD>

- **Trigger:** <metric> <x>% → <y>% (<±z>pts), week <n> vs week <m>
- **Stopped at:** <step number | completed>
- **Stop reason:** <plain language, or "n/a, completed">
- **Drivers that moved meaningfully:** <lever: figures> / <lever: figures>
- **Escalation flag:** <break rate past 56.5%: yes/no>
- **Hypotheses:**
  1. <claim> (<n>/10, <new | reused from data/metric-diagnosis.md H#>)
  2. <claim> (<n>/10, ...)
  3. <claim> (<n>/10, ...)
- **Top confidence:** <n>/10
- **SQL issued:** <yes, to whom | no>
- **What actually happened:** *(blank until known)*
- **Grade:** *(blank until graded)*
- **Grading note:** *(one line on why, not just the label)*
-->

---

## Running tallies

The learning loop maintains these. All zero until the agent runs.

| Measure | Count | What it tells you |
| --- | --- | --- |
| Completed runs | 0 | Diagnoses actually issued |
| Stopped at step 1 (below threshold) | 0 | Not logged as noise, logged silently |
| Stopped at step 2 (too few drivers) | 0 | High count means the decomposition bar is too strict |
| Stopped at step 3 (low confidence) | 0 | High count means the 6/10 gate is too strict, or the priors need work |
| Graded hit / partial / miss | 0 / 0 / 0 | The actual accuracy record |
| **Closed but ungraded** | 0 | Backlog for the learning loop |
| **Unclosed after 3 weeks** | 0 | **The number to watch.** High means nobody is checking the agent's work |
