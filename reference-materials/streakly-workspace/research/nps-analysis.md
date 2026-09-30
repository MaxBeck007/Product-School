# NPS Verbatim Analysis

> **Source:** 10 raw NPS comments provided in the P2L2 exercise.
> **Method:** each comment tagged to one or more themes; mention counts are of
> comments, not quotes (a comment can carry more than one theme).

## Themes mentioned more than once, ranked by frequency

| Rank | Theme | Mentions | Comments |
| --- | --- | --- | --- |
| 1 | Streak reset to zero is punishing and kills motivation | 6 | "I hit a 20-day streak, missed one day, and it reset to zero. I haven't opened the app since. Felt pointless to start over." / "I want Streakly to feel like a coach... not a scorekeeper that punishes me" / "I broke my streak once and there was no way to recover it. Other apps let you freeze a streak. Why not this one?" / "I wish it would make coming back easier instead of making me feel like I failed and have to start from scratch." / "Deleted after 3 weeks. The moment I lost my streak the whole thing lost its meaning." / "The streak is the only thing keeping me engaged, but the second I lost it, I was done." |
| 2 | No recovery mechanism, streak-freeze requested by name | 2 | "Other apps let you freeze a streak. Why not this one?" / "I wish it would make coming back easier instead of making me feel like I failed and have to start from scratch." |
| 2 | Notifications feel like nagging or arrive at random | 2 | "After that the daily reminder just started to feel like nagging." / "The notifications feel random. I got three in one afternoon and just turned them all off." |
| 2 | Lesson content itself is well liked | 2 | "The first week was genuinely fun." / "Love the lessons." |

`Note:` rows 2-4 tie at 2 mentions each. Rank 2 (freeze) is the specific, actionable
subset of rank 1 (punishing reset), not a separate cause, listed separately because it
names a concrete fix.

## Single mentions worth flagging (not ranked, but relevant to the actionable list below)

- "The home screen looks the same whether I'm on a 2-day streak or coming back after
  two weeks away. Nothing acknowledges where I am." (no personalization of state)
- "I just forget it exists after a couple of days. If it pulled me back with something
  useful I'd come back." (users want a specific reason to return, not a reminder)

---

## Praise vs. complaints

**Praise (2 comments):**
- "The first week was genuinely fun."
- "Love the lessons."

**Complaints (8 comments):** everything else. The volume is heavily skewed toward
complaints about the reset mechanic and notifications, not the core lesson content.
`Guess:` this suggests the retention problem is about what happens around the habit
loop (streak, notifications), not the daily lesson itself. **What would confirm it:**
session-length or lesson-completion data showing users who churn still finished their
lessons before leaving.

---

## Top 3 actionable issues

1. **No way back in after a break.** Named directly, by feature name (streak freeze),
   in 2 of 10 comments, and it's the mechanism underneath the single largest
   theme (6 mentions).
2. **Notification tone and frequency are working against retention, not for it.**
   2 comments describe nagging or randomness; both describe turning notifications off
   entirely, which cuts off the channel Streakly would need to bring lapsed users back.
3. **The app does not recognize where a user is when they return.** Only 1 comment
   states this directly, but it is the one comment that names the specific gap: no
   acknowledgment of state on the home screen. `Assumption:` grouping this with the
   "pull me back with something useful" comment as the same underlying ask.
   **What would confirm it:** a follow-up NPS or usability prompt asking returning
   users directly whether the home screen felt like it recognized their history.

---

## Findings report for Marcus

**Situation:** 10 unprompted NPS comments were reviewed for recurring themes.

**What we found:** the dominant complaint, by a wide margin, is that breaking a streak
resets everything to zero with no way back, showing up in 6 of 10 comments. Two users
name the fix by feature: a streak freeze, the same feature competitors already offer.
Notification fatigue is the second complaint theme (2 comments), and both of those
users say they turned notifications off entirely. Praise is limited to the lesson
content itself (2 comments), not the retention mechanics.

**What this means:** the two complaint themes point in the same direction as the
interview synthesis (`research/interview-synthesis.md`): users are not leaving because
the lessons are bad, they are leaving because the app punishes a miss and then has no
channel left to win them back once they've turned notifications off.
