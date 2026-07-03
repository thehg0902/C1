Run the pre-delivery QA gate.

1. Run `python3 .claude/skills/qa-review/scripts/check.py`. Fix every FAIL
   it reports, re-run until clean.
2. Then perform the manual review in the qa-review skill (read it now).
3. Write results to agency/state/BUILD_STATE.md notes. Mark phase 6 done ONLY if
   script passes and manual review has no criticals. Otherwise list what
   blocks, mark phase 6 blocked.
