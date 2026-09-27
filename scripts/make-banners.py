#!/usr/bin/env python3
"""Build the banner manifest from the post H1s and render one PNG per part."""
import html
import json
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ASSETS = ROOT / "assets"
MANIFEST = ASSETS / "banners.json"
H1 = re.compile(r"^# Part (\d+): (.+?)\s*$", re.M)

CHROME = os.environ.get("CHROME_BIN", "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome")
TEMPLATE = ASSETS / "banner-template.html"
BACKGROUND = ASSETS / "series-background.png"
BUILD = ROOT / "build" / "banners"
OUT = ASSETS / "banners"
SERIES = "THE CLIENT SEAT"
AUTHOR = "Jenova"


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


def fill(template: str, part: dict, bg_tag: str) -> str:
    title = html.escape(part["title"], quote=True)
    return (template
            .replace("{{SERIES}}", SERIES)
            .replace("{{PART}}", str(part["part"]))
            .replace("{{TITLE}}", title)
            .replace("{{TITLE_CLASS}}", "long" if len(part["title"]) > 30 else "short")
            .replace("{{AUTHOR}}", AUTHOR)
            .replace("{{HUE}}", str((part["part"] * 9) % 360))
            .replace("{{BG}}", bg_tag))


def render(parts: list[dict]) -> None:
    if not os.path.exists(CHROME):
        sys.exit(f"Chrome not found at {CHROME}; set CHROME_BIN to your Chrome binary")
    BUILD.mkdir(parents=True, exist_ok=True)
    OUT.mkdir(parents=True, exist_ok=True)
    if BACKGROUND.exists():
        bg_tag = '<img class="bg" src="../../assets/series-background.png" alt="">'
    else:
        bg_tag = '<div class="bg-fallback"></div>'
        print("notice: assets/series-background.png not found; rendering the gradient fallback")
    template = TEMPLATE.read_text().replace('url("fonts/', 'url("../../assets/fonts/')
    for part in parts:
        page = BUILD / f"{part['slug']}.html"
        page.write_text(fill(template, part, bg_tag))
        png = ROOT / part["file"]
        png.unlink(missing_ok=True)  # a stale committed PNG must not pass as a fresh screenshot
        cmd = [CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars",
               "--force-device-scale-factor=1", "--window-size=1600,900",
               "--virtual-time-budget=3000", f"--screenshot={png}", page.resolve().as_uri()]
        result = subprocess.run(cmd, capture_output=True, text=True)
        if result.returncode != 0 or not png.exists():
            sys.exit(f"screenshot failed for part {part['part']}: {result.stderr.strip()[:300]}")
        print(f"rendered {part['file']}")


def main() -> int:
    parts = read_parts()
    write_manifest(parts)
    print(f"manifest: {len(parts)} parts -> {MANIFEST.relative_to(ROOT)}")
    render(parts)
    return 0


if __name__ == "__main__":
    sys.exit(main())
