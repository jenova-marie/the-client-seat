# The Client Seat: banners, repo, and Pages — Design

**Date:** 2026-09-27
**Author:** Jenova (with Claude)
**Status:** approved in conversation, ready for planning
**Builds on:** `2026-09-26-claude-do-everything-series-design.md` (the series spec; still binding for post content)

## 1. Purpose

Give every part of the series a branded banner image that survives the paste into Medium, host those banners at stable public URLs, and rename the series to **The Client Seat**. Medium strips all styling on paste, so the only "header" a reader sees there is the story title plus one image. The banner carries the series identity as a picture.

Decisions already made in conversation:

- Series name: **The Client Seat**. Subtitle: *Learning a real software project with AI as your tutor.*
- Banner: a code-rendered card over one shared AI-generated background, with a subtle per-part hue shift.
- Rendering: Chrome headless screenshot of an HTML/CSS template (no new dependencies).
- Hosting: public GitHub repo `jenova-marie/the-client-seat` (created; initial commit pushed), GitHub Pages from the `main` branch root. Pages serves the banners and an index only; the posts are read on Medium.
- Medium's API is discontinued and this account has no integration-token option, so the paste path stays.
- The project folder is renamed from `claude-do-everything` to `the-client-seat` as the last step.

## 2. What is out of scope

- Publishing the posts themselves on Pages (a later switch, see §9).
- Any change to post content, the prompt library, or the check script's rules.
- Generating the background artwork. The author makes it with the prompt recorded in §5 and drops it in `assets/series-background.png`.

## 3. Privacy and anonymization

The repo is public, so:

- `scripts/forbidden.txt` (real client and repo names) is git-ignored. `scripts/forbidden.example.txt` is committed with the two REPLACE-ME lines. `check-post.py` keeps reading `forbidden.txt`; if it is absent, the script reports that and fails, so a fresh clone cannot silently pass the anonymization check.
- `.superpowers/` (executor ledger, verified-facts notes, fix-pass tests) and `build/` (rendered HTML) are git-ignored.
- The banner text contains only the series name, part number, part title, and "Jenova". No client detail.

## 4. The rename

- `README.md`: H1 becomes `# The Client Seat`; the first paragraph opens with the subtitle. The old series name is removed from the README.
- Part 0's H1 stays `# Part 0: Why I'm making my client learn with AI`; part titles do not change.
- The old name remains in the 2026-09-26 spec and plan as history.
- The banner template and index use the new name.
- Folder: `~/claude/claude-do-everything` → `~/claude/the-client-seat`, last step, after which the author reopens Claude Code in the new path.

## 5. Banner design

**Canvas:** 1600 × 900 PNG (16:9). Medium shows the story image full width and crops feed thumbnails toward the center, so the text block sits on the left third but not in the outer 80 px.

**Layers, bottom to top:**

1. Background: `assets/series-background.png`, full-bleed, `object-fit: cover`. Until the file exists, a CSS gradient in the same palette (dusky magenta → violet → deep teal) stands in; the template picks the image when present.
2. Hue shift: a full-card overlay using `mix-blend-mode` with a hue rotation of `(part × 9)` degrees at low opacity, so twelve banners read as a set with visible variation.
3. Text panel: left third, a translucent dark panel with a soft edge, holding four lines, top to bottom:
   - `THE CLIENT SEAT` in small caps, tracked, sans.
   - `Part N` very large, display serif.
   - The part title (from the post H1 after the colon), display serif, wrapping to at most three lines.
   - `Jenova` small, sans, bottom of the panel.
4. Sparkle: none added by CSS; the artwork carries it.

**Fonts:** two Open Font License families vendored into `assets/fonts/` as `.woff2` with their license files: **Fraunces** (display serif) and **Inter** (sans). Local `@font-face` rules only; no network fetch during render.

**Background prompt (recorded so the art can be regenerated):**

```text
A wide abstract background illustration, 16:9, for a warm and playful tech
tutorial series header. No text, no letters, no logos, no people, no faces,
no hands.

Composition: the LEFT third is calm and low-detail, a soft, slightly darker
area of smooth gradient where a block of text will later be placed. Detail
and light build gently toward the RIGHT side. Keep the whole image soft and
uncluttered; nothing in it should compete with text.

Palette: dusky magenta, violet, and soft peach melting into a deep teal
shadow, with small warm-white sparkles. Rich but not neon. Overall
luminance mid-to-dark so white text reads on top.

Motifs, subtle and abstract, drifting on the right side: a few translucent
index cards or sticky notes at gentle angles, a faint fine grid like graph
paper fading into the gradient, soft bokeh glitter, one or two thin glowing
lines like a connection being drawn between cards. Nothing literal, no
robots, no circuit boards, no brains, no binary digits.

