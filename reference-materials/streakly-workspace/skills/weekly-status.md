# Reusable Skill: Weekly Status, Calibrated by Stakeholder

> **Source of this template:** `docs/prd.md`-era weekly snapshot (P6L3 exercise),
> calibrated against `stakeholders/raj.md`, `stakeholders/lena.md`,
> `stakeholders/marcus.md`. Reuse by supplying a new Shipped/In progress/Blockers
> list and re-running the same calibration logic below.

## How to use this

Given a raw weekly snapshot (Shipped / In progress / Blockers, no formatting),
produce two updates:

1. **Team update (Raj + Lena):** async-first, bullet points over paragraphs, no
   surprises buried in prose. Surface the blocker with enough specificity that
   Raj can act without a follow-up question. Lena gets the qualitative/user-facing
   items surfaced, not just engineering status.
2. **Leadership update (Marcus):** recommendation or headline status in the first
   sentence, not the last. One page max. Connects each item to the business
   outcome (Day-7 retention), not just activity. Names the ask and the deadline
   risk explicitly, since he responds to "what would that look like" once framing
   is concrete.

Do not invent metrics or dates not present in the source snapshot. If a blocker's
estimate is genuinely unknown, say "TBD" rather than guessing a date.

---

## Example run (P6L3 source snapshot)

### 1. Team update, for Raj and Lena

**Streakly Comeback screen, weekly update**

Shipped this week:
- Interview synthesis done (Priya, Tom, Amara)
- Competitive matrix done (Duolingo, Babbel, Elevate), 2 white-space gaps
  identified
- Reddit sentiment analysis done, confirms the friction points from the
  interviews and competitive research
- Prototype v1 live, tested across all three personas

In progress:
- PRD, 70% drafted
- Usability sessions, 3 of 5 scheduled

Blockers:
- **Streak-freeze logic needs a data model change (Raj flagged this).**
  Estimate still TBD, flagging now rather than waiting so it doesn't become a
  surprise at the next planning point.
- Marcus is out Thursday and Friday, review this week will be async only, no
  live sign-off expected before next week.

Lena: the prototype and persona test notes are ready when you want to look at
them directly rather than hear a description, nothing new to review beyond
what's in the workspace already.

### 2. Leadership update, for Marcus

**Recommendation:** on track, no schedule risk yet, but flagging one open
engineering item now so it doesn't become a surprise later.

This week: interviews, competitive research, and Reddit sentiment analysis are
all complete and point the same direction, users don't come back after a
broken streak because there's no way back in, not because the lessons
themselves are bad. Prototype v1 is live and held up across all three test
personas.

Still open: the PRD is about 70% drafted; 3 of 5 usability sessions are
scheduled. One blocker worth knowing about now rather than later: Raj flagged
that the streak-freeze mechanic needs a data model change, and we don't have
an estimate yet. This doesn't change the plan today, but it's the kind of item
that could affect timeline once we do have a number.

You're out Thursday and Friday, review this week will be async, nothing needs
a live decision from you before then.
