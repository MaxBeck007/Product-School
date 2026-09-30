# Workspace Audit, Streakly (P7L1)

> **Date:** 2026-09-28
> **Method:** read the actual folder tree (41 files, pre-P7) and the full text of
> `CLAUDE.md`, `change_log.md`, `project-skeleton.md`, `skills/weekly-status.md`,
> `docs/spec-readiness.md`, `docs/qa-checklist.md`, `prototype/README.md`,
> `data/experiment-design.md`, `data/metric-findings.md`,
> `docs/decision-brief.md`, plus the headers of `docs/one-pager.md`,
> `docs/p2-one-pager.md`, `docs/pm-brief.md`. Lesson mapping cross-checked
> against `../streakly-scenario-claude-code-for-pms.md` (heading lines 48-1069).
> **Not read in full this pass:** `docs/prd.md`, `docs/objection-log.md`,
> `docs/codebase-summary.md`, `docs/design-review.md`, `docs/triad-session.md`,
> `docs/hypothesis.md`, `docs/presentation*.md`, `docs/recommendation-memo.md`,
> `data/metric-diagnosis.md`, the three `research/*` synthesis files, the three
> `stakeholders/*` files, and all `.html` renders. Findings about those files
> are based on filenames, sizes, and how other files cite them, and are labeled
> accordingly.

---

## 1. What exists today

**Verified:** 41 files before this P7 session. Root: `CLAUDE.md`,
`change_log.md`, `project-skeleton.md`. Folders: `data/` (3), `docs/` (20 incl.
5 HTML), `prototype/` (2), `research/` (9 incl. 4 HTML), `skills/` (1),
`stakeholders/` (3).

### Artifact-to-lesson map

| Lesson | Artifact | Note |
| --- | --- | --- |
| P1L1 | `project-skeleton.md` | Slack-thread PRD skeleton, `[NOT IN THREAD]` gaps intact |
| P1L3 | `CLAUDE.md` | Replaced by this pass |
| P1L4 | `change_log.md` | Partial, see gap G1 |
| P1L5 | `skills/weekly-status.md` | Merged with the P6L3 version |
| P2L1-L4 | `research/interview-synthesis.md`, `research/nps-analysis.md`, `research/competitive-matrix.md`, `research/competitive-reddit.md`, `docs/decision-brief.md` | |
| P3L1 | `prototype/index.html`, `prototype/README.md`, `docs/pm-brief.md` | |
| P3L2 / L2a | `research/usability-session-1.md` + change_log entries 1-2 | Mock sessions, labeled |
| P3L3 / L4 | `docs/hypothesis.md`, `docs/triad-session.md` | |
| P4L1 / L1.5 | `docs/codebase-summary.md`, `stakeholders/{raj,lena,marcus}.md` | |
| P4L2-L4 | `docs/spec-readiness.md`, `docs/design-review.md`, `docs/qa-checklist.md` | |
| P5L1-L4 | `data/metric-findings.md`, `data/metric-diagnosis.md`, `docs/recommendation-memo.md`, `data/experiment-design.md` | |
| P6L1-L4 | `docs/prd.md`, `docs/objection-log.md`, `skills/weekly-status.md`, `docs/presentation.md` + `docs/presentation-notes.md` | |
| Meta | `docs/one-pager.md`, `docs/p2-one-pager.md`, `docs/p2-outputs.html` | See gap G3 |

**Assessment:** coverage is strong. Every lesson P1-P6 has at least one saved
artifact, and the discipline that matters most is already consistent: nearly
every file carries a sourcing header and labels mock or roleplayed material as
such. That is the part of this workspace that would survive contact with a real
collaborator.

---

## 2. What is missing that would make Claude more useful next session

**G1, the change log has four entries' worth of holes.** It covers P3L2,
P3L2a, and P6L1/L2. Nothing for P4 (spec readiness, design review, QA) or P5
(the entire data stack, including the correction noted in
`data/metric-findings.md` about which file holds the break-rate figure). A
change log with gaps is worse than no change log, because next session I will
read it and wrongly conclude P4/P5 never happened. **Highest-value fix.**

**G2, no single open-items file.** Open items are currently spread across at
least five places: `change_log.md` carry-forwards (track personalization,
freeze self-resolution, notification-independent trigger), `docs/prd.md` Open
Questions, `project-skeleton.md` Open Questions, `docs/qa-checklist.md` rows
1/7/8/9, and `data/experiment-design.md` Step 4 (unconfirmed weekly eligible
volume). No session can reliably answer "what is actually open" without
reading all five.

