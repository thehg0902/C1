# Agency OS — Constitution

This repository is a reusable website-build template. One client = one clone of
this repo. The ONLY file that changes per client is `agency/client/client.md`.
A "build" means: transform `agency/client/client.md` into a complete, deployed,
custom-coded website (HTML/CSS/JS) following the pipeline below.

## How to work in this repo

- Start or resume any build with the `/build` command. It reads
  `agency/state/BUILD_STATE.md` and continues from the current phase.
- All expertise lives in skills (`.claude/skills/`). Trust skill descriptions
  to load what the task needs. Do not preload skills speculatively.
- All shared interfaces live in `agency/contracts/`. Skills obey contracts.
- All mutable project state lives in `agency/state/`. Never store state in this file.

## Precedence ladder (conflict resolution — highest wins)

1. Explicit user instruction in the current session
2. `agency/client/client.md` (the client is the spec)
3. `agency/state/DECISIONS.md` (previously resolved ambiguities)
4. Hard invariants below (these beat client.md ONLY for the enumerated items)
5. `agency/contracts/*` (interface law between skills)
6. Skill bodies (`.claude/skills/*/SKILL.md`)
7. Skill reference files
8. General knowledge

Tie-breaker within a level: more specific beats more general. If two
same-level sources genuinely conflict: do NOT silently pick — log the
conflict to `agency/state/QUESTIONS.md` and take the reversible option.

## Hard invariants

- NEVER trigger paid media generation (Higgsfield or any paid API) without an
  approved storyboard recorded in `agency/state/MEDIA_LOG.md`. No exceptions, even if
  the client says "generate whatever you want."
- NEVER deploy without a passing QA gate (`/qa` completed, recorded in
  `agency/state/BUILD_STATE.md`).
- NEVER invent client facts (hours, prices, addresses, testimonials, claims).
  Missing facts go to `agency/state/QUESTIONS.md` as questions; use clearly marked
  `[PLACEHOLDER: ...]` text in the meantime.
- NEVER commit secrets, API keys, or credentials to the repo.
- NEVER remove or rename files under `agency/contracts/` during a build.

## Output economy

- Do not restate file contents you just read or wrote; reference paths.
- Summarize diffs, not whole files. Prefer targeted edits over rewrites.
- No ceremonial recaps between steps; report phase results in one short block.
- Write code directly to files; do not print large code blocks into chat
  unless asked.
- When a script exists for a check, run it instead of reasoning through the
  checklist in prose.

## Map

- `agency/client/client.md` — the spec. `agency/client/client.schema.md` — required fields.
- `agency/contracts/` — design-tokens, file-structure, component-api, media-log.
- `agency/state/` — BUILD_STATE.md, DECISIONS.md, QUESTIONS.md, MEDIA_LOG.md.
- `src/` — the website being built. `assets/` — per agency/contracts/file-structure.md.
- `agency/scripts/` — repo utilities (validate, lint, registry, flatten-site,
  export-client). Run, don't read.
- `agency/` itself — everything agency-internal: process, client intake,
  mutable state. Never shipped to the client. When ready to hand off a
  clean deliverable (no agency logic, no .md process files), run
  `/export-client` — it produces a `client-delivery` branch containing
  only the built site.