Style: painterly digital illustration with a slight paper-grain texture,
soft edges, smooth gradients, gentle depth of field. Cozy, sparkly, a little
queer-fem-tech-queen glamour, zero corporate stock-photo feeling.

Output: 2048 x 1152 pixels, no border, no vignette frame, no watermark.
```

Negative prompt: `text, letters, watermark, logo, people, faces, hands, robot, circuit board, brain, binary, neon, high contrast, busy, cluttered, frame, border`.

## 6. Files and components

```
the-client-seat/
  index.html                       Pages landing page: series name, subtitle, the twelve banners with their URLs
  assets/
    series-background.png          author-supplied artwork (absent until made; template falls back to gradient)
    banner-template.html           the card: CSS + four placeholders {{SERIES}} {{PART}} {{TITLE}} {{AUTHOR}} {{HUE}} {{BG}}
    banners.json                   manifest generated from post H1s: [{part, title, slug, file}]
    banners/NN-slug.png            twelve rendered banners, committed
    fonts/                         Fraunces and Inter woff2 + OFL licenses
  scripts/
    make-banners.py                builds the manifest from the posts, fills the template, screenshots with Chrome
    check-banners.py               the test: twelve PNGs exist, each 1600×900, manifest titles equal post H1s
    render-for-medium.sh           injects the banner <img> above the H1; pagetitle instead of title
    check-post.py                  unchanged rules; fails clearly when forbidden.txt is missing
```

**`make-banners.py`:**
- Input: the twelve post files (glob `[01]*.md`), `assets/banner-template.html`.
- Reads each H1 `# Part N: Title`, derives `slug` from the post filename (minus `.md`), and writes `assets/banners.json`.
- For each part: fills the template, writes `build/banners/NN.html`, runs
  `"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless=new --disable-gpu --hide-scrollbars --window-size=1600,900 --screenshot=<out> file://<html>` (the Chrome path is a constant with an env override `CHROME_BIN` for other machines).
- Picks `{{BG}}` as the artwork if `assets/series-background.png` exists, else the gradient.
- Exit 1 with a message if Chrome is missing or a screenshot fails.

**`check-banners.py`:** exit 0 only if all twelve PNGs exist, are exactly 1600×900 (Pillow), and `banners.json` titles match the post H1s. This is the task's test.

**`render-for-medium.sh`:** for each post, computes the banner URL `https://jenova-marie.github.io/the-client-seat/assets/banners/<slug>.png`, renders with pandoc using `--metadata pagetitle=`, and inserts `<p><img src="<url>" alt="<title>"></p>` immediately before the first `<h1`. The markdown source stays untouched.

**`index.html`:** static, hand-written, lists the twelve banners in reading order with visible URLs; no scripts, no tracking.

## 7. Data flow

Post H1s → `banners.json` → filled template HTML → Chrome → PNG → committed → Pages URL → injected by the render script → pasted into Medium with the rich text → Medium fetches the image by URL.

## 8. Error handling

- Missing Chrome: `make-banners.py` prints the expected path and the `CHROME_BIN` override, exit 1.
- Missing artwork: gradient fallback, and a one-line notice so the author knows the placeholder rendered.
- Title mismatch between a post and the manifest: `check-banners.py` fails naming the part.
- Missing `scripts/forbidden.txt`: `check-post.py` fails with "copy forbidden.example.txt to forbidden.txt and fill it in."
- Pages not yet enabled: banner URLs 404 until the author turns Pages on; `index.html` links let them verify in a browser.

## 9. Later switch (not built now)

Serving the posts on Pages means committing `build/` or adding a Pages build step. The render script already produces standalone HTML per post; the switch is a workflow file and un-ignoring `build/`. Nothing in this design blocks it.

## 10. Testing and definition of done

- `python3 scripts/check-banners.py` passes: twelve PNGs, correct size, titles match.
- `bash scripts/render-for-medium.sh` produces twelve HTML files whose first body element is the banner image, no `<table>`, no slug title block.
- `for f in 0*.md 1[01]-*.md; do python3 scripts/check-post.py "$f"; done` still passes every rule except the author's REPLACE-ME gate.
- Pages enabled; opening one banner URL in a browser returns the image.
- Folder renamed; author reopens Claude Code in the new folder.

## 11. Order of work

1. README rename.
2. Fonts vendored; template written; generator and its check; twelve banners rendered with the gradient fallback.
3. Render script change; re-render; verify.
4. `index.html`; commit; push; Pages enabled; one URL verified.
5. Folder rename.
