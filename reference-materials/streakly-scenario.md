# The Streakly Scenario · Claude Code for PMs

> **Source:** https://articulateusercontent.com/rise/courses/83J6hQ0DMQJw068O2VFpOVqi3mbw2E_l/VopvNJNpGhL3kr12.html
> **Retrieved:** 2026-09-28
> **Original page title:** The Streakly Scenario · Claude Code for PMs
> Reference doc for the Claude Code for PMs course. Content below is a faithful capture of the page text (HTML converted to Markdown).

Jump to your module: P1 · P2 · P3 · P4 · P5 · P6 · P7 · P8 · Agent Registry · Appendix

---

## The product

Streakly is a consumer habit + micro-learning app that helps people learn a skill in five minutes a day, languages, guitar, coding, chess. Users pick a track, do a short daily lesson, and build a streak. The streak is the product's heartbeat: it is what turns "I downloaded an app" into "I show up every day."

Launched 4 years ago. Series B funded ($42M). 2.1 million registered users. 340,000 monthly active users. Growing at 28% year over year on MAU.

## Your role

You are a PM at Streakly. You own the Engagement squad, everything related to keeping users active in their first weeks: the home screen, the daily lesson loop, streak mechanics, and push notifications.

Your triad: Raj (Senior Engineer), Lena (Product Designer), You.

You report to the Head of Product, Marcus.

## The situation

Streakly's acquisition funnel is working, users install, pick a track, and finish their first lesson. The problem is what happens next. A large share of new users break their streak in the first week, and once a streak is gone, most of them never come back.

Your Day-7 retention rate, the percentage of users still active 7 days after their first lesson, dropped from 48% to 39% over the last two quarters, right after a v2 redesign of the streak and notification system.

Marcus wants to understand why and what to do about it.

## What you are working on

The Comeback experience. The hypothesis: users churn because breaking a streak feels like a punishment, the counter resets to zero and there is no graceful way back in. Once someone misses two days, roughly 80% never return. Streakly has not given lapsed users a reason to come back that feels personal, forgiving, and easy.

You are in discovery. No designs. No committed scope. 8 weeks from sprint kickoff.

---

# Part-by-part reference

Each part below has everything you need for that session's exercises. Work through them in order.

---

# P1, Get Oriented

What you need: your Streakly context for CLAUDE.md and your three core files.

Your project context:

- Role: PM, Engagement squad
- Product: Streakly, consumer habit + micro-learning app
- Current phase: discovery
- Key metric: Day-7 retention rate (39%, down from 48%)
- Key tension: re-engagement nudges vs notification fatigue
- Open decision: how to bring users back after they break a streak

## P1L1, The Slack thread

This is your first exercise. Open Claude Code, paste this Slack thread, and run the prompt on your slide. You will have a PRD skeleton in under 2 minutes.

**#product-growth, Monday 9:14am**

**Marcus:** Hey team, retention numbers are in. Day-7 is at 39%, down from 48% since the streak redesign shipped. We need to figure out what to do. Putting some time on the calendar for Thursday but wanted to start the thread now.

**Raj:** Was looking at the data last night. The drop is sharpest in users who break their streak in week 1. Once someone misses two days in a row, churn is almost double.

**Lena:** That tracks with what I'm hearing in user research. People hit a good streak, miss a day because life happens, come back to a counter that's reset to zero, and it feels like a punishment. There's no way back in.

**Marcus:** So is the problem the streak reset itself? Or is it that our notifications are nagging people right when they're most likely to quit?

**Raj:** Probably both honestly. But I think the bigger issue is what happens after the break. Today the app just acts like nothing happened, same home screen, streak back at 0, no acknowledgment.

**Lena:** Yes. And the "you lost your streak" push has a brutal tone. When people tap through, the app doesn't offer them anything, it just drops them back at day zero. It's jarring.

**You:** So the hypothesis is: users go passive because breaking a streak feels like failure and there's no graceful comeback. We need something that pulls them back with a reason that's specific to them, their progress, not a generic "keep going!"

**Marcus:** I like that framing. What would that look like?

**Lena:** I've been sketching something, a Comeback screen. When you break a streak, instead of a cold reset, you see your best-streak stat, one 60-second comeback lesson to get momentum back, and a one-tap streak-freeze to protect the streak you've rebuilt.

**Raj:** Technically doable with what we have. We'd need the logic for who sees it and the freeze rules, but no new data sources.

**Marcus:** Ok let's explore this. Can someone write up what we're actually trying to solve before Thursday? I want to make sure we're aligned on the problem before we start designing solutions.

**Prompt · paste into Claude Code**

```
Here is a Slack thread from a product discussion at my company. Please organize
this into a PRD skeleton with the following sections: Problem Statement, Goals,
Non-Goals, and Success Metrics. Keep it concise, this is a starting point, not a
finished document. Do not invent details that are not in the thread.

Save the skeleton to project.md.
```

## P1L2, The AI Interview

**Prompt · paste into Claude Code**

```
Before you create any files or write any code, interview me. Ask me one question
at a time until you have 95% confidence you understand what I actually need, not
just what I said I want. When you are confident, summarize what you have learned
and wait for my approval before proceeding.

Here is some information about me to kick things off: The product

Streakly is a consumer habit + micro-learning app that helps people learn a skill
in five minutes a day. Users pick a track, do a short daily lesson, and build a
streak. The streak is the core habit loop.

Launched 4 years ago. Series B funded ($42M). 2.1 million registered users.
340,000 monthly active users. Growing at 28% year over year on MAU.
```

## P1L3, CLAUDE.md

**Prompt · paste into Claude Code**

```
Help me confirm whether you have an understanding of the following:

- My role and squad
- The product and its core metric
- The key tension I am navigating
- The open decision I need to resolve
- Any constraints or context that should load every session

If there are any gaps, inform me and then ask my approval before saving to CLAUDE.md
```

## P1L4, Your Three Core Files

**Prompt · paste into Claude Code**

```
I have three files: project.md, strategy.md, and change_log.md.

Help me populate them for Streakly:

- project.md: what Streakly is, my squad, current phase, key stakeholders
- strategy.md: our hypothesis for recovering the 9-point Day-7 retention drop
- change_log.md: log today as day 1 of the discovery phase

Save each file to the project root.

As we are continuing conversations, I want you to automatically prompt me when we
should be saving any of these files, and also ones we end up creating in the future.
```

## P1L5, Your First Reusable Skill

**Prompt · paste into Claude Code**

