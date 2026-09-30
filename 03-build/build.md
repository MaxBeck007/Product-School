# Module 3 · Build — Build and Learn Fast

> Can I go from idea to validated prototype before writing production code?

Write briefs that produce working prototypes, run rapid iterative testing, form a hypothesis worth shipping, and use the prototype as a shared surface for your triad.

## Prototype + Iteration Log

*Brief that produced a working prototype, plus what each round taught you.*

The brief: a 24-year-old who hit a 12-day streak, missed two days, and hasn't opened the app since; job to be done is getting back in without feeling they lost everything. Built as a 3-screen click-through prototype (`prototype/index.html`): a Comeback screen (best-streak stat, comeback session card, one-tap freeze offer), a mocked miniature-painting lesson, and a done screen confirming the restart. Tested against three personas (Priya, Tom, Amara) in mock usability sessions and an in-character agentic interview — illustrative, not real user data, but structured to surface real friction.

| Round | What changed | What we learned |
|-------|--------------|------------------|
| 1 | Removed the "must pick the right answer to continue" gate on the comeback lesson quiz | The pass/fail gate reintroduced exactly the punishing pressure the feature exists to remove — most damaging for the anxious, early-lapse user (Amara) the feature is meant to protect |
| 2 | Relabeled the quiz prompt from "Quick check" to "Just for fun, which color was that?" | Even after the mechanic was fixed, the test-like *label* alone still primed anxiety (Amara); separately, Tom's skepticism of "no cost, no catch" freeze copy only resolved once he actually tapped the button and saw it work — copy alone didn't earn trust |
| 3 | Replaced the multiple-choice quiz with a photo check-in ("snap today's progress," or skip), same no-pass/fail principle applied to a mechanic with no correct answer to gate on | Direct instruction, not usability-driven |
| 4 | Ran a new persona, Dax (a hard-to-please, hobby-fluent tabletop wargamer); dropped the "60-second lesson" time-box framing from the eyebrow, header, meta text, and CTA button | A fixed time claim on a craft that requires paint-drying time read as evidence the app doesn't understand the hobby, damaging trust in the rest of the screen, not just the time claim. A second finding — "no critique" reads as pointless to a craft-serious user, the opposite effect it has for Amara — was left open, it's a segmentation question, not a copy fix |

**Open items carried forward, not yet actioned:** personalize the comeback lesson to the user's actual pre-lapse track (still a fixed example); whether the freeze should resolve visibly/automatically rather than require a tap-and-trust interaction; whether the Comeback screen needs to vary its "no critique" framing by user segment (craft-serious vs. anxious/early-lapse).

## Hypothesis Worth Shipping

> We believe that a personalized Comeback screen — showing a user's best-streak stat, a low-pressure comeback session, and a one-tap streak-freeze — will deliver renewed engagement after a broken streak for Streakly users in their first 7 days. We'll know we're right when Day-7 retention rises for users who break a streak in week 1, measured against the 39% baseline.

## Triad Session Plan

*Use the prototype as a shared surface with eng + design.*

30-minute session with Raj and Lena: (1) context — Marcus's original ask and the research that led to the Comeback screen bet, 5 min; (2) walk all 3 prototype screens live, calling out the two fixes already made and why, 10 min; (3) feasibility questions for Raj — where do "who sees it" and freeze-rule logic actually live in the data model, is a pre-applied (no-tap) freeze meaningfully different to build than the current one-tap version, 10 min; (4) experience questions for Lena — does the "Quick check" finding change how she'd think about copy elsewhere in the flow, what's the empty state for a user who's never had a streak, 10 min; (5) decisions to walk out with — personalize the lesson or keep one example, one-tap vs. pre-applied freeze, whether an empty-state case needs designing before this goes further, 5 min.

**Note:** this session's agenda and post-session template were prepared but the session itself has not happened — nothing in `docs/triad-session.md` records Raj's or Lena's actual positions yet.

**Source:** `reference-materials/streakly-workspace/prototype/README.md`, `prototype/index.html`, `docs/hypothesis.md`, `docs/triad-session.md`, `research/usability-session-1.md`, `research/usability-session-2-dax.md`, `personas/dax.md`, `change_log.md` Entries 1-2, 7-8.
