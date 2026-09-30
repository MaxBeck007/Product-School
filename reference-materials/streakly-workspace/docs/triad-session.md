**`AGENDA, NOT A MEETING THAT HAPPENED.` This session has not taken place. The
questions below are prepared, not asked, and the alignment doc is an empty
template. Nothing here records Raj's or Lena's actual positions.**

# Triad Session: Comeback Screen Prototype Review

> **Attendees:** Raj (Engineering), Lena (Design), Me (PM)
> **Length:** 30 minutes
> **Sources:** `prototype/index.html` (v1, 2 rounds of fixes logged in
> `change_log.md`), `docs/hypothesis.md`, `docs/decision-brief.md`

## Agenda

**1. Context, 5 min**
- Where this came from: Marcus's Thursday ask, the research (interviews, NPS,
  competitive gaps), and the decision to bet on the Comeback screen over
  notification-only fixes (`docs/decision-brief.md`).
- The hypothesis we're testing (`docs/hypothesis.md`).

**2. Walk the prototype, 10 min**
- Show all 3 screens live: comeback entry → 60-second lesson → done/re-entry.
- Call out both fixes already made and why (`change_log.md` Entries 1 and 2):
  removing the pass/fail quiz gate, and softening the "Quick check" label.
- Be explicit that the miniature-painting lesson (changed from guitar,
  `change_log.md` Entry 7) and the freeze copy are both still open items, not
  final.

**3. Questions for Raj (feasibility), 10 min**
- The original Slack thread flagged two open items: "logic for who sees it" and
  "the freeze rules." Where do those actually live in the data model, and what's
  the smallest version we could ship without resolving both fully?
- The prototype shows a fixed miniature-painting lesson. If we personalize it
  to the user's actual pre-lapse track, is that a real lift given "no new
  data sources," or does it change scope?
- Tom's mock feedback (`change_log.md` Entry 2) suggests the freeze needs to
  visibly resolve rather than requiring a tap-and-trust interaction. Is a
  pre-applied freeze (shown as already done, no tap) meaningfully different in
  build terms from the current one-tap version?

**4. Questions for Lena (experience), 10 min**
- Amara's mock feedback flagged that even after removing the actual penalty from
  the quiz, the label "Quick check" still primed test anxiety on its own. Does
  that change how you'd think about copy across the rest of this flow?
- Does the current tone balance "welcome back" against feeling too breezy about
  a real gap in progress? Where's the line?
- What's the empty state, what does this screen show if the user has never had
  a streak to protect?

**5. Decisions to walk out with, 5 min**
- Go/no-go on personalizing the comeback lesson to the user's real track vs.
  keeping a single example lesson for the first test.
- A direction on the freeze interaction: keep the one-tap version, or explore
  a pre-applied version.
- Whether an empty-state case needs to be designed before this goes further.

---

## Post-Session Alignment Doc (template, to fill in live)

**Date:**
**Attendees:**

**Decisions made:**
1.
2.
3.

**Open questions still unresolved:**
-

**Owner for next step:**

**Next checkpoint:**

---

## Slack Invite Message

```
Hey Raj, Lena — want to grab 30 min to walk through the Comeback screen
prototype (v1, already through 2 rounds of fixes) and get your read before we
take this further.

Context: this is the direction from Marcus's retention thread and the research
we did afterward, comeback screen over notification-only fixes. I'll bring the
hypothesis and a couple of specific questions for each of you, feasibility for
Raj, tone and empty states for Lena.

Should take 30 min. When's good this week?
```
