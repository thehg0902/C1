#!/usr/bin/env python3
"""Produce a clean client-delivery branch: just the built site, no agency
logic, no .md process files. Run from repo root.

Rebuilds an orphan `client-delivery` branch from scratch each run (same
model as a gh-pages branch) via a throwaway git worktree, so the human's
current branch/working tree is never touched. Reuses
agency/scripts/flatten-site.sh - the same src/ copy step already used by
.github/workflows/deploy-pages.yml - so there is one source of truth.
"""
import argparse
import pathlib
import re
import subprocess
import sys
from datetime import date

ROOT = pathlib.Path(".")
DELIVERY_BRANCH = "client-delivery"
WORKTREE_DIR = pathlib.Path("../__export-client-tmp")


def run(cmd, **kwargs):
    return subprocess.run(cmd, check=True, text=True, capture_output=True, **kwargs)


def run_ok(cmd, **kwargs):
    return subprocess.run(cmd, text=True, capture_output=True, **kwargs)


def fail(msg):
    print(f"BLOCKED: {msg}", file=sys.stderr)
    sys.exit(1)


def check_preconditions(ref):
    status = run(["git", "status", "--porcelain"]).stdout
    if status.strip():
        fail("working tree is not clean. Commit or stash changes first.")

    build_state = ROOT / "agency" / "state" / "BUILD_STATE.md"
    if not build_state.exists():
        fail(f"{build_state} not found.")
    text = build_state.read_text(encoding="utf-8")
    if not re.search(r"^\|\s*6\s*\|\s*qa\s*\|\s*done", text, re.M):
        fail("Phase 6 (qa) is not marked done in agency/state/BUILD_STATE.md. Run /qa first.")

    current = run(["git", "rev-parse", "--abbrev-ref", "HEAD"]).stdout.strip()
    if ref and current != ref:
        fail(f"on branch '{current}', but --ref {ref} was requested. Check out {ref} first.")
    return current


def client_name():
    client_md = ROOT / "agency" / "client" / "client.md"
    if client_md.exists():
        m = re.search(r"^- Name:\s*(.+)$", client_md.read_text(encoding="utf-8"), re.M)
        if m:
            return m.group(1).strip()
    return "the client"


def generate_readme(worktree, name):
    handoff = ROOT / "agency" / "docs" / "HANDOFF.md"
    if handoff.exists():
        # /handoff has already produced the richer, human-written package -
        # reuse it verbatim rather than re-deriving a thinner version.
        (worktree / "README.md").write_text(handoff.read_text(encoding="utf-8"), encoding="utf-8")
        return
    pages = sorted(p.name for p in worktree.glob("*.html"))
    lines = [
        f"# {name} - Website Files",
        "",
        f"Delivered {date.today().isoformat()}.",
        "",
        "## Pages",
        "",
    ]
    lines += [f"- {p}" for p in pages]
    lines += [
        "",
        "## Notes",
        "",
        "This is the complete, deployable site: open any .html file in a",
        "browser, or upload this whole folder to any static web host.",
        "For questions or change requests, contact the agency that built this.",
    ]
    (worktree / "README.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--ref", help="branch to export from (default: current branch)")
    args = parser.parse_args()

    current_branch = check_preconditions(args.ref)
    head_sha = run(["git", "rev-parse", "--short", "HEAD"]).stdout.strip()

    if WORKTREE_DIR.exists():
        fail(f"{WORKTREE_DIR} already exists - a previous export may have failed mid-way. Remove it and retry.")

    branch_exists = run_ok(
        ["git", "show-ref", "--verify", "--quiet", f"refs/heads/{DELIVERY_BRANCH}"]
    ).returncode == 0
    remote_branch_exists = run_ok(
        ["git", "ls-remote", "--exit-code", "--heads", "origin", DELIVERY_BRANCH]
    ).returncode == 0

    print(f"Exporting {client_name()} from {current_branch}@{head_sha}...")

    if branch_exists or remote_branch_exists:
        if remote_branch_exists and not branch_exists:
            run(["git", "fetch", "origin", f"{DELIVERY_BRANCH}:{DELIVERY_BRANCH}"])
        run(["git", "worktree", "add", str(WORKTREE_DIR), DELIVERY_BRANCH])
        # Wipe existing contents (except the worktree's own .git file) so
        # this export is a full fresh snapshot, not an incremental diff.
        run(["git", "-C", str(WORKTREE_DIR), "rm", "-rf", "--quiet", "."])
    else:
        run(["git", "worktree", "add", "--orphan", "-b", DELIVERY_BRANCH, str(WORKTREE_DIR)])

    try:
        run(["bash", "agency/scripts/flatten-site.sh", str(WORKTREE_DIR)])
        generate_readme(WORKTREE_DIR, client_name())

        run(["git", "-C", str(WORKTREE_DIR), "add", "-A"])
        commit = run_ok(
            ["git", "-C", str(WORKTREE_DIR), "commit", "-m",
             f"Client delivery export: {client_name()} - {date.today().isoformat()} (from {head_sha})"]
        )
        if commit.returncode != 0 and "nothing to commit" not in commit.stdout:
            print(commit.stdout, commit.stderr, file=sys.stderr)
            fail("commit failed")

        run_ok(["git", "fetch", "origin", DELIVERY_BRANCH])  # refresh tracking info for the lease check
        push = run_ok(["git", "-C", str(WORKTREE_DIR), "push", "origin", DELIVERY_BRANCH, "--force-with-lease"])
        if push.returncode != 0:
            print(push.stdout, push.stderr, file=sys.stderr)
            fail("push failed")

        pushed_sha = run(["git", "-C", str(WORKTREE_DIR), "rev-parse", "--short", "HEAD"]).stdout.strip()
    finally:
        run_ok(["git", "worktree", "remove", str(WORKTREE_DIR), "--force"])

    remote_url = run(["git", "remote", "get-url", "origin"]).stdout.strip()
    print()
    print(f"Pushed {DELIVERY_BRANCH}@{pushed_sha}")
    print()
    print("To hand off a zip to the client:")
    print(
        f"  git clone -b {DELIVERY_BRANCH} --single-branch {remote_url} "
        f"{client_name().lower().replace(' ', '-')}-site"
    )
    print(f"  cd {client_name().lower().replace(' ', '-')}-site && rm -rf .git")
    print(f"  zip -r ../{client_name().lower().replace(' ', '-')}-site.zip .")


if __name__ == "__main__":
    main()
