#!/usr/bin/env bash
# Render every post to standalone HTML for pasting into Medium's editor,
# with the part's banner image injected above the title.
set -euo pipefail
cd "$(dirname "$0")/.."
command -v pandoc >/dev/null || { echo "pandoc is required: brew install pandoc"; exit 1; }
[ -f assets/banners.json ] || { echo "assets/banners.json missing: run python3 scripts/make-banners.py"; exit 1; }
BASE="https://jenova-marie.github.io/the-client-seat/assets/banners"
mkdir -p build
for f in 0*.md 1[01]-*.md; do
  slug="${f%.md}"
  out="build/${slug}.html"
  pandoc "$f" --from gfm --to html5 --standalone --metadata pagetitle="$slug" -o "$out"
  python3 - "$out" "$slug" "$BASE" <<'PY'
import html, json, sys
out, slug, base = sys.argv[1:]
title = next(e["title"] for e in json.load(open("assets/banners.json")) if e["slug"] == slug)
tag = f'<p><img src="{base}/{slug}.png" alt="{html.escape(title, quote=True)}"></p>\n'
text = open(out).read()
i = text.index("<h1")
open(out, "w").write(text[:i] + tag + text[i:])
PY
  echo "rendered $out"
done
