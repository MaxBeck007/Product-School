# Capstone Session, Streakly Workspace Review (P7L4)

> **Date:** 2026-09-28
> **Read for this session:** `CLAUDE.md`, `workspace-audit.md`, `agents/`,
> `change_log.md`, `project-skeleton.md`, `docs/{hypothesis,triad-session,design-review,recommendation-memo,decision-brief,pm-brief,spec-readiness,qa-checklist}.md`,
> `data/{metric-findings,experiment-design}.md`, `prototype/README.md`,
> `skills/weekly-status.md`.
> **Not read in full:** `docs/prd.md`, `docs/objection-log.md`,
> `docs/codebase-summary.md`, `docs/presentation*.md`,
> `data/metric-diagnosis.md`, `research/*`, `stakeholders/*`. Confidence
> ratings for those are based on how other files cite them and are marked
> **indirect** below.

---

## 1. What has been built across this project

P1 through P7, all in a single day. The shape of it:

**A decision, with a paper trail.** A Slack thread became a problem statement
(`project-skeleton.md`), then three research sources
(interviews, NPS, competitive), then a decision brief that picked the Comeback
screen over two alternatives (`docs/decision-brief.md`), then a hypothesis
(`docs/hypothesis.md`), then a spec (`docs/prd.md`) that was pressure-tested
before any meeting (`docs/objection-log.md`).

**A thing to look at.** A three-screen click-through prototype
(`prototype/index.html`) that went through two rounds of copy fixes driven by
persona testing, both logged with reasoning (`change_log.md` entries 1-2).

**Numbers with the working shown.** Cohort analysis and metric diagnosis run in
DuckDB (`data/metric-findings.md`, `data/metric-diagnosis.md`), a significance
check and power calculation run in `scipy`/`statsmodels`
(`data/experiment-design.md`), and a one-page memo that leads with the
recommendation (`docs/recommendation-memo.md`).

**Three rehearsed conversations.** Raj on spec readiness, Lena on design, and
the triad session agenda. All three roleplayed, all three labeled as such.

**Automation, new today.** Three one-command workflows (`skills/`) and one
agent spec with a working script (`agents/`).

**The habit that carried all of it:** every artifact names its sources and
labels what is mock. That is the reason this workspace is worth handing to
someone else, and it is the part most likely to erode if a future session gets
sloppy.

---

## 2. Confidence by artifact, and what would get each to 95%

Confidence here means: **how much would I stake on this being right in front of
Marcus, Raj, or Lena.** It is not a quality rating of the writing.

### High confidence (85%+)

| Artifact | Conf. | What is missing for 95% |
| --- | --- | --- |
| `data/experiment-design.md` | 90% | The math was run, not estimated, and cross-checked two ways. Only gap: the weekly eligible-volume figure in Step 4, which the file itself refuses to guess at. Get the real streak-break event count and this goes to 95%. |
| `data/metric-findings.md` | 88% | Queries are shown and reproducible **in principle**. In practice the five source CSVs are not in the workspace, so nobody, including me, can re-run them. Restore them to `data/raw/` and this is 95%. |
| `data/metric-diagnosis.md` (indirect) | 85% | Same reproducibility gap. The 38.9% → 56.5% break-rate figure has already been miscited once (`change_log.md` entry 3), which is a citation-hygiene risk, not a data problem. |
| `prototype/index.html` + README | 85% | High confidence **as a click-through demo**, which is all it claims. Zero confidence as evidence about eligibility rules, and the README says so. |

### Medium confidence (60-80%)

| Artifact | Conf. | What is missing for 95% |
| --- | --- | --- |
| `docs/decision-brief.md` | 75% | The reasoning is sound and the options are real. But findings 1-3 rest on 3 interviews and 10 NPS comments. 95% needs a larger feedback sample, ideally quantified: what share of churned users mention the reset, not 6 of 10. |
| `docs/recommendation-memo.md` | 75% | Recommendation and evidence are clean. Two gaps: the duration ask is still `[TBD]`, and it describes the pilot as something that shipped (see fix F1). |
| `docs/prd.md` (indirect) | 70% | Missing two open questions it should name: the notification-independent trigger, and the reactive-only scope gap. Both are in fix F2. |
| `docs/hypothesis.md` | 70% | Honest and well-structured, and it lists its own assumptions. 95% requires real user behavior, which by definition it does not have. |
| `research/competitive-matrix.md` (indirect) | 70% | Four competitors, desk research, point-in-time. 95% needs hands-on verification in each product and a stated refresh cadence, which `skills/competitive-pulse.md` now provides. |
| `research/interview-synthesis.md`, `research/nps-analysis.md` (indirect) | 65% | The synthesis is faithful to the inputs. The inputs are small (n=3, n=10) and self-selected. 95% needs sample size, full stop. |
| `docs/qa-checklist.md` | 65% | The edge-case list is the strongest part. Rows 6 and 9 are "cannot determine" against a static prototype, so the table is partly a list of things not yet knowable. |
| `docs/design-review.md` | 65% | Fully roleplayed, so it is not evidence of Lena's actual views. But it produced the sharpest strategic point in the workspace (see below), which is why it rates above the other roleplays. |
| `stakeholders/*.md` (indirect) | 60% | Constructed from the scenario doc, not from working with these people. 95% means observing how each actually responds and correcting the profiles. |
| `docs/objection-log.md` (indirect) | 60% | Objections are constructed to match documented patterns, and the file says so. Useful as rehearsal, not as a forecast. |

