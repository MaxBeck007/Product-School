# Module 5 · Decide — Read the Numbers & Communicate Clearly

> How do I prove what happened, and get a decision on it?

Get answers from data without SQL, diagnose what moved a metric, write recommendations that get decisions, design trustworthy experiments, and produce PRDs, updates, and decks that make an argument.

## Findings · Diagnosis · Memo

*Get answers from data without SQL, diagnose what moved the metric, recommend a decision.*

Querying the course dataset (500 users, 2,347 sessions across 5 cohort weeks) in DuckDB: Day-7 retention declined steadily pre-launch, cohort 1 through 4, 60% → 44%. In week 5, the Comeback screen ran as a 50/50 pilot: **treatment 76% Day-7 / 36% Day-30 vs. control 46% / 22%** (n=50 per variant), and engagement with the Comeback send climbed from 28% to 56% across four sends while control stayed flat at 4-6%. Diagnosis: it's not a falling start rate or a failing notification channel — it's a **rising break rate among starters**, 38.9% → 56.5% across cohorts 1-4, moving in lockstep with the retention decline. The existing re-engagement nudge barely reaches this population (roughly 6% of week-1 streak-breakers ever open one).

The results memo to Marcus leads with the recommendation, not the pilot: **run a full, properly powered test before scaling company-wide** — the signal is strong but n=50/variant is too small to commit on directly.

**Important scope note carried from `CLAUDE.md`:** this data stack (`data/`, `docs/recommendation-memo.md`) works from a course-supplied exercise dataset in which the Comeback screen had *already* shipped. Nothing has actually shipped — everywhere else in this workspace (the prototype, the PRD, the hypothesis doc) the feature is still an unbuilt, discovery-stage concept. Both are real artifacts of the course sequencing; they should never be shown to the same reader without saying so first.

## Experiment Design

- **Hypothesis:** The Comeback screen improves Day-7 retention by at least 5 percentage points over the 46% control baseline.
- **Variant:** Comeback screen (best-streak stat + 60-second lesson + one-tap freeze) vs. the standard cold reset.
- **Primary metric + guardrail:** Primary — Day-7 retention. Guardrails (proposed, not yet agreed) — break rate among new users should not rise; notification opt-out rate should not rise.
- **Sample / duration:** The pilot result (76% vs. 46%) is statistically significant (z=3.075, p=0.0021) despite n=50 — but that's because the effect is unusually large, not because n=50 is generally sufficient. Detecting a more realistic 5-point lift at 80% power / 95% significance needs **≈1,568 per variant (≈3,136 total)**, which needs ≈392 eligible users/week to fit an 8-week window. **The real weekly eligible-user volume is unconfirmed** — the single biggest open input blocking a committed test duration.

## Reusable Skills + Deck

*PRD skill, status-update skill, and the deck that makes the argument.*

- **PRD skill:** The `docs/prd.md` pattern — read the full research and decision-brief stack, calibrate language to the named audience (Raj and Lena, not leadership) using their stakeholder profiles, and structure as Problem / User / Goals & Non-Goals / Success Metrics / User Stories / Open Questions, with every claim cited to a source file. Marked for promotion to a reusable skill immediately after first use.
- **Status-update skill:** `skills/weekly-status.md` (tone/calibration rules) plus `skills/friday-status.md` (derives Shipped/In progress/Blocked from the workspace itself rather than requiring it by hand).
- **Deck:** `docs/presentation.md` — a 6-slide quarterly-review deck for Marcus (Problem → Why Now → Proposal → Evidence → Plan → The Ask), backed by full speaker notes in `docs/presentation-notes.md`, built entirely from files already in the workspace with no invented numbers.

**Source:** `reference-materials/streakly-workspace/data/metric-findings.md`, `data/metric-diagnosis.md`, `data/experiment-design.md`, `docs/recommendation-memo.md`, `docs/prd.md`, `docs/presentation.md`, `skills/weekly-status.md`, `skills/friday-status.md`.
