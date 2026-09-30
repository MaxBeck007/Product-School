# Streakly Comeback Experience, PRD Skeleton

> **Status:** skeleton, not a finished document. Starting point for the Thursday session.
> **Source:** #product-growth Slack thread, Monday 9:14am (Marcus, Raj, Lena, PM).
> **Scope note:** every statement below is traceable to the thread. Gaps are marked
> `[NOT IN THREAD]` rather than filled in.

---

## Problem Statement

Day-7 retention is at 39%, down from 48% since the streak redesign shipped. The drop
is sharpest among users who break their streak in week 1: once someone misses two days
in a row, churn is almost double.

The team's read on the cause: breaking a streak feels like failure and there is no
graceful way back in. Today the app acts like nothing happened. Same home screen,
streak back at 0, no acknowledgment. The "you lost your streak" push has a brutal tone,
and when people tap through, the app offers them nothing and drops them back at day zero.

Open question raised in the thread and not resolved: is the problem the streak reset
itself, or notifications nagging people at the moment they are most likely to quit?
Raj's position is both, with the bigger issue being what happens after the break.

**Hypothesis as stated in the thread:** users go passive because breaking a streak feels
like failure and there is no graceful comeback. What is needed is something that pulls
them back with a reason specific to them and their progress, not a generic "keep going!"

---

## Goals

- Align the team on the problem before designing solutions. This is Marcus's explicit
  ask for Thursday.
- Give users who break a streak a graceful way back in, acknowledged and personal
  rather than a cold reset.
- Make the re-entry reason specific to the individual user's progress.

`[NOT IN THREAD]` No target retention number, no date, and no success threshold were
stated. See Success Metrics.

---

## Non-Goals

- Designing the solution. Marcus asked for the problem write-up first: "I want to make
  sure we're aligned on the problem before we start designing solutions."
- New data sources or integrations. Raj: "no new data sources."

`[NOT IN THREAD]` Nothing else was explicitly ruled out. Whether notification
tone and frequency are in or out of scope is unresolved, Marcus raised it and the
thread did not close it.

---

## Success Metrics

**Primary metric named in the thread:** Day-7 retention rate. Current 39%, prior 48%.

`[NOT IN THREAD]` No target value, no measurement window, and no secondary metrics
were agreed. Candidates implied by the discussion but never stated as metrics:
- share of users who break a streak in week 1
- churn rate after two consecutive missed days (described only as "almost double")
- return rate after a break (described only as "roughly 80% never return" in the
  wider scenario, not in this thread)

This section needs a decision before Thursday.

---

## Solution direction discussed, not committed

Captured for continuity, not as scope. Lena's sketch, a **Comeback screen** shown
instead of a cold reset:

- your best-streak stat
- one 60-second comeback lesson to get momentum back
- one-tap streak-freeze to protect the streak you have rebuilt

Raj's feasibility read: technically doable with what we have. Needs logic for who
sees it and the freeze rules. No new data sources.

---

## Open Questions

1. Is the root cause the streak reset, the notification timing and tone, or both?
2. Who qualifies to see a comeback experience, and what are the streak-freeze rules?
   (Raj flagged both as undefined.)
3. What Day-7 retention target counts as success, and by when?
4. Are notification tone and cadence in scope, or a separate workstream?

---

## Participants

| Person | Role in thread |
| --- | --- |
| Marcus | Head of Product. Called the Thursday meeting, asked for the problem write-up. |
| Raj | Senior Engineer. Data read on the week-1 break pattern, feasibility. |
| Lena | Product Designer. User research signal, Comeback screen sketch. |
| Me | PM, Engagement squad. Framed the hypothesis. |
