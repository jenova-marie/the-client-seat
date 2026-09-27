#!/usr/bin/env bash
# Render every post to standalone HTML for pasting into Medium's editor.
set -euo pipefail
cd "$(dirname "$0")/.."
command -v pandoc >/dev/null || { echo "pandoc is required: brew install pandoc"; exit 1; }
mkdir -p build
for f in 0*.md 1[01]-*.md; do
  out="build/${f%.md}.html"
  pandoc "$f" --from gfm --to html5 --standalone --metadata title="${f%.md}" -o "$out"
  echo "rendered $out"
done
