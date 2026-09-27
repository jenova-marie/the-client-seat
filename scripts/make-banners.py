#!/usr/bin/env python3
"""Build the banner manifest from the post H1s and render one PNG per part."""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ASSETS = ROOT / "assets"
MANIFEST = ASSETS / "banners.json"
H1 = re.compile(r"^# Part (\d+): (.+?)\s*$", re.M)


def read_parts() -> list[dict]:
    parts = []
    for post in sorted(ROOT.glob("[01]*.md")):
        m = H1.search(post.read_text())
        if not m:
            sys.exit(f"no 'Part N: title' H1 in {post.name}")
        slug = post.stem
        parts.append({
            "part": int(m.group(1)),
            "title": m.group(2),
            "slug": slug,
            "file": f"assets/banners/{slug}.png",
        })
    return parts


def write_manifest(parts: list[dict]) -> Path:
    MANIFEST.write_text(json.dumps(parts, indent=2) + "\n")
    return MANIFEST


def main() -> int:
    parts = read_parts()
    write_manifest(parts)
    print(f"manifest: {len(parts)} parts -> {MANIFEST.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
