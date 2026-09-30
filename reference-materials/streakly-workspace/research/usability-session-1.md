**`MOCK SESSIONS, NO REAL USERS.` Priya, Tom, and Amara are personas. No real
user has seen this prototype. Do not quote any line from this file as user
research.**

# Usability Session 1, Comeback Screen Prototype v1

> **Label: illustrative / mock data.** No real usability sessions were run.
> Streakly and Priya, Tom, and Amara are fictional personas from this course
> exercise; these notes are invented to complete the P3L2 exercise and should
> not be cited as real user research. Written to be plausible given each
> persona's established profile (`research/interview-synthesis.md`) and their
> actual reaction to what's built in `prototype/index.html`, not to any other
> version.

Same 4 questions asked of all three:
1. What do you think this does?
2. How would you arrive at this experience?
3. Would you come back and restart your streak based on this?
4. If you had a magic wand, what would you change?

---

## Priya (power user, 14-month streak)

1. Got it immediately, "the 'welcome back' framing is nice, feels less cold than
   what I remember."
2. "I'd probably land here if I missed a day traveling, that's the only way I'd
   ever see this."
3. Yes, but flagged: "the lesson is miniature painting, I'm on the language
   track, so this version wouldn't actually be my lesson. If it's supposed to
   be personalized it should know what I was doing before I lapsed."
4. "Make the lesson match whatever track I was actually on."

## Tom (churned, broke a 12-day streak)

1. "It's telling me my streak's still worth something, which... okay, that's
   already different from what I remember."
2. Matched his real situation without prompting: "yeah, this is exactly the spot
   I would've hit after missing two days."
3. Cautiously yes, but skeptical of the freeze copy: "'no cost, no catch' is what
   everyone says right before there's a catch. I'd want to actually see it
   applied before I trust it." (He tapped the freeze button and reacted well to
   the confirmation toast once he saw it: "oh, okay, that's actually just... done.
   Fine, that's better than I expected.")
4. "Don't make me guess if there's a catch, show me it's free before I have to
   ask."

## Amara (new user, 4 days in, anxious about streak pressure)

1. Understood the best-streak stat right away. Less clear on the freeze: "not
   sure if this happens every time I miss a day or just this once."
2. Couldn't quite picture arriving here herself, she hasn't broken a streak yet,
   but said "I can see myself being relieved if I ever do."
3. Yes, tone-wise, but flagged the lesson's quiz: "I picked wrong on the first
   try and just... nothing told me it was wrong, it just didn't let me continue.
   That's the same feeling I already have about the streak, like I have to get
   it right or I'm stuck."
4. "Don't make the comeback lesson feel like a test too. The whole point was that
   I wasn't supposed to feel like I could fail."

---

## Analysis

### What's working

- The "welcome back" tone lands with all three and is read as a clear departure
  from a punishing reset, this is the core hypothesis and it's landing.
- The best-streak stat is understood immediately by everyone without explanation.
- Once Tom actually taps the freeze button and sees the confirmation, his
  skepticism resolves. The mechanic works, the copy alone doesn't earn trust.

### Top 2 friction points

1. **The lesson content is fixed to one track (miniature painting), not
   personalized to the user's actual track.** Raised directly by Priya;
   undermines the "personalized" promise of the feature for anyone not on
   that track.
2. **The quiz-style check-in reintroduces exactly the pressure the feature is
   supposed to remove.** Raised directly by Amara, and echoes Tom's broader
   skepticism about being tested or penalized. This is the more serious issue:
   it works against the feature's entire premise, not just its polish.

### Single highest-priority change

Fix friction #2 first: remove the "right answer required to continue" gate on the
comeback lesson quiz. The feature exists to remove pressure; a wrong-answer block
recreates it, and it does so for exactly the anxious, early-lapse user (Amara's
profile) that the feature is most trying to protect. Friction #1
(track-personalization) is real but is a data/scope decision for a later pass,
this fix is a change to what's already built.
