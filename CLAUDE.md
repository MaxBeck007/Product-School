# CLAUDE.md — Persistent Memory

> The file Claude Code reads at the start of every session. Short, true, current — the difference between Claude building blind and building with context.

## The Product

*What it does, for whom, current focus.*

**Streakly** is a consumer habit + micro-learning app (pick a track, do a 5-minute daily lesson, build a streak). I'm the PM on the Engagement squad — home screen, daily lesson loop, streak mechanics, push notifications. Triad: Raj (Senior Engineer), Lena (Product Designer). I report to Marcus, Head of Product.

**Current focus:** the **Comeback experience** — Day-7 retention dropped from 48% to 39% after the v2 streak/notification redesign, and once a user breaks a streak in week 1, most never come back. The bet is a personalized Comeback screen (best-streak stat, 60-second comeback lesson, one-tap streak-freeze) that replaces the current cold reset-to-zero. We're in **discovery**: no designs committed, no scope locked, 8 weeks from sprint kickoff. Key tension: re-engagement nudges vs. notification fatigue.

## How I Want Claude to Work With Me

- **Interview first:** ask clarifying questions before building.
- **Tone:** Plain, declarative language. Cite the file behind every factual claim. Label anything mock, roleplayed, or illustrative explicitly — never let a constructed example read as real user or teammate input.
- **Defaults:** Prompt me to save a file when it's worth keeping, including new files we create later — don't wait to be asked. Log every substantive session to `change_log.md` before ending it.
- **Never:** Never invent a fact, number, quote, or file path. Never build anything substantial while an open question is unresolved without asking first. Never let technical content read as direction to the engineering team — frame it as context or an open question instead.

## Glossary (my product's words)

| Term | Meaning |
|------|---------|
| Day-7 retention | Share of a signup cohort still active on day 7. Cohort-level and pilot-arm (treatment/control) figures are different measurements — never mix them. |
| Break rate (among starters) | Share of users active on day 1 but *not* on day 7. It's a proxy — no literal streak-break event field exists in the data. |
| Comeback screen | The bet: best-streak stat + 60-second comeback lesson + one-tap streak-freeze, shown instead of a cold reset when a user breaks a streak. |
| Alert threshold | ±3 percentage points week over week (not 2 points) — at ~50 users per arm, a 2-point move is roughly one user. |
| Escalation flag | Break rate among starters passing 56.5%, cohort 4's high-water mark. |
