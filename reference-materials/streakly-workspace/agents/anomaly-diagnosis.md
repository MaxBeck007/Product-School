# Agent Spec: Anomaly-to-Hypothesis Agent (P8L3)

> **New agent.** Chains off the Metric Pulse Agent
> (`agents/monday-retention.md` + `agents/metric-pulse.md`). Fires only on
> alert. Runs a five-step diagnostic loop, stops itself at any step where the
> evidence runs out, and logs every call it makes to `outcome-log.md` so the
> stack can grade its own past diagnoses.
>
> **Built:** P8L3, 2026-09-29.
>
> **Blocking dependency:** the five source CSVs are absent
> (`workspace-audit.md` G4). This agent has never run. Everything below is a
> spec plus a **simulated** walkthrough, clearly labeled in §6.

---

## 1. What a loop is, in one paragraph, because it changes the PM job

Every agent in this workspace so far runs once and stops. A loop runs, checks a
condition against its own output, and then either continues or stops. That is
the whole idea. `agents/monday_retention.py` computes deltas and prints them;
this agent computes a delta, asks "is that enough to keep going," and only then
decomposes it, asks again, and only then generates hypotheses.

**The PM's job in a loop is defining the conditions, not the mechanics.** What
counts as signal, what counts as a complete diagnosis, where the chain stops
and asks a human. Retry logic, error handling, and the actual scheduling are
engineering's, and that split is why this file specifies conditions in plain
language and pseudo-SQL rather than shipping code. The conditions below are the
deliverable.

**A loop that cannot stop is worse than no loop.** Three of the five steps
here exist specifically to halt the chain. An agent that always produces a
confident diagnosis has not been given permission to say "I don't know," and
at n=50 per arm it will need that permission often.

## 2. Trigger and inputs

**Trigger:** the pulse agent emits an alert payload. This agent does not poll
and does not re-decide whether something moved.

**Payload contract** (from `agents/metric-pulse.md` §5):

| Field | Example | Source |
| --- | --- | --- |
| `metric` | `day7_retention_treatment` | pulse agent |
| `value_now`, `value_prev` | numeric | pulse agent |
| `delta_pts` | signed | pulse agent |
| `week`, `compare_week` | integers | pulse agent |
| `channel_splits` | organic / paid / referral, where computable | pulse agent §3 |

**The YES gate stays.** The pulse agent asks; Max replies YES; this runs.
Reason in `agents/metric-pulse.md` §5. Removing the gate is a decision to let
a chain post an unreviewed causal claim to a team channel.

## 3. The loop: five steps and their stop conditions

### Step 1, threshold check

**Condition:** is `abs(delta_pts)` **strictly greater than 3 points**?

**Threshold note, including the boundary.** The P8L3 course prompt says 2
points. This workspace uses 3, for the reason argued in
`agents/metric-pulse.md` §2 and `agents/monday-retention.md` §2: at roughly 50
users per arm, two points is about one user.

The boundary has to match the pulse agent exactly or the two disagree on a
3.0-point move. `agents/monday_retention.py` implements
`if abs(d) <= FLAT_BAND_PTS` with `FLAT_BAND_PTS = 3.0`, so **exactly 3.0
points is "flat" to the pulse agent.** Therefore this step is strictly greater
than 3, not "at or above." A move of exactly 3.0 does not alert, and so never
reaches this agent anyway. Stated here because an off-by-one at the gate is
the kind of thing that only shows up once, in the one week it matters.

If the pulse threshold ever moves to 2, this moves with it, and the boundary
convention moves with it too. They must never differ.

- **Pass:** continue to step 2.
- **Stop:** append a one-line "below threshold, no diagnosis run" entry to
  `outcome-log.md` and exit silently. No Slack post. A sub-threshold move that
  generates a message teaches the channel to mute the agent.

### Step 2, metric tree decomposition

**Decompose the move using the tree that already exists,
`data/metric-diagnosis.md` §1.** Do not invent a new tree per run; a tree that
changes shape between runs cannot be compared across runs.

The four levers, verified as the ones that tree uses:

| Lever | How it is measured | Caveat carried from the source |
| --- | --- | --- |
| Streak-start rate | day-1 activity | Flat and noisy across cohorts 1-5 (90-97%), has never been the driver |
| Break rate among starters | day-1 active, day-7 not | **Proxy, not a real event.** No streak-break field exists (`data/metric-findings.md` Q2) |
| Avg. sessions per user | sessions / users in cohort | Declined 5.74 → 3.69 across cohorts 1-4, moves with retention |
| Nudge open rate | opened / sent | No clean trend cohorts 1-4 (12.1% → 9.4%) |

**"Meaningful movement" defined, so the condition is checkable:** a lever moved
meaningfully if it moved at least 3 points (for rates) or at least 10% of its
own prior value (for session counts), in the direction consistent with the
headline move.

