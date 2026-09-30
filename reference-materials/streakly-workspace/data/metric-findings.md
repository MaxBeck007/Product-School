# Metric Findings: Comeback Screen Experiment

> **Verified:** run against the 5 uploaded CSVs (`nudge_users`, `nudge_sessions`,
> `nudge_retention`, `nudge_nudges`, `nudge_weekly_summary_sends`), confirmed
> complete: 500 users, 2,347 sessions, 1,740 nudges, 500 retention rows, 400
> weekly summary sends, matching the course's dataset note exactly. Queries run
> with DuckDB against the actual data, not estimated by hand.
> **Naming note:** table/column names are the dataset's originals (a reused
> generic sample set per the course's own dataset note), read as Streakly's
> data. `nudge_users.variant` = `'summary_v1'` (treatment) or `'control'` for
> week-5 users only; all other cohort weeks have `variant = ''` (pre-launch,
> not part of the experiment).

## Q1: Day-7 retention by cohort week, what does the decline look like?

```sql
SELECT cohort_week, COUNT(*) AS n, ROUND(AVG(day_7)*100,1) AS day7_pct
FROM nudge_retention
GROUP BY cohort_week
ORDER BY cohort_week;
```

| cohort_week | n | Day-7 retention |
| --- | --- | --- |
| 1 | 100 | 60.0% |
| 2 | 100 | 53.0% |
| 3 | 100 | 48.0% |
| 4 | 100 | 44.0% |
| 5 | 100 | 61.0% |

**Plain English:** this averages Day-7 retention for every user in each
signup cohort. Weeks 1-4 (pre-launch, before the Comeback screen shipped)
show a steady decline, 60% down to 44%. Week 5 jumps back up to 61%, but
that number blends the treatment and control groups together, it looks like
a recovery here only because half of week 5 saw the new feature. Q3 below
splits it apart.

**What it means for the decision:** the pre-launch decline (weeks 1-4) is the
trend the team is trying to reverse, on its own it shows no sign of leveling
off. Week 5's blended jump is not evidence of anything yet, that's Q3's job.

## Q2: Do users who break their streak in week 1 retain worse than those who don't?

> **Assumption, flagged:** none of the 5 tables has a literal "broke their
> streak" field. I'm using `day_1` and `day_7` as a proxy: a user active on
> day 1 but not on day 7 is treated as having broken their early momentum
> within week 1. Restricted to cohort weeks 1-4 only, to avoid mixing in the
> week-5 experiment. **What would confirm this proxy is right:** a real
> streak-break event log, if one exists elsewhere, would replace this
> approximation.

```sql
SELECT
  CASE WHEN day_1=1 AND day_7=0 THEN 'broke_in_week1'
       WHEN day_1=1 AND day_7=1 THEN 'sustained_week1'
       ELSE 'never_started_day1' END AS group_label,
  COUNT(*) AS n,
  ROUND(AVG(day_30)*100,1) AS day30_pct,
  ROUND(AVG(churned)*100,1) AS churn_pct
FROM nudge_retention
WHERE cohort_week IN (1,2,3,4)
GROUP BY group_label;
```

| Group | n | Day-30 retention | Churn rate |
| --- | --- | --- | --- |
| Sustained past week 1 | 191 | 33.5% | 66.5% |
| Broke in week 1 | 178 | 18.0% | 82.0% |
| Never started (no day-1 activity) | 31 | 25.8% | 74.2% |

**Plain English:** yes. Users who were active on day 1 but gone by day 7
retain roughly half as well by day 30 (18.0%) as users who made it past
week 1 (33.5%), and their churn rate is 16 points higher. This confirms the
premise behind the whole Comeback screen bet: whatever happens in week 1
matters more than almost anything else in the funnel.

**What it means for the decision:** this validates targeting week 1
specifically. It does not, on its own, prove the Comeback screen fixes it,
that's Q3.

## Q3: Week 5 only, Day-7 and Day-30 retention, treatment vs. control

```sql
SELECT u.variant, COUNT(*) AS n,
  ROUND(AVG(r.day_7)*100,1) AS day7_pct,
  ROUND(AVG(r.day_30)*100,1) AS day30_pct
FROM nudge_users u
JOIN nudge_retention r ON u.user_id = r.user_id
WHERE u.cohort_week = 5
GROUP BY u.variant;
```

| Variant | n | Day-7 retention | Day-30 retention |
| --- | --- | --- | --- |
| Control | 50 | 46.0% | 22.0% |
| Treatment (Comeback screen) | 50 | 76.0% | 36.0% |

**Plain English:** the treatment group retained 30 points better at Day-7 and
14 points better at Day-30 than control, in the same week, same signup
cohort. This is the actual causal comparison, not a before/after trend.

**What it means for the decision:** this is the strongest single number in
the whole dataset in favor of scaling. Caveat: n=50 per variant is small,
`docs/decision-brief.md`'s recommendation and the later P5L4 significance
check both depend on whether this holds up statistically, not just
directionally.

## Q4: Did the Comeback screen open rate improve across the 4 sends vs. control?

```sql
SELECT week_number, variant, COUNT(*) AS n, ROUND(AVG(opened)*100,1) AS open_rate_pct
FROM nudge_weekly_summary_sends
GROUP BY week_number, variant
ORDER BY week_number, variant;
```

| Send (week) | Control open rate | Treatment open rate |
| --- | --- | --- |
| 1 | 4.0% | 28.0% |
| 2 | 4.0% | 52.0% |
| 3 | 4.0% | 52.0% |
| 4 | 6.0% | 56.0% |

**Plain English:** treatment open rates climbed from 28% to 56% across the
4 sends, while control stayed flat around 4-6% the whole time. This isn't
just a one-time novelty bump, engagement with the Comeback screen grew as
users saw it more.

**What it means for the decision:** rising engagement over repeated exposure
is a good sign for durability, a one-time spike that fades would be a much
weaker case for scaling.

## Sanity check: average sessions per user, week 5

Also computed as a cross-check against the course's own stated numbers:
treatment averaged **5.28 sessions/user**, control averaged **3.68**, both
match the scenario's stated "5.3 vs 3.7" almost exactly, confirming the
dataset and queries are consistent with the intended story.
