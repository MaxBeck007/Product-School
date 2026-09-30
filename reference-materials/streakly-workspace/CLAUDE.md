# Streakly, Comeback Screen: Project Context

> Load this every session. Updated 2026-09-29 (P8L4); the body below is the
> 2026-09-28 (P7L1) rewrite plus the agent-stack additions. Supersedes the
> pre-P7 version. Audit behind the P7L1 update: `workspace-audit.md`.

## Role and squad
PM, Engagement squad. Triad: Raj (Senior Engineer), Lena (Product Designer),
Max (PM). Reports to Marcus, Head of Product.
Stakeholder profiles: `stakeholders/{raj,lena,marcus}.md`.

## Product and core metric
Streakly, a consumer habit + micro-learning app (pick a track, 5-minute daily
lesson, build a streak). Core metric: **Day-7 retention rate**, dropped from
48% to 39% after the v2 streak/notification redesign.

## Key tension
Re-engagement nudges vs. notification fatigue. Users who feel nagged turn
notifications off entirely, which closes the one channel that could otherwise
win them back after a lapse.

## What is actually real, read this before quoting any artifact
Two incompatible framings live in this workspace, and both are artifacts of how
the work was sequenced. Know which one you are in before you quote anything.

**Framing A, the concept is unbuilt.** `CLAUDE.md`, `docs/pm-brief.md`,
`docs/hypothesis.md`, `prototype/README.md`, `docs/spec-readiness.md`,
`docs/design-review.md`, `docs/qa-checklist.md`. In these, the Comeback screen
exists only as a three-screen click-through prototype. No scope is committed,
the freeze eligibility rule is a proposal, and no real user has seen it.

**Framing B, a pilot already ran.** `data/metric-findings.md`,
`data/metric-diagnosis.md`, `data/experiment-design.md`,
`docs/recommendation-memo.md`, `docs/one-pager.md`. These work from a dataset in
which the Comeback screen shipped as a 50/50 experiment to 100 users in cohort
week 5. `docs/recommendation-memo.md` says "we shipped" in its first line.

**What is actually true:** nothing shipped. Framing B is the course's supplied
dataset (P5), used to practice analysis, not a record of a real Streakly
release. Treat Framing B numbers as a realistic exercise dataset, never as
company results.

**Practical rule:** do not put a Framing A document and a Framing B document in
front of the same person without saying this out loud first. The question "wait,
did this ship or not?" costs you the room.

## Where the work stands
Discovery. No committed scope. The recommendation is **not** "ship it," it is
"run a properly powered confirmatory test first" (`docs/one-pager.md`,
`docs/recommendation-memo.md`).

- **Direction:** the Comeback screen, best-streak stat, 60-second lesson,
  one-tap freeze. Chosen over status quo and notification-only fixes
  (`docs/decision-brief.md`).
- **Evidence for it:** pilot 76% vs 46% Day-7, n=50/variant, p=0.0021 by
  two-proportion z-test, cross-checked p=0.0038 Fisher's exact
  (`data/experiment-design.md`). Treatment open rate climbed 28% → 56% across
  4 sends vs. flat 4-6% control (`data/metric-findings.md` Q4).
- **Why not scale on it:** n=50 detects only large effects. Detecting a 5pt
  lift needs ≈1,568/variant (≈3,136 total), which needs ≈392 eligible users
  per week to fit 8 weeks. **That weekly volume is unconfirmed** and is the
  single biggest open input.
- **Built:** click-through prototype only (`prototype/index.html`), two copy
  fixes already made from persona testing (`change_log.md` entries 1-2).
  Freeze eligibility is a discussed position, not built.

