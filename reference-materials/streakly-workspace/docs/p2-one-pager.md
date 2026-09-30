# P2, Know Your Users: What We Accomplished

> **Scope:** section P2 of "The Streakly Scenario, Claude Code for PMs"
> (`streakly-scenario-claude-code-for-pms.md`, lines 174-301).
> **Status:** complete, all 4 lessons plus the P2L3 bonus.
> **Date of work:** 2026-09-28.

## Outcome in one line

P2 turned three interview excerpts and ten NPS comments into a single, sourced
conclusion: the retention problem is the irreversible streak reset, not the
lessons and not primarily notifications. That conclusion is what the Comeback
screen recommendation rests on, and everything from P3 onward cites it.

## What we produced

| Lesson | Deliverable | File |
| --- | --- | --- |
| P2L1 | Top 5 themes, verbatim quotes, contradictions, week-1 insight | `research/interview-synthesis.md` |
| P2L2 | Themes ranked by frequency, praise vs complaints, top 3 actionable issues, findings report for Marcus | `research/nps-analysis.md` |
| P2L3 | 4-competitor matrix and 2 white-space gaps | `research/competitive-matrix.md` |
| P2L3 bonus | Competitor sentiment summary, gap re-test | `research/competitive-reddit.md` |
| P2L4 | 1-page decision brief for Marcus | `docs/decision-brief.md` |

## What we learned

1. **The punishing reset is the dominant theme.** 6 of 10 NPS comments cite it
   directly; 2 name a streak freeze as the fix by feature name.
   (`research/nps-analysis.md`)
2. **Users hit the punishing side of the mechanic before the rewarding side.**
   Priya's "look what you built" moment took about 3 weeks; Amara is anxious at
   day 4 and Tom churned at week 5. (`research/interview-synthesis.md`)
3. **Notification fatigue is real but secondary, and self-defeating.** 2 of 10
   comments cite nagging or random notifications, and both users turned
   notifications off entirely, closing the channel that could win them back.
   (`research/nps-analysis.md`)
4. **The white space is free forgiveness.** Duolingo sells recovery (gem-priced
   streak freeze and streak repair); Babbel, Elevate, and Habitica have no
   reactive comeback flow at all. No competitor pairs acknowledgment with a
   low-effort re-entry action. (`research/competitive-matrix.md`)
5. **Priya undercuts herself as a template,** unprompted: "I think most people
   quit long before the habit forms." Worth keeping when anyone argues from
   power-user behavior. (`research/interview-synthesis.md`)

## The decision it produced

Recommended **Option B, the personalized Comeback screen** (best-streak stat,
60-second comeback lesson, one-tap streak freeze) over status quo (A) or a
notifications-only fix (C). Rationale: the reset theme is the largest and most
consistently confirmed finding across every source, and it is unclaimed white
space. (`docs/decision-brief.md`)

## Confidence and caveats

- **Course-supplied inputs.** The interview excerpts and NPS verbatims are the
  fictional scenario data provided in the course prompts, not IDEXX or real
  Streakly research. Findings 1-3 and 5 are faithful to those inputs; they are
  not evidence about a real product.
- **Competitive matrix is real research,** web search retrieved 2026-09-28, with
  live source links per claim.
- **The Reddit bonus is the weak link.** Primary Reddit threads were not
  retrievable, so `research/competitive-reddit.md` is aggregator and blog
  commentary about Reddit-adjacent sentiment, explicitly labeled as such rather
  than backfilled with invented quotes. Elevate returned no usable signal.
  Confidence: medium for Duolingo and Habitica, low for Babbel, none for
  Elevate.
- **Method note kept honest in P2L1:** where a theme appeared in only one
  interview, the file says so instead of pairing it with a second person's
  quote, so "2 quotes per theme" was not met everywhere by design.

## What P2 fed downstream

- `docs/prd.md` (P6L1) is written from the P2 research stack plus P3 hypothesis
  work. (`change_log.md`, Entry 3)
- The freeze mechanic tested in the prototype and challenged by the Tom persona
  in P3 traces back to the 2 NPS comments naming it.
- **Open question still unresolved from P2's own logic:** if a lapsed user has
  already turned notifications off (finding 3), how do they ever see the
  Comeback screen? Raised as the highest-risk objection in
  `docs/objection-log.md` and carried into the PRD's open questions.