**G3, no ruling on which document is current.** `docs/` holds `pm-brief.md`,
`decision-brief.md`, `recommendation-memo.md`, `one-pager.md`,
`p2-one-pager.md`, and `prd.md`. Two of these (`p2-one-pager.md`,
`p2-outputs.html`) are course-progress recaps, not product artifacts, and read
as product docs from the filename alone. Without a stated precedence order, a
future session (or a teammate) can quote a superseded position.

**G4, the P5 data is not reproducible from this workspace.**
`data/metric-findings.md` cites five CSVs (`nudge_users`, `nudge_sessions`,
`nudge_retention`, `nudge_nudges`, `nudge_weekly_summary_sends`) that are not
in the folder. Every number downstream, including the 76% vs 46% pilot result
that the whole recommendation rests on, traces to files Claude cannot re-open.
**Guess:** they were session uploads, cleared when that session ended.
**What would confirm:** checking whether the course CSVs are still available
to re-save under `data/raw/`.

**G5, no `agents/` folder.** P7L3 needs it. Also no place for scheduled or
automated outputs to land.

**G6, `stakeholders/` has no template and no entry for Max.** Three profiles
exist (Raj, Lena, Marcus) but nothing describes what a profile should contain,
which is the exact blocker for the P7L4 question about letting each user build
their own stakeholder folder. There is also no profile for Max, so
`skills/weekly-status.md` can calibrate *to* stakeholders but nothing
calibrates *from* Max's own defaults.

**G7, no metric glossary.** "Day-7 retention" is used loosely across files for
at least two different things: retention of a signup cohort
(`data/metric-findings.md` Q1) and retention in the pilot's treatment arm
(Q3). Separately, `data/metric-diagnosis.md`'s 38.9% → 56.5% figure is break
rate *among starters* (day-1 active, day-7 not), which `docs/prd.md` already
miscited once (`change_log.md` entry 3). That mistake will recur without a
definitions file.

**G8, `CLAUDE.md` had no file map.** The old version described the problem
well but never told a fresh session which file to open for what. Fixed in this
pass.

---

## 3. Reorganization that would reduce friction

Ordered by value-to-risk. **Nothing in this section has been executed.** Every
move risks breaking cross-file references, which are heavily used here
(`docs/qa-checklist.md` alone cites three other files by path), so each move
needs a grep-and-fix pass on inbound links.

| # | Change | Why | Risk |
| --- | --- | --- | --- |
| R1 | Add `open-items.md` at root | Closes G2, one place to read what's open | None, additive |
| R2 | Add `agents/` | Needed for P7L3 | None, additive |
| R3 | Add `docs/definitions.md` | Closes G7, stops the break-rate miscite recurring | None, additive |
| R4 | Add `stakeholders/_template.md` and `stakeholders/max.md` | Closes G6, makes the folder portable to other users | None, additive |
| R5 | Backfill `change_log.md` entries for P4 and P5 | Closes G1 | None, append-only |
| R6 | Move `p2-one-pager.*` and `p2-outputs.html` to `course-progress/` | Stops course recaps reading as product docs | Low, check inbound links first |
| R7 | Move all `.html` renders to a `renders/` subfolder in place, or suffix them `-render.html` | 8 of the 41 files are HTML renders of an adjacent `.md` file (4 in `docs/`, 4 in `research/`); halves the apparent size of both folders. `docs/p2-outputs.html` is a 9th HTML file with **no `.md` source**, so it cannot be regenerated, handle it separately. `prototype/index.html` is the prototype itself, not a render, leave it | Low, but `docs/presentation.html` may be opened directly for the Marcus readout, confirm before moving |
| R8 | Add `data/raw/` with a README recording CSV provenance even if the files are gone | Makes the reproducibility gap visible instead of silent | None, additive |
| R9 | Leave `project-skeleton.md` at root as-is | It is the P1 baseline, its value is being the unedited starting point | n/a |

**Deliberately not recommended:** creating `project.md` and `strategy.md` from
P1L4. Their content now lives in `CLAUDE.md`, `docs/decision-brief.md`, and
`docs/hypothesis.md`. Adding them this late would create a fourth and fifth
place for the same facts to drift. **Assumption:** you care more about a
workspace that stays consistent than about literal P1L4 completion. Say the
word if you want them backfilled anyway.

---

## 4. Recommendation

Do R1 through R5 now (all additive, no link risk, and R5 closes the worst
gap). Defer R6 through R8 until after P7L4, since the capstone review will read
the workspace as-is and moving files mid-P7 adds noise for no benefit.
