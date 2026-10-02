# Open Items

> Closes `workspace-audit.md` gap G2: before this file, open items were
> scattered across at least five places (`change_log.md` carry-forwards,
> `docs/prd.md` Open Questions, `project-skeleton.md` Open Questions,
> `docs/qa-checklist.md` rows, `data/experiment-design.md` Step 4). This is
> the one place to read what's actually open. Updated 2026-10-02. Items
> resolved during this session are kept here, struck through, with the
> entry that closed them, rather than deleted, so this file also shows what
> used to be open.

## Product / scope

- [ ] **Freeze eligibility and expiry rules.** One per lapse, streaks 3+
  days, no stacking, is a discussed position only (`docs/spec-readiness.md`),
  not built or validated. Blocks a real spec. (`docs/prd.md`, Open Q1)
- [ ] **Empty state design.** Undesigned. Scheduled before the next testing
  round, owned by Lena (`docs/triad-session.md`, Post-Session Alignment
  Doc). (`docs/prd.md`, Open Q2)
- [ ] **Success threshold and measurement window.** No target value or
  window has been agreed. (`docs/prd.md`, Open Q4)
- [ ] **Weekly eligible-user volume.** Unconfirmed. The powered test needs
  ~0.46% of 85,000 WAU/week to fit an 8-week window; without this number no
  duration can be committed. (`data/experiment-design.md`, Step 4)
- [ ] **Notification tone and cadence, in scope or parallel workstream?**
  Raised in the original thread, never closed. (`docs/prd.md`, Open Q6)
- [ ] **Discovery trigger.** How a user actually reaches the screen. Now
  has a real cost attached: the reactive screen sizes as an L if this is a
  cheap server-side check, an XL if it needs new push infrastructure.
  (`docs/prd.md`, Open Q7; `docs/effort-tshirt-sizing.md`)
- [ ] **Personalize the lesson to the user's actual pre-lapse track.**
  Logged as its own fast-follow ticket, not started. (`change_log.md`,
  Entry 9)
- [ ] **The proactive/anticipatory piece for not-yet-lapsed anxious users.**
  Scope decision made (expand, not a non-goal), but the piece itself has no
  mechanic, trigger, or metric yet. Confirmed mechanically distinct from the
  freeze, a freeze only exists at the moment of a qualifying lapse.
  (`change_log.md`, Entries 6 and 9; `CLAUDE.md`, Known gaps)
- [ ] **The "no critique" tension on the photo check-in.** Reassuring to
  an anxious, early-lapse user (Amara's segment); reads as pointless to a
  craft-serious user who wants a photo looked at (Dax's finding). A
  segmentation question, not a copy fix. (`change_log.md`, Entry 8)
- [x] ~~Reactive-only reach: non-goal or scope expansion?~~ **Resolved
  2026-09-30:** scope expands. (`change_log.md`, Entry 6)
- [x] ~~Auto-apply versus one-tap freeze.~~ **Resolved 2026-09-30:**
  auto-apply, pre-applied freeze implemented. (`change_log.md`, Entry 10)

## Data / measurement

- [ ] **Channel/platform independence not checked.** H1 (acquisition
  channel) and H2 (platform) in the churn-hypothesis ranking may not be
  independent, whether control shows the same iOS/Android gap has never
  been run. (`data/metric-diagnosis.md`, H2)
- [x] ~~The `channel` and `platform` column names are unverified.~~
  **Resolved 2026-10-02:** the real column is `acquisition_channel`, not
  `channel`; `platform` is named as assumed. Fixed in the three agent specs
  that flagged it. (`change_log.md`, Entry 17)
- [x] ~~Agents have never run on real data.~~ **Resolved 2026-10-02:** ran
  `agents/monday_retention.py` against the real CSVs in `data/raw/` for
  real. Reproduced `data/metric-findings.md` Q3 exactly (76.0%/46.0%, week
  5). Required 3 real schema fixes (boolean casts, the `"comeback"` variant
  label, `send_number` column name). (`change_log.md`, Entry 16)
- [ ] **A real `broke_streak_week1` field exists; its relationship to the
  break-rate proxy is unresolved.** The real CSVs carry a literal field not
  in the course's original schema. Checked against the day1/day7 proxy:
  only 57.3% agreement (262/457 starters), meaning they measure related but
  different things, not two versions of the same signal. Not a validation,
  not a refutation. Whether any analysis should prefer the literal field
  over the proxy now that it exists is undecided. (`change_log.md`, Entry 17)
- [ ] **New, from the same run: weeks 1-4 don't match the real data.**
  `data/metric-findings.md` Q1 and `data/metric-diagnosis.md`'s metric tree
  report cohort-1-4 Day-7 retention and break rate figures that don't match
  the real CSVs now in `data/raw/` (same schema, same row counts, different
  values). Week 5 matches closely in both forms (blended and split by
  variant). Guess: a reseeded sample from a shared course dataset, not
  confirmed. Not actioned, no file rewritten. (`change_log.md`, Entry 16;
  `agents/monday-retention.md`, §4a, full discrepancy table)
- [ ] **`outcome-log.md`'s `what_actually_happened` field has no owner.**
  It's human-written and the only input to the learning loop; unowned, the
  agent stack will look like it's compounding while learning nothing.
  (`agents/registry.md`, §6 question 1)

## Workspace / process

- [ ] **Sprint kickoff date and team size beyond the triad.** Still
  unknown. (`CLAUDE.md`, Known gaps)
- [x] ~~No stakeholder template, no profile for Max.~~ **Resolved
  2026-10-02:** `stakeholders/_template.md` and `stakeholders/max.md`
  added. (`workspace-audit.md`, gap G6)
- [x] ~~No metric glossary.~~ **Resolved, folded into `CLAUDE.md`** rather
  than a separate file, during the same P7L1 pass that found the gap.
  (`workspace-audit.md`, gap G7; `CLAUDE.md`, "Metric definitions, use
  these exactly")
- [x] ~~P1L4's `project.md`/`strategy.md` never built as separate files.~~
  **Deliberately not done**, confirmed by Max on 2026-09-30: the same facts
  already live in `CLAUDE.md`, `docs/decision-brief.md`, and
  `docs/hypothesis.md`; a third and fourth copy would just drift.
  (`workspace-audit.md`, §3; `change_log.md`, header note)

## Deferred, not forgotten

- **R6-R8** (move course-progress recaps to a subfolder, move HTML renders
  to a `renders/` subfolder, add `data/raw/` with a CSV-provenance README):
  explicitly deferred in `workspace-audit.md` as link-risk reorg work, not
  revisited since.
