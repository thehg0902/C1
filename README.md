# Agency OS — Website Build Template

Per-client workflow:
1. Clone this repo → rename to the client.
2. Replace `client/client.md` (follow `client/client.schema.md`). Drop client
   assets in `client/assets-intake/`.
3. Open Claude Code in the repo root. Say `/build`.
4. Answer questions in `state/QUESTIONS.md` when the pipeline stops at gates
   (intake, media storyboard approval, deploy confirmation).

Architecture: `docs/ARCHITECTURE.md`. Skill index: `docs/REGISTRY.md`
(regenerate with `python3 scripts/generate-skill-registry.py`).

Maintenance: run `python3 scripts/lint-skills.py` before committing skill
changes.

VERIFY BEFORE RELYING ON (see docs/ARCHITECTURE.md Appendix B):
- Path-scoped rule frontmatter format in `.claude/rules/` against current
  Claude Code docs (https://code.claude.com/docs/en/memory).
- Hook wiring in `.claude/settings.json` against current hooks docs.
