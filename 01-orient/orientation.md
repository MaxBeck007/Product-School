# Module 1 · Orient — Get Oriented

> How do I make Claude Code know my product, and stop it building blind?

Set up persistent memory so Claude Code knows your product and stops building blind. Run your first real session, learn the interview-first habit, and set up `CLAUDE.md` plus the three core files.

## project.md

*What are we building and why?*

- **Goal this quarter:** Recover Streakly's Day-7 retention, which dropped from 48% to 39% after the v2 streak/notification redesign, by validating a "Comeback experience" for users who break a streak in their first week.
- **Bet:** The Comeback screen — a personalized best-streak stat, a 60-second comeback lesson, and a one-tap streak-freeze — replacing the current cold reset-to-zero and its "you lost your streak" push.
- **Not doing:** New third-party integrations (new data *fields* are still in scope); fixing notification tone/cadence (a real but secondary theme); personalizing lesson content to the user's actual track (logged as an open item, not this pass).

## strategy.md

*Where does this fit in the bigger picture?*

I'm the PM on Streakly's Engagement squad — everything about keeping new users active in their first weeks (home screen, daily lesson loop, streak mechanics, push notifications). My triad is Raj (Senior Engineer) and Lena (Product Designer); I report to Marcus, Head of Product. We're in **discovery**: no committed scope, 8 weeks from sprint kickoff.

The key tension I'm navigating: re-engagement nudges vs. notification fatigue — users who feel nagged turn notifications off entirely, closing the one channel that could otherwise win them back after a lapse. The open decision is how to bring users back after they break a streak, and the working hypothesis (from Marcus/Raj/Lena's Monday Slack thread) is that users go passive because breaking a streak feels like failure with no graceful way back in, not because the daily lessons themselves are bad.

## change_log.md

*Running log of decisions and what changed, and why.*

| Date | Change | Why |
|------|--------|-----|
| 2026-09-28 (backfilled 2026-09-30) | Logged day 1 of discovery: role/squad, phase, and the Comeback-screen hypothesis | P1L4 asked for this on day 1; the team skipped straight to P2/P3 before it happened, so it was written after the fact from `project-skeleton.md`, `CLAUDE.md`, and `docs/decision-brief.md` |
| 2026-09-28 | Removed the "must pick the right answer to continue" gate on the comeback lesson quiz | Mock usability testing (Amara, Tom) showed the pass/fail gate reintroduced the exact punishing pressure the feature exists to remove |
| 2026-09-28 | Relabeled the quiz prompt from "Quick check" to "Just for fun" | Even after the penalty was removed, the test-like label alone still primed anxiety (Amara) |
| 2026-09-28 | Rewrote the PRD constraint from "no new integrations" to explicitly allow new *fields* | Roleplayed spec-readiness session caught that the freeze rule needs new fields (pre-break streak length, freeze-spent state) that "no new integrations" had implicitly ruled out |
| 2026-09-28 | Added a "What is actually real" section to CLAUDE.md distinguishing the unbuilt prototype (Framing A) from the P5 exercise dataset that assumes a pilot already ran (Framing B) | The workspace otherwise contradicts itself about whether anything shipped — nothing has |

## First Skill

*Name + what it does + when to use it.*

- **Name:** `skills/weekly-status.md` — Reusable Weekly Status Update, the first skill built in this workspace (P1L5).
- **What it does:** Takes a raw, unformatted list of what shipped, what's in progress, and what's blocked, and turns it into two calibrated updates: a team version for Raj and Lena (async-first, bullet points, blockers specific enough to act on without a follow-up question) and a leadership version for Marcus (recommendation or headline status in the first sentence, tied to Day-7 retention rather than activity, one page max). It never invents a metric or date — "TBD" beats a guess.
- **When to use it:** Every week, any time I need to report status to two audiences who need different levels of detail. Later extended by `skills/friday-status.md` (Module 6), which derives the raw Shipped/In progress/Blocked list from the workspace itself instead of requiring it by hand.

**Source:** `reference-materials/streakly-workspace/CLAUDE.md`, `reference-materials/streakly-workspace/project-skeleton.md`, `reference-materials/streakly-workspace/change_log.md`, `reference-materials/streakly-workspace/skills/weekly-status.md`.
