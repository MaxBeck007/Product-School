# Skill: Competitive Pulse Check (one-command)

> **Built:** P7L2, 2026-09-28.
> **Honest constraint up front:** this skill depends on web search. When
> primary sources are not reachable (the P2L3 bonus run hit exactly this,
> `research/competitive-reddit.md` is built entirely on aggregator commentary
> because no primary Reddit thread was accessible), the run must say so and
> mark the finding low-confidence rather than presenting secondhand
> commentary as observed fact. A run that finds nothing is a valid run.

## Trigger prompt

```
Run my competitive pulse skill: skills/competitive-pulse.md
```

## Watch list

From `research/competitive-matrix.md`: **Duolingo, Babbel, Elevate, Habitica.**
Edit this line to change the watch list, the skill reads it from here.

## What counts as a move, in priority order

1. **Anything touching streak forgiveness, repair, freeze, or comeback
   mechanics.** This is the white space the whole Streakly bet depends on
   (`docs/decision-brief.md` finding 4: no competitor offers a free, personal
   comeback moment after an unplanned miss). If a competitor closes it, that
   is the single most decision-relevant thing this skill can find.
2. Changes to notification tone, cadence, or re-engagement messaging.
3. Retention or engagement features generally.
4. Pricing changes that move a forgiveness mechanic behind or out from behind
   a paywall.

Ignore: funding news, marketing campaigns, executive hires, and content
launches with no mechanic change.

## Steps Claude runs

1. **Read the baseline** `research/competitive-matrix.md` and the previous run
   in `research/competitive/`, so the output is a diff, not a fresh profile.
2. **Search per competitor** across changelogs and release notes, app store
   "what's new" entries, official blog and newsroom, and community discussion.
   Cover roughly the last 7 days plus a few days of overlap so nothing falls
   between runs.
3. **Grade every finding by source tier:**
   - **Tier 1, primary:** the company's own changelog, release notes, or blog,
     or an app store listing. Quotable as fact.
   - **Tier 2, direct observation:** a screenshot or first-hand user report of
     the feature in the product.
   - **Tier 3, secondhand:** aggregator, roundup, or summary article.
     **Labeled low-confidence, never stated as fact.**
4. **Say explicitly which searches returned nothing**, and which sources were
   unreachable. Silence and inaccessibility are different results.
5. **Assess impact on the Streakly bet** for each finding: does it close the
   white space, validate the direction, or neither?
6. **Flag anything that would change a saved artifact**, especially
   `research/competitive-matrix.md` finding 4 and
   `docs/decision-brief.md`. Propose the edit, do not make it.
7. **Prompt to save**, then write the file.

## Output format

````
# Competitive Pulse, week of <date>

**Headline:** one sentence. "No material moves this week" is a complete and
acceptable headline.

## Moves in the forgiveness/comeback space
| Competitor | What changed | Source tier | Link | Impact on our bet |
| --- | --- | --- | --- | --- |

## Other retention or notification moves
| Competitor | What changed | Source tier | Link | Impact |
| --- | --- | --- | --- | --- |

## Searched, nothing found
- Competitor: sources checked, nothing in scope.

## Could not reach
- Source, and why. Findings depending on it are marked Tier 3 above.

## Would this change a saved artifact?
- File, the specific claim affected, and the proposed edit. Awaiting your
  approval, not applied.
````

## Where the output gets saved

`research/competitive/pulse-<YYYY-MM-DD>.md`.

## Rules

- Every factual claim carries a link and a source tier. No link, no claim.
- Never infer a feature exists because a roundup article says it does. That is
  Tier 3.
- Do not edit `research/competitive-matrix.md` inside this run. Propose it.
- Restate the scope of the competitive baseline honestly: four named
  competitors, and it was never exhaustive.
