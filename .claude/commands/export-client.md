Produce the clean client-delivery branch (no agency logic, no .md
process files) from the current state of src/ (self-contained, includes
assets/ nested inside it).

Preconditions (verify, do not assume): working tree clean; phase 6 qa =
done in agency/state/BUILD_STATE.md; on main (or human specifies --ref).

1. Run `python3 agency/scripts/export-client.py`.
2. Report the pushed branch name, commit SHA, and the clone/zip command
   for the human to hand to the client.
3. Do NOT switch the human's current branch/worktree as a side effect.
