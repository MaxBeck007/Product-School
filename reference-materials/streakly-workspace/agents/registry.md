# Streakly PM Agent Registry: The Comeback Coach

> **Built:** P8L4, 2026-09-29. Owner of every agent below: **Max (PM,
> Engagement squad).** None is an engineering ask and none is direction to the
> team.
>
> **Status of the whole stack, stated once so it is not buried:** all three
> agents are **specified and unverified**. The five source CSVs
> (`nudge_users`, `nudge_sessions`, `nudge_retention`, `nudge_nudges`,
> `nudge_weekly_summary_sends`) are absent from this workspace
> (`workspace-audit.md` G4). One script exists and compiles
> (`agents/monday_retention.py`, smoke-tested against synthetic CSVs, one real
> bug found and fixed, `change_log.md` entry 4). **No agent here has ever
> produced a real Streakly number.**

---

## 1. The registry

Three agents: one senses, one diagnoses, one synthesizes. Read this table as
the current state, not the target state.

### Metric Pulse Agent (sense)

| Field | Value |
| --- | --- |
| **Specs** | `agents/monday-retention.md` (primary), `agents/metric-pulse.md` (P8L1 extensions) |
| **Implementation** | `agents/monday_retention.py`, compiles, never run on real data |
| **Trigger** | Manual, Monday morning. Target state: nightly run, Monday 8am delivery |
| **Data sources** | `data/raw/` (five CSVs, **absent**) via DuckDB |
| **Watches** | Day-7 retention (headline), break rate among starters, sessions/user, comeback open rate. Channel splits where computable |
| **Alert threshold** | ±3 percentage points week over week. **Not the course's 2pts**, see `agents/metric-pulse.md` §2 |
| **Escalation flag** | Break rate among starters passing 56.5%, cohort 4's high-water mark |
| **Output format** | Three-slot digest: headline, signal to watch, one thing to look at. Template in `agents/monday-retention.md` §5, channel block in `agents/metric-pulse.md` §6 |
| **Delivery** | Prints to stdout, writes `agents/output/`. **Max pastes to Slack. No auto-post in v1** |
| **Owner** | Max |
| **Gate to production** | `agents/monday-retention.md` §4 steps 1-4, plus the channel-count check in `agents/metric-pulse.md` §7 |

### Anomaly-to-Hypothesis Agent (diagnose)

| Field | Value |
| --- | --- |
| **Spec** | `agents/anomaly-diagnosis.md` |
| **Implementation** | None. Spec only |
| **Trigger** | Event-driven. Fires on pulse-agent alert, **behind a manual YES gate** |
| **Data sources** | Inherits the pulse agent's alert payload. Priors from `data/metric-diagnosis.md` §1 (metric tree) and §4 (H1-H4 with scores) |
| **Loop** | Five steps, three of which can stop the run. Full conditions in `agents/anomaly-diagnosis.md` §3 |
| **Confidence gate** | Top hypothesis must score above 6/10 to issue SQL |
| **Output format** | Three variants: full diagnostic, inconclusive, low confidence (`agents/anomaly-diagnosis.md` §5) |
| **Delivery** | Slack before 9am standup + a row in `outcome-log.md`. **Writes SQL, does not run and interpret it in the same step** |
| **Owner** | Max |
| **Gate to production** | `agents/anomaly-diagnosis.md` §7, six steps, including `DESCRIBE nudge_users` to verify the channel column name |

### Weekly Insight Report (synthesize)

| Field | Value |
| --- | --- |
| **Spec** | `agents/weekly-insight.md` (P8L2), compresses `skills/friday-status.md` (P7L2) |
| **Implementation** | None. Spec only |
| **Trigger** | Friday, after `skills/friday-status.md` has run. **Stops if it has not** |
| **Data sources** | `status/friday-<date>.md` (primary), plus `data/`, `change_log.md`, `research/nps-analysis.md` |
| **Output format** | 3-2-1: three Done, two Changed, one Watch |
| **Delivery** | `reports/<YYYY-MM-DD>.md` + printed Slack text. **No auto-post in v1** |
| **Owner** | Max |
| **Gate to production** | Run by hand three weeks. Specifically: check whether the *Changed* section ever fills (`agents/weekly-insight.md` §7) |

**One rule that applies to all three: none of them posts to Slack
automatically.** Three separate specs reached that conclusion independently for
the same reason. At roughly 50 users per arm these agents will sometimes be
wrong, and an agent that is wrong in a team channel costs more credibility than
the time it saves.

## 2. Connection plan

