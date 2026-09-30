**`CONSTRUCTED OBJECTIONS, NOT A REAL REVIEW.` No one raised these. They are
generated to match each person's documented pattern. Useful as rehearsal, not
as a forecast, and not quotable as anyone's view.**

# Objection Log: PRD Pressure-Test

> **Method:** `docs/prd.md` pressure-tested against three reviewer profiles in
> sequence. Raj and Marcus are built from their sourced stakeholder profiles
> (`stakeholders/raj.md`, `stakeholders/marcus.md`). Tom is built from his
> interview profile (`research/interview-synthesis.md`) per the exercise brief:
> churned user, broke a 12-day streak, switched to Duolingo, felt punished by
> the reset.
> **Label: the questions below are constructed to match each person's
> documented pattern of pushback, not real quotes from a real review. No
> reviewer actually said these lines.**

---

## 1. Raj (Senior Engineer)

**Pattern he's matched to:** pushes back on conclusions not grounded in data,
and has already surfaced feasibility gaps unprompted rather than waiting to be
asked (`stakeholders/raj.md`).

**Hardest question 1:** "The PRD lists freeze eligibility and expiry as an open
question again. That's the third time this has come up since the original
Slack thread. What's actually blocking an answer, is it a data question, a
design question, or has nobody owned it?"

**Hardest question 2:** "Story 1 says the user sees their pre-break best-streak
value 'on first open after a qualifying break.' What defines qualifying? One
missed day, two, does it reset per attempt? If that's not nailed down, I can't
scope the data model change this needs."

**Why these fit his pattern:** both go directly at the PRD's own Open Questions
section (items 1 and, implicitly, the qualifying-break definition folded into
story 1's acceptance criteria) rather than the parts of the PRD that are
already sourced and settled. That matches his documented behavior of pushing
on ungrounded conclusions and open feasibility items specifically
(`stakeholders/raj.md`, "What he pushes back on").

---

## 2. Marcus (Head of Product)

**Pattern he's matched to:** separates problem from solution, wants a specific
falsifiable cause, moves fast once framing is concrete, wants the ask and the
number up front (`stakeholders/marcus.md`).

**Hardest question 1:** "Success Metrics says no target exists yet. Before I
sign off on anything, what number are we actually trying to hit, and by when?
'Improve Day-7 retention' isn't a decision I can act on."

**Hardest question 2:** "This whole PRD leans on a 50-person pilot. What's the
cost of waiting for the full powered test before we commit engineering time,
versus the cost of shipping now on this sample?"

**Why these fit his pattern:** question 1 mirrors his documented habit of
pushing past a vague framing to a specific, falsifiable one ("I like that
framing. What would that look like?"). Question 2 mirrors his default pattern
of asking about the cost of waiting, and the PRD itself flags the sample-size
caveat, so this is the gap he'd go straight to (`stakeholders/marcus.md`;
`docs/prd.md`, Success Metrics).

---

## 3. Tom (churned user, interview persona)

**Pattern he's matched to:** broke a 12-day streak, got a "you lost your
streak" notification that "just made me feel bad," found no path back, and
switched to Duolingo for its freeze, which he described as forgiving
(`research/interview-synthesis.md`).

**Hardest question 1:** "I already tried something like this feeling, the
freeze idea, somewhere else. What makes this actually different from a badge
that just sits there, versus something that would have made me open the app
again after I missed those two days?"

**Hardest question 2:** "Would I have even seen this? By the time I gave up, I
had already turned off notifications because they made me feel worse. If this
Comeback screen only shows up because of a notification, it doesn't reach me."

**Why these fit his pattern:** question 1 reflects that his actual switch was
driven by Duolingo's freeze already feeling forgiving to him, so a new
Streakly freeze has to clear a bar he's already experienced elsewhere, not a
theoretical one. Question 2 surfaces a gap the PRD does not address: it
specifies the screen's content but not the trigger or channel that gets a
user who has disabled notifications to see it at all, and Tom's own account
ties his churn to disengaging from notifications (`research/interview-synthesis.md`,
theme 3).

---

## Most likely to kill the initiative if not addressed upfront

**Tom's question 2, the discovery/trigger gap.**

Reasoning: Raj's and Marcus's objections are both about rigor, definition, and
sequencing, real risks, but each has a clear owner and a clear path to an
answer (define the eligibility rule; set a target number). Tom's second
question exposes something the PRD does not currently answer at all: how a
user who has already disengaged from notifications, which the NPS data shows
is a real and recurring behavior (2 of 10 comments describe turning
notifications off entirely, `research/nps-analysis.md`), ever sees the
Comeback screen in the first place. If the trigger depends on the same
notification channel users are shown to abandon, the feature could be built,
tested, and still fail to reach the exact segment it exists to win back. This
is not called out anywhere in the current PRD (`docs/prd.md`), including its
Open Questions section, which means it would surface for the first time in
review rather than being anticipated. `Assumption:` this ranks above Raj's and
Marcus's objections specifically because it's undetected by the PRD as
written, not because it's inherently harder to solve. **What would confirm
it:** checking whether the qualifying break event can trigger an in-app
surface (home screen state) independent of push notifications, versus
depending on the push itself.
