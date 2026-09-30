# PRD: Streakly Comeback Screen

> **Audience:** Raj (Senior Engineer) and Lena (Product Designer). Not a leadership doc.
> **Status:** discovery. No committed scope. Open questions in the last section are
> open on purpose, not placeholders.
> **Sources:** `research/interview-synthesis.md`, `research/nps-analysis.md`,
> `research/competitive-matrix.md`, `research/competitive-reddit.md`,
> `docs/hypothesis.md`, `docs/decision-brief.md`, `stakeholders/raj.md`,
> `stakeholders/lena.md`. Retention and pilot figures: `data/metric-diagnosis.md`,
> `data/metric-findings.md`, `data/experiment-design.md`.
> Every claim below cites a file. Anything not sourced is labeled Assumption or Guess.

---

## Problem Statement

Day-7 retention is 39%, down from 48% after the v2 streak and notification redesign
(`docs/decision-brief.md`, Situation). The measured driver is not fewer signups and
not a failing notification channel: it is a rising break rate among starters
(day-1 active, day-7 not), 38.9% to 56.5% across cohort weeks 1 to 4
(`data/metric-diagnosis.md`).

When a user breaks a streak today, the app resets the counter to zero, sends a
"you lost your streak" push, and returns them to an unchanged home screen. Six of
ten unprompted NPS (Net Promoter Score) comments name this punishing reset directly,
and two name a streak freeze as the fix they want by feature name
(`research/nps-analysis.md`). Lena's own read in the original thread was that the
push has "a brutal tone... It's jarring" (`stakeholders/lena.md`).

The structural problem is sequencing. Users hit the punishing side of the streak
mechanic before they ever reach the rewarding side. Priya's "look what you built"
moment took about three weeks; Amara is anxious at day 4 and Tom churned at week 5,
both well before that (`research/interview-synthesis.md`).

## User

**Primary user:** a Streakly user in their first 7 days who has just broken a streak
and has not yet reached any acknowledgment moment (`docs/hypothesis.md`,
Hypothesis Statement).

**Job to be done:** get back in without feeling they lost everything.

