Run or resume the website build pipeline.

1. Read state/BUILD_STATE.md. If "Client:" is unset, this is a fresh build:
   set client name from client/client.md, set Started date.
2. Find the first phase not marked done and execute phases in order:
   - Phase 0 intake: run `python3 scripts/validate-client-md.py`. If it
     reports blockers, write them as questions to state/QUESTIONS.md, mark
     phase 0 blocked, STOP and tell the user what's needed. If clean (or
     only optional gaps), record gaps as questions, mark done, continue.
   - Phase 1 architecture: use the site-architecture skill. Output: page
     map + section list per page, appended to state/DECISIONS.md.
   - Phase 2 design: use design-direction then design-tokens skills.
     Output: src/css/tokens.css + a 10-line design rationale in DECISIONS.md.
   - Phase 3 content: use the copywriting skill. Output: final copy for
     every section of every page, written directly into the HTML files
     (create page skeletons per contracts/file-structure.md if absent).
   - Phase 4 media: use the media-generation skill. Produce a storyboard in
     state/MEDIA_LOG.md (status=planned). STOP. The human must set
     storyboard-approved=YES per row. Never generate before approval.
     After approval: generate, log credits, place files per contracts.
   - Phase 5 build: use layout-systems, components, hero-media,
     frontend-animation (per Stack flags), accessibility, performance,
     plus integration skills matching Stack flags (forms, booking,
     email-marketing, analytics, maps-gbp). Output: complete site in src/.
   - Phase 6 qa: run the /qa command logic. Only mark done if it passes.
   - Phase 7 deploy: STOP for human confirmation, then use deploy-hostinger.
   - Phase 8 handoff: use maintenance-retainer + write client handoff doc.
3. After each phase: update BUILD_STATE.md (status, completed date, notes).
4. Respect all hard invariants in CLAUDE.md at every phase.
