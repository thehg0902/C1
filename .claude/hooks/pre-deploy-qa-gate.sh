#!/usr/bin/env bash
# PreToolUse hook: blocks git push (deploy trigger on Hostinger Git
# integration) unless BUILD_STATE.md shows phase 6 (qa) = done.
INPUT=$(cat)
CMD=$(echo "$INPUT" | python3 -c 'import sys,json;print(json.load(sys.stdin).get("tool_input",{}).get("command",""))' 2>/dev/null)
case "$CMD" in
  *"git push"*)
    if [ -f agency/state/BUILD_STATE.md ] && ! grep -E '^\|\s*6\s*\|\s*qa\s*\|\s*done' agency/state/BUILD_STATE.md >/dev/null; then
      echo "BLOCKED: QA phase not marked done in agency/state/BUILD_STATE.md. Run /qa first." >&2
      exit 2
    fi ;;
esac
exit 0
