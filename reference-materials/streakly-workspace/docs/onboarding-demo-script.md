# 15-Minute Onboarding Demo, Facilitator Script

> **For:** Max, running this live with one teammate.
> **Goal:** they leave having run the workspace prompt themselves on their own
> product. Not having watched you run it.
> **Companion:** `docs/onboarding-guide.md`, send it beforehand, do not read it
> aloud.

---

## Before they arrive, 5 minutes of setup

- [ ] Streakly folder open and ready, `CLAUDE.md` and `docs/` visible.
- [ ] `../streakly-scenario-claude-code-for-pms.md` open to the P1L1 Slack
      thread (lines 65-91) so you can paste it without hunting.
- [ ] An empty folder created for them, named after their product.
- [ ] `docs/onboarding-guide.md` sent to them, with the reusable prompt in it.
- [ ] Ask them to bring one real product problem. If they arrive without one,
      the last three minutes fall flat, so have a fallback: their most recent
      messy Slack thread works fine.
- [ ] Decide which you are demoing, the desktop app or the terminal. The steps
      are the same; only "open the folder" differs (pick the folder in the app
      vs. `cd` into it and run `claude`). Do not explain both, it doubles the
      cognitive load for no gain.

**Timing note:** this is tight. The one section to protect is minutes 12-15.
If you are running over, cut the second half of minutes 7-12, not the ending.

---

## Minutes 0-2, the folder already knows things

**Do:** open the Streakly folder. Start a session. Then ask:

```
What are you working on with me, and what's the most important open question
right now?
```

**They should see:** Claude answer with Streakly, Day-7 retention at 39% down
from 48%, the Comeback screen direction, and the unconfirmed weekly
eligible-user volume. Without being told any of it.

**Say:** "I didn't paste any of that. It read `CLAUDE.md`, which lives in this
folder. Every session I start here begins knowing that much."

**Then open `CLAUDE.md` and point at exactly two things:**

1. The "where to look for what" table. "Fifty files in here. This is how Claude
   finds the right one instead of guessing."
2. The evidence labels section. "This is the part that matters most. Verified,
   Assumption, Mock. Every file in this folder says which it is."

**Do not:** tour the folder. Do not open a second file. You have two minutes.

---

## Minutes 2-7, the interview, and letting Claude push back

**Do:** paste the P1L1 Slack thread, then this:

```
Before you create any files, interview me. Ask me one question at a time until
you have 95% confidence you understand what I actually need, not just what I
said I want. When you're confident, summarize what you've learned and wait for
my approval before proceeding.

Here's a Slack thread from a product discussion at my company. I want to turn
it into a PRD skeleton.
```

**Answer the first two or three questions out loud, in character**, thinking
aloud as you go. Then, deliberately, answer one question vaguely, something like
"we just need retention to go up."

**They should see:** Claude not accept it. It will ask which retention, measured
over what window, against what baseline.

**Say:** "That is the whole value. It refused a vague answer. When I write a
one-line request instead, I get a document built on that vague answer, and I
don't find out until someone asks me a hard question in a review."

**Then show the outcome, not the process.** Open `project-skeleton.md` and
scroll to the `[NOT IN THREAD]` markers.

**Say:** "Four things the thread never settled. No retention target, no date,
no success threshold, notification scope unresolved. It marked the gaps instead
of filling them in with something plausible. Those four gaps became my agenda
for the Thursday meeting."

**If you are demoing in the terminal**, mention plan mode here in one sentence
(Shift+Tab: Claude plans and waits for your approval before touching files) and
move on. If you are in the desktop app, skip it, the interview pattern above is
the same idea and you have already shown it.

**This is the section to cut from if you are over time.** The vague-answer
moment is the part that lands; the `[NOT IN THREAD]` markers are the part to
drop.

---

## Minutes 7-12, a workflow, then their hands on the keyboard

**Do:** run it once yourself:

```
Run my Friday status skill: skills/friday-status.md
```

**Say, while it runs:** "That file is a workflow I wrote once. It reads the
change log and the known-gaps list, works out what shipped and what's blocked,
and writes two versions, one for my engineer and designer, one for my boss. It's
the thing I used to spend forty minutes on every Friday."

**When the output appears, point at one specific thing:** the "Not derivable
from the workspace" section. "That's the honesty check. If it couldn't source
something, it says so instead of writing a nice-sounding sentence."

**Then hand over the keyboard.** This is the pivot point of the whole session.

**Say:** "Your turn. Give it your week, whatever you've got, rough notes, three
bullets, doesn't matter."

```
Here are my rough notes from this week. Turn them into a status update, one
version for my team and one for my manager. Don't invent anything I didn't say,
and tell me what you couldn't source.
```

**They type their own notes.** Sit back. Let them read the output themselves.
Resist narrating it.

**The reaction to listen for:** "wait, that's actually usable." If you get it,
say nothing and move to the last section. If you do not, ask what is off about
it and fix it live in one turn. That recovery is more convincing than a clean
first output.

---

## Minutes 12-15, they start their own

**Do:** open the empty folder you made for their product. Hand them the
keyboard again and do not take it back.

**Say:** "Last three minutes. Paste the prompt from the guide I sent you. It
will interview you about your product. You won't finish here, and that's fine,
the point is it's started, and it'll pick up where you left off next time."

**They paste the reusable prompt from `docs/onboarding-guide.md` and answer the
first question or two.**

**Close with exactly three things, then stop talking:**

1. "Answer the rest of that interview today, while it's fresh. Fifteen minutes."
2. "End every session by asking: what should be saved, and where? Then update
   `CLAUDE.md`."
3. "If it gives you a number, ask which file it came from. If it can't tell
   you, it's a guess."

**Do not** offer to set up their skills, agents, or stakeholder profiles. Those
are session three. Today is one folder and one habit.

---

## Facilitator notes

**If the first output is wrong or thin:** good. Say "watch this," fix it in one
turn, and name what you changed. A visible recovery teaches more than a
rehearsed success, and it is the honest version of what using this is like.

**If they ask "can it do my whole PRD?":** yes, and it will be mediocre if you
ask for it in one line. The quality comes from the interview, and that is worth
saying plainly rather than overselling.

**If they ask about accuracy:** answer directly. It will produce confident wrong
answers. Citing sources is not politeness, it is the control. Point at the
evidence labels in `CLAUDE.md` again.

**If they go quiet:** they are probably thinking about their own product. Let
the silence sit, then ask what they would point it at first.

**The one sentence to land:** it is not a faster way to write documents, it is a
folder that remembers, and the value shows up in week three, not today.
