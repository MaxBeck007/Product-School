# Claude for PMs, Your First Session

> Five-minute read. Written for a PM who has never used Claude Code.
> **Before your session:** nothing to install or read. Bring one real product
> problem you are working on right now, not a practice one.

## What this is

Claude Code is Claude with access to a folder on your computer. Instead of
copying text into a chat window and copying the answer back out, you point it
at a folder and it reads and writes the files in there directly.

That one difference is the whole thing: your work accumulates in a place that
stays, so every session starts with everything the last one produced.

## What you will build in your first session

One folder that contains your product's context, set up so that any future
session, on any day, opens already knowing your product, your metric, your
stakeholders, and what you decided last week.

You will not build it by filling in a template. Claude will interview you, one
question at a time, and build it from your answers. Paste this to start:

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

Expect the interview to take ten to fifteen minutes and to feel slightly
tedious. That tedium is the product. Everything you do in that folder afterward
is better for it.

## The three habits that matter

**1. Update CLAUDE.md every session.** It is the file Claude reads first, every
time. If it is current, a session six weeks from now opens knowing where things
stand. If it is stale, Claude will confidently work from last month's position,
and you will not notice until it matters.

**2. Run the interview before anything gets built.** Ask Claude to interview you
before it writes a document, a plan, or a spec. The version built from a
fifteen-minute interview is not a slightly better version of the one built from
a one-line request, it is a different document, because the interview surfaces
what you actually meant.

**3. Save everything, and label what is real.** Every file gets a header saying
where its content came from: Verified, Assumption, or Mock. This sounds
bureaucratic until the first time someone asks "where did that number come
from?" in a review, and you can answer in four seconds. It is also the only
thing that stops a Claude-generated draft of your engineer's opinion from
quietly becoming, three weeks later, your engineer's opinion.

## The mistake everyone makes

**Treating it like a chat window.** Asking a question, getting a good answer,
copying the answer somewhere else, closing the session. You get a fast assistant
and nothing accumulates. Next week you start over, because the folder holds
nothing.

**How to avoid it:** end every session by asking

```
What from this session should be saved, and where? Then update CLAUDE.md and
add a change_log.md entry.
```

Two minutes. It is the difference between a tool you use and a workspace that
compounds.

## The second mistake, worth knowing about

**Believing a confident answer without checking it.** Claude will produce
plausible numbers, citations, and file paths, and a wrong one reads exactly like
a right one. The habit that catches this: ask "which file or source is that
from?" and follow the answer. If it cannot cite it, treat it as a guess, which
is fine as long as it is labeled as one.

---

**One session in, you will have:** a workspace that carries its own context, and
a repeatable way to open it. That is the whole first session. Everything else,
research synthesis, specs, data analysis, scheduled digests, is built on top of
it.
