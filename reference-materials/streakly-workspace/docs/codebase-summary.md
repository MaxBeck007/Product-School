# Codebase Tour: Habitica (reference repo for the Comeback screen exercise)

> **Method note:** Streakly has no real codebase, it's fictional. Per the course
> exercise, this tour is of the actual public repo
> [HabitRPG/habitica](https://github.com/HabitRPG/habitica) (`develop` branch),
> used as a stand-in so the mapping-to-a-real-codebase exercise has something
> real to look at. Every claim below links the exact file fetched.
> **Access note:** the GitHub MCP connector wasn't available this session (auth
> config issue), so this was done via direct web fetch of public GitHub pages,
> not the GitHub API. That means I read the actual current file contents, not a
> mock, but I did not run a full repo-wide code search, only the files linked
> below.

## 1. What this product does, in one sentence

Habitica is an open-source habit tracker that turns your real-life to-do list
into a role-playing game: you level up and earn gold for completing habits,
dailies, and to-dos, and lose HP for missing them.
([README](https://github.com/HabitRPG/habitica))

## 2. How the codebase is organized

Top-level folders (from the repo root):

- **`website/`** — the actual application: server (`website/server`) and client
  (`website/client`), confirmed by `package.json`'s `main` field
  (`./website/server/index.js`) and its `client:dev`/`client:build` scripts.
- **`migrations/`** — standalone database migration scripts, notable on its own:
  see the spec-writing flag below.
- **`test/`** — split by test type: `test/sanity`, `test/common`, `test/content`,
  plus API v3/v4 integration suites (from `package.json` scripts).
- **`scripts/`**, **`gulp/`** — build and dev tooling (gulpfile-driven build).
- **`.github/`, `.ebextensions/`, `.heroku/`, `kubernetes/`** — CI and deploy
  config for GitHub Actions, AWS Elastic Beanstalk, Heroku, and Kubernetes,
  suggesting this app has shipped through more than one hosting era.
- **`habitica-images`** — a separate git submodule, not part of the main repo,
  for image assets.
- **`database_reports/`** — ad hoc reporting scripts.

Stack, from [`package.json`](https://github.com/HabitRPG/habitica/blob/develop/package.json):
Node 20, Express, MongoDB via Mongoose, a Vue client, gulp for build/sprites,
Stripe/PayPal/Amazon payment integrations, Firebase, and push notification
libraries (`node-gcm`, `apple-auth`).

## 3. The 3 most important files for a PM

1. **[`package.json`](https://github.com/HabitRPG/habitica/blob/develop/package.json)**
   — one file to see the entire stack, dependencies, and every build/test
   command, fastest way to answer "what is this actually built with."
2. **[`website/server/models/user/schema.js`](https://github.com/HabitRPG/habitica/blob/develop/website/server/models/user/schema.js)**
   — the entire per-user data model, 766 lines. Everything the app tracks
   about one person lives here: stats, achievements, items, preferences,
   party membership.
3. **[`website/server/models/group.js`](https://github.com/HabitRPG/habitica/blob/develop/website/server/models/group.js)**
   — the party/guild/quest system, 1,723 lines. Shows how the *social*
   layer (parties doing quests together) is where a lot of the sustained
   engagement logic actually lives, not just individual streak-keeping.

## 4. Key data models and what they tell you about product decisions

- **The streak itself is a single integer with no history.**
  `achievements.streak: { $type: Number, default: 0 }` is the entire streak
  field in the schema. There is no "best streak," no dated log of past streaks,
  and, notably, **no streak-freeze or grace-period field anywhere in this
  schema.** ([source](https://github.com/HabitRPG/habitica/blob/develop/website/server/models/user/schema.js))
  This is directly relevant: it's the same class of gap Raj flagged in the
  original P1 Slack thread ("we'd need the logic for who sees it and the
  freeze rules"), the real reference app doesn't model this either.
- **Achievements are a flat bag of ~80 hardcoded fields**
  (`streak`, `veteran`, `beastMaster`, `mountMaster`, `triadBingo`, etc.), not
  a flexible, extensible system. Product decision this implies: adding a new
  badge or milestone in this architecture means adding a new schema field and
  code path, not just writing new data, that's a real cost per new
  achievement type.
- **`stats.buffs.streaks: Boolean`** exists as a temporary bonus flag, so there
  is *some* concept of a streak-based buff, but it's a boolean modifier, not a
  protection mechanic like a freeze.
- **The social/quest system (`Group` model) is comparatively rich:**
  `quest.progress` tracks boss HP or collected items, `quest.members` tracks
  per-member accept/decline, and there's a full invite/RSVP flow. Product
  decision this implies: Habitica's retention answer leans on *group*
  commitment (a party quest fails or succeeds together) more than on
  individual streak protection.
- **Nearly every field has an explicit Mongoose default, and the schema uses
  `strict: true`.** That means undefined fields are rejected outright, not
  silently allowed. A new field cannot just appear from the client without a
  schema change shipping first.

## 5. Mapping the Comeback screen feature to this codebase (by analogy)

- **Where it would live:** extending the `User` model's `achievements`/`stats`
  block with new fields (e.g. a best-streak value and a freeze state), plus new
  server logic parallel to how streak and buff fields are already handled.
  The actual screen UI would live in the Vue client (`website/client`), not
  reviewed in this pass.
- **What it would touch:** the `User` schema (new fields), and likely the
  notification-preference pattern already established per-type (e.g.
  `emailNotifications.questStarted`, `pushNotifications.questStarted`), a
  "streak broken" or "comeback offered" notification would plausibly follow
  that same existing per-type toggle pattern rather than inventing a new one.
- **Blast radius:** the `User` document is touched by nearly every part of
  this app (stats, items, party, tasks). Any new field added here has to
  account for the population that already exists, this repo has a dedicated
  top-level `migrations/` folder for exactly that reason. Adding a field is
  not free even when it's additive.

## 6. Flags for spec-writing

- **Data that doesn't exist yet:** there is no best-streak or streak-freeze
  field in this reference schema, only a plain streak counter. A real spec
  needs to define exactly what "best streak" and "freeze" persist as, a
  single number, a dated history, or an expiring flag, before engineering can
  scope it.
- **Existing constraint to call out:** the strict schema and explicit defaults
  mean a schema change has to ship before, or together with, any client change
  that depends on a new field. That's a sequencing dependency for a ticket, not
  just a nice-to-know.
- **The one thing engineers will ask before kickoff:** "what does 'best streak'
  actually persist as, given today's streak is just a live counter with no
  history to fall back on?" This is the same open question Raj raised in the
  original Slack thread, seeing it show up independently in a real reference
  codebase is a signal it's a real question, not a hypothetical one.