```
Help me build a reusable SKILL.md file for weekly status updates.

The skill should:

- Accept raw bullet-point notes as input
- Output a formatted leadership update with: Shipped, In Progress, Blockers, and Next Week
- Keep each section to 3 bullets maximum
- Use plain declarative language, no jargon

Save it as skills/weekly-status.md
```

---

# P2, Know Your Users

## P2L1, Interview excerpts

Paste all three excerpts into a single Claude Code session. Run the prompt on your slide.

Here are interview excerpts from three Streakly users at different stages of their journey, a long-term retained user, a churned user, and a new user still in their first week.

**Priya S., Power user, 14-month streak.** I open Streakly every morning with my coffee. It has become a ritual. The thing that made it stick was hitting a 30-day streak and the app actually celebrating it, that little moment of "look what you built." After that I did not want to lose it. But honestly it took me about three weeks to get there, and I think most people quit long before the habit forms.

**Tom R., Churned user, left after breaking a 12-day streak (5 weeks in).** I really wanted it to work. I got to a 12-day streak and I was proud of it. Then I traveled for work, missed two days, and came back to a big fat zero. The app sent me this "you lost your streak" notification that just made me feel bad. There was no way to recover it, nothing. So I gave up. I switched to Duolingo, at least there a missed day doesn't wipe everything, and a streak freeze feels forgiving.

**Amara L., New user, 4 days in.** I signed up because a friend recommended it. The first few lessons were genuinely fun. But I'm already stressed about the streak, I keep thinking, what happens if I miss a day? I don't want to lose everything I've built after four days. I check it, but the pressure is starting to feel like a chore instead of a game.

Please:

1. Identify the top 5 themes across all three interviews
2. Extract the 2 strongest verbatim quotes per theme
3. Note any contradictions or tensions between what users said
4. Identify the single most important insight for a PM trying to improve week-1 retention

Save to `research/interview-synthesis.md`.

## P2L2, NPS verbatims

**Prompt · paste into Claude Code**

Here is a set of raw NPS feedback from Streakly users.

- I hit a 20-day streak, missed one day, and it reset to zero. I haven't opened the app since. Felt pointless to start over.
- The first week was genuinely fun. After that the daily reminder just started to feel like nagging.
- I want Streakly to feel like a coach that helps me get back on track, not a scorekeeper that punishes me for missing a day.
- The notifications feel random. I got three in one afternoon and just turned them all off.
- Love the lessons. I just forget it exists after a couple of days. If it pulled me back with something useful I'd come back.
- I broke my streak once and there was no way to recover it. Other apps let you freeze a streak. Why not this one?
- The home screen looks the same whether I'm on a 2-day streak or coming back after two weeks away. Nothing acknowledges where I am.
- I wish it would make coming back easier instead of making me feel like I failed and have to start from scratch.
- Deleted after 3 weeks. The moment I lost my streak the whole thing lost its meaning.
- The streak is the only thing keeping me engaged, but the second I lost it, I was done.

Please:

1. Extract all themes mentioned more than once
2. Rank by frequency
3. Separate praise from complaints
4. Identify the top 3 actionable issues
5. Produce a findings report I can share with Marcus

Save to `research/nps-analysis.md`.

## P2L3, Competitive research

Run the prompt on your slide. Claude searches the web and identifies the most relevant competitors itself.

What to look for: how do competitors keep users engaged after the first week? What do their streak, reminder, and comeback (win-back) systems look like?

**Prompt · paste into Claude Code**

```
Streakly is a consumer habit + micro-learning app focused on engagement and
retention in the first weeks. Core loop: pick a track, do a 5-minute daily
lesson, build a streak. Day-7 retention dropped from 48% to 39%, users break
their streak in week 1 and most never come back.

Identify the 3 to 5 most relevant competitors in this space. Focus on
apps built around streaks, daily habits, and micro-learning (start with
Duolingo, Babbel, and Elevate). Do not include apps that are primarily
social media or long-form course platforms.

For each competitor you identify:

- Core features
- Pricing model
- Target customer
- How they keep users engaged after the first week (streaks, freezes, reminders, comeback flows)
- Notable recent changes

Then produce a comparison matrix and identify 2 gaps none of them are
owning well, that is the white space for Streakly.

Save to research/competitive-matrix.md.
```

## P2L3 (Bonus)

```
Using the competitors you just identified, search Reddit for recent posts
and comments about each one. Focus on r/languagelearning, r/duolingo,
r/GetStudying, and any app-specific subreddits you find.

For each competitor, synthesize:

- What users love (recurring praise themes)
- What users complain about most (recurring friction)
- Any mentions of switching away and why
- What users wish the app did that it does not

Then give me:

- A sentiment summary showing where each competitor has the most user friction
- Whether the gaps you identified in the comparison matrix hold up against what real users are actually saying

Save to research/competitive-reddit.md.
```

## P2L4, Decision brief inputs

```
Read the following research files from this workspace:

- research/interview-synthesis.md, what Priya, Tom, and Amara told us
- research/nps-analysis.md, recurring themes from NPS feedback
- research/competitive-matrix.md, structured product research on the top competitors
- research/competitive-reddit.md, what real users are saying about those competitors on Reddit

Synthesize everything into a 1-page decision brief for Marcus, Head of Product:

- Situation (2 sentences)
- Key Findings (max 5 bullets, draw from all four sources, flag where Reddit sentiment confirms or contradicts the structured research)
- Options Considered (2-3)
- Recommended Action (1 sentence)
- Why Now

Save to docs/decision-brief.md.
```

---

# P3, Build and Learn Fast

## P3L1, Prototype brief

```
I want to build a working prototype for the Streakly Comeback screen.

Before you interview me, read what we already know:

- research/interview-synthesis.md, what Priya, Tom, and Amara told us
- research/nps-analysis.md, recurring themes from NPS feedback
- research/competitive-matrix.md, gaps in the competitive landscape
- research/competitive-reddit.md, what real users are saying about competitors on Reddit
- docs/decision-brief.md, the recommendation Marcus approved

Use that context to inform your interview questions. Do not ask me things we
already know from the research.

Here is my PM brief to build on top of that foundation:

User: 24-year-old who hit a 12-day streak, missed two days, and has not opened the app since.
Job to be done: get back in without feeling they lost everything.
Feature: personalized Comeback screen, best-streak stat, one 60-second comeback lesson, one-tap streak-freeze offer.
Constraint: use data Streakly already has, no new integrations.

Before you build anything, interview me. Ask me one question at a time until you
have 95% confidence you understand what I actually need. When confident, show me
the plan and wait for my approval.

Once I approve:

- Save the brief to docs/pm-brief.md
- Build the prototype and save to prototype/index.html
- Save a README to prototype/README.md that includes the PM brief and the key decisions made during the interview
```

