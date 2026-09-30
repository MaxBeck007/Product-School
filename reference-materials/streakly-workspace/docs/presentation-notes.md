# Speaker Notes: Comeback Screen Quarterly Review

> Full sentences, meant to be said out loud. Calibrated to Marcus: lead with
> the number and the ask, don't bury either in the middle of a paragraph.

---

## Slide 1: The Problem

Day-7 retention dropped from 48% to 39% after the v2 streak and notification
redesign shipped, that's the number this whole deck is about. What that drop
actually is matters more than the headline: it's not fewer people signing up,
and it's not our notification channel breaking down, it's that a rising share
of new users break their momentum early and never come back. I want to spend
thirty seconds on that distinction before we go further, because it changes
where we should be spending effort.

## Slide 2: Why Now

The decline didn't start when we noticed it, it was already there in every
cohort before the Comeback screen existed, Day-7 retention fell every single
week from 60% down to 44% across the first four cohorts. What the data adds
that the trend alone doesn't: users who break their momentum in week 1 retain
about half as well thirty days out as users who make it past week 1, and they
churn sixteen points higher. That's the moment we're trying to intervene on,
not a general retention fix, specifically the week-1 break.

## Slide 3: The Proposal

Here's what we're actually proposing: a Comeback screen shown right after a
user breaks a streak, their best-streak stat, a sixty-second lesson to get
momentum back, and a one-tap streak freeze, and we can build this with data
we already have, no new integrations required. I want to be equally clear
about what this isn't, because I don't want to oversell it in the room.
It doesn't touch notification tone or frequency, that's a real issue but a
separate one. It's not monetized, we're intentionally not charging for the
freeze, that's the gap none of our competitors have claimed. And to be
straightforward, this is still discovery, I'm not asking you to approve a
committed build today.

## Slide 4: Evidence

Let me walk through what we actually know, starting with the weakest evidence
and ending with the strongest. We ran a prototype through three mock personas,
and I want to flag clearly that these are illustrative test sessions, not real
users, so treat this as directional signal about tone and mechanics, not proof.
What we did learn from it: the welcome-back tone landed immediately, but trust
in the freeze came from actually tapping it, not from reading about it. Now
the real evidence: in a live fifty-person-per-variant pilot, the Comeback
screen group hit seventy-six percent Day-7 retention against forty-six percent
for control, and that gap held at Day-30 too, thirty-six versus twenty-two.
And this wasn't a one-time novelty spike, open rates on the Comeback send
climbed from twenty-eight to fifty-six percent across four sends while control
stayed flat the whole time. Behind all of this are real user words: six of ten
unprompted NPS comments name the punishing reset directly, and one of our
interview subjects told us in his own words that he left for a competitor
specifically because their freeze felt forgiving and ours offered nothing.

## Slide 5: The Plan

We already have a fully designed, properly powered test ready to run, that's
not a next step we still need to figure out, it's built and sized to detect a
five-point lift with the statistical rigor a fifty-person pilot can't give us.
I want to be upfront about what's still blocking us from committing to a
timeline for that test. We don't yet know how many weekly active users
actually break a streak in a given week, and until we know that number we
can't commit to how long the test will take to run. Separately, Raj still
needs the freeze eligibility and expiry rules defined before engineering can
scope the work. And I'll say this plainly rather than paper over it: we don't
have a sprint kickoff date yet, so I can't give you a rollout date today, and
I'd rather tell you that now than invent one. The cost of not moving is real
though, every week we wait is another week at the same break rate that's
already cost us nine points of retention, and the pilot data shows that gap
compounding, not holding steady.

## Slide 6: The Ask

Here's the actual ask: sign off on running the full powered test before we
commit to scaling this company-wide, and help me get an answer to the one
number blocking that test's timeline, how many users per week actually break
a streak. I want to be direct about what I'm not asking for. I'm not asking
you to approve scaling this today, the pilot result is strong, but fifty
people per variant is not a sample I'd want to bet the whole company's
retention number on, and I don't think you would either.
