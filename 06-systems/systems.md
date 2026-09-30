# Module 6 · Systematize — Build Your Systems & Agent Stack

> How do I make this stick, and run while I sleep?

Build a durable workspace and skills worth keeping, then layer on an autonomous agent stack — metric pulse, weekly insight, anomaly-to-hypothesis — wired into one connected system. Finalize the capstone repo.

## Workspace + Three Skills

*What's worth keeping, and the skills that make it durable.*

A P7 workspace audit (41 files) rewrote `CLAUDE.md` with a file map, a document-precedence rule, exact metric definitions, and evidence labels (Verified / Assumption-Guess / Mock-illustrative), so a fresh session inherits context instead of building blind.

1. **`skills/friday-status.md`** — one-command Friday status. Derives Shipped/In-progress/Blocked from real workspace evidence (new files, `change_log.md` entries, `CLAUDE.md` Known gaps) rather than memory, applies the tone rules from `skills/weekly-status.md`, and explicitly lists anything it couldn't source.
2. **`skills/research-pulse.md`** — weekly research synthesis from a `research/inbox/` drop folder. Classifies each new theme as confirming, contradicting, or new relative to the existing baseline, and tests it against the Comeback-screen bet.
3. **`skills/competitive-pulse.md`** — weekly competitive watch focused on the one thing that matters most: any competitor closing the "free comeback moment" white space. Grades every finding by source tier (primary / direct observation / secondhand) so aggregator commentary is never quoted as fact.

## Agent Stack

*The Comeback Coach: senses, diagnoses, and synthesizes.*

| Agent | Trigger | Output | Boundaries |
|-------|---------|--------|------------|
| Metric pulse | Manual, Monday morning (target state: nightly, 8am delivery) | Three-slot Slack digest — headline Day-7 delta, channel breakdown (organic/paid/referral, with per-channel sample-size caveats), one signal to watch | Alert threshold is **±3 points**, not the course's 2pts — at ~50 users/arm a 2pt move is about one user; never posts to Slack automatically, Max pastes it by hand |
| Weekly insight | Friday, after `skills/friday-status.md` has run | 3-2-1 report (3 Done, 2 Changed, 1 Watch) to `reports/YYYY-MM-DD.md` plus printable Slack text | Stops and says so if friday-status hasn't run that week; never promotes a "Done" item into "Changed" — work happening isn't the same as a number moving; no auto-post |
| Anomaly → hypothesis | Fired by a pulse-agent alert, behind a manual YES gate | Full diagnostic, "inconclusive," or "low confidence" variant, posted before the 9am standup, plus a row in `outcome-log.md` | Three of five loop steps can stop the run; top hypothesis must score above 6/10 to issue SQL; writes the confirming SQL but does not run or interpret it itself |

**The one fact that matters most about this stack:** all three agents are specified and **unverified**. The five source CSVs the pilot data depends on are absent from this workspace, so no agent here has ever produced a real Streakly number — `agents/monday_retention.py` compiles and was smoke-tested against synthetic data only. The registry (`agents/registry.md`) also defines a weekly **learning loop**: it reads `outcome-log.md`, grades each closed diagnosis (hit/partial/miss), and proposes exactly one heuristic update to `CLAUDE.md` per run — it proposes, it never applies; Max decides. A six-month, one-agent-per-month roadmap is sequenced by which open gap it closes, starting with a Break-Event Volume Counter to answer the single biggest blocker: real weekly eligible-user volume.

## Final Presentation

Generated from this repo with the Module 6 Final Presentation Generator, and committed to [`final-presentation.html`](final-presentation.html): what you shipped (Streakly Comeback experience), the Day-7 retention impact, and what's next. Submitted alongside your repo URL.

**Source:** `reference-materials/streakly-workspace/skills/`, `agents/registry.md`, `agents/metric-pulse.md`, `agents/weekly-insight.md`, `agents/anomaly-diagnosis.md`, `workspace-audit.md`.