## P3L2, Usability testing

```
I just ran usability sessions on my Streakly Comeback screen prototype.

Here are my observations: Questions to ask interviewees

1. What do you think this does?
2. How would you arrive at this experience?
3. Would you come back and restart your streak based on this?
4. If you had a magic wand, what would you change?

Please:

1. Identify what is working
2. Identify the top 2 friction points
3. Suggest the single highest-priority change to make before the next round
4. Update the prototype with that change

Log the change and the reasoning to change_log.md.
```

## P3L2a, Agentic Interview

```
Read prototype/index.html in this project.

Play the role of [Priya / Tom / Amara] using the profile below.

Stay in character throughout. React the way this specific person would, including
confusion, skepticism, or delight. Do not give me PM-style feedback until I ask
for it at the end.

Priya: 28, software engineer, San Francisco. Busy but consistent. Streakly became
a morning ritual; a 14-month streak she is proud of. Motivated by progress and by
not breaking the chain; anxious when she almost misses a day.

Tom: 34, marketing manager, Chicago. Has abandoned three habit apps in two years.
Hit a 12-day streak, missed two days on a work trip, came back to a reset and quit.
Skeptical that any app will make coming back feel worth it. Does not want to be
made to feel guilty.

Amara: 41, operations lead, Atlanta. Four days in, learning Spanish before a trip.
Already anxious about the streak pressure. High bar for trust, if the app feels
punishing or nagging, she will drop it.

Based on what is actually in prototype/index.html, answer these four questions in
character as [Priya / Tom / Amara]:

1. What do you think this does?
2. How would you arrive at this experience?
3. Would you come back and restart your streak based on this?
4. If you had a magic wand, what would you change?

After all four, step out of the persona and give me a synthesis: what this persona
struggled with, what surprised you about their answers, and which of the four
answers would worry you most if a real user said it.

1. Suggest the single highest-priority change to make before the next round
2. Update the prototype with that change

Log any changes and reasoning to change_log.md.
```

## P3L3, Hypothesis

**Prompt · paste into Claude Code**

```
- Read the change-log.md file and the decision-brief.md
- Write a learning synthesis and capture what we know, what we assume, and what we still do not know
- Write a hypothesis statement in this format, "We believe that [feature] will
  deliver [outcome] for Streakly users in their first 7 days, as measured by
  Day-7 retention rate"

Save to docs/hypothesis.md.
```

## P3L4, Triad session

Bring the prototype and hypothesis to a 30-minute session with Raj and Lena. Run the prompt on your slide to prep the agenda and post-session doc.

**Prompt · paste into Claude Code**

```
I have the Streakly Comeback screen prototype, tested across multiple rounds. I am
about to share it with Raj (eng lead) and Lena (designer) in a 30-minute working session.

Help me:

1. Write the session agenda, what to show, what questions to ask, what decisions we need to walk out with
2. Draft the post-session alignment doc template
3. Write the Slack message inviting them to the session

Save the agenda and template to docs/triad-session.md.
```

---

# P4, Work with Your Team

## P4L1, Codebase tour

What to produce: a PM-level tour you can reference when writing tickets for the Comeback screen feature.

**Prompt · paste into Claude Code**

```
Query this GitHub repo directly:

https://github.com/HabitRPG/habitica

I am a PM working on a Comeback screen feature, an in-app experience shown
when a user breaks a streak, offering a best-streak stat, a 60-second comeback
lesson, and a one-tap streak-freeze.

Do three things:

1. Give me a PM-level tour:
   - What this product does in one sentence
   - How the codebase is organized, what each major folder does
   - The 3 most important files I should know about as a PM
   - The key data models and what they tell me about product decisions

2. Map the Comeback screen feature to the codebase:
   - Where would this feature live in the existing structure?
   - What existing components (streaks, tasks, notifications) would it touch or depend on?
   - What is the blast radius, what else could break if this feature ships with a bug?

3. Flag anything that would affect how I write the spec:
   - Any data that does not exist yet that the feature needs (e.g. a streak-freeze field)
   - Any existing constraints I should call out in the ticket
   - The one thing engineers will ask that I should answer before I schedule the kickoff

Save your summary to docs/codebase-summary.md.
```

## P4L1.5 BETA, Build your stakeholder profiles

```
Read docs/decision-brief.md, docs/triad-session.md, research/interview-synthesis.md,
and anything else in docs/ that references Raj, Lena, or Marcus.

Extract everything you already know about each stakeholder from those files. Then
use the default profiles below to fill any gaps. Do not ask me questions, generate
the files now and I will update anything that is not accurate.
```

**DEFAULT PROFILES:**

**RAJ, Engineering Lead**

- Role: owns technical architecture, sprint scope, and feasibility decisions for the Streakly squad
- Pushes back on: underspecified requirements, scope that grows mid-sprint, anything that touches the streak/notification pipeline without a clear rollback plan
- Needs before saying yes: clear acceptance criteria, edge cases called out upfront, an answer to "what does done look like"
- Has asked before that I struggled to answer: "how will we know if this is working after it ships?" and "what happens if the user has never set a streak, or breaks it twice in a week?"
- Communication preference: async first, short messages, bullet points over paragraphs, does not like being surprised in standups
- Open items: still waiting on data model clarification for the streak-freeze field

**LENA, Designer**

- Role: owns the end-to-end user experience, interaction design, and design system consistency for Streakly
- Pushes back on: feature requests that skip the problem definition, copy that reads like it was written by a product manager, anything that adds cognitive load without a clear user benefit
- Needs before saying yes: evidence from real users (not assumptions), a clear definition of the primary user and their context, understanding of what the empty state looks like
- Has asked before that I struggled to answer: "what does the user do after they see the Comeback screen?" and "how do we make a broken streak feel forgiving instead of like a guilt trip?"
- Communication preference: prefers to see things rather than read about them, responds well to "here is what users told us" framing
- Open items: wants to revisit the streak-freeze UI after seeing Amara's feedback

**MARCUS, Head of Product**