**Condition:** did **at least two** levers move meaningfully?

- **Pass (2+ levers):** continue to step 3.
- **Stop (1 lever):** post the **inconclusive** variant (§5), log it, exit. One
  lever moving alongside a retention change is as consistent with noise as with
  a cause, and a single-driver story is the easiest kind to talk yourself into.
- **Stop (0 levers):** this is the interesting failure. Retention moved and no
  component did. Post the inconclusive variant with the note "headline moved
  without any tree component moving, check the retention query itself before
  looking for a cause." **A decomposition that does not add up is more likely a
  measurement bug than a discovery.** `change_log.md` entry 4 is a live example:
  a NULL-handling bug in `monday_retention.py` silently dropped a figure.

**Escalation flag, independent of the above:** if break rate among starters
passes **56.5%**, cohort 4's high-water mark
(`data/metric-diagnosis.md` §1), flag it explicitly in whatever gets posted.
That trigger is already named in `data/experiment-design.md` Step 6 and
`agents/monday-retention.md` §2.

### Step 3, hypothesis generation

**Start from the hypotheses that already exist, then add.**
`data/metric-diagnosis.md` §4 holds four scored hypotheses. Regenerating from
scratch each run throws away work and produces a new story every week.

| Prior | Claim | Recorded confidence | Current state |
| --- | --- | --- | --- |
| H1 | Acquisition channel quality explains a share of it | **7/10** | Best supported. Organic 43.3% Day-30 (n=30) vs paid 28.6% (n=14) vs referral 16.7% (n=6) |
| H2 | Platform correlates with who the screen helps | **6/10** | iOS 47.8% (n=23) vs Android 27.3% (n=22). Unchecked against control |
| H3 | Users churn because they don't engage the nudge | **2/10** | Largely ruled out, 94.4% vs 96.9% open rates |
| H4 | Repeat lapses aren't helped by one comeback screen | **unscoreable** | No lapse-count field exists |

**Output:** three hypotheses ranked, each with a confidence score out of 10, a
prediction, what would confirm it, and what would rule it out. Reuse a prior
where the new movement is consistent with it; say explicitly when a prior is
being reused versus newly generated.

**Condition:** is the top hypothesis scored **above 6/10**?

- **Pass (7+):** continue to step 4.
- **Stop (6 or below):** post the **low-confidence** variant (§5), log it,
  exit. No SQL, no causal claim.

**Flag worth sitting with, and it is not a detail.** Under this gate, H1 at
7/10 passes by one point and H2 at 6/10 does not pass at all. The workspace's
second-best hypothesis is, by this rule, never actionable. Two readings:

- The gate is calibrated about right, and a 6/10 platform hypothesis with an
  unchecked control comparison genuinely should not drive a Monday morning
  claim.
- Or the gate is too blunt, and the real problem is that H2's score is held
  down by one missing check (does control show the same iOS/Android gap?) that
  would take one query to run.

`Assumption:` I lean to the second reading. **What would settle it:** run the
control-arm platform comparison. If control shows no gap, H2's score should
rise and the gate was right to hold it back until someone checked. That query
is a better use of an hour than tuning the threshold.

### Step 4, SQL and Slack post

Write the SQL that would confirm the top hypothesis, and post the full
diagnostic before the 9am standup.

**The agent writes the query. It does not run it and interpret the result in the
same breath.** Max runs it, or Raj does, and replies with the output. Reason:
the agent's own decomposition is built on a proxy (break rate) and a dataset
that is not currently present. A chain that queries, interprets, and concludes
without a human between steps will eventually publish a confident reading of
its own bug.

**Example confirming query for H1** (channel quality), written against the
schema used in `data/metric-findings.md`:

```sql
-- Day-7 retention by acquisition channel, treatment arm, two weeks side by side
SELECT u.channel,
       u.cohort_week,
       COUNT(*)                        AS n,
       ROUND(AVG(r.day_7) * 100, 1)    AS day7_pct
FROM nudge_users u
JOIN nudge_retention r ON u.user_id = r.user_id
WHERE u.variant = 'summary_v1'
  AND u.cohort_week IN (:week, :compare_week)
GROUP BY u.channel, u.cohort_week
ORDER BY u.channel, u.cohort_week;
```

> `Assumption:` the column is named `u.channel`. The channel values
> (organic / paid / referral) are **verified** present, they are quoted in
> `data/metric-diagnosis.md` H1, but that file reports the figures without
> showing its SQL, so the **exact column name is not recorded anywhere in this
> workspace**. Same caveat for `platform` in an H2 query. **What would confirm
> it:** one `DESCRIBE nudge_users` against the restored CSVs. Do not paste this
> query to Raj as final until that runs.

