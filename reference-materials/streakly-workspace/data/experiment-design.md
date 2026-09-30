# Experiment Design: Full Comeback Screen Test

> **Verified:** every calculation below was run with `scipy`/`statsmodels`
> in Python, not estimated by hand. Test parameters as given: pilot 76% vs.
> 46% Day-7 (n=50/variant), MDE 5pts, power 80%, significance 95%, available
> WAU 85,000, max duration 8 weeks.

## Step 1: Is the pilot result statistically significant?

**In one sentence:** statistical significance tells a PM whether a result is
unlikely to be due to random chance alone, not whether the effect is big
enough to matter, those are two different questions.

**Calculation:** two-proportion z-test on 38/50 (76%) vs. 23/50 (46%):
**z = 3.075, p = 0.0021.** Cross-checked with Fisher's exact test (more
appropriate for small samples): **p = 0.0038.** Both are well under the 0.05
threshold for 95% confidence.

**Plain English:** yes, this result is statistically significant, despite
only 50 people per group. That's because the observed effect (30 percentage
points) is unusually large, large effects are easier to detect with small
samples. **This does not mean n=50 is generally "enough,"** it was enough to
catch *this specific, large* effect. A smaller true effect could easily be
missed at this sample size, that's exactly what Step 3 addresses.

## Step 2: What is MDE, and why set it before running a test?

**In one sentence:** minimum detectable effect (MDE) is the smallest lift
worth being able to detect, and a PM sets it before the test so sample size
isn't chosen to fit a desired answer after the fact. **MDE for this test: 5
percentage points**, meaning the team wants the test to reliably detect a
lift as small as 5pts off the 46% control baseline, not just the 30pt lift
the pilot happened to show.

## Step 3: Required sample size

**In one sentence:** statistical power is the chance of actually detecting a
real effect if one exists; too little power means a real improvement can
look like nothing happened, and the team would wrongly abandon something
that works.

**Calculation:** for baseline 46%, MDE 5pts (46% vs. 51%), power 80%,
significance 95%, two-sided: **required n ≈ 1,568 per variant (≈3,136
total).** For comparison, detecting the pilot's full 30pt lift would only
require about 40 per variant, which is why the small pilot was enough to
catch that specific effect but says nothing about a 5pt effect.

## Step 4: Test duration, does it fit 8 weeks?

To hit 3,136 total participants in 8 weeks requires an average of
**392 eligible users per week** (users who break a streak and are routed
into the test).

**Honest gap, flagged rather than guessed past:** I don't have a real
figure for what share of the 85,000 weekly active users actually break a
streak and become eligible in a given week. The dataset used in
`data/metric-findings.md` is a small illustrative sample (~100 new
signups/cohort-week), not the same scale as 85,000 WAU, so I'm not stretching
that sample's break-rate percentages to stand in for a company-wide weekly
volume.

**What this means in practice:** the test fits within 8 weeks *if* at least
roughly **0.46% of WAU (392 of 85,000) break a streak and enter the test in
a typical week.** That's the number to check against real product
analytics before committing to the 8-week window. **What would confirm
this:** an actual weekly count of streak-break events from Streakly's data,
not assumed.

## Step 5: The decision

**Plain-English recommendation:** don't treat this as a binary "wait 8 full
weeks" vs. "scale now" choice. The pilot's result is real (Step 1), but its
size might not hold at scale (small pilots can overstate effects, a
so-called "winner's curse"). A defensible middle path: run a shorter
confirmatory test sized to detect a more conservative lift (for example,
half the observed 30pts, ~15pts) rather than the full 5pt MDE, which needs
far fewer than 1,568/variant and could plausibly finish inside the eligible-
volume constraint above.

**Risk of waiting for the full test:** more weeks at the current ~39%
baseline before any fix reaches most users.
**Risk of scaling now on n=50:** rolling out something that doesn't
reproduce this exact lift company-wide, especially since the true weekly
eligible volume isn't yet confirmed.

## Step 6: Leading indicators to watch weekly, without waiting the full duration

1. **Comeback-send open rate in the treatment arm.** Get nervous if it drifts
   back down toward control's flat 4-6% baseline, that would mean the
   engagement gain isn't holding as more users see it.
2. **Weekly (not just Day-30) retention within the treatment arm.** Get
   nervous if it trends down from the pilot's ~70%+ range toward control's
   46%, that's an early signal the effect is regressing before the full test
   even finishes.
3. **Company-wide break rate among new-user starters.** Get nervous if it
   keeps climbing past cohort 4's 56.5% high-water mark
   (`data/metric-diagnosis.md`), that would mean the underlying problem is
   still getting worse even while the fix is mid-test.