### Low confidence, use with care (below 60%)

| Artifact | Conf. | What is missing for 95% |
| --- | --- | --- |
| `docs/spec-readiness.md` | 50% | Roleplayed, so the freeze rule (one per lapse, 3+ days, no stacking) is a Claude-generated proposal, not Raj's position. **But it contains the single most valuable correction in the workspace:** that "no new integrations" is not "no new fields." 95% requires one real conversation with Raj. |
| `research/usability-session-1.md` | 40% | Three mock sessions. No real user has seen this prototype. The two prototype fixes made from it are low-risk copy changes, so the downside was contained, but 95% means five real sessions. |
| `docs/codebase-summary.md` (indirect) | 40% | Written against a **reference** codebase, not Streakly's. Its main finding (the pre-break streak length and freeze-spent fields may not exist) was independently reached by `docs/spec-readiness.md`, which is what makes it useful. Transferability to the real codebase is unverified. |
| `research/competitive-reddit.md` | 35% | Self-labeled: no primary threads were reachable, everything is aggregator commentary. 95% needs primary sources, and it may not be gettable. Leave the label on. |
| `agents/monday-retention.md` + script | 35% as output, 80% as design | The script's logic is smoke-tested against synthetic data and it fails loudly with no data. It has never produced a real number. 95% means step 2 of its verification plan passing against the real CSVs. |
| `skills/friday-status.md`, `research-pulse.md`, `competitive-pulse.md` | Unrated | Written today, never run. Confidence is unknown by definition, not low. First run is the test. |

**The pattern worth naming:** everything computational rates high and everything
involving a person rates medium or low. That is the accurate shape of this
project, not a flaw in the work. The data was real; the users and teammates were
not.

---

## 3. The three things worth fixing before handing this to a real collaborator

### F1. The workspace contradicts itself about whether anything shipped

**This is the one that would actually embarrass you.**
`docs/recommendation-memo.md` opens: *"We shipped the Comeback screen as a 50/50
experiment to 100 users in cohort week 5."* Meanwhile `CLAUDE.md`,
`docs/hypothesis.md`, and `prototype/README.md` all say nothing is built beyond a
click-through prototype and no scope is committed.

Both are artifacts of the course structure: P5 handed over a dataset in which the
experiment had already run, while P3 and P4 treated the feature as unbuilt. A
real collaborator reading both in one sitting cannot tell which world they are
in, and the question "wait, did this ship or not?" undermines every number in the
room.

**Fix:** add a short "What is actually real" section to `CLAUDE.md` that states
plainly which artifacts describe a run pilot and which describe an unbuilt
concept. Optionally add a one-line header to `docs/recommendation-memo.md`
scoping its "we shipped" framing to the P5 dataset.

### F2. Two structural gaps are known but not written into the spec

**Correction to this section, made during the fix pass:** I originally wrote
that *both* gaps were missing from `docs/prd.md`. That was wrong. The
notification-independent trigger is already there as Open Question 7, added
when `change_log.md` entry 3 flagged it. I asserted it was missing without
reading `docs/prd.md` in full, exactly the failure the "not read in full"
disclaimer at the top of this file exists to warn about. Only the second gap
was genuinely absent.

1. **The notification-independent trigger.** ~~Missing from the PRD.~~
   **Already present** as `docs/prd.md` Open Question 7, with sourcing to
   `research/nps-analysis.md` theme 3 and `docs/objection-log.md`. No action
   needed. It remains the objection most likely to stall the initiative, but it
   is named where it should be.
2. **The reactive-only scope gap.** `docs/design-review.md` makes the sharpest
   argument anywhere in this workspace: the Comeback screen only reaches users
   who have *already* lapsed, but Day-7 retention measures a population that
   includes users like Amara, anxious from day 4, who have not broken anything.
   A reactive-only fix structurally cannot reach her. This is either a named
   non-goal or a scope expansion, and right now it is neither.

**Fix, applied 2026-09-28:** the reactive-only gap is now `docs/prd.md` Open
Question 8, and is in `CLAUDE.md`'s Known gaps. No PRD change was needed for
the trigger question.

### F3. The change log has holes, and mock material is one hop from looking real

`change_log.md` has entries for P3 and P6 only. Nothing for P4 (spec readiness,
design review, QA) or P5 (the entire data stack). A collaborator, or a future
session, reads that and concludes those lessons never happened.

