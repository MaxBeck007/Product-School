# Agent Spec: Metric Pulse Agent (P8L1)

> **This is an extension spec, not a second agent.** The Metric Pulse Agent
> already exists as `agents/monday-retention.md` plus `agents/monday_retention.py`,
> built in P7L3. This file records only what P8L1 adds on top of it, and one
> place where P8L1's spec conflicts with the existing one.
>
> **Read `agents/monday-retention.md` first.** Anything not contradicted below
> still applies: the three-slot digest, the honesty rule, the four-step manual
> verification, the no-auto-post decision.
>
> **Built:** P8L1, 2026-09-29.
>
> **Blocking dependency, unchanged since P7L3:** the five source CSVs
> (`nudge_users`, `nudge_sessions`, `nudge_retention`, `nudge_nudges`,
> `nudge_weekly_summary_sends`) are cited by `data/metric-findings.md` but are
> **not in this workspace** (`workspace-audit.md` G4). Nothing in this spec has
> ever produced a real number.

---

## 1. Why this is an extension and not a rebuild

P8L1 asks for an agent that monitors Day-7 retention and streak-break rate,
alerts on threshold, breaks down by channel, and delivers a Monday Slack digest.
`agents/monday-retention.md` already does four of those five things.

| P8L1 requirement | Already covered in `monday-retention.md` | Status |
| --- | --- | --- |
| Monitor Day-7 retention | Section 1, headline slot | Covered |
| Monitor streak-break rate | Section 1, signal slot; section 2 high-water mark | Covered |
| Alert threshold on week-over-week movement | Section 2, thresholds | Covered, **different number**, see §2 |
| Baseline 39% Day-7 | `CLAUDE.md` core metric | Covered |
| Slack digest template | Section 5 | Covered |
| Breakdown by acquisition channel | Not present | **New, §3** |
| Nightly run, Monday 8am delivery | Section 6 says run manually | **New, §4** |
| Hand off to anomaly diagnosis | Not present | **New, §5** |

Building a separate `metric-pulse` agent would put two specs with two different
alert thresholds in the same folder. `CLAUDE.md`'s "What is actually real"
section exists because this workspace already made that mistake once with the
shipped-vs-not contradiction. Not repeating it.

## 2. Threshold conflict: 2 points or 3 points

**The conflict.** The P8L1 course prompt specifies "movement of 2 percentage
points or more week over week." `agents/monday-retention.md` section 2 sets
**±3 points** and argues that at roughly 50 users per arm, a two-point move is
noise.

**Decision: keep ±3 points as the alert threshold, and record 2 points as the
threshold to adopt once arm sizes grow.**

**Reasoning.** At n=50 per arm, one percentage point is half a user. A 2-point
threshold would fire on a single user's behavior, and an agent that alerts on
one user teaches you to ignore it. `agents/monday-retention.md` §2 puts it as
"a few percentage points is noise" at these arm sizes; the specific two-point
framing is mine. The course's 2-point figure is written for a product at the
scale `data/experiment-design.md` uses (available WAU 85,000, also
`docs/prd.md` Open Question 5), where 2 points is a real population. That same
file puts the sample needed to detect a 5-point lift at ≈1,568 per variant; at
that size a 2-point threshold becomes defensible.

**The switch condition, so this is not a permanent override:** move to 2 points
when arm sizes exceed roughly 500 per variant. Below that, ±3 points with the
small-sample caveat in the message.

`Assumption:` the 500-per-variant switch point is my judgment, not a computed
figure. **What would confirm it:** a power calculation for the weekly
comparison specifically, rather than for the full test, which
`data/experiment-design.md` does not currently contain.

## 3. New: acquisition channel breakdown

**Feasible, with a real caveat about sample size.**

**Verified that the channel values exist.** `data/metric-diagnosis.md` H1
reports Day-30 retention in the week-5 treatment arm split three ways: organic
43.3% (n=30), paid 28.6% (n=14), referral 16.7% (n=6). So organic / paid /
referral are real values in the data, and H1 is ranked the most data-supported
of the four hypotheses there. **Not verified: the column name.** H1 reports
those figures without showing its SQL, so no query against the channel field is
recorded anywhere in this workspace. See §8 question 2 and
`agents/anomaly-diagnosis.md` §3 step 4.

