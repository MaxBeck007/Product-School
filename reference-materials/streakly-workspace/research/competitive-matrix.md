# Competitive Matrix: Streak, Reminder, and Comeback Systems

> **Method:** web search, retrieved 2026-09-28. Streakly context: consumer habit +
> micro-learning app, Day-7 retention dropped 48% → 39%, users break a streak in
> week 1 and mostly don't return. Excluded social-media and long-form course
> platforms per the brief.

## Competitors identified

4 selected (course brief asked for 3-5, starting with Duolingo, Babbel, Elevate):
**Duolingo, Babbel, Elevate, Habitica.** Habitica added as the 4th because it is a
streak/habit-gamification app outside language learning, and it's already the
reference codebase used later in this course (P4L1), so the two exercises reinforce
each other.

---

## Duolingo

- **Core features:** gamified daily lessons, streak counter, leaderboards,
  achievements. [Duolingo streak help](https://www.duolingo.com/help/what-is-a-streak)
- **Pricing model:** freemium; Duolingo Max add-on at $29.99/mo or $168/yr for AI
  conversation partner ("Video Call") and AI roleplay. As of early 2026, the
  AI grammar-explainer ("Explain My Answer") that used to be Max-only is now free
  for everyone. [Duolingo Max review](https://copycatcafe.com/blog/duolingo-max)
- **Target customer:** broad consumer mass market, casual to committed language
  learners.
- **Comeback/streak-freeze system:** streak freeze must be bought *in advance* with
  gems (200 gems on iOS/Android, 10 lingots on web) to protect a specific day; a
  *streak repair* can be purchased *after* a miss to restore a broken streak, also
  with gems. Users who reach a 100-day streak get 3 free freezes.
  [Duolingo Wiki: Streak freeze](https://duolingo.fandom.com/wiki/Shop/Streak_freeze),
  [Lingoly streak freeze guide](https://lingoly.io/duolingo-streak-freeze/)
- **Notable recent changes:** reported streak-freeze gem prices increasing over time
  (users cite 200 → 480 gems on some platforms/regions); broader 2025 "energy system"
  overhaul drew backlash, in an 11,000-user community poll nearly half disliked it,
  most commonly because it penalizes skilled learners. In 2026 CEO Luis von Ahn said
  the company is deliberately prioritizing growth and the free experience over
  near-term monetization. [X/Grok summary](https://x.com/grok/status/1959194747001790695),
  [Globe and Mail on Duolingo AI/financials](https://www.theglobeandmail.com/investing/markets/stocks/DUOL-Q/pressreleases/267659/can-ai-actually-improve-duolingo-s-financials-in-2026/)

## Babbel

- **Core features:** flashcards, fill-in-the-gap, multiple choice, listen-and-repeat,
  spaced-repetition review; newer AI pronunciation-feedback beta ("Babbel Speak").
  [Babbel review, Forbes Advisor](https://www.forbes.com/advisor/education/student-resources/babbel-review/)
- **Pricing model:** subscription, roughly $18/mo full price, $8-15/mo discounted;
  e.g. $107.40 for 12 months all-language, $299.99 lifetime.
  [Babbel pricing](https://my.babbel.com/en/prices)
- **Target customer:** adults who want structured, curriculum-style language
  learning over gamified competition.
- **Comeback/streak-freeze system:** tracks activity streaks and badges, but by its
  own positioning leans on reminders and spaced repetition rather than a
  streak-protection mechanic. No streak-freeze feature found in search results.
- **Notable recent changes:** launch of Babbel Speak (AI pronunciation feedback).
  [Babbel review 2026](https://www.studyfrenchspanish.com/babbel-review/)

## Elevate

- **Core features:** 40+ cognitive-training games (math, memory, speaking,
  vocabulary), adaptive difficulty, weekly performance reports.
  [Elevate review](https://nibble-app.com/blog/elevate-app-review)
- **Pricing model:** ~$39.99/yr or $9.99/mo, reported at roughly $4/mo effective on
  the annual plan as of May 2026; limited free tier (3 games/day, no skill choice).
- **Target customer:** professionals building practical desk-job skills (public
  speaking, speed reading, vocabulary), not casual gamers.
- **Comeback/streak-freeze system:** training streaks plus 150+ achievements and a
  "workout calendar" for motivation. No streak-freeze or reactivation-after-lapse
  feature surfaced in search results.
- **Notable recent changes:** none specific to streak/comeback mechanics found in
  this search pass.

## Habitica

- **Core features:** RPG-style habit tracking; an avatar gains XP/gold for
  completed habits and loses HP for missed ones; social "party" quests with friends.
  [Habitica comparison](https://66streaks.com/blog/streaks-app-vs-habitica/)
- **Pricing model:** free with a functional core tier; paid subscription ~$4.17/mo
  or $49.99/yr for unlimited habits, advanced reminders, an "off mode" for planned
  breaks, and Apple Health integration; $119.99 lifetime option.
  [Habitica pricing summary](https://www.jotform.com/blog/best-apps-for-habit-tracking/)
- **Target customer:** habit-trackers who respond to game mechanics broadly, not
  limited to learning.
- **Comeback/streak-freeze system:** no simple streak counter; damage/HP loss for a
  miss is the analog. "Off mode" lets a user pause tracking *in advance* of a known
  break, so nothing is lost, but this must be toggled proactively; it isn't a
  reactive comeback flow for an unplanned miss.
- **Notable recent changes:** none specific to comeback mechanics found in this
  search pass.

---

## Comparison matrix

| | Duolingo | Babbel | Elevate | Habitica |
| --- | --- | --- | --- | --- |
| Streak mechanic | Yes, core | Yes, secondary | Yes, secondary | No counter; HP/damage instead |
| Recovery after a miss | Paid streak repair (gems) | None found | None found | None found (only proactive "off mode") |
| Prevent a miss in advance | Paid streak freeze (gems) | None found | None found | Proactive "off mode" (free w/ subscription) |
| Acknowledgment of return after a lapse | Not found; miss triggers guilt-toned notifications per user complaints, not a personalized welcome-back | Not found | Not found | Not found |
| Monetizes the recovery mechanic | Yes | N/A | N/A | N/A |

---

## White-space gaps for Streakly

1. **No competitor offers a free, personal "welcome back" moment after an unplanned
   miss.** Duolingo's recovery mechanic (streak repair) exists, but it is paid and
   transactional, exactly the kind of monetized friction that drove the 2025 energy-
   system backlash. Babbel, Elevate, and Habitica have no reactive comeback flow at
   all for an unplanned lapse. Streakly's Comeback screen concept (best-streak stat,
   short lesson, one-tap freeze) as a *free, immediate* response to a lapse is not
   something any of the four are doing.

2. **No competitor pairs acknowledgment with a low-effort re-entry action.** All four
   either penalize a miss (Duolingo, Habitica's HP loss) or say nothing about it
   (Babbel, Elevate). None combine "here's what you built" with "here's one small
   thing to rebuild momentum" in the moment right after a lapse. Habitica's "off
   mode" is the closest analog to forgiveness, but it only works if the user plans
   the break in advance, it does not help someone who already missed unexpectedly,
   which is exactly Tom and Amara's situation in the interview and NPS research.
