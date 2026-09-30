# Module 4 · Collaborate — Work with Your Team

> How do I make a validated idea survive contact with delivery?

Read a codebase as a map, pair with engineering and design without slowing them down, and own the last 20%: QA, edge cases, and launch readiness.

## Codebase Tour + Spec Readiness

*Read the codebase as a map; confirm the spec is ready for delivery.*

Streakly has no real codebase, so the tour was run against a public reference repo (Habitica, `HabitRPG/habitica`) that models the same class of problem. Key finding: the streak is a single integer with **no history** — no best-streak field, no dated log, and critically, **no streak-freeze or grace-period field anywhere in the schema**. That's the same gap Raj flagged in the original Slack thread ("we'd need the logic for who sees it and the freeze rules"), independently confirmed in a real reference codebase. Blast radius: the equivalent `User` document is touched by nearly every part of the app, so new fields aren't free even when additive — this repo has a dedicated migrations folder for exactly that reason.

A roleplayed spec-readiness session (standing in for Raj, clearly labeled as such) caught the most valuable correction in the whole workspace: the PM brief's constraint, "use data Streakly already has, no new integrations," had conflated *no new third-party systems* with *no new data fields*. The freeze rule needs pre-break streak length and freeze-spent state — real new fields, not assumed away. The brief's constraint section was rewritten as a result.

## Design Review + QA

*Confirm the spec is ready for delivery, then own the last 20%.*

A roleplayed design review (standing in for Lena) surfaced the sharpest strategic point in the workspace: the Comeback screen is **reactive-only** — it only reaches users *after* they lapse — but Day-7 retention measures a population that includes anxious, not-yet-lapsed users like Amara (day 4). A reactive-only fix structurally can't reach her, so part of the metric this feature is accountable for is outside its reach by design. That was PRD Open Question 8, a product/roadmap call for PM and Marcus, not a design call.

**Resolved 2026-09-30:** scope expands. The Comeback experience now includes a proactive, anticipatory piece for not-yet-lapsed anxious users, alongside the existing reactive screen — the proactive piece itself is still undesigned, this closed which of the two options, not the design work.

| Edge case | Expected behavior | Status |
|-----------|--------------------|--------|
| User has never held a streak | Show a designed empty state, not a hardcoded best-streak stat | ☐ Fail — hardcoded to always show "12" |
| Second lapse in the same week | Comeback screen still shows; freeze offer withheld per the proposed 3+ day / no-stacking rule | ☐ Fail — rule discussed, not built |
| Freeze already used for this lapse | Freeze offer not shown again | ☐ Fail / cannot determine — no such state in a static prototype |
| Freeze tap | Clear inline confirmation, no navigation away | ☑ Pass |
| Comeback session check-in (photo or skip, replaced the multiple-choice quiz 2026-09-30) | Photo or skip both advance; no test-like framing | ☑ Pass, with an open caveat — Dax's persona review found "no critique" reads as pointless rather than reassuring to a craft-serious user, logged as an open question, not a blocker |

**Read on this table:** the three failing rows aren't prototype bugs — they're the gap between what was *discussed* in the spec-readiness conversation and what's actually *built* in a click-through prototype. First real PR comment queued for Raj: does the freeze-eligibility check resolve before or after the offer renders if the user is offline, so an ineligible user is never briefly shown a freeze they can't actually get?

**Source:** `reference-materials/streakly-workspace/docs/codebase-summary.md`, `docs/spec-readiness.md`, `docs/design-review.md`, `docs/qa-checklist.md`, `stakeholders/raj.md`, `stakeholders/lena.md`.
