# QA and Launch: Comeback Screen

> **Sources:** `docs/spec-readiness.md`, `prototype/README.md`,
> `prototype/index.html`. Note: `docs/spec-readiness.md` was a fully
> roleplayed exercise, so some rules referenced below (freeze eligibility,
> second-lapse behavior) exist only as discussed positions, not as anything
> built into the prototype. That gap is exactly what several checklist items
> below surface.
>
> **Re-verified 2026-09-30 after `change_log.md` Entry 7:** the check-in
> mechanic is a photo capture (or skip), not a multiple-choice quiz. Rows 4,
> 5, and 10 test that mechanic, re-run by hand against the live prototype,
> not just relabeled.

## 1. Edge case list

**Empty states**
- User has never held a streak, there's no best-streak stat to show.
- No lesson content exists for the user's track.
- User has no lessons remaining in general (finished the whole track).

**Edge data conditions**
- Streak of 1 (does a 1-day streak count as "worth protecting"?).
- User broke a streak twice in the same week.
- User already used their one freeze for this lapse.

**Timing scenarios**
- Missed exactly one day vs. missed many days.
- Time zone boundaries (did they actually miss a day, or is it a UTC/local
  offset issue).
- Comeback screen surfaced too late (days after the lapse, momentum already
  fully gone).

**Permission states**
- Push notifications off (can they even be re-engaged if the entry point is a
  notification).
- Background refresh off (does the best-streak stat load fresh or go stale).

## 2. PM QA checklist run against `prototype/index.html`

| # | Check | Result | Blocks launch? |
| --- | --- | --- | --- |
| 1 | Handles a user with no best-streak stat (never had a streak) | **Fail** | Yes, hardcoded to show "12" always |
| 2 | Lesson content matches the user's actual track | **Fail** (known, logged) | No for a v1 discovery test, per `docs/pm-brief.md`'s explicit assumption, but must be resolved before real launch |
| 3 | Freeze tap shows clear confirmation | **Pass** | — |
| 4 | Photo check-in doesn't block progress if skipped | **Pass** | — |
| 5 | Check-in copy avoids test-like framing | **Pass**, with a caveat | Passes the test-like-framing check Amara's segment needed; a different, unactioned finding from Dax's review (`change_log.md` Entry 8) is that "no critique" reads as pointless, not reassuring, to a craft-serious user — not a launch blocker, a logged open question |
| 6 | User can decline/skip the screen | **Cannot fully determine** | The button exists but only shows a placeholder alert in this static prototype, not real navigation |
| 7 | Second lapse in the same week shows screen but no freeze (per `docs/spec-readiness.md`) | **Fail** | Yes if this rule ships as discussed, nothing in the prototype implements it |
| 8 | Freeze offer respects the 3+ day eligibility rule (per `docs/spec-readiness.md`) | **Fail** | Yes, the prototype shows the freeze offer unconditionally |
| 9 | Already-used freeze can't be reused | **Cannot determine / likely fail** | Yes, no such state exists in this static prototype |
| 10 | Restarting the demo resets all UI state correctly | **Pass**, re-verified live 2026-09-30 against freeze + photo state together | — |

**Read on this table:** items 1, 7, 8, and 9 are not really prototype bugs,
they're the gap between what got *discussed* in the spec-readiness
conversation and what's actually *built*. That gap is expected at this stage
(this is a click-through prototype, not a working build), but it means the
prototype cannot be used as evidence that the eligibility rule works, only
that the tone and lesson mechanic do.

## 3. First PR comment for Raj (question, not a rubric stamp)

```
Quick one before this merges: the freeze-eligibility check (3+ day streak,
not already spent this lapse) reads like something that has to be resolved
server-side against real streak history. If a user opens this screen while
offline or on a flaky connection, does the freeze offer render optimistically
before that check resolves, or does it wait? Want to make sure we're not
briefly showing a freeze offer to someone who isn't actually eligible.
```