**The caveat, which belongs in the digest itself.** Those are the whole-arm
counts: 30, 14, and 6 users. A week-over-week channel delta at n=6 is not a
signal, it is a rounding artifact. `data/metric-diagnosis.md` already says the
referral figure "is too small to trust on its own."

**How the digest should handle it:**

- **Organic** (n≈30): report the delta with the standard small-sample caveat.
- **Paid** (n≈14): report the raw figure, suppress the delta, label it
  "directional only."
- **Referral** (n≈6): report the count, not a rate. A percentage on six users
  invites over-reading.
- **Never rank the three channels against each other in the digest.** H1's own
  "rules it out" clause in `data/metric-diagnosis.md` says the channel gap may
  disappear once platform is controlled for, because channel and platform could
  be correlated in this data and that was never checked. A ranked channel list
  in a Monday message implies a causal read the data does not support.

**Open question this raises, and it is the useful one:**
`data/metric-diagnosis.md` §5 names H1 (acquisition channel quality) as the
hypothesis to act on first. If that is right, channel is not a digest
breakdown, it is a segmentation question for the test design itself: should the
confirmatory test stratify by channel, or is channel a confound to control for?
That is a question for Raj and Marcus, not something this agent answers.

**The query is specified but has never been run.** Day-7 by channel does not
exist anywhere in the workspace; `data/metric-diagnosis.md` H1 computed Day-30.
The pulse agent needs the Day-7 version, and it cannot be produced until the
CSVs return.

## 4. New: nightly run, Monday 8am delivery

`agents/monday-retention.md` section 6 says run it manually, Monday morning,
and explicitly defers automation. P8L1 asks for nightly execution with a Monday
8am delivery.

**Decision: keep manual for now, and treat nightly-plus-Monday-8am as the
target state gated on `monday-retention.md` section 4 step 2 passing.**

Step 2 is "reproduce a known result against the real CSVs." It cannot pass
while the CSVs are absent. Scheduling a job that has never produced a verified
number is how a wrong figure ends up in a channel on a Monday morning.

**What "nightly" would actually buy you, and it is not what it sounds like.**
The data in this workspace is cohort-weekly, not daily. A nightly run against
weekly cohorts recomputes the same numbers six times before anything changes.
The honest version of "nightly" here is: run nightly so that *when* the week
rolls over the digest is ready at 8am Monday without anyone remembering to run
it, not because there is new signal every night.

**Real-world wiring, as context rather than direction.** Three options, in
increasing order of what they ask of engineering:

| Option | What it is | Cost to the team |
| --- | --- | --- |
| Windows Task Scheduler or cron on your own machine | A timer runs `monday_retention.py --week N --compare-week N-1 --save` | None. Breaks when your laptop is off |
| n8n or a hosted scheduler | Same script, runs off your machine, can post to Slack | Small. Needs someone to hold the credentials |
| A ticket to Raj | A real scheduled job against the warehouse, not CSVs | Real sprint cost, and needs the §7 source question answered first |

**Stay in lane:** which of these three is right is Raj's call, not mine. What I
owe him is the answer to "which source becomes the real one"
(`agents/monday-retention.md` §7 question 1), because the answer decides which
option is even possible.

## 5. New: the handoff to anomaly diagnosis

P8L1's sample output ends with "Next: run anomaly diagnosis? Reply YES to
trigger." That is the seam between this agent and `agents/anomaly-diagnosis.md`
(P8L3).

**The contract between the two agents:**

- The pulse agent decides **whether** something moved past threshold. It does
  not diagnose.
- On alert, it emits a trigger payload: the metric that moved, the two values,
  the delta, the week pair, and the channel splits it was able to compute.
- The anomaly agent consumes that payload as its Step 1 input. It does not
  re-query the raw data to decide whether to run.
- **The YES gate stays in v1.** The pulse agent asks; Max replies YES; the
  anomaly agent runs. Reason: same as the no-auto-post decision in
  `monday-retention.md` §6. A chain that fires automatically at n=50 will
  sometimes produce a confident diagnosis of noise, and it will do it in public.

Full loop logic lives in `agents/anomaly-diagnosis.md`.

## 6. Slack template addition

The base template is `agents/monday-retention.md` §5. This adds one block,
inserted after the headline and before *Watching*:

```
*By channel (treatment arm):*
Organic: <x>% (<±y>pts, n=<n>)
Paid: <x>% (n=<n>, directional only, delta suppressed)
Referral: <n> of <n> retained (too few for a rate)
<one line, or "Channel splits not comparable week over week at these counts.">
```