- Role: owns product strategy, roadmap prioritization, and the relationship with the exec team and board
- Pushes back on: recommendations without a clear ask, data that does not connect to a business outcome, anything that requires more than one page to explain
- Needs before saying yes: a clear why now, a specific ask with a deadline, confidence that the team has pressure-tested the idea
- Has asked before that I struggled to answer: "what is the cost of waiting another quarter?" and "how does this affect our Day-7 retention number specifically?"
- Communication preference: reads the brief before the meeting, wants the recommendation in the first sentence not the last, follows up async if he needs more detail
- Open items: asked for a rollout timeline before committing to the Q3 sprint

```
Now generate three files with what you know and what the defaults provide. Flag
anything you are inferring versus anything that came directly from the workspace files.

Save to:

- stakeholders/raj.md
- stakeholders/lena.md
- stakeholders/marcus.md

After saving, tell me the one thing about each stakeholder that would most change
how I prepare for the next conversation with them.
```

## P4L2, Spec readiness

**Prompt · paste into Claude Code**

```
Read docs/decision-brief.md, anything in docs/ related to the
Streakly Comeback screen feature, and stakeholders/raj.md.

You are now Raj. Use the stakeholders/raj.md profile to inform how
you show up in this conversation, what you push back on, what you
need before saying yes, how you communicate.

Stay in character as Raj throughout this conversation. Start by telling
me the first thing you would ask after reading this spec. I will respond.
We will go back and forth until you are satisfied the spec is ready,
or until you tell me what it would take to get there.

When we are done, step out of character and give me:

1. A spec readiness summary, what was solid, what needed work
2. A rewrite of the sections we identified as unclear
3. An async Slack message I can send you to confirm scope before sprint kickoff

Save to docs/spec-readiness.md.
```

## P4L3, Design review

**Prompt · paste into Claude Code**

```
Read prototype/index.html, research/interview-synthesis.md,
docs/spec-readiness.md, and stakeholders/lena.md.

I am preparing for a design review with Lena. Use the
stakeholders/lena.md profile to inform how she shows up,
what she pushes back on, what evidence she needs, what she
has asked before that I struggled to answer.

Help me prepare by doing three things:

1. Review the prototype and the user research together:
   - What user needs from the interviews does the current prototype address well?
   - What user needs are not yet addressed?
   - Cite Priya, Tom, or Amara for every point, no opinions

2. Play Lena in a design review. Ask me the 3 hardest questions she
   would ask about this prototype. I will answer each one. Push back
   if my answers are not grounded in evidence.

3. After our exchange, step out of character and give me:
   - A structured one-page design review doc I can share with Lena
   - The single change that would have the highest impact on week-1 retention and why
   - What is a product decision versus what Lena should own

Save to docs/design-review.md.
```

## P4L4, QA and launch

The Streakly Comeback screen is heading into QA. Open the spec. Run the prompt on your slide.

**Prompt · paste into Claude Code**

```
Read docs/spec-readiness.md, prototype/README.md, and prototype/index.html.

The Streakly Comeback screen feature is heading into QA. Do three things:

1. Generate a comprehensive edge case list grouped by category:
   - Empty states (user never held a streak, no best-streak stat, no lessons available in their track)
   - Edge data conditions (streak of 1, broke the streak twice in a week, streak-freeze already used)
   - Timing scenarios (missed one day vs many, time zone boundaries, comeback shown too late)
   - Permission states (notifications off, background refresh off)

2. Simulate running the PM QA checklist against the prototype:
   - Go through prototype/index.html screen by screen
   - For each of the 10 most important things to verify before sign-off, tell me
     whether the prototype passes, fails, or cannot be determined from what is in the file
   - Flag anything that would block launch versus anything that can ship as a known issue

3. Draft my first meaningful PR comment for Raj:
   - Not a rubber stamp, one specific thing I noticed from the PM perspective that
     is worth calling out before merge (e.g. what the streak-freeze does if the user is offline)
   - Frame it as a question, not a demand

Save to docs/qa-checklist.md.
```

---

# P5, Data

The Comeback screen shipped as an experiment in cohort week 5. Users were split 50/50, treatment users who broke a streak saw the Comeback screen, control users got the standard reset experience.

**Dataset note:** the shared sample dataset keeps its original table names (`nudge_users`, `nudge_sessions`, `nudge_retention`, `nudge_nudges`, `nudge_weekly_summary_sends`) and a `summary_v1` variant label. Read them as Streakly's tables and the Comeback-screen experiment, the schema and the columns (including `day_7` and `day_30`) are what your SQL needs. A future refresh will rename the tabs to `streakly_*`.

The story the data tells:

- Weeks 1–4: retention declines steadily across new-user cohorts
- Week 5 treatment: 76% day-7 retention, 36% day-30
- Week 5 control: 46% day-7, 22% day-30
- Comeback screen open rate: 28% (send 1) → 56% (send 4) vs 4% control
- Avg sessions: 5.3 (treatment) vs 3.7 (control) in week 5

Dataset: 500 users · 2,347 sessions · 1,740 nudges · 400 comeback sends.
Google Sheet: https://docs.google.com/spreadsheets/d/1jMZXItXhbYxdBkzM74z2BXbCHHbnvqh4Eyclmmhdiww/edit

## P5L1, Getting Answers from Data Without Writing SQL

Context: Your first task is to query the dataset and surface the retention story. You have five tables. The queries will show the decline weeks 1–4 and the treatment vs control split in week 5. The data answers the question: did the Comeback screen work?

Key join note: `nudge_users.variant` is `summary_v1` (treatment) or `control` for week-5 users. All other cohort weeks have `variant = ''`, those users were pre-launch and were never part of the experiment.

Setup, connect Google Sheets via MCP before running this prompt:

In Claude Code, connect to the Streakly Google Sheet using the Google Sheets MCP. This means Claude reads the data directly, no copying and pasting five tabs of CSV.

Google Sheet: https://docs.google.com/spreadsheets/d/1jMZXItXhbYxdBkzM74z2BXbCHHbnvqh4Eyclmmhdiww/edit

If you do not have the Google Sheets MCP connected, you can still run the prompt by pasting the CSV data from each tab, but connecting the MCP is the better path and the one this course is designed around.

**Prompt to paste**