**Secondary user, not the design target:** a long-streak user who breaks a streak
later (Priya's segment). Behavior is different and the evidence is thinner, so this
PRD does not design for them (`research/interview-synthesis.md`).

**Empty state:** a user who has never held a streak longer than one day has no
best-streak stat to show. This is an unresolved design case, see Open Questions.

## Goals

1. Give a user who breaks a streak in week 1 an acknowledged, personal way back in
   rather than a cold reset (`docs/decision-brief.md`, Recommended Action).
2. Pair acknowledgment with one low-effort re-entry action in the same moment. No
   competitor does both today (`research/competitive-matrix.md`, gap 2).
3. Keep the comeback moment free and immediate. Duolingo's recovery mechanic is paid
   and transactional, and secondhand sentiment reads the paywall itself as the
   complaint (`research/competitive-matrix.md`, gap 1; `research/competitive-reddit.md`,
   lower confidence, aggregator sources only).

## Non-Goals

- **Notification tone and cadence.** A real theme, 2 of 10 NPS comments, but
  secondary to the reset and not scoped here (`docs/decision-brief.md`, finding 3).
  Whether it is a separate workstream is still unresolved.
- **New third-party integrations.** Ruled out by Raj in the original thread. New data
  *fields* (pre-break streak length, freeze-spent state) are in scope
  (`CLAUDE.md`, Constraints).
- **Personalizing lesson content to the user's own track.** A known gap from the P3
  prototype, carried as an open item, not scoped here (`change_log.md`, Entry 1).
- **Monetizing the freeze.** Goal 3 makes this an explicit non-goal.

## Success Metrics

**Primary:** Day-7 retention rate for users who break a streak in their first 7 days.
Current baseline 39% overall (`docs/decision-brief.md`).

**Reference result, not a target:** in the cohort week 5 pilot, treatment hit 76%
Day-7 and 36% Day-30 versus control at 46% and 22%, n=50 per variant
(`data/metric-findings.md`, Q3). The result is statistically significant
(p=0.0021) but the sample is too small to scale on directly
(`data/experiment-design.md`).

**No agreed success threshold exists yet.** No target value, measurement window, or
secondary metric has been decided (`project-skeleton.md`, Success Metrics). This is
the question Raj has effectively already asked: how will we know if this is working
after it ships (`stakeholders/raj.md`). It needs an answer before scope is committed.

**Guardrail proposed, not agreed:** break rate among new users should not rise, and
notification opt-out rate should not rise. `Assumption:` both are measurable from
existing data. **What would confirm it:** Raj confirming both are already
instrumented.

## User Stories

1. **Acknowledged instead of reset.** As a week-1 user who just missed two days, I
   want the app to show me what I actually built before it shows me a zero, so
   returning does not feel like starting from scratch (`research/nps-analysis.md`,
   theme 1; `research/interview-synthesis.md`, theme 1).
   *Acceptance:* on first open after a qualifying break, the user sees their
   pre-break best-streak value, not a zeroed counter, as the first thing on screen.

2. **One small thing to rebuild momentum.** As a returning user, I want one short
   lesson I can finish immediately, so I leave the session having done something
   rather than having been told what I lost (`research/competitive-matrix.md`, gap 2).
   *Acceptance:* the lesson is completable in roughly 60 seconds and has no pass or
   fail state. Any answer advances (`change_log.md`, Entry 1).

3. **Forgiveness without a price tag.** As a user who has broken a streak once, I
   want a way to protect the streak I am rebuilding without paying, so a second
   unplanned miss does not end the attempt (`research/nps-analysis.md`, theme 2, freeze
   requested by name; `research/competitive-matrix.md`, gap 1).
   *Acceptance:* the freeze is granted in one tap, at no cost, and the resulting
   state is visible to the user without leaving the screen.

4. **No test-like pressure.** As an anxious new user, I want the comeback moment to
   carry no evaluative framing, so it does not reproduce the pressure that made the
   streak feel like a chore (`research/interview-synthesis.md`, theme 4;
   `change_log.md`, Entry 2, where the label "Quick check" alone still primed test
   anxiety after the penalty had already been removed).
   *Acceptance:* no scoring, no correct-answer gate, and no evaluative language in
   any copy on the screen.

5. **Believing the offer.** As a previously skeptical user, I want the freeze to be
   visibly real rather than claimed, because copy alone did not earn my trust
   (`change_log.md`, Entry 2, Tom compared "no cost, no catch" to what an app says
   right before it asks him to pay).
   *Acceptance:* the freeze is pre-applied and shown as already resolved on
   screen load, no tap required (`change_log.md` Entry 10, decided in the
   P3L4 triad session).

## Open Questions

1. **Freeze eligibility and expiry rules.** Who qualifies, how often, what happens on
   a second break in the same week. Raj flagged this in the original thread and it is
   still unresolved through the P3 prototype (`stakeholders/raj.md`, Open items;
   `docs/codebase-summary.md`, section 6, which found the same gap independently).
   This is the one open item that blocks a spec, and it is mine to bring an answer to,
   not Raj's to ask a third time.
2. **Empty state.** What a user with no meaningful best streak sees instead. Lena's
   stated pattern is to define the empty state before the happy path
   (`stakeholders/lena.md`).
3. **Auto-apply versus one-tap freeze.** Resolved 2026-09-30: auto-apply.
   See story 5's acceptance criteria and `change_log.md` Entry 10.
4. **Success threshold and measurement window.** See Success Metrics. Undecided.
5. **Weekly eligible-user volume.** How many weekly active users break a streak per
   week is unconfirmed. The powered test needs roughly 0.46% of 85,000 WAU per week
   to fit an 8-week window (`data/experiment-design.md`, Step 4). Without this
   number, no test duration can be committed.
6. **Is notification tone in or out of scope, or a parallel workstream?** Raised in
   the original thread and never closed (`project-skeleton.md`, Open Questions).
7. **Discovery trigger.** This PRD specifies what the Comeback screen shows but not
   how a user reaches it. If the trigger depends on a push notification, it may not
   reach exactly the users it exists for: 2 of 10 NPS comments describe disabling
   notifications entirely (`research/nps-analysis.md`, theme 3), and Tom's own churn
   is tied to disengaging from notifications before he stopped opening the app
   (`research/interview-synthesis.md`). Added after pressure-testing surfaced it as
   the objection most likely to stall the initiative if raised for the first time in
   a Raj/Marcus review rather than named here first (`docs/objection-log.md`).
8. **Reactive-only reach: is this a named non-goal or a scope expansion?** The
   Comeback screen reaches a user only *after* a lapse. But the primary metric,
   Day-7 retention, measures a population that includes users who are anxious and
   have **not** lapsed, Amara is anxious from day 4 with nothing broken
   (`research/interview-synthesis.md`). A reactive-only fix structurally cannot
   reach her, so some share of the Day-7 number this PRD is accountable for is
   outside the feature's reach by design. Two honest options: name proactive
   reassurance as an explicit non-goal and accept the ceiling, or scope it as
   parallel work. Currently it is neither, which means the PRD implicitly claims
   more reach than the feature has. This is a product and roadmap call for PM and
   Marcus, not a design call (`docs/design-review.md`, Part 3). Added 2026-09-28
   after the P7L4 capstone review found it recorded in the design review but
   nowhere in the spec.

   **Resolved 2026-09-30 (`change_log.md`, Entry 6):** scope expands. The
   Comeback experience will include a proactive, anticipatory piece for
   not-yet-lapsed anxious users, alongside the existing reactive screen. The
   proactive piece itself is not yet designed, this closes the "which of the
   two options" question, not the underlying design work.
