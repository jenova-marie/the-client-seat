#!/usr/bin/env python3
"""Verify the banner manifest and PNGs. Exit 0 on pass, 1 on fail."""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MANIFEST = ROOT / "assets" / "banners.json"
H1 = re.compile(r"^# Part (\d+): (.+?)\s*$", re.M)


def post_titles() -> dict[int, str]:
    titles = {}
    for post in sorted(ROOT.glob("[01]*.md")):
        m = H1.search(post.read_text())
        if m:
            titles[int(m.group(1))] = m.group(2)
    return titles


def main() -> int:
    fails = []
    if not MANIFEST.exists():
        print("FAIL: assets/banners.json missing")
        return 1
    entries = json.loads(MANIFEST.read_text())
    titles = post_titles()
    if len(entries) != 12:
        fails.append(f"manifest has {len(entries)} entries, expected 12")
    for e in entries:
        want = titles.get(e["part"])
        if want != e["title"]:
            fails.append(f"part {e['part']}: manifest title {e['title']!r} != post H1 {want!r}")
        if not e["slug"] or not e["file"].endswith(f"{e['slug']}.png"):
            fails.append(f"part {e['part']}: slug/file mismatch")
    for f in fails:
        print("FAIL:", f)
    print("PASS banners" if not fails else "FAIL banners")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
