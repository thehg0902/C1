---
name: deploy-hostinger
description: Deploy the static site via Hostinger hPanel Git integration -
  branch strategy, deploy steps, rollback, post-deploy checks. Use via
  /deploy in Phase 7 and for retainer redeploys. Not for DNS (domains-dns).
metadata: {version: 1.0.0, category: deploy, tier: E}
---
# Deploy (Hostinger Git)

## Purpose
Push-to-deploy: the repo's deploy branch is the live site.

## Inputs
QA-passed src/ + assets/, Hostinger repo connection (one-time setup below),
human deploy confirmation (CLAUDE.md invariant + hook gate).

## Outputs
Live site; deploy record (URL, date, commit) in BUILD_STATE.md.

## Rules
1. One-time setup (human does in hPanel, Claude provides this checklist):
   Websites -> manage -> Advanced -> Git -> connect the client repo,
   branch `production`, target directory public_html (or subdir), enable
   auto-deploy webhook if offered. VERIFY current hPanel labels against
   Hostinger docs at setup time - panels change.
2. Branch strategy: work on main; `production` receives only QA-passed
   merges. Deploy = merge main -> production, push. The pre-deploy hook
   blocks push when QA isn't done - do not bypass.
3. Hostinger serves the repo as-is: file-structure contract must place
   deployables correctly. If the Git target dir maps to repo root, add a
   one-time decision: either target subdir src/ in hPanel, or a
   production-branch layout where src/ contents sit at root - log which
   in DECISIONS.md at first deploy and never mix.
4. Post-deploy checks (do all, record results): live URL 200s per page;
   assets load (no mixed-content, correct paths); form test submission;
   Calendly opens; https padlock; sitemap.xml reachable; analytics
   realtime hit.
5. Rollback: revert the merge commit on production, push. Practice path
   documented > clever path.

## Anti-patterns
- Deploying from an uncommitted working tree; force-push to production;
  editing files directly in hPanel file manager (breaks Git state).

## Changelog
- 1.0.0 initial (encodes the hPanel Git workflow)