**Read the n column before the percentage.** §3's channel counts are 30, 14, and
6. Splitting those across two weeks makes them smaller. The query is worth
running; a channel comparison at n=6 is not worth acting on.

### Step 5, log the call

Append to `outcome-log.md`, including every stop, not only the runs that
completed. **The stops are the most valuable rows in the file:** they are the
record of the agent declining to guess, and they are what tells you later
whether the gates are set too tight.

**Row schema:**

| Field | Contents |
| --- | --- |
| `date` | run date |
| `trigger` | metric, both values, delta, week pair |
| `stopped_at` | step number, or `completed` |
| `stop_reason` | which condition failed, in plain language |
| `drivers` | levers that moved meaningfully, with figures |
| `hypotheses` | up to 3, ranked, with confidence scores |
| `top_confidence` | numeric, the gate input |
| `sql_issued` | yes/no, and who it went to |
| `what_actually_happened` | **left blank at write time** |
| `grade` | **left blank.** hit / miss / partial, filled by the learning loop |

The last two fields stay empty until someone knows the answer. The learning
loop in `agents/registry.md` §4 reads this file weekly and grades the closed
rows. A row whose `what_actually_happened` is still blank after three weeks is
itself a finding: the diagnosis was posted and nobody ever checked it.

## 4. The loop, drawn

```
pulse agent alert  ──►  Step 1: |delta| >= 3pts?
                              │ no  ──► log "below threshold", exit silent
                              │ yes
                              ▼
                              Step 1: |delta| > 3pts?
                              │ 1 lever  ──► post INCONCLUSIVE, log, exit
                              │ 0 levers ──► post INCONCLUSIVE + "check the
                              │              retention query itself", log, exit
                              │ 2+
                              ▼
                        Step 3: top hypothesis confidence > 6/10?
                              │ no  ──► post LOW CONFIDENCE, log, exit
                              │ yes
                              ▼
                        Step 4: write SQL, post full diagnostic (pre-standup)
                              │
                              ▼
                        Step 5: append row to outcome-log.md
                                (what_actually_happened + grade left blank)
                              │
                              ▼
                        weekly learning loop grades closed rows
                                (agents/registry.md §4)
```

Three of the five steps can end the run. That ratio is deliberate.

## 5. Slack formats

### 5a. Full diagnostic (passed all gates)

```
🔍 Streakly anomaly, <date> <time>

Trigger: <metric> moved <x>% → <y>% (<±z>pts), week <n> vs week <m>

Metric tree (data/metric-diagnosis.md §1):
Break rate among starters: <a>% → <b>% (<±>pts) <⚠️ past cohort-4 high-water 56.5% if true>
Avg sessions per user: <a> → <b> (<±>%)
Streak-start rate: <a>% → <b>% (<±>pts)
Nudge open rate: <a>% → <b>% (<±>pts)
<levers that did not move meaningfully are listed but marked "flat">

Top 3 hypotheses:
1. <claim> (<n>/10, <new | reused from data/metric-diagnosis.md H#>)
2. <claim> (<n>/10, ...)
3. <claim> (<n>/10, ...)

SQL to confirm #1:
<query>

⚠️ Column names in this query are unverified, see agents/anomaly-diagnosis.md §3 step 4.
Run it and reply with the output. I'll interpret, I won't conclude for you.

Logged to outcome-log.md, row <id>. Arm sizes ~50/variant, treat small moves
as noise.
```

### 5b. Inconclusive (stopped at step 2)

```
🟡 Streakly anomaly, inconclusive, <date>

Trigger: <metric> moved <±z>pts, above threshold.

Only <one | zero> tree lever moved meaningfully: <lever, figures>.
Not enough to decompose. A single-driver story at this sample size is as
consistent with noise as with a cause, so no hypotheses generated.
<if zero levers: "The headline moved and no component did. Check the retention
query before looking for a cause, change_log.md entry 4 is a live precedent.">

Nothing to run. Logged to outcome-log.md, row <id>.
```

### 5c. Low confidence (stopped at step 3)

```
🟠 Streakly anomaly, low confidence, <date>

Trigger: <metric> moved <±z>pts. <n> tree levers moved: <list>.

Best hypothesis scored <n>/10, below the 7/10 bar to act on:
<claim>
What would raise it: <the specific missing check>

No SQL issued and no causal claim made. Logged to outcome-log.md, row <id>.
```

**Note what 5c does.** It names the single missing check that would raise the
score. A low-confidence alert that just says "not sure" wastes the run; one
that says "not sure, and here is the one query that would settle it" is the
most useful message this agent sends.

## 6. Simulated test: a 4-point drop

> **⚠️ SIMULATED. Every number in this section is constructed to exercise the
> loop, not measured.** The five source CSVs are absent
> (`workspace-audit.md` G4) and this agent has never run. The only figures below traceable to real files are the reference
> points named as such: the 56.5% cohort-4 break-rate high-water mark
> (`data/metric-diagnosis.md` §1) and the H1/H2 confidence scores
> (`data/metric-diagnosis.md` §4). **Do not quote anything else here as a
> Streakly figure.**

