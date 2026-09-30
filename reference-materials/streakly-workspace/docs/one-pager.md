# Streakly Comeback Screen: One-Pager

> **Added 2026-09-28 (P7L4 fix F1):** the pilot figures below come from the P5
> exercise dataset. **Nothing has actually shipped**, the feature exists only as
> a click-through prototype. See the "What is actually real" section of
> `CLAUDE.md` before sharing this.

**Status:** pilot is statistically significant (p=0.002, n=50/variant), but
too small to scale on directly. Recommendation: run a full powered test
(design ready) before company-wide rollout. Full detail: `docs/recommendation-memo.md`.

**The number that matters:** Day-7 retention dropped 48% → 39% after the v2
redesign. Root cause, confirmed with real data: rising break rate among new
users, 38.9% → 56.5% across 4 weeks, not fewer signups or a failing
notification channel.

**The fix and its result:** a personalized Comeback screen (best-streak stat,
a comeback session, one-tap freeze) tested 50/50 in cohort week 5: **76% vs.
46% Day-7 retention, 36% vs. 22% Day-30.** [The P5 pilot dataset predates the
2026-09-30 track/mechanic change (`change_log.md` Entries 7-8); the pilot
numbers are unaffected, only the "60-second lesson" wording is updated here.]

---

## What's built, by phase

**P1, Get Oriented** (partial, L2-L5 still open)
- `project-skeleton.md`, PRD skeleton from the original Slack thread.

**P2, Know Your Users** (complete)
- `research/interview-synthesis.md`, `research/nps-analysis.md`,
  `research/competitive-matrix.md`, `research/competitive-reddit.md`
- `docs/decision-brief.md`, the recommendation to bet on the Comeback screen
  over notification-only fixes.

**P3, Build and Learn Fast** (complete)
- `docs/pm-brief.md`, `prototype/index.html` + `README.md`, a 3-screen
  click-through, 2 fixes logged from mock usability testing
- `docs/hypothesis.md`, `docs/triad-session.md`

**P4, Work with Your Team** (complete)
- `docs/codebase-summary.md`, real tour of a public reference repo (Habitica),
  found it has the same streak-freeze data gap Raj flagged
- `stakeholders/raj.md`, `lena.md`, `marcus.md`
- `docs/spec-readiness.md`, `docs/design-review.md`, `docs/qa-checklist.md`

**P5, Data** (complete)
- `data/metric-findings.md`, 4 questions answered with real SQL against your
  5 uploaded CSVs (500 users, 2,347 sessions, 1,740 nudges, 500 retention
  rows, 400 sends, all verified complete)
- `data/metric-diagnosis.md`, metric tree + 4 ranked hypotheses (one already
  ruled out by the data: churn wasn't from ignoring the comeback nudge)
- `docs/recommendation-memo.md`, `data/experiment-design.md`, real
  significance and sample-size math (need ~1,568/variant for a 5pt MDE)

---

## Open gaps, carried forward

- **P1L2-L5** never finished: no CLAUDE.md, no `strategy.md`, no weekly-status
  skill.
- **Freeze eligibility rule exists only as a discussed position**
  (`docs/spec-readiness.md`), not built into the prototype.
- **Real weekly eligible-user volume is unknown** (`data/experiment-design.md`
  flags this as the number to confirm before committing to the 8-week test
  window).
- **Track personalization** (lesson content is fixed to one example track,
  miniature painting as of `change_log.md` Entry 7, guitar before that) is
  still an open design decision.

## Next: P6, Communicate Clearly
