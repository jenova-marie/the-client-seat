#!/usr/bin/env python3
"""Check one blog post against the series spec. Exit 0 on pass, 1 on fail."""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PROMPTS = ROOT / "prompts"
FORBIDDEN = ROOT / "scripts" / "forbidden.txt"

SKELETON = ["## The idea", "## Paste this into Claude", "## Check it", "## Do it", "## Next time"]
OPTIONAL = "## Sidebar for the developer"
NEEDS_SOURCES = {"01", "03", "04", "05", "06", "07", "09", "10", "11"}
TELLS = [
    "**the confident specific**", "**the invented feature**", '**the "wow, really?"**',
    "**the silent assumption**", "**the drift**", "**the agreeable flip**",
]
CLOSING = "**Ask for the source, open the source, compare.**"
STUCK_SENTENCE = "You cannot see my screen, so ask me what I see."
EMAIL = re.compile(r"[\w.+-]+@[\w-]+\.[\w.]+")
PHONE = re.compile(r"\(?\b\d{3}\)?[-. ]?\d{3}[-. ]?\d{4}\b|\b\d{10,11}\b")


def heading_pos(text: str, heading: str) -> int:
    """Position of an exact markdown heading line, or -1. Substring mentions don't count."""
    m = re.search(r"^" + re.escape(heading) + r"\s*$", text, re.M)
    return m.start() if m else -1


def prompt_body(path: Path) -> str:
    text = path.read_text()
    head, _, body = text.partition("\n\n")
    if not head.startswith("Where to paste:"):
        return ""
    return body.strip()


def main(post_path: str) -> int:
    post = Path(post_path)
    text = post.read_text()
    part = post.name[:2]
    fails = []

    words = len(text.split())
    lo, hi = (500, 900) if part == "00" else (1200, 1800)
    if not lo <= words <= hi:
        fails.append(f"word count {words} outside {lo}-{hi}")

    if part != "00":
        positions = [heading_pos(text, h) for h in SKELETON]
        if any(p < 0 for p in positions):
            missing = [h for h, p in zip(SKELETON, positions) if p < 0]
            fails.append(f"missing headings: {missing}")
        elif positions != sorted(positions):
            fails.append("skeleton headings out of order")
        sidebar = heading_pos(text, OPTIONAL)
        if sidebar >= 0 and not (heading_pos(text, "## Do it") < sidebar < heading_pos(text, "## Next time")):
            fails.append("sidebar must sit between Do it and Next time")

        check_it = text[heading_pos(text, "## Check it"):heading_pos(text, "## Do it")]
        if not any(t in check_it for t in TELLS):
            fails.append("Check it names no tell")
        if CLOSING not in check_it:
            fails.append("Check it lacks closing line")
        if part >= "03" and "the verification card from Part 2" not in text:
            fails.append("no reference to the verification card from Part 2")

        for pf in sorted(PROMPTS.glob(f"{part}-*.md")):
            body = prompt_body(pf)
            if not body:
                fails.append(f"{pf.name}: missing 'Where to paste:' first line")
                continue
            if body not in text:
                fails.append(f"{pf.name}: body not embedded verbatim in post")
            if "-stuck-" in pf.name and not body.startswith(STUCK_SENTENCE):
                fails.append(f"{pf.name}: stuck prompt must start with screen sentence")
        if text.count("```text") < 1:
            fails.append("no ```text prompt block")
        if "*Why it's written this way:*" not in text:
            fails.append("no 'Why it's written this way' note")

    if part in NEEDS_SOURCES and heading_pos(text, "## Sources") < 0:
        fails.append("missing ## Sources section")

    if part == "07":
        for pat, name in ((EMAIL, "email"), (PHONE, "phone")):
            if pat.search(text):
                fails.append(f"Part 7 contains a {name}-shaped string")

    if part in {"03", "08"} and "**Don't fear the clear!**" not in text:
        fails.append("missing pull quote")

    if part != "10" and re.search(r"\b(Windows|macOS|Mac)\b", text) and part not in {"02"}:
        fails.append("mentions an OS outside Part 10")

    if FORBIDDEN.exists():
        for line in FORBIDDEN.read_text().splitlines():
            term = line.strip()
            if term and not term.startswith("#") and term.lower() in text.lower():
                fails.append(f"forbidden term present: {term}")
        if "REPLACE-ME" in FORBIDDEN.read_text():
            fails.append("scripts/forbidden.txt still has REPLACE-ME entries")

    if re.match(r"^---\s*\n", text):
        fails.append("frontmatter present")

    if re.search(r"^\|.*\|\s*$", text, re.M):
        fails.append("markdown table present (Medium has no tables)")

    for f in fails:
        print(f"FAIL {post.name}: {f}")
    print(("PASS " if not fails else "FAIL ") + post.name + f" ({words} words)")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1]))