## Where to look for what
| Need | File |
| --- | --- |
| Exec-ready summary | `docs/one-pager.md` |
| The recommendation and its reasoning | `docs/recommendation-memo.md`, `docs/decision-brief.md` |
| Spec for Raj and Lena | `docs/prd.md` |
| Anticipated objections | `docs/objection-log.md` |
| Marcus readout | `docs/presentation.md` + `docs/presentation-notes.md` |
| Data analysis and SQL | `data/metric-findings.md`, `data/metric-diagnosis.md` |
| Test design and power math | `data/experiment-design.md` |
| User research | `research/` (interviews, NPS, competitive, Reddit, usability) |
| What is built and what changed | `prototype/README.md`, `change_log.md` |
| Launch risks and edge cases | `docs/qa-checklist.md`, `docs/spec-readiness.md` |
| Weekly status workflow | `skills/weekly-status.md` (tone rules), `skills/friday-status.md` (one-command) |
| Weekly research and competitor runs | `skills/research-pulse.md`, `skills/competitive-pulse.md` |
| Monday retention digest | `agents/monday-retention.md`, `agents/monday_retention.py` |
| The whole agent stack, at a glance | `agents/registry.md` |
| Agent specs | `agents/metric-pulse.md`, `agents/anomaly-diagnosis.md`, `agents/weekly-insight.md` |
| Past diagnoses and their results | `outcome-log.md` |
| Workspace gaps and reorg options | `workspace-audit.md` |
| Per-artifact confidence ratings | `docs/capstone-session.md` |
| The untouched P1 baseline | `project-skeleton.md` |

**Precedence when documents conflict:** `docs/one-pager.md` and
`docs/recommendation-memo.md` are current. `docs/prd.md` is the working spec.
`docs/decision-brief.md` and `docs/pm-brief.md` are earlier-stage and may hold
superseded positions. `docs/p2-one-pager.md` and `docs/p2-outputs.html` are
course-progress recaps, **not product artifacts**, do not quote them as
product positions.

## Constraints and context to load every session
- "No new integrations" means no new third-party systems. It does **not**
  mean no new data fields. New fields (pre-break streak length, freeze-spent
  state) are in scope and must not be assumed away
  (`docs/spec-readiness.md`).
- Discovery phase, no committed scope, 8 weeks from sprint kickoff (per the
  original scenario framing). Kickoff date not known.
- Real weekly eligible-user volume (how many WAU break a streak per week) is
  still unconfirmed, needed before committing to any test's duration.

## Metric definitions, use these exactly
- **Day-7 retention:** share of a signup cohort active on day 7. Cohort-level
  (`data/metric-findings.md` Q1) and pilot-arm (Q3) figures are different
  measurements, do not mix them.
- **Break rate 38.9% → 56.5%:** break rate **among starters** (day-1 active,
  day-7 not), not all new users. Lives in `data/metric-diagnosis.md`, **not**
  `data/metric-findings.md`. `docs/prd.md` miscited this once already
  (`change_log.md` entry 3).
- **"Broke their streak" in the P5 data is a proxy**, day-1 active and day-7
  inactive. No streak-break event field exists in the dataset.
- **Alert threshold, ±3 percentage points** week over week, not the 2 points
  the course specifies. At ~50 users per arm a 2-point move is about one user.
  Reasoning and the switch condition (~500/variant) in `agents/metric-pulse.md`
  §2. The pulse agent and the anomaly agent must always use the same number.
- **Escalation flag, break rate among starters passing 56.5%**, cohort 4's
  high-water mark (`data/metric-diagnosis.md` §1). Named as a trigger in
  `data/experiment-design.md` Step 6.

## The agent stack, the Comeback Coach
Full registry, connection plan, learning loop, and roadmap:
`agents/registry.md`. Owner of all three: Max.

| Agent | Role | Trigger | Spec |
| --- | --- | --- | --- |
| Metric Pulse | sense | manual Monday (target: nightly, 8am delivery) | `agents/monday-retention.md` + `agents/metric-pulse.md` |
| Anomaly-to-Hypothesis | diagnose | pulse alert, behind a manual YES gate | `agents/anomaly-diagnosis.md` |
| Weekly Insight | synthesize | Friday, after `skills/friday-status.md` | `agents/weekly-insight.md` |

**The one fact to carry into every session about these:** all three are
specified and **unverified**. No agent in this workspace has ever produced a
real Streakly number, because the five source CSVs are absent
(`workspace-audit.md` G4). `agents/monday_retention.py` compiles and was
smoke-tested against synthetic CSVs only.

**None of them posts to Slack automatically.** Each prints its message and Max
pastes it. Three specs reached that independently: at ~50 users per arm these
agents will sometimes be wrong, and being wrong in a team channel costs more
than the time saved. Do not "helpfully" add auto-posting.

**The learning loop writes back into this file.** It reads `outcome-log.md`,
grades past diagnoses, and proposes **one** heuristic update to `CLAUDE.md`
per run (`agents/registry.md` §4). It proposes; it never applies. Max decides.

