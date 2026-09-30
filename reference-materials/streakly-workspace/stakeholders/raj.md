# Stakeholder Profile: Raj (Engineering Lead)

> **Sourced** = drawn directly from a workspace file, quoted or closely
> paraphrased with a citation. **Default** = filled from the course's given
> default profile because the workspace didn't cover it.

## Role
**Sourced:** Senior Engineer on the Streakly Engagement squad, part of the
triad with Lena and the PM. (`project-skeleton.md`, Participants)
**Default:** owns technical architecture, sprint scope, and feasibility
decisions for the squad.

## What he pushes back on
**Sourced (inferred from behavior, not a direct quote):** in the P1 Slack
thread, Raj's first move was to look at the data before forming an opinion
("Was looking at the data last night"), and his read on causes was
deliberately non-committal until the evidence supported it ("Probably both
honestly"). This suggests he pushes back on conclusions that aren't grounded
in data yet. (`project-skeleton.md`)
**Default:** underspecified requirements, scope that grows mid-sprint, anything
touching the streak/notification pipeline without a clear rollback plan.

## What he needs before saying yes
**Sourced:** he flagged feasibility and open items in the same breath as
agreeing something was "technically doable": "We'd need the logic for who sees
it and the freeze rules, but no new data sources." (`project-skeleton.md`) That's
a real, sourced example of what he needs spelled out before commitment.
**Default:** clear acceptance criteria, edge cases called out upfront, an
answer to "what does done look like."

## Has asked before that the PM struggled to answer
**Default (no workspace source for this specific history):** "how will we know
if this is working after it ships?" and "what happens if the user has never set
a streak, or breaks it twice in a week?"

## Communication preference
**Default:** async first, short messages, bullet points over paragraphs, does
not like being surprised in standups.

## Open items
**Sourced:** the streak-freeze data model and eligibility logic are still
unresolved, this is a running thread from the original Slack conversation
through the P3 prototype work. (`project-skeleton.md`, `change_log.md` Entry 2,
`docs/codebase-summary.md` section 6, which independently found the same gap
in a real reference codebase)

---

**One thing that would most change how the PM prepares for the next
conversation with Raj:** he already surfaces the hard open question himself
(freeze rules, who qualifies) before being asked, so the prep isn't "convince
him it's feasible," it's "come with an actual answer to the question he's
already asked twice."
