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
1. Lesson content is fixed to the miniature-painting track, not personalized
   to the user's actual track (Priya).
2. The lesson's quiz-style check-in reintroduced pass/fail pressure, the exact
   feeling the feature exists to remove (Amara, echoed by Tom's broader
   skepticism).

**Change made:** removed the "must pick the right answer to continue" gate on
the comeback lesson quiz in `prototype/index.html`. Any answer now shows an
affirming message ("Nice, brushwork takes reps either way") and unlocks
Continue. No answer is marked wrong.

**Reasoning:** friction #2 directly undermines the feature's core premise
(forgiving, not punishing) for exactly the anxious, early-lapse user segment the
feature is meant to protect. Friction #1 (track personalization) is a real gap
but is a data/scope decision for a later pass, not a fix to what's already
built, so it's logged here as an open item rather than actioned yet.

**Open item carried forward:** personalize the comeback lesson to the user's
actual pre-lapse track instead of a fixed miniature-painting example.

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
color did you just apply?" to "Just for fun, which color was that?" in
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

---

## Entry 7, comeback lesson check-in changed: quiz → photo

**Date:** 2026-09-30. Max instructed this directly, not roleplayed, not
triggered by usability feedback.

**What happened:** the check-in mechanic in `prototype/index.html` changed
from the 3-option multiple-choice quiz ("Just for fun, which color was
that?") to a photo capture
(`<input type="file" accept="image/*" capture="environment">`) styled as a
drop zone, plus a "Skip today, no photo" option. Either path shows the same
affirming message and unlocks Continue, no pass/fail, same principle as the
original P3L2 quiz-gate fix, just applied to a mechanic that has no "correct
answer" to gate on in the first place.

- The "60-SECOND COMEBACK LESSON" eyebrow, the "Comeback lesson" header, and
  the "1 min" meta text were **left as-is** in this pass. Whether a discrete
  "60-second lesson" framing fits a painting session is an open question,
  not resolved here.

**Why:** direct instruction, no research citation to attach.

**Changes made:** `prototype/index.html` only, as described above.
`prototype/README.md` and the CLAUDE.md gap list are updated separately to
match.

**Open item carried forward:** whether "60-second lesson" is the right frame
for a craft session that doesn't fit a fixed time box. Untested against this
version. See Entry 8 for a first read on this from a new persona.

---

## Entry 8, P3L2a rerun with a new persona (Dax), one fix made

**Date:** 2026-09-30. **Label: mock/illustrative.** Dax (`personas/dax.md`) is
a constructed persona, not a real user. Full transcript:
`research/usability-session-2-dax.md`.

**What happened:** ran the standard 4 P3L2/P3L2a questions against
`prototype/index.html` as it stood after Entry 7, in character as Dax, a
competitive tabletop wargamer built specifically to stress-test the new
miniature-painting content with hobby-fluent skepticism Priya/Tom/Amara can't
provide.

**What was working:** the best-streak stat carrying over (not resetting) and
the streak-freeze both landed with him as they did for the other personas.
The reference card's instruction text ("basecoat is dry, add one highlight
layer") read as authentic, not invented-sounding.

**Top 2 friction points:**
1. **"60-second lesson" framing doesn't fit the craft.** Painting requires
   dry time between coats; a fixed time box reads as evidence the app doesn't
   actually understand the hobby, which damages trust in everything else on
   the screen, not just the time claim.
2. **"No critique" reads as pointless, not reassuring, to this segment.** The
   copy that removes pressure for Amara removes the entire point of
   photographing progress for Dax, a craft hobbyist expects a photo to be
   looked at. Same line, opposite effect depending on the user, an echo of
   the same-mechanic-opposite-effect pattern the original interview synthesis
   found in Priya vs. Tom/Amara (`research/interview-synthesis.md`,
   Contradictions).

**Change made:** dropped the "60-second lesson" time-box framing. "60-SECOND
COMEBACK LESSON" → "Today's comeback session," "Comeback lesson" header →
"Comeback session," removed "1 min" from the lesson-card meta line, and the
primary CTA "Start the 1-minute lesson" → "Start today's session" (missed on
the first pass, same mismatch Dax named, caught on review). Fix #2 (the "no
critique" tension) was **not** actioned, see below.

**Reasoning:** fix #1 is a labeling mismatch, low-risk, matches the class of
fix already used for the original quiz-gate/label corrections (Entries 1-2).
Fix #2 is a segmentation question, does this screen serve craft-serious users
differently than anxious early-lapse users, not something a copy tweak
resolves, and picking a resolution here would be inventing a product
decision Dax's feedback alone doesn't settle.

**Open item carried forward:** the "no critique" tension (friction #2) is
unresolved. Whether the Comeback screen needs to know which kind of user it's
talking to, or whether one forgiving default is an acceptable tradeoff across
segments, is a real open product question, not decided in this entry.

---

## Entry 9, P3L4 triad session run for real (Max, Raj, Lena), roleplayed

**Date:** 2026-09-30. **Label: fully roleplayed, not a real meeting.** Full
transcript: `docs/triad-session-transcript.md`. All three voices, including
Max, generated by Claude at Max's explicit request. Follows the actual
`docs/triad-session.md` agenda exactly, same attendees as scripted (Raj,
Lena, PM), no additions.

**What happened:** ran the P3L4 exercise end to end instead of leaving it as
a prepared-but-unheld agenda. Walked the prototype, ran Raj's 3 feasibility
questions and Lena's 3 experience questions exactly as drafted, and reached
real decisions on the "Decisions to walk out with" list.

**Decisions made:**
1. **Personalization:** ship the single miniature-painting example for the
   first test; personalizing to the user's actual pre-lapse track becomes
   its own ticket, not a blocker.
2. **Freeze interaction:** switch from one-tap to pre-applied/auto-resolved,
   shown as already done. Raj's read: this is *less* implementation work,
   not more, the eligibility check already has to run server-side before
   the screen renders. Directly answers Tom's mock-feedback skepticism from
   Entry 2, tap-and-trust never fully earned his trust.
3. **Empty state:** confirmed undesigned, scheduled before the next round of
   testing (not before this review, not indefinitely deferred). Owner: Lena.

**New, undecided flag from Lena:** whether "no critique" on the photo
check-in reads as dismissive to a user who'd want feedback, not just as
reassuring to an anxious one. No evidence either way yet, not resolved here.

**Change made:** filled in `docs/triad-session.md`'s Post-Session Alignment
Doc template with the decisions above. Decision 2 (freeze mechanic)
implemented, see Entry 10.

**Open item carried forward:** decision 1 (personalization ticket) and
decision 3 (empty-state design) are scheduling commitments, not yet
executed. Lena's "no critique" flag is unresolved.

---

## Entry 10, freeze mechanic changed: one-tap → pre-applied

**Date:** 2026-09-30. Implements the Entry 9 triad decision, not roleplayed
itself.

**What happened:** in `prototype/index.html`, the freeze offer no longer
requires a tap. The "Apply streak freeze" button and its confirmation toast
are gone; the freeze card now renders already resolved ("Streak freeze
applied... Already done, nothing to tap.") as soon as the comeback screen
loads. `applyFreeze()` and the toast element were removed; `restart()`
updated to match (no freeze-button state to reset).

**Why:** Entry 9, Raj's read that pre-applied is less state to manage than
one-tap, and it directly answers Tom's persistent skepticism (Entry 2) that
copy alone, "no cost, no catch," never earned his trust, only seeing the
mechanic resolve did. Pre-applied removes the tap-then-trust gap entirely
instead of asking copy to close it.

**Verified live:** started the lesson, skipped the photo, finished to the
done screen, and restarted, full flow still works with no freeze button in
the loop.

**Open item carried forward:** none, `docs/prd.md` Story 5's acceptance
criteria and Open Question 3 were updated in this same pass to match.

---

## Entry 11, stakeholder color profiles added (Insights Discovery model)

**Date:** 2026-09-30. Max asked for each stakeholder to get an Insights
Discovery color profile (Cool Blue / Fiery Red / Earth Green / Sunshine
Yellow) based on a wheel image they shared. **Label: inferred, not a real
assessment.** No one took an actual Insights Discovery survey; these are
Claude's read of documented behavior, sourced the same way the rest of each
profile already is.

**What happened:** added a color-profile section to each of
`stakeholders/raj.md`, `stakeholders/lena.md`, `stakeholders/marcus.md`.

- **Raj:** primary Cool Blue (analytical-before-opinion, wants acceptance
  criteria and edge cases named upfront, async/bullet-point communicator),
  secondary Earth Green (pushes back on disruption and scope creep, not on
  slowness).
- **Lena:** primary Earth Green (leads with "here's what users told us"
  before her own design opinion, wants the empty state defined so no real
  user hits a broken moment), secondary Cool Blue (won't design from a vibe,
  wants to see the evidence directly).
- **Marcus:** primary Fiery Red (wants the recommendation in the first
  sentence, separates problem from solution on purpose, moves fast once a
  framing is concrete), secondary Cool Blue (wants the ask connected to a
  specific number, not a hunch).

**Reasoning:** each profile's color read is tied to a specific already-
sourced quote or behavior in that person's file, not invented from the role
title alone (a designer doesn't have to be Yellow, an engineer doesn't have
to be Blue, both colors here are argued from evidence already in the
workspace).

**Changes made:** three stakeholder files only. No change to
`docs/spec-readiness.md` or `docs/design-review.md`, this doesn't retroactively
change what roleplayed-Raj or roleplayed-Lena already said, it's a new lens
on the same documented behavior.

**Open item carried forward:** none.

---

## Entry 12, Raj T-shirt sizes the effort (end of Module 4), roleplayed

**Date:** 2026-09-30. **Label: roleplayed, not a real estimate.** Full
writeup: `docs/effort-tshirt-sizing.md`. Not a scripted course exercise,
Max asked for this directly, grounded in everything accumulated through P4.

**What happened:** sized the reactive Comeback screen only (schema change +
migration, freeze eligibility logic, client build, empty-state edge case),
explicitly excluding personalization (already its own ticket) and the
proactive piece (no concept exists, sizing nothing would be a guess).

**The size: L.** Schema change and migration is the long pole, not the
client screen, the equivalent of the `User` model is touched everywhere
(`docs/codebase-summary.md` section 5).

**Assumption the size depends on, stated rather than buried:** the
discovery trigger is assumed to be a cheap server-side check on next app
open. If it actually needs new push notification infrastructure, size
becomes **XL** instead. This ties a real cost to `docs/prd.md` Open
Question 7, which was previously just a documented gap, not a decision with
a price attached.

**Change made:** new file only, `docs/effort-tshirt-sizing.md`. No changes
to `docs/prd.md`, `docs/spec-readiness.md`, or the prototype.

**Open item carried forward:** `docs/prd.md` Open Question 7 (discovery
trigger) now has a cost attached (L vs. XL), which raises its priority
relative to the other open questions, but the question itself is still
unresolved.

---

## Entry 13, Raj translates L into weeks, roleplayed

**Date:** 2026-09-30. **Label: roleplayed, not a real estimate.** Follow-up
to Entry 12, added to `docs/effort-tshirt-sizing.md` rather than a new file.

**What happened:** Max asked what "L" means in weeks. Raj flagged upfront
that there's no real sprint velocity in this workspace to calibrate
against, then sized the individual pieces from Entry 12 and added them up
instead of guessing at a label.

**The number: roughly 2.5-3 weeks for one engineer** (Raj, this squad has
no second backend engineer), with the schema/migration work (1-1.5 weeks)
as the long pole and the client build explicitly sequential to it, not
parallel.

**Change made:** appended to `docs/effort-tshirt-sizing.md`, no new file.

**Open item carried forward:** unchanged from Entry 12, the discovery
trigger question still decides whether this stays at ~3 weeks or grows past
it into unsized XL work.

---

## Entry 14, final presentation deck redesigned with real charts

**Date:** 2026-10-02. Max asked for the deck to be made more visually
appealing, not a roleplay, a direct design request against `06-systems/final-presentation.html`.

**What happened:** rebuilt the deck using the house dataviz method (form
before color, a validated palette, direct labels, status colors reserved
for state not series). Every number that was previously a static text stat
is now an actual chart:

- Slide 1: two dumbbells (48%&rarr;39% Day-7; 38.9%&rarr;56.5% break rate),
  the before/after form, not a one-bar bar chart.
- Slide 2: a 4-point line (cohort weeks 1-4 decline) and an emphasis bar
  pair (broke-in-week-1 vs. sustained), accent color on the number that's
  the point, muted gray on the baseline.
- Slide 4: a grouped bar (treatment vs. control, Day-7 and Day-30) and a
  2-line chart (open rate across 4 sends), both with a legend since 2
  series are genuinely being compared.
- Slide 5: status chips (good-green for the one milestone reached,
  warning-amber for each open item), icon + label per the palette's status
  rule, never color alone.
- Slide 3: converted the bullet lists to a dot/dash icon system distinguishing
  "is" from "isn't" at a glance.

**Fixed while rebuilding:** the deck still said "60-second lesson" and
"one-tap streak-freeze" in three places (slides 3, 4's notes, the proposal
copy), the same staleness flagged during the P6L4 walkthrough. Now reads
"comeback session" and "pre-applied streak-freeze" throughout, consistent
with Entries 8 and 10.

**Verified:** resized the live page to 1000px and 1440px and checked
computed layout (no horizontal overflow, no clipped cards), clicked through
all 6 slides and confirmed the notes panel and counter work via real
navigation, not just visual inspection.

**Not touched:** `reference-materials/streakly-workspace/docs/presentation.html`
and `docs/presentation.md`, the raw workspace's own copies, left as the
historical pre-redesign record. `06-systems/final-presentation.html` is the
capstone's actual submitted artifact and the one this request was about.

**Open item carried forward:** none.

---

## Entry 15, closed workspace-audit gaps G2 and G6; confirmed G7 already closed

**Date:** 2026-10-02. Max asked to act on `workspace-audit.md`'s deferred
R1 and R4 recommendations.

**What happened:**
- **R1 / G2 (no single open-items file):** added `open-items.md`,
  consolidating what was scattered across `change_log.md` carry-forwards,
  `docs/prd.md` Open Questions, `data/experiment-design.md`, and
  `CLAUDE.md`'s Known gaps. Resolved items are kept struck-through with the
  entry that closed them, not deleted.
- **R4 / G6 (no stakeholder template, no profile for Max):** added
  `stakeholders/_template.md` (reusable for a new teammate or product) and
  `stakeholders/max.md`, sourced entirely from `CLAUDE.md`'s existing
  "How I Want Claude to Work With Me" and "Working habits" sections, not
  invented. Includes an Insights Discovery read (Cool Blue primary, Fiery
  Red secondary), extending the pattern from Entry 11.
- **R3 / G7 (no metric glossary):** checked first rather than assumed.
  Already closed, folded into `CLAUDE.md`'s "Metric definitions, use these
  exactly" section during the same P7L1 pass that found the gap. No
  duplicate file created.
- Added all three new files to `CLAUDE.md`'s file map.

**Change made:** three new files (`open-items.md`,
`stakeholders/_template.md`, `stakeholders/max.md`), plus three new rows
in `CLAUDE.md`'s "Where to look for what" table.

**Open item carried forward:** R6-R8 (file-move reorg) remain explicitly
deferred, unchanged from the original audit.

---

## Entry 16, Monday retention agent run for real against real data

**Date:** 2026-10-02. Not roleplayed. Max asked to actually close
`workspace-audit.md` G4 rather than leave it as an offer.

**What happened:** copied the 5 real CSVs Max added to `reference-materials/`
on 2026-09-28 into `data/raw/`, renamed to match the schema
`agents/monday_retention.py` expects (`nudge_users.csv`, etc.), installed
`duckdb`, and ran the script for real: `python agents/monday_retention.py
--week 5 --compare-week 4`.

**It failed twice before it ran, for real reasons, each fixed and kept:**
1. `AVG(BOOLEAN)` error, the real CSVs use literal `true`/`false`, not 0/1
   integers as assumed. Cast with `::INT`.
2. `KeyError: 'all'`, the real variant label is `"comeback"`, not
   `"summary_v1"`. Every reference in `build()` updated.
3. (Caught before running, by inspecting headers first) the real
   `nudge_weekly_summary_sends` column is `send_number`, not `week_number`.

**Step 2 of the script's own verification protocol passed exactly:**
treatment 76.0% vs. control 46.0% in week 5, matching `data/metric-findings.md`
Q3 to the decimal. First real-data result any agent in this workspace has
ever produced.

**Second finding, not smoothed over:** the same real data's cohort weeks 1-4
(Day-7 retention and break rate, queried directly, independent of the
week-5 split) do not match what `data/metric-findings.md` Q1 and
`data/metric-diagnosis.md` report for those cohorts. Same row counts per
cohort (100), same schema, different values. Week 5 (both blended and
split by variant) matches closely. **Guess, not confirmed:** a reseeded or
regenerated sample from a shared course dataset. **Not actioned:**
`metric-findings.md`/`metric-diagnosis.md` were not rewritten, that's a
bigger call than a script fix.

**Change made:** `data/raw/*.csv` added (5 files), `agents/monday_retention.py`
fixed (3 schema corrections), `agents/monday-retention.md` updated with the
real run and the full discrepancy table.

**Open item carried forward, new:** reconcile or explain the weeks 1-4
discrepancy between `data/metric-findings.md`/`data/metric-diagnosis.md`
and the real CSVs now in `data/raw/`. Added to `open-items.md`.

---

## Entry 17, column name resolved; a real streak-break field investigated, not oversold

**Date:** 2026-10-02. Max asked for a reasonable next step out of the P8
walkthrough. Not roleplayed.

**What happened, part 1, the easy close:** three files
(`agents/metric-pulse.md` §8.2, `agents/anomaly-diagnosis.md` §3 step 4 and
§7.2, `agents/registry.md` §6.3) independently flagged the same unverified
question, is the channel column actually named `channel`. Ran `DESCRIBE
nudge_users` against the real, restored CSVs: **it's `acquisition_channel`,
not `channel`**; `platform` is named as assumed. Fixed the example SQL in
`anomaly-diagnosis.md` §3 step 4 to match (also fixed its variant label and
boolean cast, same issues as `change_log.md` Entry 16), and closed the
question in all three files plus the registry's top-of-file status banner.

**What happened, part 2, the one worth being careful about.** `nudge_users.csv`
and `nudge_retention.csv` both carry a field, `broke_streak_week1`, that
doesn't exist in the course's originally-described schema and that nobody in
this workspace knew about until this session. Every break-rate figure
everywhere (`CLAUDE.md`'s glossary, `data/metric-findings.md` Q2,
`data/metric-diagnosis.md`) is explicitly labeled a proxy, day-1-active and
day-7-inactive, because "no literal streak-break event field exists in the
data." That sentence needed checking now that one appears to.

**Checked, not assumed:** cross-tabbed `broke_streak_week1` against the
day_1/day_7 proxy for all 457 "starters" (day_1 = true). **Agreement: 57.3%
(262/457).** That is not a validation of the proxy and not a refutation of
it, it's evidence the two fields measure **related but different things**:
`broke_streak_week1` appears to track whether a user's streak ever broke
during week 1 at any point, while the day_1/day_7 proxy tracks whether they
were active on two specific days. A user can break a streak mid-week and
still be active by day 7 (looks "sustained" to the proxy, "broke" to the
field), or vice versa. 129 of 276 proxy-"broke" users are *not* flagged by
the literal field; 48 of 181 proxy-"sustained" users *are*.

**Not actioned:** none of the "proxy" language in `CLAUDE.md`,
`data/metric-findings.md`, or `data/metric-diagnosis.md` was rewritten. A
57% agreement rate does not license swapping the proxy for the literal
field, or vice versa, that is a bigger analytical call than this check
settles, and `data/metric-diagnosis.md`'s whole metric tree is built on the
proxy. Logged as a real open question instead of a quiet upgrade.

**Change made:** `agents/metric-pulse.md`, `agents/anomaly-diagnosis.md`,
`agents/registry.md` (column name, 3 files); no changes to `CLAUDE.md`,
`data/metric-findings.md`, or `data/metric-diagnosis.md`.

**Open item carried forward, new:** what does `broke_streak_week1` actually
mean, and should any analysis prefer it over the proxy now that it exists?
Not decided here. Added to `open-items.md`.