Related and more consequential: the labels distinguishing roleplay from reality
are currently in each file's header. That works when files are read whole. It
fails the moment someone quotes a line out of `docs/spec-readiness.md` or
`docs/design-review.md` in Slack, at which point a Claude-generated Raj position
becomes, to the reader, Raj's position.

**Fix:** backfill P4 and P5 change log entries, and add a single `ROLEPLAYED`
line at the top of the three fully-constructed files plus a one-line inline tag
on their most quotable claims.

**Ranking:** F1 first (it is a credibility problem, not a completeness problem),
then F2 (it is meeting-ready or it is not), then F3 (hygiene, but it is what
keeps the workspace trustworthy over time).

---

## 4. Reusable workspace prompt for a different product

Paste this into a fresh session in an empty folder for any new product. It
reproduces this workspace's structure and, more importantly, its habits.

````
I'm a product manager starting work on a new product area. Set up a workspace
you can pick up cold in any future session.

First, interview me. One question at a time, and wait for my answer before the
next one. Do not write any files until the interview is done. Ask me about:

- the product, what it does, who uses it
- my role, my squad, who I report to, who I work with day to day
- the core metric I'm accountable for, its current value, and where it should be
- the problem or decision in front of me right now
- what phase I'm in: discovery, delivery, or post-launch
- what constraints I've been given, and what I think they actually mean
- what data, research, or documents already exist that you should read

When the interview is done, create:

1. CLAUDE.md, loaded every session. It must contain: my role and squad, the
   product and core metric, where the work stands right now, a "where to look
   for what" table mapping needs to files, a precedence rule for which document
   wins when two conflict, the constraints, exact definitions of every metric I
   use, the evidence labels below, working habits, and a known-gaps list.
2. This folder structure, empty is fine, with a one-line README in each saying
   what belongs there: research/ docs/ data/ data/raw/ prototype/ skills/
   agents/ stakeholders/ status/
3. open-items.md at the root, the single place open questions live so they
   aren't scattered across five files.
4. change_log.md at the root, with a stated rule that every substantive session
   gets an entry before it ends.
5. stakeholders/_template.md, and a profile for me covering my own defaults.

Then operate under these rules for every future session in this workspace, and
write them into CLAUDE.md:

- Label every claim: Verified (with the file, query, or URL it came from),
  Assumption or Guess (with what would confirm it), or Mock/Roleplayed (no real
  person said this). Never invent a number, quote, date, or file path.
- Prompt me to save any file worth keeping. Don't wait to be asked.
- Ask before building anything substantial while open questions are unresolved.
- Stay in the PM lane: the who, the what, the why. Frame technical content as
  context or open questions, not as direction to the team.
- When I'm wrong, say so, and separate what the evidence says from what you
  conclude from it.

Start with question one.
````

**Why this works from a cold start:** `CLAUDE.md` tells Claude who you are and
what you are building. The saved files tell Claude what you have built. Neither
depends on staying in the same session or the same terminal window. The test of
this workspace is whether it is well documented, not whether you kept the tab
open.

## 5. Letting each user build their own stakeholder folder

`stakeholders/` is the one part of this workspace that cannot be copied between
people. Raj, Lena, and Marcus are Max's stakeholders. Anyone else running this
workspace has different ones, and a profile copied from someone else is worse
than no profile, because it reads as authoritative while being wrong.

**How to make it portable in three parts:**

**1. Ship the template, not the profiles.** `stakeholders/_template.md` defines
the sections every profile needs. Suggested, based on what
`skills/weekly-status.md` actually consumes from them: role and what they own;
what they optimize for; how they prefer to receive information (format, length,
channel, live vs. async); what earns their trust and what loses it; their
standing objections; how to open a hard conversation with them; and a
confidence line stating whether the profile is constructed or observed.

**2. Generate each profile by interview, never by inference.** A prompt for a
new user:

```
Interview me to build a stakeholder profile. One question at a time. Ask about
their role, what they're measured on, how they like information delivered, what
makes them trust or distrust a recommendation, the objection they raise most,
and a time a conversation with them went badly and why.

Then write it to stakeholders/<firstname>.md using stakeholders/_template.md.

Mark every line as Observed (I've seen this happen) or Inferred (my read).
Don't fill a section I couldn't answer, leave it blank and note it as unknown.
```

**3. Keep them out of anything shared.** If this workspace is ever templated,
shared, or committed, `stakeholders/*.md` (except `_template.md`) stays out.
These files contain candid reads on named colleagues. That is exactly what makes
them useful and exactly why they should not travel. **Note:** this folder sits
in OneDrive, so it is already syncing to the cloud. Worth a deliberate decision
rather than a default.

**One thing missing today:** there is no profile for Max. Every profile here
describes how to adapt to someone else, and nothing records your own defaults,
what you want led with, how much hedging you tolerate, when you want to be
asked versus told. A future session, or a teammate covering for you, has to
infer it.

---

## 6. Decision needed

The fixes in section 3 are not implemented. See the question in the chat
response for this session.