```
Read the data in this public Google Sheet:

https://docs.google.com/spreadsheets/d/1jMZXItXhbYxdBkzM74z2BXbCHHbnvqh4Eyclmmhdiww/edit

The five tables are:

nudge_users (user_id, acquisition_channel, signup_date, goal_set_date, platform, cohort_week, variant)
nudge_sessions (session_id, user_id, session_date, session_duration_seconds, screen)
nudge_retention (user_id, day_1, day_7, day_30, churned, cohort_week)
nudge_nudges (nudge_id, user_id, nudge_type, sent_date, opened, acted_on)
nudge_weekly_summary_sends (send_id, user_id, send_date, week_number, opened, open_time_seconds, acted_on, variant)

Key join: nudge_users.variant is 'summary_v1' (treatment) or 'control' for week-5
users only. All other cohort weeks have variant = '' and were not part of the experiment.

Answer these 4 questions:

1. Show Day-7 retention by cohort week, what does the decline look like?
2. Do users who break their streak in week 1 retain worse than those who do not?
3. Week 5 only: what is day-7 and day-30 retention for treatment vs control?
4. Did the Comeback screen open rate improve across the 4 sends vs control?

For each: write the SQL, explain it in plain English, and tell me what the result
means for the decision of whether to scale the Comeback screen.

Save your findings to data/metric-findings.md.
```

## P5L2, Diagnosing What Moved a Metric

Now that we have the query results, run a full diagnosis.

```
1. Build a metric tree decomposing Day-7 retention into its component drivers,
   what levers actually move this number? (streak-start rate, streak-break rate,
   comeback rate, notification opt-in)

2. Explain what caused the decline in weeks 1 through 4, be specific, not generic

3. Explain what the week 5 treatment vs control split tells us about what the
   Comeback screen actually fixed

4. Generate 4 ranked hypotheses for why some treatment users still churned. For
   each hypothesis:
   - State it as a testable prediction, not a guess ("Users who churned despite
     seeing the Comeback screen had already broken their streak twice, after a
     second reset the comeback offer lands as noise")
   - Rank it by likelihood based on what the data already shows
   - Give it a confidence score from 1 to 10 based on what the data already
     supports, and one sentence explaining the score
   - Name the one data point that would confirm it
   - Name the one data point that would rule it out

5. Which hypothesis would you act on first if you had to choose one to test in
   the next sprint? Why?

Save your diagnosis to data/metric-diagnosis.md.
```

## P5L3, Writing Recommendations That Get Decisions

```
Read stakeholders/marcus.md.

Now write a results memo for Marcus based on what we found. Use the
stakeholders/marcus.md profile to make sure the format, length, and framing match
what Marcus actually responds to:

- Situation (what we shipped and what we were testing)
- Evidence (3 bullets, the numbers that matter)
- Recommendation (what to do next, one sentence)
- Ask (what you need from Marcus)
- Risk if we wait (one sentence)

Then play a skeptical Marcus and give me the 3 hardest questions he would ask,
starting with whether n=50 per variant is enough to trust this. Use his profile to
make the questions feel like him, not like a generic stakeholder.

Save the memo to docs/recommendation-memo.md.
```

## P5L4, Designing Experiments You Can Actually Run

**Test parameters**

| Parameter | Value |
| --- | --- |
| Pilot result | 76% treatment vs 46% control day-7 retention (n=50 per variant) |
| Observed lift | +30pts at day-7 |
| Control baseline | 46% |
| Minimum detectable effect | 5 percentage points |
| Statistical power | 80% |
| Significance level | 95% |
| Available WAU | 85,000 |
| Max test duration | 8 weeks |

**Prompt:**

```
Before we finalize the recommendation, I need to pressure-test the pilot result
and design the full test.

Do this as a guided walkthrough, explain each concept in plain English before you
calculate anything. Assume I understand the product but not the statistics.

Step 1, Statistical significance of the pilot: Before you calculate, explain in
one sentence what statistical significance means for a PM making a go/no-go
decision. Then check: is the pilot result (76% vs 46%, n=50 per variant)
statistically significant at 95% confidence? Tell me what the answer means in
plain English, not just the p-value.

Step 2, Minimum detectable effect: Before you calculate, explain in one sentence
what MDE means and why a PM sets it before running a test, not after. MDE for this
test: 5 percentage points.

Step 3, Sample size: Before you calculate, explain in one sentence what
statistical power means and what we risk if it is too low. Calculate the required
sample size per variant (power: 80%, significance: 95%, MDE: 5pts, baseline: 46%).

Step 4, Test duration: Available WAU: 85,000. Max test duration: 8 weeks. How long
does the full test need to run? Does it fit within the 8-week constraint?

Step 5, The decision: Based on everything above, give me a plain-English
recommendation: should I wait for the full test or recommend scaling now? What is
the risk of each path in one sentence each?

Step 6, Leading indicators: What 3 metrics should I monitor weekly while the full
test runs so I am not waiting 8 weeks to find out something went wrong? For each,
tell me what movement would make you nervous and why.

After the walkthrough, compile everything into a clean experiment design document.

Save to data/experiment-design.md.
```

Context: The pilot showed a signal. Before Marcus commits to full rollout, you need a significance check on the pilot and a properly powered test design. The answer to the first question may change what you put in the recommendation memo.

---

# P6, Communicate Clearly

## P6L1, A PRD Process That Improves Every Time

Your full research stack is already in the workspace from P2 and P3. Claude can read it directly, no pasting needed. The prompt tells Claude which files to load and what to produce.

**Prompt · paste into Claude Code**

```
Read the following files from the workspace:

- research/interview-synthesis.md, what Priya, Tom, and Amara told us
- research/nps-analysis.md, recurring NPS themes
- research/competitive-matrix.md, structured competitor research
- research/competitive-reddit.md, what real users say about competitors
- docs/hypothesis.md, the hypothesis we are building toward
- docs/decision-brief.md, what Marcus approved
- stakeholders/raj.md, who is reading this spec
- stakeholders/lena.md, who is reading this spec

Using all of this as context, write the PRD for the Streakly Comeback screen
feature. The audience is Raj and Lena, not leadership. Calibrate the
language and level of detail to what each of them actually needs based on
their stakeholder profiles.

Structure:

- Problem Statement
- User (who, job to be done)
- Goals and Non-Goals
- Success Metrics
- User Stories (3-5)
- Open Questions

One page. Plain declarative language. No opinions, ground every point in the
research files.

Save to docs/prd.md.
```

--- After the PRD is completed

> Okay, I like the format of this PRD, I want to upgrade this to a skill.

## P6L2, Pressure-Testing Docs Before the Meeting

Stay in the same session. Claude just wrote the PRD in P6L1, it's in context and saved to `docs/prd.md`. Run the follow-on prompt.

**Prompt · paste into Claude Code**