## Evidence labels used throughout this workspace
Keep using them. They are the reason these artifacts are safe to hand to
someone else.
- **Verified:** computed or quoted from a named file, query, or the scenario
  doc.
- **Assumption / Guess:** inferred, with what would confirm it stated.
- **Mock / illustrative:** persona tests (`research/usability-session-1.md`,
  `change_log.md` entries 1-2), constructed reviewer objections
  (`docs/objection-log.md`), and the fully roleplayed Raj session
  (`docs/spec-readiness.md`). No real user or teammate said these things.

## Working habits
- Prompt Max when a file should be saved, including new files created in
  future sessions. Do not wait to be asked.
- Flag assumptions explicitly. Never invent facts, numbers, quotes, or file
  paths. Cite the file for every factual claim.
- Ask before building anything substantial while open questions are
  unresolved.
- Stay in the PM lane: the who, what, and why. Frame technical content as
  context or open questions, not direction to the team.
- Log every substantive session in `change_log.md` before ending it.

## Known gaps as of this update
- **Weekly eligible-user volume unconfirmed** (`data/experiment-design.md`
  Step 4). Blocks committing to a test duration.
- **The workspace contradicts itself on whether anything shipped.**
  `docs/recommendation-memo.md` describes a 50/50 pilot that ran to 100 users
  in cohort week 5; everything else describes an unbuilt concept with a
  click-through prototype. The P5 dataset assumes the experiment already ran.
  Do not let a reader hit both framings without warning
  (`docs/capstone-session.md` F1).
- **Reactive-only scope gap, resolved 2026-09-30:** the Comeback screen
  reaches users only *after* a lapse, but Day-7 retention measures a
  population that includes users who are anxious and have not lapsed yet
  (Amara, day 4). Max decided to expand scope rather than name this a
  non-goal (`change_log.md` Entry 6, `docs/design-review.md` Part 3,
  `docs/prd.md` Open Question 8). **New open item this creates:** the
  proactive/anticipatory piece itself, mechanic, trigger, and metric, is not
  yet designed. Treat "Comeback experience" from here on as reactive screen +
  an undesigned proactive piece, not the reactive screen alone.
- **Notification-independent trigger unanswered:** how a user who already
  turned notifications off ever sees the feature meant to win them back.
  Judged the objection most likely to stall the initiative
  (`docs/objection-log.md`). Named in `docs/prd.md` Open Question 7, so it is
  documented but not answered.
- **Freeze eligibility rule** (one per lapse, streaks 3+ days, no stacking)
  is a discussed position only, not validated and not in the prototype.
- **Lesson content is fixed to one track (miniature painting)**, not
  personalized to the user's actual track.
- **Whether the freeze should self-resolve** rather than require a tap. Tom's
  skepticism was not resolved by copy alone. Changes the mechanic, so it is a
  product decision.
- **Prototype cannot evidence the eligibility rule**, only tone and the
  lesson mechanic (`docs/qa-checklist.md` rows 1, 7, 8, 9).
- **P5 source CSVs are not in this workspace**, so the data analysis is not
  re-runnable here (`workspace-audit.md` G4). This now also blocks all three
  agents, none has ever run on real data.
- **The `channel` column name is unverified.** Channel values (organic, paid,
  referral) are quoted in `data/metric-diagnosis.md` H1, but that file reports
  the figures without its SQL, so the actual column name is recorded nowhere.
  Same for `platform` in H2. One `DESCRIBE nudge_users` settles both. Do not
  hand Raj a query built on the guess (`agents/anomaly-diagnosis.md` §3 step 4).
- **`outcome-log.md`'s `what_actually_happened` field has no owner.** It is
  human-written and it is the only input to the learning loop. Unowned, the
  stack will look like it is compounding while learning nothing
  (`agents/registry.md` §6 question 1).
- **H1 and H2 may not be independent.** `data/metric-diagnosis.md` H2 flags
  that channel and platform could be correlated and says the check was never
  run. Until it is, every channel figure could be a platform effect wearing a
  channel label. The missing check is one query: does the **control** arm show
  the same iOS/Android gap?
- **`change_log.md` has no entries for P4 or P5.** Do not read that as those
  lessons not having happened.
- Sprint kickoff date and team size beyond the triad, still unknown.
