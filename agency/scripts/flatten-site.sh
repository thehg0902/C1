#!/usr/bin/env bash
# Flattens src/ + assets/ into a target directory and rewrites the
# "../assets/" browser-relative paths (correct when src/ and assets/ are
# separate sibling directories, per agency/contracts/file-structure.md)
# down to "assets/" (correct once both are copied into one flat root).
#
# Shared by .github/workflows/deploy-pages.yml (GitHub Pages demo) and
# agency/scripts/export-client.py (client-delivery branch) so there is
# exactly one place this transform is defined.
#
# Usage: flatten-site.sh <target-dir>
set -euo pipefail
TARGET="$1"
mkdir -p "$TARGET"
cp -r src/. "$TARGET/"
cp -r assets "$TARGET/assets"
grep -rlZ '\.\./assets/' "$TARGET" --include='*.html' --include='*.css' \
  | xargs -0 -r sed -i 's#\.\./assets/#assets/#g'