```
Read stakeholders/raj.md, stakeholders/marcus.md, and docs/prd.md.

Now pressure-test the PRD with three reviewers in sequence. Use the
stakeholder profiles to make Raj and Marcus sound like themselves, not
like generic reviewers.

For each, give me their 2 hardest questions:

1. Raj, use his profile: what would he push back on given what he cares about and what he has asked before?
2. Marcus, use his profile: what would he challenge given his focus on business outcomes and his communication style?
3. Tom, churned Streakly user, broke a 12-day streak, switched to Duolingo: does
   this actually solve why he stopped using the app? (Profile: felt punished by the
   reset, wanted a forgiving way back, found the reset demoralizing)

After all three, tell me which objection is most likely to kill the initiative if
I do not address it upfront.

Save the objection log to docs/objection-log.md.
```

## P6L3, Status Updates in Under Two Minutes

```
Read stakeholders/raj.md, stakeholders/lena.md, and stakeholders/marcus.md.

Here is my week on the Streakly Comeback screen:

Shipped:
- Interview synthesis complete (Priya, Tom, Amara)
- Competitive matrix done, Duolingo, Babbel, Elevate; 2 white space gaps
- Reddit sentiment analysis complete, gaps confirmed by real user friction
- Prototype v1 live and tested across three personas

In progress:
- PRD first draft, 70% done
- Usability session scheduling, 3 of 5 confirmed

Blockers:
- Raj flagged the streak-freeze logic needs a data model change, estimate TBD
- Marcus out Thu–Fri, async review only

Generate two status updates. Use the stakeholder profiles to calibrate the tone,
format, and level of detail for each person:

1. Team update for Raj and Lena, match how they each prefer to receive information based on their profiles
2. Leadership update for Marcus, match his preference for format and what he needs to feel informed without being overwhelmed

Save to skills/weekly-status.md as a reusable template.
```

## P6L4, Presentations That Make an Argument

Marcus wants a planning deck for the Comeback screen before the quarterly review. Six slides. You have 48 hours.

**Prompt · paste into Claude Code**

```
Read the following files from the workspace:

- CLAUDE.md, project context
- docs/decision-brief.md, what Marcus already approved
- docs/recommendation-memo.md, the results memo from P5
- data/metric-findings.md, the retention data and experiment results
- research/interview-synthesis.md, user quotes and themes
- stakeholders/marcus.md, who is in the room

Design the narrative structure for a 6-slide leadership deck for the
quarterly review. Use the recommendation memo and metric findings as the
backbone, do not invent numbers or insights that are not in the files.

Use the Marcus stakeholder profile to make sure the framing, the ask, and
the level of detail match what he actually responds to.

- Slide 1: The problem (1 number, 1 insight)
- Slide 2: Why now (what changed, what we learned)
- Slide 3: The proposal (what it is, what it isn't)
- Slide 4: Evidence (prototype, user quotes, data)
- Slide 5: The plan (timeline, milestones, risks)
- Slide 6: The ask

Then write full speaker notes for every slide, not bullet points, full
sentences you could actually say out loud. Each slide's notes should be 3-5
sentences: what the slide shows, what it means, and what you want Marcus to
take away before you move on.

Save the narrative structure to docs/presentation.md.
Save the speaker notes to docs/presentation-notes.md.
```

---

# P7, Make It Stick

## P7L1, Setting Up a Workspace That Works for You

You have been building the Streakly workspace since P1. This lesson formalizes it, the architecture that makes every future session start with full context. Claude can see your workspace directly, no need to paste the folder structure.

**Prompt · paste into Claude Code**

```
Review my current Streakly project folder. Look at the structure, the files
that exist, and what is in CLAUDE.md.

Then:

1. Tell me what is missing that would make Claude more useful next session
2. Suggest any reorganization that would reduce friction
3. Write a CLAUDE.md update that reflects everything I have built so far

Save the updated CLAUDE.md.
Save the audit summary to workspace-audit.md.
```

## P7L2, Turning Repetitive Work into One-Command Workflows

Three Streakly PM tasks you do every week. One command each.

**Prompt · paste into Claude Code**

```
Here are my 3 most repetitive PM tasks on Streakly:

1. Friday status update, compile what shipped, what's in progress, what's blocked
2. Weekly research synthesis, summarize new user feedback, support tickets, or NPS comments
3. Competitive pulse check, any new moves from Streakly's competitors this week?

For each task, design a one-command workflow:

- The trigger prompt (what I paste to start it)
- The steps Claude runs
- The output format
- Where the output gets saved

I want each to run with a single paste, no additional input from me.

Save each workflow to skills/ (one file per workflow).
```

## P7L3, Building Agents That Work While You Sleep

Your first scheduled agent. Runs Monday morning. No terminal open.

**Prompt · paste into Claude Code**

```
I want to build an agent that runs every Monday morning before my standup.

Task: check Streakly Day-7 retention and streak-break rate against last week's
baseline, compare session counts and push notification open rates, and post a
plain-English digest to Slack.

Format:

- One headline number (Day-7 retention vs last week)
- One signal to watch (biggest mover)
- One suggested action (what I should look at this week)

Help me:

1. Write the agent script
2. Show me how to run it manually first to verify the output
3. Write the Slack message template it posts
```

In the real world this would run via a cron job, n8n, or a Python script on a timer.

For now save the agent spec to `agents/monday-retention.md`.

## P7L4, Putting It All Together (Full Session)

Run a complete Streakly session that works from your saved workspace, proof that your setup carries its own context.

```
Read my CLAUDE.md, my agents/ folder, and my workspace-audit.md.

Based on everything in the workspace, run a review session:

- What have I built so far across this project?
- What is your confidence level in each artifact we developed? What additional
  information would get each one to 95%?
- Based on the gaps above, what are the two or three things worth fixing before I
  hand any of this to a real collaborator?
- If I wanted to recreate this workspace for a different product, what prompt
  would I use? Write it out so I can copy and paste it into a fresh session.
- Information, such as stakeholder profiles, will depend on each user running the
  workspace, so how do we go about letting each user create their own stakeholder folder?

For each fix, suggest the fix and ask if I want you to implement it now.

At the end, update CLAUDE.md to reflect the current state of the project. Save a
session summary to docs/capstone-session.md.
```

Why this works from a fresh session: CLAUDE.md tells Claude who you are and what you are building. Your saved files tell Claude what you have built. This tests whether your workspace is well-documented, not whether you stayed in the same terminal window.

## P7L5, Getting Your Team Started

