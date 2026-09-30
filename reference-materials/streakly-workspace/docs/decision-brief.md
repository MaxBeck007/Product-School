# Decision Brief: The Comeback Experience

> **For:** Marcus, Head of Product
> **Sources:** research/interview-synthesis.md, research/nps-analysis.md,
> research/competitive-matrix.md, research/competitive-reddit.md

## Situation

Day-7 retention dropped from 48% to 39% after the v2 streak/notification redesign,
and once a user breaks a streak, most never come back. Across every research source
we have, the same root cause surfaces: the reset is all-or-nothing and there is no
way back in.

## Key Findings

1. **The punishing reset is the single largest theme in unprompted feedback.** 6 of
   10 NPS comments cite it directly, and 2 name a streak-freeze as the fix they
   want by feature name. (`research/nps-analysis.md`)
2. **Interviews show users hit the punishing side of the mechanic before they ever
   reach a rewarding one.** Priya's positive "look what you built" moment took
   about 3 weeks; Amara is already anxious at day 4, and Tom churned at week 5,
   both well before Priya's arc. (`research/interview-synthesis.md`)
3. **Notification fatigue is a real but secondary theme, and it's self-defeating.**
   2 of 10 NPS comments cite nagging or random notifications, and both say they
   turned notifications off entirely, closing the one channel that could otherwise
   win them back. (`research/nps-analysis.md`)
4. **No competitor offers a free, personal comeback moment after an unplanned
   miss.** Duolingo has a paid streak-repair mechanic; Babbel, Elevate, and
   Habitica have no reactive comeback flow at all. (`research/competitive-matrix.md`)
5. **Lower-confidence Reddit/aggregator sentiment does not contradict finding 4,
   and arguably strengthens it:** secondhand sources report Duolingo users
   resenting that its forgiveness mechanic is paywalled, not just that a miss
   resets the streak. This finding carries materially lower confidence than 1-4,
   no primary Reddit threads were accessible, everything here is aggregator
   commentary. (`research/competitive-reddit.md`)

## Options Considered

- **A. Status quo.** Keep iterating on the current reset flow. Risk: every source
  above already shows this is failing, and it's the path most likely to keep
  losing the users we're trying to save.
- **B. Ship the personalized Comeback screen** (best-streak stat, 60-second
  comeback lesson, one-tap streak-freeze), the concept Lena sketched and Raj
  called technically feasible with no new data sources.
- **C. Fix notification tone and frequency only.** Cheaper, but does not address
  the larger and more consistently confirmed theme, the irreversible reset itself.

## Recommended Action

Move forward with Option B, the personalized Comeback screen, as the primary bet
into discovery.

## Why Now

The reset theme is the largest, most consistently confirmed finding across every
source available (interviews, NPS, and competitive research), and it's white
space no competitor has claimed for free. Waiting risks designing a fix aimed at
the smaller theme (notifications) while the dominant driver of the 9-point
retention drop goes unaddressed.
