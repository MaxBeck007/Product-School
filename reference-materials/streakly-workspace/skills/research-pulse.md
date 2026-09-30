# Skill: Weekly Research Synthesis (one-command)

> **Built:** P7L2, 2026-09-28.
> **Honest constraint up front:** Claude cannot reach Streakly's support desk,
> NPS tool, or app store reviews from this workspace. For this to run on a
> single paste, the raw input has to already be sitting in a folder Claude can
> read. That is what `research/inbox/` is for. Drop files there during the
> week; the skill does the rest on Friday.

## Trigger prompt

```
Run my research synthesis skill: skills/research-pulse.md
```

## Setup, once

Create `research/inbox/`. During the week, drop anything raw in there with no
formatting or cleanup: exported tickets, NPS verbatims, review screenshots,
pasted Slack complaints, interview notes. Filename convention
`<source>-<date>.<ext>` (e.g. `nps-2026-10-02.csv`, `tickets-2026-10-02.md`)
so the skill can report provenance per finding.

## Steps Claude runs

1. **Inventory `research/inbox/`.** List every file, its source type, its date,
   and its item count. If the folder is empty, stop and say so, do not
   synthesize from the existing `research/` files and present it as new.
2. **Load the existing baseline** so this week is read as change, not from
   scratch: `research/interview-synthesis.md`, `research/nps-analysis.md`,
   `research/usability-session-1.md`, and the previous run in `research/pulse/`.
3. **Cluster this week's raw items into themes.** Report each theme with a
   count and at least one verbatim quote, attributed to its source file. A
   theme with one mention is reported as one mention, not as a trend.
4. **Classify each theme against the baseline:**
   - **Confirms** an existing finding (name which one, and which file)
   - **Contradicts** an existing finding (this is the highest-value output,
     lead with it)
   - **New**, not previously seen in `research/`
5. **Test each theme against the current bet.** Does it support, weaken, or
   not bear on the Comeback screen direction in `docs/decision-brief.md`? A
   theme that weakens it gets stated plainly, not softened.
6. **Check the open items.** Does anything this week answer a carry-forward
   item in `CLAUDE.md`'s Known gaps, specifically track personalization,
   freeze self-resolution, or the notification-independent trigger?
7. **Prompt to save**, then write the file. Move processed inputs to
   `research/inbox/processed/` so next week's run does not double-count them.

## Output format

````
# Research Pulse, week of <date>

**Input this week:** <n> items across <n> sources. Sources: <file list>.
**Baseline compared against:** <files>.

## Contradicts what we believed
- Theme, count, quote + source file, which existing finding it challenges, and
  what it would take to settle it. Empty section = say "nothing contradicted
  this week."

## Confirms what we believed
- Theme, count, quote + source, the finding it reinforces.

## New signals
- Theme, count, quote + source. Marked **single mention** where n=1.

## Effect on the Comeback screen bet
- Supports / weakens / neutral, in one line each, with the reason.

## Open items this moved
- Which `CLAUDE.md` known gap this week's input speaks to, and how.

## Confidence
- Sample size, source bias (e.g. support tickets over-represent frustrated
  users), and what would raise confidence.
````

## Where the output gets saved

`research/pulse/pulse-<YYYY-MM-DD>.md`. Processed raw inputs move to
`research/inbox/processed/`.

## Rules

- Quote verbatim or do not quote. Never paraphrase into quotation marks.
- Attribute every finding to a source file. Unattributable observations belong
  in a "my read" line, labeled as yours.
- Count honestly. Six of ten NPS comments is a theme; one ticket is an
  anecdote, and gets labeled as one.
- Support tickets and NPS skew negative by construction. State that bias every
  run rather than concluding sentiment has dropped.
- Do not let a new theme quietly rewrite `research/` baseline files. Propose
  the edit, ask first.
