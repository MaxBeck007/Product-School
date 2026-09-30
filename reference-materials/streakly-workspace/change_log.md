# Streakly, Comeback Experience: Change Log

> Note: this file was meant to be initialized in P1L4 (part of the three core
> files). We skipped ahead to P2/P3 before that lesson ran, so Entry 1 below was
> originally the first entry rather than day 1 of discovery. **Backfilled
> 2026-09-30:** Entry 0 now logs that day-1 kickoff. Per `workspace-audit.md`
> §3 (R9 / "deliberately not recommended"), `project.md` and `strategy.md` are
> staying unbuilt as separate files, Max confirmed on 2026-09-30 that the
> content already living in `CLAUDE.md`, `docs/decision-brief.md`, and
> `docs/hypothesis.md` should stay the one source rather than adding two more
> places for the same facts to drift.

---

## Entry 0 (backfilled), P1L4, day 1 of discovery logged

**Date of the work being logged:** 2026-09-28 (P1, the original session).
**Entry written:** 2026-09-30, closing the specific P1L4 gap named in this
file's header note and in `workspace-audit.md`'s artifact map ("P1L4 →
`change_log.md`, partial"). Reconstructed from `project-skeleton.md`,
`CLAUDE.md`, and `docs/decision-brief.md`, not from session notes.

**What happened:** day 1 of discovery for the Streakly Comeback experience.
Role and squad confirmed: PM, Engagement squad; triad is Raj (Senior Engineer)
and Lena (Product Designer); reports to Marcus, Head of Product
(`project-skeleton.md` Participants table). Current phase: discovery, no
committed scope, 8 weeks from sprint kickoff.

**The hypothesis logged today:** users go passive after breaking a streak
because the reset feels like failure with no graceful way back in, not because
the daily lessons are bad. The bet under discovery: a personalized Comeback
screen (best-streak stat, 60-second comeback lesson, one-tap streak-freeze),
in place of the current cold reset-to-zero (`project-skeleton.md` "Solution
direction discussed, not committed").

**Key tension carried into every future session:** re-engagement nudges vs.
notification fatigue, users who feel nagged turn notifications off entirely,
closing the one channel that could otherwise win them back after a lapse
(`CLAUDE.md`).

**Changes made:** none, this entry documents kickoff, it does not action
anything.

**Open item carried forward:** the four questions `project-skeleton.md` left
open, whether the root cause is the reset, notification timing, or both;
who qualifies for a comeback experience and what the freeze rules are; what
Day-7 target counts as success and by when; whether notification tone/cadence
is in scope. All four were still open as of the 2026-09-30 backfill.

---

## Entry 1, P3L2 usability pass on Prototype v1

**Date:** 2026-09-28 (session date, not a real calendar milestone in the scenario)

**What happened:** ran a usability pass against `prototype/index.html` using 3
mock sessions (Priya, Tom, Amara), see `research/usability-session-1.md`.
**Label: mock/illustrative data, no real sessions occurred.**

**What was working:** the "welcome back" tone reads as a real departure from a
punishing reset across all three personas; the best-streak stat needed no
explanation; the freeze mechanic earned Tom's trust once he actually tapped it,
the copy alone didn't.

**Top 2 friction points identified:**
1. Lesson content is fixed to the guitar track, not personalized to the user's
   actual track (Priya).
2. The lesson's quiz-style check-in reintroduced pass/fail pressure, the exact
   feeling the feature exists to remove (Amara, echoed by Tom's broader
   skepticism).

**Change made:** removed the "must pick the right answer to continue" gate on
the comeback lesson quiz in `prototype/index.html`. Any answer now shows an
affirming message ("Nice, chords take reps either way") and unlocks Continue.
No answer is marked wrong.

**Reasoning:** friction #2 directly undermines the feature's core premise
(forgiving, not punishing) for exactly the anxious, early-lapse user segment the
feature is meant to protect. Friction #1 (track personalization) is a real gap
but is a data/scope decision for a later pass, not a fix to what's already
built, so it's logged here as an open item rather than actioned yet.

**Open item carried forward:** personalize the comeback lesson to the user's
actual pre-lapse track instead of a fixed guitar example.

---

## Entry 2, P3L2a agentic interview (in-character persona test)

**Date:** 2026-09-28

**What happened:** ran an in-character test against Prototype v1 (post Entry 1
fix) as Priya, Tom, and Amara, answering the standard 4 questions per persona.
**Label: mock/illustrative, not a real user test.** Full transcript in this
session's chat, not saved as a separate file since the course exercise doesn't
call for one.

**What surprised me:** Tom's trust in the "no cost, no catch" freeze copy didn't
move until he actually performed the tap and saw the confirmation, the copy
alone didn't do it. Amara surfaced a new issue even after the Entry 1 fix already
removed the pass/fail quiz gate: the label "Quick check" still primed test-like
anxiety on its own, independent of how the mechanic actually behaves.

**Most concerning answer:** Tom comparing "no cost, no catch" to what an app says
"right before it asks me to pay," specifically because he's a previously-churned,
already-skeptical user, exactly the segment this feature most needs to win back,
and he might not have tapped the button to find out it was genuine.

**Change made:** relabeled the lesson's quiz prompt from "Quick check: which
chord did you just practice?" to "Just for fun, which chord was that?" in
`prototype/index.html`.

**Reasoning:** the mechanic was already fixed in Entry 1 (no wrong answers), but
Amara's reaction showed the copy itself was still doing the damage independent of
the mechanic. This is a small, low-risk copy fix, not a scope change.

**Open item carried forward:** Tom's skepticism about the freeze claim is not
resolved by copy alone, an open question for the next round is whether the
freeze should visibly resolve itself (e.g. shown as already-applied) rather than
requiring the user to tap and then trust the result. Not actioned yet because it
would change the "one-tap streak-freeze offer" mechanic specified in the
original brief, that's a product decision, not a copy fix.

---

## Entry 2a, P4, working with the team (backfilled)

**Date of work:** 2026-09-28. **Entry written:** 2026-09-28, during P7 (fix F3
in `docs/capstone-session.md`). Numbered 2a/2b to preserve the original
sequence rather than renumbering entries that are already cited elsewhere.
**Reconstructed from the artifacts themselves, not from session notes**, so it
records what the files say, not everything that was discussed.

**What happened:** four P4 lessons produced four artifacts.

- **P4L1, codebase tour →** `docs/codebase-summary.md`. Written against a
  **reference** codebase, not Streakly's. Its main finding: the fields the
  freeze rule needs (pre-break streak length, freeze-spent state) may not
  exist. Transferability to the real codebase is unverified.
- **P4L1.5, stakeholder profiles →** `stakeholders/{raj,lena,marcus}.md`.
  **Constructed from the scenario document**, not from working with these
  people.
- **P4L2, spec readiness →** `docs/spec-readiness.md`. **Fully roleplayed**,
  both "Raj" and "Max" generated by Claude at Max's explicit request.
- **P4L3, design review →** `docs/design-review.md`. **Fully roleplayed**,
  both "Lena" and "Max" generated.
- **P4L4, QA and launch →** `docs/qa-checklist.md`. Edge-case list plus a
  10-row PM QA table run against `prototype/index.html`.

**Most valuable finding:** `docs/spec-readiness.md` caught that the brief
conflated "no new integrations" with "no new fields." The freeze rule needs
pre-break streak length and freeze-spent state, which is a real scope item that
the original constraint appeared to rule out. `docs/pm-brief.md`'s constraint
wording was rewritten as a result, and the corrected version is now in
`CLAUDE.md`. `docs/codebase-summary.md` reached the same gap independently,
which is what raised confidence in it despite both artifacts being
non-authoritative.

**Second finding, under-recorded until P7:** `docs/design-review.md` Part 3
argued that the Comeback screen is reactive-only and therefore structurally
cannot reach users who are anxious but have not lapsed, while Day-7 retention
measures a population that includes them. This sat only in that file until the
P7L4 capstone, and is now `docs/prd.md` Open Question 8.

**Changes made:** `docs/pm-brief.md` constraint section rewritten (see
`docs/spec-readiness.md` for before and after). No prototype changes; four QA
rows failed, but all four are gaps between what was *discussed* and what is
*built*, not prototype bugs.

**Open items carried forward:** freeze eligibility rule is a proposal only
(one per lapse, streaks 3+ days, no stacking), untested and not in the
prototype. Empty state undesigned. Whether the freeze should self-resolve
rather than require a tap.

---

## Entry 2b, P5, the data work (backfilled)

**Date of work:** 2026-09-28. **Entry written:** 2026-09-28, during P7 (fix F3).
Reconstructed from the artifacts.

**What happened:** four P5 lessons produced four artifacts, all computed rather
than estimated.

- **P5L1, answers from data →** `data/metric-findings.md`. Four questions run in
  DuckDB against five CSVs (500 users, 2,347 sessions, 1,740 nudges, 500
  retention rows, 400 weekly summary sends), with the SQL shown.
- **P5L2, what moved the metric →** `data/metric-diagnosis.md`. Identified a
  rising break rate among starters, 38.9% → 56.5% across four cohort weeks, as
  the driver, rather than a falling start rate or a failing notification
  channel.
- **P5L3, recommendations →** `docs/recommendation-memo.md`, plus
  `docs/one-pager.md`.
- **P5L4, experiment design →** `data/experiment-design.md`. Significance check
  and power calculation run in `scipy`/`statsmodels`: pilot z = 3.075,
  p = 0.0021, cross-checked with Fisher's exact at p = 0.0038; required sample
  ≈1,568 per variant to detect a 5pt lift at 80% power.

**Headline result:** treatment 76% vs control 46% Day-7 in cohort week 5
(n=50/variant), 36% vs 22% at Day-30, with treatment send open rates climbing
28% → 56% across four sends while control stayed flat at 4-6%.

**Two things flagged rather than guessed past.** First,
`data/experiment-design.md` Step 4 refused to estimate the weekly eligible-user
volume, since the illustrative ~100-signups-per-cohort-week dataset cannot
stand in for 85,000 WAU. That number is still the input blocking any committed
test duration. Second, `data/metric-findings.md` Q2 states plainly that "broke
their streak" is a proxy (day-1 active, day-7 inactive) because no
streak-break event field exists in the data.

**Most concerning finding, named during P7 rather than here:** this entire P5
stack works from a dataset in which the Comeback screen had **already
shipped**, while every P3 and P4 artifact treats it as unbuilt. Nothing
actually shipped. See the "What is actually real" section of `CLAUDE.md`.

**Changes made:** none to the prototype or spec. P5 produced analysis, not
product changes.

**Open items carried forward:** weekly eligible-user volume unconfirmed; test
duration uncommitted; the five source CSVs are not saved in this workspace, so
none of the P5 analysis is re-runnable here.

---

## Entry 3, P6L1/P6L2, PRD drafted and pressure-tested

**Date:** 2026-09-28

**What happened:** wrote `docs/prd.md` for Raj and Lena from the full P2/P3
research stack (`research/interview-synthesis.md`, `research/nps-analysis.md`,
`research/competitive-matrix.md`, `research/competitive-reddit.md`,
`docs/hypothesis.md`, `docs/decision-brief.md`). Then pressure-tested it
against constructed Raj, Marcus, and Tom reviewer profiles, saved to
`docs/objection-log.md`. **Label: objection-log questions are constructed to
match each person's documented pattern, not real quotes from a real review.**

**Correction made during drafting:** the PRD initially cited the 38.9% →
56.5% break-rate figure to `data/metric-findings.md`; it actually lives in
`data/metric-diagnosis.md`, and the metric is break rate among starters
(day-1 active, day-7 not), not all new users generally. Fixed before saving.

**Most concerning finding:** of the three reviewers' objections, Tom's
question about discovery (would he have even seen the Comeback screen, given
he'd already turned off notifications before churning) is the one judged most
likely to kill the initiative if unaddressed. Raj's and Marcus's objections
are real but have a clear owner and a clear path to an answer; Tom's exposes
a gap the PRD doesn't currently name anywhere, including its own Open
Questions section, how a user who has disengaged from notifications ever
sees the feature that exists to win them back.

**Change made:** none to the prototype or spec yet, this entry documents the
PRD and objection log as artifacts, not an actioned fix.

**Open item carried forward:** add the notification-independent trigger
question to `docs/prd.md`'s Open Questions before the next Raj/Marcus review,
so it doesn't surface for the first time in that meeting. Also still open
from Entry 1/2: track personalization, and whether the freeze should
visibly resolve itself vs. requiring a tap.

---

## Entry 4, P7 (all five lessons), workspace formalized

**Date:** 2026-09-28

**What happened:** ran P7L1 through P7L5 in one session.

- **P7L1:** audited the folder (42 files) and rewrote `CLAUDE.md`. Audit saved
  to `workspace-audit.md`, 8 gaps (G1-G8) and 9 reorganization options (R1-R9).
  `CLAUDE.md` gained a file map, a document-precedence rule, a metric
  definitions section, and the evidence-label conventions.
- **P7L2:** three one-command workflows saved to `skills/`:
  `friday-status.md`, `research-pulse.md`, `competitive-pulse.md`. The existing
  `skills/weekly-status.md` is kept and now holds the stakeholder tone rules
  that `friday-status.md` calls.
- **P7L3:** `agents/monday-retention.md` plus a working script,
  `agents/monday_retention.py`.
- **P7L4:** capstone review saved to `docs/capstone-session.md`, per-artifact
  confidence ratings, three prioritized fixes, a reusable workspace prompt, and
  an approach for per-user stakeholder folders.
- **P7L5:** `docs/onboarding-guide.md` and `docs/onboarding-demo-script.md`.

**Correction made during the session:** the P7L3 script had a real bug. DuckDB
loads the pre-launch `variant = ''` values as NULL, so the previous week's
Day-7 figure was silently dropped and the digest reported "no comparable
figure" when one existed. Found by smoke-testing against **synthetic** CSVs
built to the schema in `data/metric-findings.md`, fixed, and re-verified. The
real CSVs are still absent, so the script has never produced a real number.

**Most concerning finding:** the workspace contradicts itself about whether
anything shipped. `docs/recommendation-memo.md` says the Comeback screen ran as
a 50/50 pilot to 100 users in cohort week 5; `CLAUDE.md`,
`docs/hypothesis.md`, and `prototype/README.md` all say nothing exists beyond a
click-through prototype. Both trace to the course structure (P5 supplied a
dataset in which the experiment had already run), but a real collaborator
reading both cannot tell which is true, and the question undermines every
number in the room. Logged as fix F1 in `docs/capstone-session.md`.

**Second finding worth carrying:** `docs/design-review.md` contains the
sharpest strategic argument in the workspace and it was not recorded as a gap
anywhere, the Comeback screen only reaches users who have already lapsed, while
Day-7 retention measures a population that includes users who are anxious and
have not lapsed. A reactive-only fix structurally cannot reach them. Added to
`CLAUDE.md` Known gaps this session.

**Changes made:** `CLAUDE.md` rewritten and then extended with both findings
above. No changes to the prototype, PRD, or any research artifact.

---

## Entry 5, P7L4 fixes F1-F3 implemented

**Date:** 2026-09-28. Max approved all three fixes from
`docs/capstone-session.md` section 3.

**F1, the shipped-vs-not contradiction.** Added a "What is actually real"
section to `CLAUDE.md` that sorts every artifact into Framing A (concept
unbuilt) or Framing B (a pilot already ran) and states plainly that nothing
shipped, Framing B is the P5 exercise dataset. Added scope headers to
`docs/recommendation-memo.md` and `docs/one-pager.md`, the two documents most
likely to be handed to someone, since both lead with pilot figures.

**F2, missing PRD open questions.** Added the reactive-only scope gap as
`docs/prd.md` Open Question 8.

**Premise error found and corrected during this fix.** The capstone claimed
*both* gaps were missing from the PRD. Wrong: the notification-independent
trigger was already Open Question 7, added after Entry 3 flagged it. The
capstone asserted it was absent without reading `docs/prd.md` in full, which is
exactly what that file's own "not read in full" disclaimer was warning about.
`docs/capstone-session.md` and `CLAUDE.md` both corrected. Worth noting as a
pattern: the disclaimer was accurate and the claim still went out, so a
disclaimer is not a substitute for reading the file.

**F3, change log and labeling.** Backfilled Entries 2a (P4) and 2b (P5), both
reconstructed from the artifacts rather than session notes and labeled as such.
Numbered 2a/2b rather than renumbering entries already cited elsewhere. Added a
one-line bold tag at the very top of the five files whose contents are not real:
`docs/spec-readiness.md` and `docs/design-review.md` (roleplayed),
`docs/triad-session.md` (agenda for a meeting that has not happened),
`docs/objection-log.md` (constructed objections), and
`research/usability-session-1.md` (mock sessions). Each already had a header
note; the tags are positioned so the warning survives a partial read or a
quote pulled out of context.

**Changes made:** no prototype, research, or data changes. All edits were
labeling, sourcing, and one new open question.

**Open items carried forward:** unchanged from Entry 4 and earlier, track
personalization, freeze self-resolution, notification-independent trigger
(documented, not answered), reactive-only scope decision, weekly eligible-user
volume, and the missing P5 source CSVs. Deferred from `workspace-audit.md`:
R1 `open-items.md`, R3 `docs/definitions.md`, R4 stakeholder template and a
profile for Max, and the R6-R8 file moves.

---

## Entry 6, reactive-only scope decision made

**Date:** 2026-09-30. Max decided, reviewing `docs/design-review.md` Part 3 and
`docs/prd.md` Open Question 8 directly (this was not roleplayed).

**What happened:** `docs/design-review.md` Part 3 named the sharpest unresolved
strategic gap in the workspace: the Comeback screen only reaches a user *after*
they lapse, but Day-7 retention measures a population that also includes
anxious, not-yet-lapsed users (Amara's profile, day 4). `docs/prd.md` Open
Question 8 named the same gap and left it as a choice between two options:
name it a non-goal and accept the ceiling, or scope a proactive piece as
parallel work. It was logged as "currently neither," undecided.

**Decision made: expand scope.** The Comeback experience will include a
proactive, anticipatory piece for users who are anxious but have not yet
broken a streak, alongside the existing reactive Comeback screen for users who
have. This is a real scope decision, not a roleplay output.

**What this decision does not do:** it does not yet define what the proactive
piece is. No mechanic, screen, or trigger has been specified. That is new,
unstarted work, not a detail filled in here.

**Changes made:** none to the prototype, PRD text, or design review content
itself. `docs/prd.md` Open Question 8 and `docs/design-review.md` Part 3 each
get a short resolution note pointing to this entry rather than being rewritten,
so the original roleplayed reasoning that led here stays intact and readable.

**Open item carried forward, new:** define the proactive/anticipatory
intervention, mechanic, trigger, and how it's measured (likely a leading
indicator distinct from Day-7 retention, since by definition it targets users
who have not yet lapsed). Not yet scoped in any file.