```
   nightly / Monday 8am                 Friday, after friday-status
           │                                        │
           ▼                                        ▼
  ┌─────────────────┐                     ┌──────────────────────┐
  │  METRIC PULSE   │                     │   WEEKLY INSIGHT     │
  │     (sense)     │                     │    (synthesize)      │
  └────────┬────────┘                     └──────────▲───────────┘
           │ alert payload                           │
           │ (metric, both values, delta,            │ closed diagnoses
           │  week pair, channel splits)             │ from the week
           ▼                                         │
      [ manual YES gate ]                            │
           │                                         │
           ▼                                         │
  ┌─────────────────────┐                            │
  │ ANOMALY DIAGNOSIS   │──── every run, incl. ──────┤
  │     (diagnose)      │     every stop             │
  └─────────┬───────────┘                            │
            │                                        │
            ▼                                        │
      outcome-log.md ───────────────────────────────►┤
            │                                        │
            │ weekly grading pass                    │
            ▼                                        │
   ┌──────────────────┐                              │
   │  LEARNING LOOP   │──► one proposed heuristic ───┘
   │     (§4)         │    update to CLAUDE.md
   └──────────────────┘
```

**Three seams, and what each one passes:**

**Pulse → Anomaly.** The payload contract in `agents/anomaly-diagnosis.md` §2.
The pulse agent decides *whether* something moved; the anomaly agent decides
*why*. That split is why the anomaly agent does not re-query the raw data at
step 1: two agents independently deciding whether a move is real is how they
start disagreeing.

**Anomaly → Weekly Insight.** Any diagnosis closed during the week (a
`what_actually_happened` filled in) becomes a candidate *Changed* bullet. This
is the seam that fixes the real problem named in `agents/weekly-insight.md` §2:
without it, the *Changed* section has no source that updates week to week, and
a weekly report whose middle section is permanently empty gets skipped.

**Anomaly → outcome-log → Learning Loop → CLAUDE.md.** The only seam that
writes back into the workspace's own instructions. It is what makes this a
stack rather than three scripts, and it is also the one most likely to quietly
stop working, because it depends on a human filling in
`what_actually_happened`.

**What is deliberately not connected.** The weekly insight report does not feed
the pulse agent. A synthesis step influencing what the sensing step watches is
how an agent stack talks itself into a narrative and stops noticing anything
that does not fit.

## 3. CLAUDE.md update

`CLAUDE.md` has been updated this session. The additions:

- An **agent stack** section naming all three agents, their triggers, and the
  single fact that matters most about them: none has produced a real number.
- The ±3pt threshold and the 56.5% escalation flag added to **Metric
  definitions**, since they are now decision rules and not just script
  internals.
- `outcome-log.md`, `agents/registry.md`, and the three new specs added to
  **Where to look for what**.
- A **Known gaps** entry for the unverified `channel` column name.

## 4. The learning loop

A weekly self-review. Reads `outcome-log.md`, grades what can be graded, and
proposes exactly one change to how the stack thinks.

**Trigger prompt:**

```
Run the Comeback Coach learning loop: agents/registry.md §4
```

**Steps:**

1. **Read `outcome-log.md`.** Every row, not just the recent ones.
2. **Grade each closed row** (one with `what_actually_happened` filled):
   - **hit** — the top hypothesis was the actual cause.
   - **partial** — the cause was in the top three but not ranked first, or the
     hypothesis was right in mechanism and wrong in magnitude.
   - **miss** — the cause was not in the top three at all.
   - Record the grade and one line on *why*, not just the label.
3. **Grade the stops separately, and count them.** A stop is not a failure. But
   the stop rate is the calibration signal: if most runs stop at step 2 or 3,
   the gates are too tight and the agent is silent when it should be helping.
   If nothing ever stops, they are too loose and it is narrating noise.
4. **Flag rows still blank after three weeks.** These are diagnoses nobody ever
   checked. Report the count. **If it is most of them, stop the loop and say
   so:** the problem is not the agent's calibration, it is that nothing closes
   the feedback cycle, and no amount of heuristic tuning fixes that.
5. **Propose exactly one heuristic update to `CLAUDE.md`.** One, not a list.
   Stated as a specific edit with the evidence from the log that justifies it.
   Examples of the shape it should take:
   - "Three misses all over-ranked channel quality when platform also moved.
     Propose: `CLAUDE.md` gains a note that H1 and H2 are not independent and
     should be scored jointly until the control comparison runs."
   - "Four of five runs stopped at step 2 with exactly one lever moving, and in
     three the single lever was break rate. Propose: lower the step 2 bar to
     one lever when that lever is break rate, since it is the driver
     `data/metric-diagnosis.md` §1 already identified."
