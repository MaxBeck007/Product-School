# Skill: Friday Status (one-command)

> **Built:** P7L2, 2026-09-28.
> **Relationship to `skills/weekly-status.md`:** that file holds the
> *calibration logic* (how to tune an update for Raj, Lena, and Marcus) and
> requires you to supply a Shipped/In progress/Blocked list by hand. This file
> removes that step: it derives the list from the workspace, then applies the
> other file's calibration rules. Keep both. Edit stakeholder tone in
> `weekly-status.md`, edit the compile step here.

## Trigger prompt

```
Run my Friday status skill: skills/friday-status.md
```

## Steps Claude runs

1. **Read the state of the workspace.** `CLAUDE.md` (current standing, known
   gaps), `change_log.md` (entries added since the last status), `open-items.md`
   if it exists, and the last output of this skill in `status/` to find the
   previous week's baseline.
2. **Derive the three buckets from evidence, not memory.**
   - *Shipped:* new or materially edited files since the last status, plus any
     `change_log.md` entry with an actioned "Change made."
   - *In progress:* artifacts that exist but whose own headers mark them
     incomplete, draft, or untested.
   - *Blocked:* items in `CLAUDE.md`'s Known gaps section plus every
     carry-forward open item in `change_log.md`.
3. **Check what moved.** Diff against the previous week's file in `status/`.
   Anything that was blocked last week and is still blocked gets flagged as
   *unchanged for N weeks*, because an item silently sitting still is the
   failure mode this skill exists to catch.
4. **Apply the calibration rules in `skills/weekly-status.md`** to produce two
   versions, team and leadership.
5. **Stop and list any bucket it could not populate from the workspace.** Do
   not fill a bucket by inference. An empty Shipped section is a real signal.
6. **Prompt to save**, then write the file.

## Output format

````
# Friday Status, week of <date>

## 1. Team update (Raj + Lena)
**Shipped this week**
- 3 bullets max, each naming the artifact or file it landed in

**In progress**
- 3 bullets max, each with what it is waiting on

**Blocked**
- Each blocker stated specifically enough for Raj or Lena to act without a
  follow-up question. Include "unchanged for N weeks" where it applies.

**For Lena specifically**
- Anything user-facing or qualitative, or "nothing new this week."

## 2. Leadership update (Marcus)
**Status:** <on track / at risk / blocked> + the recommendation or headline in
the first sentence, never the last.

<One short paragraph tying the week to Day-7 retention, not to activity.>

**The ask:** <what you need from Marcus, and by when, or "nothing this week.">

## 3. Not derivable from the workspace
- Anything this run could not source. This section is the honesty check, an
  empty one means the workspace is fully current.
````

## Where the output gets saved

`status/friday-<YYYY-MM-DD>.md`. One file per week, never overwritten, so the
week-over-week diff in step 3 keeps working.

## Rules

- Never invent a metric, date, or estimate. "TBD" beats a guess.
- Never carry a claim forward from last week's file without re-checking it
  against the workspace this week.
- Distinguish "shipped" (a real artifact exists) from "discussed" (a position
  exists in a roleplayed or mock session). Most of this workspace is the
  second kind, say so.
- Keep the leadership version to one page.
