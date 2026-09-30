# Quarterly Review Deck: Comeback Screen, Narrative Structure

> **Audience:** Marcus, in the room for a quarterly review. Calibrated to his
> profile (`stakeholders/marcus.md`): recommendation and number up front, one
> page of substance per slide, connects to Day-7 retention specifically.
> **Sources:** `CLAUDE.md`, `docs/decision-brief.md`, `docs/recommendation-memo.md`,
> `data/metric-findings.md`, `data/metric-diagnosis.md`, `data/experiment-design.md`,
> `research/interview-synthesis.md`. No number or insight below is invented; where
> a slide needs something the files don't have (a date, a target), it's marked
> `[NOT IN SOURCES]` rather than filled in.

---

## Slide 1: The Problem

**1 number:** Day-7 retention dropped from 48% to 39% after the v2
streak/notification redesign (`CLAUDE.md`; `docs/decision-brief.md`).

**1 insight:** the drop isn't fewer signups or a failing notification channel,
it's a rising break rate among starters, 38.9% to 56.5% across cohort weeks
1-4 (`data/metric-diagnosis.md`, section 1; `docs/recommendation-memo.md`).

---

## Slide 2: Why Now

**What changed:** the v2 redesign shipped, and the pre-launch trend shows no
sign of leveling off on its own, Day-7 retention fell every week from cohort
1 to cohort 4 (60% to 44%) before the Comeback screen existed
(`data/metric-findings.md`, Q1).

**What we learned:** users who break their early momentum in week 1 retain
roughly half as well by day 30 (18.0%) as users who make it past week 1
(33.5%), and churn 16 points higher (`data/metric-findings.md`, Q2). Across
every research source, the same root cause surfaces: the reset is
all-or-nothing and there's no way back in (`docs/decision-brief.md`).

---

## Slide 3: The Proposal

**What it is:** a personalized Comeback screen shown after a broken streak:
best-streak stat, a 60-second lesson, a one-tap streak-freeze
(`docs/decision-brief.md`, Option B). Built with data Streakly already has,
no new integrations (`CLAUDE.md`).

**What it isn't:**
- Not a fix for notification tone or frequency, that's a real but separate
  theme (`docs/decision-brief.md`, finding 3).
- Not monetized, the freeze is free by design, that's the identified white
  space competitors haven't claimed (`docs/decision-brief.md`, finding 4).
- Not a committed, scoped build yet, this is discovery, no committed scope
  (`CLAUDE.md`).

---

## Slide 4: Evidence

**Prototype:** tested across three personas in a usability pass and an
in-character interview (`change_log.md`, Entries 1-2). **Label: mock,
illustrative personas, not real user sessions.** The "welcome back" tone and
best-streak stat needed no explanation; the freeze mechanic earned trust once
tapped, not from copy alone.

**Pilot data (real, cohort week 5, n=50/variant):**
- Day-7 retention: 76% treatment vs. 46% control. Day-30: 36% vs. 22%
  (`data/metric-findings.md`, Q3).
- Engagement grew with exposure, not a one-time bump: open rate on the
  Comeback send rose 28% to 56% across 4 sends; control stayed flat at 4-6%
  (`data/metric-findings.md`, Q4).

**User voice:** 6 of 10 unprompted NPS comments name the punishing reset
directly; 2 name a streak freeze as the fix they want, by feature name
(`research/nps-analysis.md`). Tom, a churned user: "I switched to Duolingo,
at least there a missed day doesn't wipe everything, and a streak freeze
feels forgiving." (`research/interview-synthesis.md`)

---

## Slide 5: The Plan

**Milestone reached:** the full powered test is designed and ready to run
(`data/experiment-design.md`). It's built to detect a 5-point lift at 80%
power, 95% significance, using the pilot's own result as the basis for the
calculation.

**What's still open, named plainly, not glossed over:**
- Real weekly eligible-user volume, how many WAU actually break a streak per
  week, is unconfirmed. The test needs roughly 0.46% of 85,000 WAU per week
  to fit an 8-week window; without that number, no duration can be committed
  (`data/experiment-design.md`, Step 4; `CLAUDE.md`).
- Freeze eligibility and expiry rules are still undefined
  (`stakeholders/raj.md`; `docs/prd.md`).
- **[NOT IN SOURCES]:** sprint kickoff date and a committed rollout timeline.
  Discovery is scoped as 8 weeks from kickoff per the original framing, but
  kickoff itself isn't scheduled yet (`CLAUDE.md`, Known gaps).

**Risk of waiting:** every week without addressing the week-1 break problem
locks in the same drop we're already fighting, the pilot's own numbers show
the gap compounds, it doesn't hold flat (`docs/recommendation-memo.md`).

---

## Slide 6: The Ask

Sign-off to run the full powered test (`data/experiment-design.md`) before
committing to a company-wide scale decision, and a decision on the one number
that currently blocks committing to that test's duration: real weekly
eligible-user volume (`docs/recommendation-memo.md`; `CLAUDE.md`).

This is not a request to scale the feature today. The pilot result is real
and directionally strong, but n=50 per variant is not enough on its own to
commit the whole company to (`docs/recommendation-memo.md`, Recommendation).
