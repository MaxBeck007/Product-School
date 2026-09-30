# Module 2 · Discover — Know Your Users

> How do I turn raw signal into a decision leadership acts on?

Synthesize interviews, process feedback at scale, run repeatable competitive analysis, and land on a one-page decision brief that drives action.

## Insight Synthesis & Feedback

*Turn raw signal into themes. What pattern repeats?*

Three interviews (Priya, a 14-month power user; Tom, churned after breaking a 12-day streak; Amara, 4 days in and already anxious) and ten unprompted NPS comments point at the same root cause: **the streak reset is all-or-nothing, and there's no way back in.** 6 of 10 NPS comments name the punishing reset directly, and 2 name a streak-freeze as the fix they want by feature name. The interviews add the mechanism: users hit the *punishing* side of the mechanic well before they ever reach the *rewarding* side — Priya's "look what you built" moment took about three weeks, but Amara is already anxious at day 4 and Tom churned at week 5. Notification fatigue is a real but secondary theme (2 of 10 comments), and it's self-defeating: both of those users turned notifications off entirely, closing the one channel that could otherwise win them back.

## Competitive Matrix

| Competitor | Strength | Weakness | Implication |
|------------|----------|----------|-------------|
| Duolingo | Streak-freeze and streak-repair mechanics exist and work | Both are paid, bought with gems; prices reportedly rising; 2025 "energy system" backlash | The forgiveness mechanic itself validates the need — but paywalling it is exactly the friction Streakly can avoid |
| Babbel | Structured, curriculum-style lessons, spaced repetition | No streak-freeze or recovery mechanic found at all | Leans on content quality, not retention mechanics — no direct comeback competitor |
| Elevate | Streaks + 150+ achievements for motivation | No streak-freeze or reactivation-after-lapse feature | Same gap as Babbel |
| Habitica | "Off mode" lets a user pause proactively before a planned break | Only proactive — no reactive comeback flow for an *unplanned* miss (Tom and Amara's exact situation) | **No competitor offers a free, personal "welcome back" moment after an unplanned miss** — that's the white space |

## Decision Brief

- **Decision needed:** How to recover the 9-point Day-7 retention drop (48% → 39%) after the v2 streak/notification redesign.
- **Recommendation:** Move forward with the personalized Comeback screen (best-streak stat, 60-second comeback lesson, one-tap streak-freeze) as the primary discovery bet, over status quo or a notification-only fix.
- **Evidence:** The punishing reset is the single largest theme in unprompted feedback (6/10 NPS comments); interviews show users hit the punishing side of the mechanic before any rewarding one; no competitor offers a free, personal comeback moment after an unplanned miss; lower-confidence Reddit/aggregator sentiment doesn't contradict this and arguably strengthens it (Duolingo users reportedly resent that its forgiveness mechanic is paywalled).
- **Risk if wrong:** Notification fatigue is real but secondary — designing around it first would leave the dominant, most cross-source-confirmed driver of the retention drop unaddressed while the smaller theme gets fixed.

**Source:** `reference-materials/streakly-workspace/research/interview-synthesis.md`, `research/nps-analysis.md`, `research/competitive-matrix.md`, `research/competitive-reddit.md`, `docs/decision-brief.md`.
