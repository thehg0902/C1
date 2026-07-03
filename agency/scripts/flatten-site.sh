#!/usr/bin/env bash
# Copies src/ (which already contains assets/ nested inside it, per
# agency/contracts/file-structure.md) into a target directory as the
# deployable site root.
#
# Shared by .github/workflows/deploy-pages.yml (GitHub Pages demo) and
# agency/scripts/export-client.py (client-delivery branch) so there is
# exactly one place this copy step is defined.
#
# Usage: flatten-site.sh <target-dir>
set -euo pipefail
TARGET="$1"
mkdir -p "$TARGET"
cp -r src/. "$TARGET/"
find "$TARGET" -name '.gitkeep' -delete