**Scenario constructed:** week 6 arrives. Treatment Day-7 retention reads 72.0%
against week 5's 76.0%, a 4-point drop.

**Step 1, threshold.** 4 points, at or above 3. **PASS** → step 2.

**Step 2, decomposition.** Constructed lever movements:

| Lever | Week 5 (real) | Week 6 (simulated) | Move | Meaningful? |
| --- | --- | --- | --- | --- |
| Break rate among starters | 40.0% | 47.0% | +7pts | Yes (≥3pts, right direction) |
| Avg sessions per user | 4.48 | 3.90 | −13% | Yes (≥10% of prior) |
| Streak-start rate | 90.0% | 91.0% | +1pt | No, flat |
| Nudge open rate | 10.4% | 9.8% | −0.6pts | No, flat |

Two levers moved meaningfully. **PASS** → step 3.
Break rate at 47.0% is below the 56.5% high-water mark, so no escalation flag.

**Step 3, hypotheses.**

1. **Acquisition channel mix shifted toward paid** (7/10, reused from H1).
   Prediction: the drop concentrates in paid-acquired users, organic roughly
   flat. Confirms it: the step 4 query showing paid down materially and organic
   within noise. Rules it out: the drop spread evenly across channels.
2. **Platform mix or an Android-specific regression** (6/10, reused from H2).
   Still held down by the unrun control comparison.
3. **Sessions fell first and retention followed** (4/10, newly generated).
   The −13% sessions move could be the mechanism rather than a parallel
   symptom. Low confidence because with two weeks of data the ordering cannot
   be established.

Top score 7/10, above the 6/10 bar. **PASS** → step 4.

**Step 4, SQL and post.** Issues the H1 channel query from §3 step 4, with its
unverified-column-name caveat attached, and posts format 5a.

**Step 5, log.** Appends a row: stopped_at `completed`, top_confidence 7,
sql_issued yes, `what_actually_happened` blank, `grade` blank.

### 6b. The same drop, one lever short

**Constructed variant to exercise the step 2 stop.** Same 4-point headline
drop, but break rate moves +7pts and sessions only −4% (below the 10% bar),
with start rate and open rate flat.

Step 1 **PASS**. Step 2: one meaningful lever. **STOP.** Posts format 5b,
logs `stopped_at: 2`, `stop_reason: only one tree lever moved (break rate
+7pts); single-driver story not decomposable at n≈50`. No hypotheses, no SQL.

**This is the run worth checking by hand before trusting the agent.** It is the
only path that looks like a false negative, and the whole question of whether
the gates are calibrated lives in how often it fires.

## 7. Before this runs for real

In order, and none of these are optional:

1. **Restore the CSVs.** Nothing here works without them
   (`workspace-audit.md` G4).
2. **Run `DESCRIBE nudge_users`.** Confirm or correct the `channel` and
   `platform` column names, then fix §3 step 4's query. An agent posting a
   broken query to Raj loses his trust once and does not get it back cheaply.
3. **Pass `agents/monday-retention.md` §4 steps 1-4** for the pulse agent. This
   agent inherits its inputs, so an unverified pulse agent makes this one
   unverifiable by construction.
4. **Replay a known week.** Run the chain against week 5 vs week 4 and confirm
   it refuses the comparison as not like for like, exactly as
   `agents/monday-retention.md` §5's worked example does. If it produces a
   confident diagnosis of a +32pt "improvement," the chain is broken in the
   most dangerous possible direction.
5. **Run the step 2 stop by hand** (the §6b case). Confirm it stops.
6. Only then: run live, with the YES gate, for three weeks before touching the
   thresholds.

## 8. Open questions

1. **Is the 6/10 gate right, or is H2 just one query short?** §3 step 3. The
   control-arm platform comparison decides it and has not been run.
2. **Should the escalation flag (break rate past 56.5%) bypass the gates?** As
   specified it is a note attached to whatever gets posted, so a sub-threshold
   run that crosses the high-water mark currently posts nothing at all. That may
   be wrong. `data/experiment-design.md` Step 6 treats it as an escalation
   trigger, and an escalation trigger that can be silenced by a gate is not
   one.
3. **Who owns `what_actually_happened`?** The field is the entire point of the
   log, and nothing in this spec makes anyone responsible for filling it. If it
   stays blank the learning loop has nothing to grade and the stack stops
   compounding.
4. **Does the break-rate proxy survive contact with a real event log?** Every
   break-rate figure in this workspace is day-1-active / day-7-inactive
   (`data/metric-findings.md` Q2). Step 2 leans on that lever more than any
   other.