Write the guide that gets one teammate started in under 15 minutes.

```
Take the reusable workspace prompt you generated in P7L4. I want to use it to
onboard a teammate who has never used Claude Code.

Write me two things:

- A one-page onboarding guide they can read in 5 minutes: what Claude Code is in 2
  sentences with no jargon, what they will build in their first session using the
  prompt you just generated, the 3 habits that matter most (update CLAUDE.md every
  session, use the AI interview before building anything, save everything), and the
  single most common mistake and how to avoid it.

- A 15-minute live demo script I can run with them in the Streakly workspace:
  minutes 0-2 open the Streakly folder, run claude, show CLAUDE.md loading and
  point out what Claude already knows. Minutes 2-7 run the AI interview with the
  Streakly Slack thread from the scenario doc and show plan mode in action.
  Minutes 7-12 run the weekly status skill, then hand them the keyboard and have
  them run it with their own notes. Minutes 12-15 they paste the reusable prompt
  into a new folder for their own product and start their first interview.

The session ends with them running the prompt themselves, not watching me run it.

Save the onboarding guide to docs/onboarding-guide.md.
Save the demo script to docs/onboarding-demo-script.md.
```

---

# P8, Your Agent Stack: The Comeback Coach

In P8 you assemble the Comeback Coach: a connected stack that senses the streak-break spike, diagnoses it, synthesizes the weekly story, and learns from an outcome log.

## P8L1, The Metric Pulse Agent

Your first production agent. Monitors Streakly Day-7 retention and streak-break rate daily. Alerts on signal, not noise.

**Prompt · paste into Claude Code**

```
Build a metric pulse agent for Streakly.

Specification:

- Metrics to monitor: Day-7 retention rate and streak-break rate
- Baseline: 39% Day-7 retention
- Alert threshold: movement of 2 percentage points or more week over week
- Breakdown: split by acquisition channel (organic, paid, referral)
- Output: Monday morning Slack digest
- Schedule: run nightly, deliver Monday 8am

Build me:

1. The agent script
2. The Slack message template (headline metric, channel breakdown, alert if threshold crossed)
3. Instructions for how to run it manually to verify the output
4. A note on how this would be wired in the real world: Python + cron, n8n, or a developer ticket
5. A test run using the Streakly metrics snapshot so I can verify output before scheduling

Save the agent spec to agents/metric-pulse.md.
```

**Sample Slack output format:**

```
📊 Streakly Retention Pulse, Mon May 12

Day-7 retention: 39% (↓ 2pts vs last week) ⚠️ ALERT

By channel:
Organic: 43% (↓ 1pt)
Paid: 34% (↓ 4pts) ← watch this
Referral: 46% (→ flat)

Top signal: Paid channel drop accelerating. Check campaign changes from last week.

Next: run anomaly diagnosis? Reply YES to trigger.
```

## P8L2, The Weekly Insight Report

Every Friday at 4pm. Pulls from three sources. Posts to Slack. Saves a versioned file.

**Prompt · paste into Claude Code**

```
Build a weekly insight report agent for Streakly.

Sources to pull:

1. Retention metrics (from data/ folder)
2. Sprint completions this week (from change_log.md)
3. Top NPS themes this week (from research/nps-analysis.md)

Output format:

- Done this week (3 bullets)
- Changed this week (2 bullets, metrics or user signals that moved)
- Watch next week (1 bullet, the thing most likely to matter)

Delivery:

- Save to reports/YYYY-MM-DD.md
- Post the 3-2-1 summary to Slack

In the real world this runs every Friday at 4pm via cron, n8n, or a scheduled
Python script.

Build me the agent spec and a sample output using Streakly data.
Run it manually first to verify the output structure.

Save the agent spec to agents/weekly-insight.md.
```

**Sample report output:**

```
📋 Streakly Weekly Insight, Fri May 9

Done this week:
• Interview synthesis complete, 5 themes across Priya, Tom, Amara
• Competitive matrix done, Duolingo, Babbel, Elevate; 2 white space gaps
• Prototype v1 live, Comeback screen, streak-freeze logic working

Changed this week:
• Paid channel retention dropped 4pts, now 34%, accelerating decline
• Push notification open rate recovered 1pt to 10% after copy change test

Watch next week:
• Raj's streak-freeze data model change due Wednesday, gates the build

Saved to reports/2026-05-09.md
```

## P8L3, The Anomaly-to-Hypothesis Agent

Chain the pulse agent to an automatic diagnosis. When retention moves, the diagnosis starts before your standup.

This lesson is also where we introduce the concept of loops, one of the most powerful things a PM can build with agents without writing a single line of code.

**What a loop is in plain English:**

A loop is a process that checks its own output before deciding what to do next. Most of the agents we have built so far run once and stop. A loop runs, evaluates a condition, and either continues or stops based on what it finds.

The anomaly-to-hypothesis agent is already a loop, you just have not called it that yet:

- Pulse agent checks retention, is the move above the threshold?
- If yes, anomaly agent fires and decomposes the metric tree
- It generates hypotheses and checks: do I have enough signal to rank them?
- It writes the SQL and posts to Slack, but only if the diagnostic is complete
- It appends the diagnosis and its confidence to `outcome-log.md`, so the Comeback Coach can grade itself later

At each step the agent is checking a condition before moving to the next one. That is the loop. Your job as a PM is to define the conditions, what counts as signal, what counts as complete, where the chain stops and asks for your input. Engineering wires up the retry logic and error handling when they build it for real.

**Prompt · paste into Claude Code**

```
Take the Streakly metric pulse agent and add an anomaly trigger.

When Day-7 retention or streak-break rate moves more than 2 points,
run a diagnostic loop with the following steps and conditions:

Step 1, Threshold check: Is the move above 2 points? If yes, continue. If no, log and stop.

Step 2, Metric tree decomposition: Decompose the move into component drivers.
Condition: only proceed if at least 2 drivers show meaningful movement. If only 1
driver moved, flag as inconclusive and stop.

Step 3, Hypothesis generation: Generate 3 ranked hypotheses with confidence scores.
Condition: only proceed if the top hypothesis has a confidence score above 6/10.
If not, post a "low confidence" alert to Slack and stop.

Step 4, SQL and Slack post: Write the SQL to confirm the top hypothesis. Post the
full diagnostic to Slack before my 9am standup.

Step 5, Log the call: Append the ranked hypotheses, the confidence, and a
placeholder for "what actually happened" to outcome-log.md.

Chain this to the existing pulse agent so it only triggers on alert.

Build me:

1. The updated agent with anomaly trigger and loop logic
2. The conditions at each step, what passes, what stops
3. The Slack diagnostic format (including a "low confidence" variant)
4. A simulated test using a 4-point retention drop so I can verify the loop runs correctly end to end

Save the agent spec to agents/anomaly-diagnosis.md.
```

