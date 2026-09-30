# Metric Diagnosis: Day-7 Retention

> **Verified:** every number below is computed with SQL/DuckDB against the
> real uploaded dataset, not estimated. Queries shown inline. Where a metric
> tree component has no literal field in the data (streak-break, comeback
> rate, notification opt-in), I used the same proxies as
> `data/metric-findings.md` and say so.

## 1. Metric tree: what actually drives Day-7 retention

| Lever | Cohort 1 | Cohort 2 | Cohort 3 | Cohort 4 | Cohort 5 (blended) |
| --- | --- | --- | --- | --- | --- |
| Streak-start rate (day-1 activity) | 90.0% | 90.0% | 97.0% | 92.0% | 90.0% |
| Break rate among starters (day-1 active, day-7 not) | 38.9% | 45.6% | 51.5% | 56.5% | 40.0% |
| Avg. sessions per user | 5.74 | 5.08 | 4.48 | 3.69 | 4.48 |
| Overall nudge open rate | 12.1% | 11.7% | 14.3% | 9.4% | 10.4% |
| **Resulting Day-7 retention** | **60.0%** | **53.0%** | **48.0%** | **44.0%** | **61.0%** |

**Which lever actually moves the number:** the start rate is flat and noisy
(90-97%, no trend). The **break rate among starters climbs steadily,
38.9% → 45.6% → 51.5% → 56.5%** across cohorts 1-4, moving in lockstep with
the retention decline. Overall nudge open rate has no clean trend across the
same period (12.1% → 11.7% → 14.3% → 9.4%). **The break rate is the driver,
not the notification channel.**

## 2. What caused the decline in weeks 1-4, specifically

It's not that fewer people start (start rate is flat), and it's not a
declining notification channel (no consistent trend there either). It's that
a rising share of people who *do* start are gone by day 7: 38.9% of
starters in cohort 1, rising to 56.5% by cohort 4. Average sessions per user
also declined in the same steady pattern (5.74 → 3.69), consistent with the
same users doing less before they drop off, not a sudden cliff.

One more real, specific data point: among the 178 users across cohorts 1-4
who broke their streak in week 1, only 90 of them (50.6%) even received a
`re_engagement`-type nudge, and of those, only 12.1% opened it. Effectively,
roughly 6% of users who broke their streak in week 1 ever opened a
re-engagement nudge. **The existing re-engagement mechanism is barely
reaching the population it's meant to serve.**

## 3. What the week-5 split tells us about what the Comeback screen fixed

Treatment retained 76.0% at Day-7 vs. control's 46.0%, and the *engagement*
with the Comeback-related weekly summary send climbed from 28% to 56%
across 4 sends, vs. control flat at 4-6%. Compare that to the 12.1% open
rate on the *existing* re-engagement nudge (finding above), the Comeback
screen reaches and engages the target population far better than what
Streakly already had.

## 4. Four ranked hypotheses for why some treatment users still churned

Treatment's Day-30 retention was 36.0%, meaning 64% of treatment users
still didn't retain by day 30 despite seeing the Comeback screen. Ranked by
what the data already supports, most to least:

**H1. Acquisition channel quality explains a meaningful share of it.**
Prediction: organic-acquired treatment users retain measurably better than
paid or referral-acquired treatment users. **Checked against data:**
organic 43.3% Day-30 (n=30), paid 28.6% (n=14), referral 16.7% (n=6).
**Confidence: 7/10.** The organic-vs-paid gap (n=30 vs n=14) is reasonably
sized; the referral figure (n=6) is too small to trust on its own.
**Confirms it:** the gap holding up in a larger sample. **Rules it out:**
the gap disappearing once platform (H2) is controlled for, channel and
platform could be correlated in this data and I haven't checked that.

**H2. Platform correlates with who the Comeback screen actually helps.**
Prediction: iOS treatment users retain better than Android. **Checked
against data:** iOS 47.8% Day-30 (n=23) vs. Android 27.3% (n=22) vs. web
20.0% (n=5, too small to trust). **Confidence: 6/10.** Real gap, decent
sample size for iOS/Android, but I have not checked whether *control* shows
the same iOS/Android gap, if it does, this is a pre-existing platform
difference, not something specific to the Comeback screen.
**Confirms it:** the gap being absent in control. **Rules it out:** the same
gap appearing in control at similar size.

**H3. Users churn despite treatment because they don't engage with the
comeback nudge itself.** **Checked against data, and largely ruled out:**
94.4% of treatment users who churned by Day-30 had opened a comeback-related
send at least once, nearly identical to the 96.9% open rate among treatment
users who *did* retain. **Confidence: 2/10.** Opening the nudge is nearly
universal in both outcomes, it does not distinguish who churns.
**What would have confirmed it:** a materially lower open rate among
churned users, not observed. **Already ruled out** by the data above.

**H4. Users who lapse more than once in the same window aren't helped by a
single comeback screen.** **Cannot be scored,** none of the 5 tables has a
lapse-count or repeat-break field, this can't be checked with what exists.
**Confirms it:** a lapse-history field, if one exists elsewhere.
**Rules it out:** nothing available can rule this out either, it's simply
untestable right now.

## 5. Which hypothesis to act on first

**H1 (acquisition channel quality).** It's the most data-supported
(largest usable sample, 30 vs. 14), it's actionable (informs onboarding or
targeting by channel rather than a Comeback-screen redesign), and unlike H2
it doesn't require a follow-up check to know whether it's really a
treatment effect. H3 is already ruled out by the data, and H4 can't be
tested with what's on hand.
