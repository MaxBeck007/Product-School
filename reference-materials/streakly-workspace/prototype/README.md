# Streakly Comeback Screen, Prototype v1

A single-file HTML click-through prototype. Open `index.html` in a browser.

> **Track changed 2026-09-30** (`change_log.md` Entry 7): the mocked lesson
> content is now **miniature painting**, not guitar, and the check-in is a
> **photo capture** (or skip), not a multiple-choice quiz. Everything below
> describes the current, painting-track version. `research/usability-session-1.md`
> and `change_log.md` Entries 1-2 tested the earlier guitar/quiz version and
> are left as a historical record, not updated to match.

## PM Brief

**User:** 24-year-old who hit a 12-day streak, missed two days, and has not opened
the app since.
**Job to be done:** get back in without feeling they lost everything.
**Feature:** personalized Comeback screen, best-streak stat, one 60-second comeback
lesson, one-tap streak-freeze offer.
**Constraint:** use data Streakly already has, no new integrations.

Full brief with sourcing: `../docs/pm-brief.md`.

## What's in this prototype

Three screens, walkable in the browser with real clicks (no code changes needed to
demo):

1. **Comeback screen** (entry point): personalized welcome, best-streak stat (🔥
   12), a comeback session card (no time-box, dropped 2026-09-30 per
   `change_log.md` Entry 8), and a one-tap streak-freeze offer.
2. **Lesson mock**: a miniature-painting reference card ("Skirmisher, Layer 2,"
   basecoat + highlight), then a photo check-in, take/upload a photo of
   today's progress, or skip. `Continue` unlocks either way, no pass/fail.
   Content is a realistic mock, not wired to Streakly's real lesson engine or
   a real camera roll.
3. **Done screen**: confirms day 1 is restarted and that the best-streak stat is
   still saved.

Clicking "Apply streak freeze" shows an inline confirmation toast without leaving
the screen, no separate flow.

## Key decisions made during the interview (P3L1)

- **Miniature painting track, mocked content.** Originally guitar at P3L1,
  chosen then to make the lesson concrete for usability testing and design
  review, not because guitar was the primary track in scope. Changed to
  miniature painting 2026-09-30 (`change_log.md` Entry 7), same reasoning
  applies to the new track.
- **Streak freeze is a single free, one-tap grant.** No cost or expiry logic
  shown. The real freeze rules (how many, when they expire) are an open item
  Raj flagged in the original P1 Slack thread and are out of scope here.
- **In-app screen only.** Notification tone/copy is a separate, already-identified
  problem (`research/nps-analysis.md`) but is not part of this feature's scope.
- **Tone is deliberately "welcome back," never "you lost your streak."** This is
  the direct response to the dominant theme across interviews and NPS: the reset
  feels punishing and irreversible.
- **Mobile-width single screen**, matching the product's "app" framing, no
  desktop layout in this pass.

## What this prototype is not

- Not wired to real user data, the best-streak number (12) is hardcoded to match
  the brief's example user.
- Not testing streak-freeze eligibility rules, who qualifies and how many freezes
  they get is still an open product decision.
- Not testing notification copy, that's a separate workstream.