6. **Do not apply the update.** Present it for Max's decision. An agent stack
   that edits its own instructions without a human in the loop has no audit
   trail, and `CLAUDE.md` is the file every session inherits.
7. **Log the review itself** to `change_log.md`.

**The honest constraint, stated plainly.** This loop has nothing to grade until
the anomaly agent has run against real data several times. Running it now
returns "0 rows, 0 closed, nothing to learn." That is the correct output, and
it is worth running once for exactly that reason: to confirm the loop reports
an empty log rather than inventing a lesson.

**What would make this loop fail quietly, which is the risk worth naming.** Not
bad grading. An empty `what_actually_happened` column. The field has no owner
(`agents/anomaly-diagnosis.md` §8 question 3), and a stack whose learning input
is an unowned field will look like it is compounding while learning nothing.

## 5. Six-month roadmap: one agent per month

Each month is tied to a **named open gap in `CLAUDE.md`**, not to a capability
that sounds good. Ordered by which gap is currently blocking the most.

| Month | Agent | The gap it closes | Why here in the order |
| --- | --- | --- | --- |
| **1** | **Break-Event Volume Counter** | Weekly eligible-user volume unconfirmed (`data/experiment-design.md` Step 4) | This is the single biggest open input in the workspace. It blocks committing to a duration for the confirmatory test, which *is* the current recommendation. Nothing else on this list matters as much |
| **2** | **Experiment Readout Agent** | No monitoring for the confirmatory test once it starts | Watches the running test against its own power calculation (≈1,568/variant) and refuses to report a result before the sample is reached. Its main job is preventing an early peek from ending the test |
| **3** | **Research Pulse Agent** | `research/nps-analysis.md` is 10 comments from a one-off exercise, with no feed (`agents/weekly-insight.md` §2) | Promotes `skills/research-pulse.md` from a manual workflow to a scheduled one. Gives the weekly report's *Changed* section its user-signal half, which is currently structurally empty |
| **4** | **Stakeholder Prep Agent** | `stakeholders/{raj,lena,marcus}.md` are constructed from the scenario doc and go stale silently | Pre-reads before a triad or Marcus review: what changed since you last spoke, which of their open objections (`docs/objection-log.md`) are still unanswered |
| **5** | **Framing Guard** | The Framing A / Framing B contradiction (`CLAUDE.md`, `docs/capstone-session.md` F1) | Checks any document about to leave the workspace for mixed framings or unlabeled pilot figures. Automates the F1 fix instead of relying on remembering it. The gap that has already cost the most |
| **6** | **Hypothesis Library Maintainer** | `data/metric-diagnosis.md` H1-H4 are frozen at their original scores | Keeps the priors current from graded `outcome-log.md` rows: re-scores, retires ruled-out hypotheses, promotes new ones. Last because it needs five months of graded log to work from |

**Two things this roadmap deliberately does not do.**

It does not add an agent that writes or edits product documents. The PRD, the
one-pager, and the memo are positions Max owns and defends in a room, and an
agent drafting them makes it harder to know what he actually thinks.

It does not automate any Slack posting before month 6. Every spec in this
folder reached the same conclusion for the same reason, and six months of
correct manual runs is the evidence that would justify revisiting it, not a
calendar date.

**And the honest caveat on the whole roadmap:** month 1 assumes the CSVs come
back. If they do not, the roadmap is one item long and that item is "find out
which source becomes the real one" (`agents/monday-retention.md` §7 question 1).
Everything else is downstream of that answer.

## 6. Open questions across the stack

1. **Who owns `what_actually_happened` in `outcome-log.md`?** Unanswered, and
   §4 is inert without it.
2. **Which data source becomes the real one** (product analytics, warehouse, or
   an export)? Decides whether the CSV path survives at all, and gates every
   month of §5.
3. **Is the `channel` column actually named `channel`?** Unverified
   (`agents/anomaly-diagnosis.md` §3 step 4). One `DESCRIBE` settles it.
4. **Channel or DM for all three agents?** Asked separately in each spec. It
   should be answered once, here, for the whole stack. A channel post raises
   the accuracy bar for every agent simultaneously.
5. **Should the 56.5% escalation flag bypass the step 1 threshold gate?** As
   specified, a sub-threshold run that crosses the high-water mark posts
   nothing (`agents/anomaly-diagnosis.md` §8 question 2).
