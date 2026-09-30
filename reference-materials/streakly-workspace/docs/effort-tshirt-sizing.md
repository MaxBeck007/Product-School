**`ROLEPLAYED, NOT A REAL ESTIMATE.` Raj said none of this. Every number and
size below is Claude-generated at Max's request, standing in for Raj using
`stakeholders/raj.md`. Do not put this in front of engineering as if it were
a real sizing session.**

# T-Shirt Sizing: Comeback Screen, as of end of Module 4

> **Grounded in:** everything accumulated through P4, `docs/spec-readiness.md`
> (the freeze eligibility rule as a discussed, unvalidated position),
> `docs/codebase-summary.md` (schema gap, blast radius, sequencing
> dependency), `docs/qa-checklist.md` (items 1, 7, 8, 9 failing), `docs/prd.md`
> Open Questions, `change_log.md` Entries 6, 9, 10 (the reactive-only scope
> decision and the pre-applied freeze), and `stakeholders/raj.md` (Cool
> Blue, won't commit a number without naming the assumption under it).

---

**Raj:** Before I give you a size, I'm splitting this into what's actually spec'd and what isn't, because lumping them together gives you a number that's wrong in both directions.

## What I'm sizing

The **reactive Comeback screen only** — best-streak stat, the comeback session, and the freeze, as decided in the P3L4 triad session. Specifically:

1. **Schema change + migration.** A best-streak field that persists (not just today's live counter), plus freeze-spent state and pre-break streak length. This touches the equivalent of the `User` model, which is touched by nearly every part of the app (`docs/codebase-summary.md` section 5), so it needs a real migration, not just a new field added quietly.
2. **Freeze eligibility logic, server-side.** One free freeze per lapse, streaks 3+ days only, no stacking on a second lapse in the same week (`docs/spec-readiness.md`). New business logic, not a config flag.
3. **Client build.** The screen itself is basically done as a prototype, this is re-implementing it against real data instead of a hardcoded "12." Cheap **only if** the schema from item 1 lands first, that's a real sequencing dependency, not parallel work.
4. **Edge cases from QA.** Empty state (no best streak to show, `docs/qa-checklist.md` row 1) and the offline/race-condition question I raised in the PR comment, does the freeze render before or after the eligibility check resolves.

## What I'm explicitly not sizing

- **Personalizing the lesson to the user's actual track.** Already logged as its own ticket, not part of v1 (`change_log.md` Entry 9).
- **The proactive piece for not-yet-lapsed users.** There's no concept yet, no mechanic, no trigger (`change_log.md` Entry 6). Sizing nothing isn't an estimate, it's a guess. Come back to me with even a rough shape and I'll size it.
- **The empty state's actual design.** That's Lena's, not built yet. I'm sizing the engineering work to implement whatever she hands me, not the design itself.

## The size

**L.**

The schema change and migration is the long pole, not the client screen. Everything downstream, the freeze logic, the client build, is bounded and mostly known. The migration against a table that's touched everywhere is the part that eats a sprint, not the UI.

**One assumption this size depends on, and I want it said out loud, not discovered later:** I'm assuming the discovery trigger is "checked server-side on next app open after a qualifying lapse," cheap, no new infrastructure. If it actually needs a new push notification path, that's a different ticket, and this becomes an **XL**, not an L. That's still an open PRD question (`docs/prd.md`, Open Question 7), not something I'm deciding here by assuming the cheap version.

---

## Translating L into weeks

**Max:** What's an L actually mean in weeks?

**Raj:** Caveat first, this workspace has no real sprint history for me, no real velocity to calibrate against. What I can do is size the actual pieces and add them up, that's still an estimate, not a guess, because it's tied to specific work, not a label.

- **Schema change + migration:** the long pole. Writing it, testing it against existing users, and a rollout plan given the blast radius (`docs/codebase-summary.md` section 5), roughly a week to a week and a half on its own.
- **Freeze eligibility logic** (one per lapse, 3+ day streaks, no stacking, plus tests): 3 to 4 days.
- **Client build**, re-implementing what's already prototyped against real data: 2 to 3 days, but only *after* the schema lands, this is sequential, not parallel (`docs/codebase-summary.md`'s sequencing flag).
- **Empty state implementation**, once Lena hands me a design: 1 to 2 days.
- **QA edge cases** (second-lapse handling, already-used freeze, the offline race condition from my PR comment): 1 to 2 days.

Add it up with the sequencing dependency respected, roughly **2.5 to 3 weeks for one engineer**, meaning me, this squad doesn't have a second backend engineer. If that needs to move faster, that's a headcount conversation, not a scope conversation, I can't parallelize a migration with a client build that depends on it.

That's still the L scenario, cheap discovery trigger assumed. The XL branch, if the trigger needs new push infrastructure, adds work I haven't sized at all yet, because I don't know what that infrastructure looks like until someone answers the question.

## Step out of character, notes for Max

**Why this matters before P5/P6:** the experiment design in P5 assumes the Comeback screen already shipped (it's the course's supplied dataset). This sizing is the real-world reminder that "shipped" is an L-sized bet resting on one unconfirmed assumption about the discovery trigger, not a small follow-on to the prototype.

**Open item carried forward:** the discovery trigger question (`docs/prd.md` Open Question 7) now has a cost attached to it, not just an open question. Resolving it doesn't just answer a PRD question, it decides whether this is an L or an XL.