And one block at the end, replacing the footer's last line when an alert fired:

```
⚠️ <metric> moved <±z>pts, past the 3pt threshold.
Run the anomaly diagnosis? Reply YES.
```

**What the template deliberately does not do:** it does not order the channels
best-to-worst, and it does not print a referral percentage. Both are §3
decisions, and both are the kind of thing a template quietly undoes if it is
not written down.

## 7. Test run before scheduling anything

P8L1 asks for a test run against the Streakly snapshot. Here is what can and
cannot be produced today.

**Can be produced.** The headline comparison, from
`data/metric-findings.md` Q3. **Verified** figures, week 5, **pilot-arm**
(not cohort-level, which is 61.0% blended in Q1, and `CLAUDE.md` Metric
definitions forbids mixing the two): treatment Day-7 76.0% (n=50), control
46.0% (n=50).

**Cannot be produced.** Day-7 by channel, week over week. The channel field
exists (`data/metric-diagnosis.md` H1) but only Day-30 has been computed from
it, and the CSVs needed to compute the Day-7 version are absent.

**Illustrative digest, built only from figures that exist in this workspace.
Not a live run. Channel rows are shown as unfilled on purpose:**

```
*Streakly retention, Monday 2026-10-05*

*Day-7 retention (treatment, pilot-arm):* 76.0% vs 46.0% control, same week, same cohort
Week 5 only. Reported against control rather than against last week, because
week 4 is a pre-launch cohort with no treatment arm and is not like for like.

*By channel (treatment arm):*
Organic: not computed (Day-7 by channel has never been run; n≈30)
Paid: not computed (n≈14, directional only if it is)
Referral: not computed (n≈6, too few for a rate)
Channel splits not comparable week over week at these counts.

*Watching:* comeback open rate in the treatment arm, 28% → 56% across four
sends, while control stayed at 4-6% (data/metric-findings.md Q4).
Rising engagement over repeated exposure is the durability signal.

*Worth a look this week:* the weekly count of streak-break events. Still the
missing input blocking any committed test duration
(data/experiment-design.md Step 4).

_No alert fired: no like-for-like week-over-week comparison exists yet._

_Illustrative, assembled from data/metric-findings.md · not a live run · source
CSVs absent (workspace-audit.md G4) · arm sizes ~50/variant_
```

**Note what this example refuses to do.** It does not fill the channel rows
with plausible numbers, and it does not print the flattering +32pt week-4
comparison that `agents/monday-retention.md` §5 already rejected. A digest that
would rather show a blank than a guess is the behavior being specified here.

**Do not schedule until:** `agents/monday-retention.md` §4 steps 1-4 all pass
against real CSVs, plus a fifth step added by this spec, run the channel query
and confirm the counts are what §3 assumes (roughly 30 / 14 / 6). If they are
materially different, §3's per-channel rules need redoing.

## 8. Open questions

Carried from `agents/monday-retention.md` §7 and still open: which source
becomes the real one, whether a genuine streak-break event log exists, channel
vs. DM. Added by this lesson:

1. **Is channel a digest breakdown or a test-design decision?**
   `data/metric-diagnosis.md` §5 ranks H1 (channel quality) as the hypothesis
   to act on first. If channel really drives outcomes, the confirmatory test
   probably needs to account for it, which is a bigger question than a Monday
   digest row. For Raj and Marcus.
2. **Are channel and platform correlated in this data?** H1's "rules it out"
   clause flags the possibility and says it has not been checked. Until it is,
   every channel number in the digest could be a platform effect wearing a
   channel label. **Note this is a different unrun check from H2's**, which is
   whether the *control* arm shows the same iOS/Android gap. Two separate
   queries, and neither answers the other.
   **Resolved 2026-10-02:** ran `DESCRIBE nudge_users` against the real,
   restored CSVs. The column is `acquisition_channel`, not `channel`, and
   `platform` is named as assumed. Queries elsewhere in this stack that say
   `u.channel` need `u.acquisition_channel` substituted before they run.
   (`change_log.md` Entry 17)
3. **At what arm size does the 3pt threshold become 2pt?** §2 proposes ~500 per
   variant as a judgment call. A weekly-comparison power calculation would
   replace the guess with a number.
