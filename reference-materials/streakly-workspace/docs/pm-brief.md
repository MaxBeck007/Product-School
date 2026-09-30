# PM Brief: Comeback Screen Prototype

> **Status:** approved for prototyping. Given brief from the course exercise plus
> decisions made to fill gaps the research doesn't answer. Every decision below is
> labeled by source.

## Given (from the exercise brief, not invented)

- **User:** 24-year-old who hit a 12-day streak, missed two days, and has not
  opened the app since.
- **Job to be done:** get back in without feeling they lost everything.
- **Feature:** personalized Comeback screen: best-streak stat, one 60-second
  comeback lesson, one-tap streak-freeze offer.
- **Constraint:** use data Streakly already has, no new integrations.

## Grounded in research (from the four P2 files, not invented)

- The reset must feel forgiving, not punishing, this is the dominant theme across
  interviews and NPS (`research/interview-synthesis.md`, `research/nps-analysis.md`).
- No competitor offers this for free today, this is the identified white space
  (`research/competitive-matrix.md`).
- The comeback moment needs to pair acknowledgment with a low-effort action, not
  just one or the other (`research/competitive-matrix.md`, gap 2).

## Decisions made to fill what the brief and research don't specify

*Max confirmed proceeding on my recommendation for the open questions rather than
answering each individually. Flagging each as an assumption so it's easy to
challenge later.*

- **Assumption:** the comeback lesson uses the **guitar** track (one of the four
  tracks named in the product description: languages, guitar, coding, chess),
  chosen because it's easy to mock a plausible 60-second lesson for and easy for
  a design reviewer to evaluate without domain knowledge.
  **Changed 2026-09-30 (`change_log.md` Entry 7):** Max instructed a track
  change to miniature painting, with the quiz replaced by a photo check-in.
  This paragraph is left as-is as the original assumption and its reasoning;
  it is superseded, not deleted.
- **Assumption:** the lesson content is a **realistic mock**, not wired to a real
  lesson engine, since the lesson content system itself isn't in scope for this
  prototype.
- **Assumption:** the streak-freeze offer is a **single free, one-tap grant** with
  no cost or expiry logic shown, kept simple because the constraint is "no new
  integrations" and freeze-rule complexity (how many, when they expire) is an
  open item Raj already flagged in the P1 Slack thread, not something to resolve
  in a prototype.
- **Assumption:** the best-streak stat shows just the number and a short label
  ("Your best: 12 days"), no badge or animation, to keep this a discovery-stage
  prototype rather than a polished design.
- **Non-goal:** notification copy and tone are a separate, already-identified
  issue (`research/nps-analysis.md`) but are **not** part of this feature's scope.
  This prototype is the in-app screen only.
- **Assumption:** single mobile-width screen, matching "app" in the product
  description; no responsive/desktop layout for this pass.
- **Tone:** personal and forgiving throughout, "welcome back," not "you lost your
  streak."

## What this prototype needs to prove

Whether a forgiving, personalized comeback moment (vs. a cold reset) makes a lapsed
user willing to re-engage, this is the mechanism behind the hypothesis in
`docs/decision-brief.md`.
