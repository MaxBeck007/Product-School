**`MOCK SESSION, NO REAL USER.` Dax is a persona (`personas/dax.md`), constructed
2026-09-30, not a real user. No real usability session has been run against
the miniature-painting prototype. Do not quote any line from this file as
user research.**

# Usability Session 2, Comeback Screen Prototype (Miniature Painting track), Dax

> **Method note:** run against `prototype/index.html` as it stood right after
> `change_log.md` Entry 7 (quiz → photo check-in), before any fix from this
> session. Same 4 questions as `research/usability-session-1.md`
> (P3L2/P3L2a format), one persona this time, chosen specifically because
> Priya/Tom/Amara have no reason to react to hobby-craft authenticity and Dax
> does.

Same 4 questions, in character throughout, no PM-style feedback until the end.

---

## Dax (competitive tabletop wargamer, 10+ years painting)

**1. What do you think this does?**

"Okay, so it's a 'come back after you fall off' screen. Fine, that's a real thing, I've fallen off. The best-streak number carrying over instead of zeroing out, that's actually the right call, I'll give it that.

The reference card though, 'Skirmisher, Layer 2, add one highlight layer on the raised edges,' somebody in there knows the hobby, that's not a made-up instruction. But calling it 'Layer 2' is a little sloppy. Layering's a specific technique, building up thin coats of gradually lighter tone, it's not just 'the second thing you do.' If this is coat two of a basecoat-then-highlight process, that's not 'a layer,' that's the highlight coat. Small thing, but if you're going to use hobby language, use it right or hobbyists will clock it in about four seconds."

**2. How would you arrive at this experience?**

"Same as anyone, I skip a couple days, painting gets shoved aside by work or whatever, I open the app expecting the usual 'you lost your streak' gut-punch and instead I get this. That part I believe, that's a real moment."

**3. Would you come back and restart your streak based on this?**

"Probably, yeah, the streak-freeze and the best-streak stat would get me to tap through. But this line, 'a quick photo, no critique, just a record you showed up today,' that's the one that actually bugs me.

No critique is doing a lot of work in that sentence and I don't think it's doing it on purpose. If I post a WIP in my painting Discord, the entire point is someone looks at it and tells me the blend on that highlight is chalky. A photo that goes into a void with an explicit promise that nobody's going to have an opinion about it isn't comforting, it's just... a photo nobody looks at. What's it for? If the app's trying to be gentle so it doesn't feel like homework, fine, I get the instinct, but 'no critique' reads like the app dodging having any opinion at all, not like it's being kind to me."

**4. If you had a magic wand, what would you change?**

"Two things. One, drop the '60-second lesson' framing. Nothing about painting happens in 60 seconds, paint has to dry, you can't rush a highlight layer, and calling it a 'lesson' like it's a Duolingo language card makes me trust the rest of the content less, because now I'm wondering if whoever built this actually paints or just knows the vocabulary. Call it a session. Don't put a fake time box on a craft.

Two, do something with the photo besides swallow it. Even just, show it to me next time I open the app, 'here's where you were a week ago.' Doesn't need critique from a stranger, I'm not asking for that here, just don't tell me upfront that nothing's going to happen with it."

---

## Step out of character, synthesis

**What Dax struggled with:** trusting that the app understands the craft it's asking him to do, not trusting the emotional safety of the mechanic (that's Amara's and Tom's struggle, not his). Two concrete tells: "Layer 2" used loosely, and a fixed "60-second lesson" time box that doesn't fit how painting actually works.

**What surprised me:** his objection to "no critique" is close to the opposite of what softened the copy for Amara and Tom. For them, removing evaluation removed pressure. For Dax, removing evaluation removed value, the whole reason a craft hobbyist photographs their work is to invite a look. Same copy choice lands as reassurance for one segment and as emptiness for another. That's a real tension in trying to serve both with one line of copy, not a bug in either reaction.

**Most concerning answer:** the "60-second lesson" framing, not the critique point. It's the more fixable one right now (a labeling mismatch, not a missing feature), and it's the one that actively damages trust in the rest of the content ("now I'm wondering if whoever built this actually paints"), which is a worse failure mode than a single missing feature: it makes him doubt every other detail on the screen, not just the time claim.

**Single highest-priority change:** drop the "60-second lesson" / fixed time-box framing. Rename "60-SECOND COMEBACK LESSON" and "Comeback lesson" to something that doesn't claim a specific duration, and remove the "1 min" meta text. This is a copy-only fix, same class of fix as the original P3L2 quiz-gate correction, not a scope change.

**Change made:** see `change_log.md` Entry 8.

**Open item carried forward, not actioned:** the photo check-in currently promises "no critique" and does nothing else with the photo. For an anxious, early-lapse user (Amara's segment) that's likely still the right call. For a craft-serious user (Dax's segment) it reads as pointless. No copy fix resolves this cleanly, it's a segmentation/scope question (does this screen need to know who it's talking to), not something to patch here.