**Sample diagnostic Slack output:**

```
🔍 Streakly Anomaly Detected, Tue May 13, 8:47am

Trigger: Day-7 retention dropped 4pts (39% → 35%) overnight

Metric tree decomposition:
Streak-break rate: 22% → 29% (↑ 7pts)
Sessions in week 1: 4.1 → 3.2 (↓ 22%)
Push opt-in rate: 54% → 51% (↓ 3pts)

Top 3 hypotheses:
1. Push notification delivery issue (high likelihood, correlates with session drop)
2. New user cohort quality shift from paid channel (medium, paid down 4pts last week)
3. Streak-reset copy regression after last deploy (low, needs confirmation)

SQL to confirm hypothesis 1:

SELECT date, COUNT(*) as push_sent, SUM(delivered) as push_delivered,
AVG(opened) as open_rate FROM streakly_notifications
WHERE sent_date >= CURRENT_DATE - 7 GROUP BY date ORDER BY date;

Logged to outcome-log.md. Run this query and reply with the output. I'll interpret.
```

## P8L4, Connecting the Comeback Coach (and Its Learning Loop)

Three agents. One registry. A learning loop. A system that compounds instead of a stack of scripts.

**Prompt · paste into Claude Code**

```
Here are all the agents I built in this course, together they are the Comeback Coach:

1. Metric Pulse Agent, nightly, monitors Day-7 retention + streak-break rate, posts Monday digest
2. Anomaly-to-Hypothesis Agent, triggered by pulse agent on 2pt move, posts diagnosis, logs to outcome-log.md
3. Weekly Insight Report, Friday 4pm, pulls metrics + sprint + NPS, saves versioned file

Build me:

1. An agent registry document (agents/registry.md) with, for each agent: name,
   trigger, data sources, output format, delivery channel, trigger schedule, owner
2. A connection plan, how the output of the pulse agent feeds the anomaly agent,
   and how the anomaly diagnosis feeds the weekly insight report
3. A CLAUDE.md update that tells Claude about all three agents so every session
   inherits the full agent context
4. The learning loop, a weekly self-review prompt that reads outcome-log.md, scores
   each past diagnosis against what actually happened (hit / miss / partial), and
   proposes one heuristic update to CLAUDE.md
5. A 6-month roadmap: what would a fully connected Streakly PM agent stack look
   like if you added one agent per month?

Save the registry to agents/registry.md.
```

### Agent registry template

**Streakly PM Agent Registry, the Comeback Coach**

Last updated: [date]

**Metric Pulse Agent (sense)**

- Trigger: nightly (cron or n8n in production)
- Data source: data/retention-metrics.md
- Alert threshold: ±2pts week over week
- Output: Slack #pm-streakly
- Schedule: nightly, delivers Monday 8am
- Owner: [your name]

**Anomaly-to-Hypothesis Agent (diagnose)**

- Trigger: fired by Pulse Agent on alert
- Data source: inherits from pulse agent output
- Output: Slack #pm-streakly diagnostic thread + outcome-log.md
- Schedule: event-driven (fires when pulse agent detects anomaly)
- Owner: [your name]

**Weekly Insight Report (synthesize)**

- Trigger: Friday 4pm (cron or n8n in production)
- Data sources: data/, change_log.md, research/nps-analysis.md, outcome-log.md
- Output: reports/YYYY-MM-DD.md + Slack #pm-streakly
- Schedule: weekly Friday 4pm
- Owner: [your name]

---

# APPENDIX: Workspace Catch-Up Prompt

If you completed P1–P4 and have your workspace files, skip this. Jump straight to P5L1.

If your workspace is missing files or you are starting fresh, run this prompt first. It builds the minimum context Claude needs to work effectively through P5–P8.

Run this in a new Claude Code session in your Streakly project folder:

```
I am a Product Manager working on the Streakly Comeback screen, an in-app
experience that wins back users who break their streak on the Streakly habit +
micro-learning app.

Here is everything you need to know to work with me effectively:

PRODUCT CONTEXT

- App: Streakly, habit + micro-learning app; pick a track, do a 5-minute daily lesson, build a streak
- Feature: the Comeback screen, shown when a user breaks a streak. Shows best-streak
  stat, a 60-second comeback lesson, and a one-tap streak-freeze
- Problem: Day-7 retention dropped from 48% to 39% after the v2 streak redesign.
  Users break a streak in week 1 and most never come back
- Hypothesis: a forgiving Comeback experience re-establishes momentum and brings
  users back into an active habit

MY SQUAD

- Raj (Engineering Lead), pragmatic, focused on scope and feasibility
- Lena (Designer), user advocate, pushes back on complexity
- Marcus (Head of Product), strategic, data-driven, needs a clear ask
- Priya, Tom, Amara, interviewed users with different retention outcomes

CURRENT PHASE

- Week 5 experiment complete: Comeback screen shipped to 50% of users who broke a streak
- Treatment: 76% day-7 retention, 36% day-30 (n=50)
- Control: 46% day-7 retention, 22% day-30 (n=50)
- Comeback screen open rate climbed 28% → 56% across 4 sends
- Next: analyze the results, write the recommendation memo, design the full rollout experiment

MY WORKING STYLE

- Always save outputs to the correct file path when I ask you to
- Ask clarifying questions before building anything substantial
- Flag assumptions explicitly, do not invent details
- Keep docs to one page unless I ask for more

Please:

1. Write a CLAUDE.md file that captures all of the above so you load this context
   automatically every session

2. Create a research/ folder with:
   - interview-synthesis.md: a 3-user synthesis for Priya (retained, streak-proud,
     forms the habit), Tom (churned, broke a streak, felt punished), and Amara
     (new, anxious about streak pressure)
   - hypothesis.md: the hypothesis statement for the Comeback screen feature based
     on the retention data above

3. Create a data/ folder (empty, we will populate it in P5)

4. Create a docs/ folder (empty, we will populate it in P6)

Save CLAUDE.md to the project root.
Save all research files to research/.
```

Once Claude confirms the files are saved, open a new session in the same folder, CLAUDE.md will load automatically and you are ready for P5L1.
