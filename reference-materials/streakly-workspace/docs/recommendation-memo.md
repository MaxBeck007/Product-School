# Results Memo: Comeback Screen Pilot

> **For:** Marcus, Head of Product. Calibrated to his profile
> (`stakeholders/marcus.md`): recommendation first, one page, connects to the
> Day-7 number specifically.
>
> **Scope of "we shipped" below, added 2026-09-28 (P7L4 fix F1):** this memo is
> written against the P5 exercise dataset, in which the Comeback screen had
> already run as a 50/50 experiment in cohort week 5. **Nothing has actually
> shipped.** Everywhere else in this workspace the feature exists only as a
> click-through prototype (`prototype/README.md`, `docs/hypothesis.md`,
> `CLAUDE.md`). The numbers below are a realistic exercise dataset, not Streakly
> results. Do not hand this memo to anyone without that context.

**Recommendation up front:** run a full, properly powered test of the
Comeback screen before scaling company-wide, the pilot signal is strong but
the sample is too small to commit to a full rollout on its own.

## Situation

We shipped the Comeback screen as a 50/50 experiment to 100 users in cohort
week 5, testing whether a forgiving, personalized re-entry moment (best-streak
stat, 60-second lesson, one-tap freeze) recovers users after they break a
streak.

## Evidence

- **Day-7 retention: 76% treatment vs. 46% control (n=50/variant); Day-30:
  36% vs. 22%.** (`data/metric-findings.md`, Q3)
- **Engagement climbed across exposure, not just a one-time bump:** the
  Comeback-related send's open rate rose from 28% to 56% across 4 sends,
  control stayed flat at 4-6%. That's far above the 12.1% open rate on
  Streakly's *existing* re-engagement nudge for users who already broke a
  streak. (`data/metric-diagnosis.md`, sections 2-3)
- **We targeted the right lever.** The pre-launch decline in weeks 1-4 was
  driven by a rising break rate among starters (38.9% → 56.5%), not a
  falling start rate or a failing notification channel.
  (`data/metric-diagnosis.md`, section 1)

## Recommended Action

Run the full powered test (design in `data/experiment-design.md`) before
scaling, n=50 per variant is directionally strong but not enough on its own
to commit company-wide.

## Ask

Sign-off to run the full test for [duration TBD in `data/experiment-design.md`]
before a scale decision.

## Risk if we wait

Every week without addressing the week-1 break problem locks in the same
retention drop we're already fighting, the pilot's own numbers show the gap
compounds, not stays flat.

---

## Skeptical Marcus: 3 hardest questions

**Marcus, Q1:** "n=50 per variant, is that actually enough to trust, or are
we reading noise as signal?"
*(This is the right first question, and it's the one `data/experiment-design.md`
answers directly with a real significance check, not addressed by hand-waving
here.)*

**Marcus, Q2:** "What's the cost of waiting another quarter to run a bigger
test instead of just shipping this now?"
*Short answer for the memo: the cost is continued exposure to the same
break-rate problem that's already driven a 9-point drop, but the cost of
scaling on n=50 and being wrong is worse, a full rollout of something that
doesn't actually hold up wastes the quarter differently, not less.*

**Marcus, Q3:** "How does this affect our Day-7 retention number
specifically, company-wide, not just in this 100-person cohort?"
*Short answer for the memo: today's actual Day-7 retention is 39%
company-wide (`docs/decision-brief.md`). The pilot shows what's possible in
a small cohort (76% vs. 46%), it does not yet show what happens at full
population scale, that's exactly what the powered test is for.*
