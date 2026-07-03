#!/usr/bin/env bash
# PreToolUse hook: blocks git commits that stage likely secrets.
# Receives tool input as JSON on stdin. Exit 2 = block (per hooks docs);
# VERIFY exit-code convention against current docs before relying on it.
INPUT=$(cat)
echo "$INPUT" | grep -q '"command"' || exit 0
CMD=$(echo "$INPUT" | python3 -c 'import sys,json;print(json.load(sys.stdin).get("tool_input",{}).get("command",""))' 2>/dev/null)
case "$CMD" in
  *"git commit"*|*"git add"*)
    if git diff --cached 2>/dev/null | grep -Eiq '(api[_-]?key|secret|password|token)[\"'"'"' ]*[:=][\"'"'"' ]*[A-Za-z0-9_\-]{12,}'; then
      echo "BLOCKED: staged changes appear to contain a secret. Remove it, use env vars." >&2
      exit 2
    fi ;;
esac
exit 0
