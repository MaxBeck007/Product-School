# Learning Synthesis and Hypothesis

> **Sources:** `change_log.md`, `docs/decision-brief.md`.

## What we know

- Day-7 retention dropped from 48% to 39% after the v2 streak/notification
  redesign, and the punishing, irreversible reset is the dominant, most
  cross-source-confirmed driver (`docs/decision-brief.md`, findings 1-3).
- No competitor offers a free, personal comeback moment after an unplanned miss,
  this is real white space (`docs/decision-brief.md`, finding 4).
- In prototype testing, the "welcome back" tone and the best-streak stat land
  immediately, no explanation needed (`change_log.md`, Entry 1).
- Copy claims alone ("no cost, no catch") don't earn trust from a previously
  churned, skeptical user, seeing the mechanic actually resolve did
  (`change_log.md`, Entry 2, Tom).
- Test-like framing can persist even after the underlying penalty is removed;
  wording alone can still trigger the anxiety the feature is trying to remove
  (`change_log.md`, Entry 2, Amara).

## What we're assuming

- **Assumption:** a mocked, single-track lesson (guitar) is a fair stand-in for
  what a fully personalized, track-matched lesson would do in production.
- **Assumption:** a simple, free, one-tap streak-freeze grant is the right
  version of the mechanic to test; the real eligibility and expiry rules are
  still an open item Raj flagged and are not resolved here.
- **Assumption:** the comeback experience is the highest-leverage fix relative
  to notification tone, based on the NPS split (6 comments on the reset vs. 2 on
  notifications), not on a controlled comparison of the two.

## What we still don't know

- Whether real users respond the way the mocked personas did, everything in
  `change_log.md` so far is illustrative test data, not real user behavior.
- Whether Tom's specific "no cost, no catch" skepticism generalizes to other
  churned users or is particular to his profile.
- What actual retention lift this produces, that requires live data (P5).
- The real streak-freeze eligibility and expiry rules, still open with Raj.

---

## Hypothesis Statement

We believe that a personalized Comeback screen, showing a user's best-streak
stat, a low-pressure 60-second comeback lesson, and a one-tap streak-freeze, will
deliver renewed engagement after a broken streak for Streakly users in their
first 7 days, as measured by Day-7 retention rate.
