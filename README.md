# Agency OS — Website Build Template

Per-client workflow:
1. Clone this repo → rename to the client.
2. Replace `agency/client/client.md` (follow `agency/client/client.schema.md`). Drop client
   assets in `agency/client/assets-intake/`.
3. Open Claude Code in the repo root. Say `/build`.
4. Answer questions in `agency/state/QUESTIONS.md` when the pipeline stops at gates
   (intake, media storyboard approval, deploy confirmation).
5. Once QA passes, run `/export-client` any time you want a clean
   deliverable to hand off - it produces a `client-delivery` branch
   containing only the built site, safe to re-run.

Architecture: `agency/docs/ARCHITECTURE.md`. Skill index: `agency/docs/REGISTRY.md`
(regenerate with `python3 agency/scripts/generate-skill-registry.py`).

Maintenance: run `python3 agency/scripts/lint-skills.py` before committing skill
changes.

VERIFY BEFORE RELYING ON (see agency/docs/ARCHITECTURE.md Appendix B):
- Path-scoped rule frontmatter format in `.claude/rules/` against current
  Claude Code docs (https://code.claude.com/docs/en/memory).
- Hook wiring in `.claude/settings.json` against current hooks docs.
