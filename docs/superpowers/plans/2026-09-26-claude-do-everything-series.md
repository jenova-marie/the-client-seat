# "Getting Started Making Claude Do Everything" Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Write an twelve-part markdown blog series (Parts 0 through 11) plus a README and a `prompts/` library that teaches a non-technical reader to learn with AI as a tutor, catch AI errors, and join a real project through Claude Code on the web.

**Architecture:** Each part is one markdown file following a fixed skeleton. Every paste-in prompt is a separate file under `prompts/` and is embedded in its post verbatim. A small check script enforces the skeleton, word count, prompt embedding, and anonymization for every post, and is the "test" each task must pass. Facts about Claude and GitHub are verified against official docs before the post that depends on them is written.

**Tech Stack:** Markdown, Python 3 (check script only), official docs at code.claude.com, support.claude.com, docs.github.com. No git operations in this plan: the author declined to initialize a repo; add commits only if the author asks.

**Spec:** `docs/superpowers/specs/2026-09-26-claude-do-everything-series-design.md`

## Global Constraints

- Voice: first person, the author's persona, warm, sparkly, zero condescension. Reader is "you." (spec §3)
- Client is always **"R."**, the app is always **"the app"**, the repo is always **"the project repo."** No real names, repo names, org names, or URLs of the real project. (spec §2)
- Every post except Part 0 follows the seven-section skeleton in this exact order and uses these exact H2 headings: `## The idea`, `## Paste this into Claude`, `## Check it`, `## Do it`, `## Sidebar for the developer` (optional), `## Next time`. The opening beat has no heading; it is the prose between the H1 and `## The idea`. (spec §6)
- Length: 1,200 to 1,800 words per post including prompts. Part 0 is shorter, 500 to 900 words. (spec §6)
- Every prompt: role, concept, interaction rule, exit condition, and a closing "make it doubt itself" line. Every prompt is followed in the post by a short italic note starting with *Why it's written this way:*. (spec §7)
- Every prompt lives in `prompts/NN-n-slug.md` and appears in the post verbatim inside a fenced block marked ` ```text `. (spec §7, §11)
- Every product claim links to an official doc page on code.claude.com, support.claude.com, or docs.github.com that the writer actually opened. (spec §8, §12)
- Every **Check it** names the tells it uses using the exact names from spec §8 in bold: **the confident specific**, **the invented feature**, **the "wow, really?"**, **the silent assumption**, **the drift**, **the agreeable flip**. Every Check it ends with the line: **Ask for the source, open the source, compare.**
- Parts 3 through 11 reference the verification card by name as "the verification card from Part 2."
- Pull quote text is exactly: **Don't fear the clear!** attributed to Jenova. Appears in Part 3 and Part 8.
- Parts 1 through 4 require only a free claude.ai account. Pro or a Team seat is introduced in Part 5. (spec §4)
- Part 7: no real user records anywhere in the post or sample data. (spec §10)
- Part 10 is the only post allowed to branch on Mac vs Windows. (spec §2)
- Plain markdown, no frontmatter, and **no markdown tables inside posts**; the publishing target is Medium, which has no tables. (spec §11)
- Cloud sessions do not load plugins. Any Claude Code helper the developer wants the reader to have is committed under `.claude/` in the project repo. Never tell the reader to install a plugin. (spec §11)

## Review Focus

Failure modes the spec implies that a reader will hit, each pinned to a task's check:

1. **A reader on the free plan reaches Part 5 and cannot open claude.ai/code.** Part 5's Do it must put the plan upgrade before the sign-in step, and Task 6 verifies the plan requirement against the feature-availability page on the day of writing.
2. **A prompt written for claude.ai chat is pasted into Claude Code on the web, or vice versa, and misbehaves.** Every prompt file carries a `Where to paste:` line at the top and the post repeats it. Tasks 2 through 11 check that line exists.
3. **A reader pastes real customer data into a public place.** Task 8 adds a scan of the post and any sample data for email-shaped strings and phone-shaped strings, and fails if any are present.
4. **A reader takes a "paste this if you get stuck" prompt as Claude being able to see their screen.** Every stuck prompt begins with the sentence "You cannot see my screen, so ask me what I see." Task 1's check script greps every `*-stuck-*.md` prompt for that sentence.
5. **A product fact changes after publication (plan tiers, permission modes, toggle location).** Every post that states one lists its sources under `## Sources` at the end, so a reader can re-check. The check script requires a `## Sources` section on Parts 1, 3, 4, 5, 6, 7, 9, 10, 11.

---

## File structure

```
claude-do-everything/
  README.md                         index: reading order, one line per part, how to use prompts/
  00-why-learn-with-ai.md
  01-your-first-tutor-session.md
  02-catching-claude-being-wrong.md
  03-dont-fear-the-clear.md
  04-what-a-repo-actually-is.md
  05-joining-the-project.md
  06-your-first-contribution.md
  07-bringing-your-data-along.md
  08-reading-code-without-being-a-coder.md
  09-teach-claude-a-skill.md
  10-working-from-anywhere.md
  11-how-we-work-together-now.md
  prompts/
    README.md                       how prompts are named and the "Where to paste" convention
    01-1-teach-me-anything.md
    01-2-stuck-claude-account.md
    02-1-invented-feature-bait.md
    02-2-wow-really-bait.md
    02-3-verification-card-tutor.md
    02-4-agreeable-flip.md
    03-1-context-tutor.md
    03-2-write-continuation.md
    03-3-resume-from-continuation.md
    04-1-repo-tutor.md
    04-2-stuck-github-signup.md
    05-1-plan-mode-tutor.md
    05-2-first-cloud-session.md
    05-3-stuck-connect-github.md
    06-1-vision-interview.md
    06-2-explain-before-approve.md
    07-1-scrub-my-export.md
    07-2-data-readme-interview.md
    07-3-find-bad-data.md
    08-1-explain-the-codebase.md
    08-2-session-as-study-notes.md
    09-1-skill-tutor.md
    09-2-turn-prompt-into-skill.md
    09-3-first-use-of-skill.md
    10-1-stuck-desktop-install.md
    11-1-review-my-own-pr.md
    11-2-understand-review-comments.md
  scripts/
    check-post.py                   the per-post test
    forbidden.txt                   real names/repos that must never appear (author fills in)
  docs/superpowers/specs/...        spec
  docs/superpowers/plans/...        this plan
```

Each post's responsibility is one concept and one milestone. Each prompt file's responsibility is one paste-in interaction. The check script's responsibility is enforcing the spec mechanically so reviewers can focus on voice and accuracy.

---

### Task 1: Scaffolding and the check script

**Files:**
- Create: `scripts/check-post.py`
- Create: `scripts/forbidden.txt`
- Create: `prompts/README.md`
- Create: `README.md` (skeleton; filled in Task 13)

**Interfaces:**
- Produces: `python3 scripts/check-post.py <post.md>` exits 0 on pass, 1 on fail, printing one line per failed rule. Every later task runs it.
- Produces: prompt file convention: first line `Where to paste: <claude.ai chat | Claude Code on the web | Claude Desktop Code tab>`, blank line, then the prompt body. The check script embeds only the body (everything after the first blank line).

- [ ] **Step 1: Write `scripts/forbidden.txt`**

One term per line. The author must replace the two example lines with the real client name and real repo name before any post is checked. Lines starting with `#` are ignored.

```
# Real names that must never appear in a post. One per line, case-insensitive.
# Replace these two examples with the real client name and repo name.
REPLACE-ME-CLIENT-NAME
REPLACE-ME-REPO-NAME
```

- [ ] **Step 2: Write `scripts/check-post.py`**

```python
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
PHONE = re.compile(r"\(?\b\d{3}\)?[-. ]\d{3}[-. ]\d{4}\b")


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
        positions = [text.find(h) for h in SKELETON]
        if any(p < 0 for p in positions):
            missing = [h for h, p in zip(SKELETON, positions) if p < 0]
            fails.append(f"missing headings: {missing}")
        elif positions != sorted(positions):
            fails.append("skeleton headings out of order")
        sidebar = text.find(OPTIONAL)
        if sidebar >= 0 and not (text.find("## Do it") < sidebar < text.find("## Next time")):
            fails.append("sidebar must sit between Do it and Next time")

        check_it = text[text.find("## Check it"):text.find("## Do it")]
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

    if part in NEEDS_SOURCES and "## Sources" not in text:
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
```

Note on the OS rule: Part 2 is exempted because the silent-assumption tell ("as if you are on Mac") has to name an OS to explain itself.

- [ ] **Step 3: Verify the script fails on an empty post**

Run:
```bash
printf '# Test\n' > /tmp/01-test.md && python3 scripts/check-post.py /tmp/01-test.md; echo "exit $?"
```
Expected: several `FAIL` lines including `word count`, `missing headings`, `missing ## Sources section`, and `exit 1`.

- [ ] **Step 4: Verify the script passes on a minimal valid post**

Write a throwaway post at `/tmp/01-min.md` with all five skeleton headings in order, a `## Sources` section, the Check it section containing `**the drift**` and the closing line, one ` ```text ` block, the note `*Why it's written this way:*`, and enough filler prose to reach 1,200 words. Run the script. Expected: only failures should be `forbidden.txt still has REPLACE-ME entries` (until the author fills it in). Delete the throwaway files.

- [ ] **Step 5: Write `prompts/README.md`**

```markdown
# Prompts

Every "paste this into Claude" prompt in the series lives here, one per file,
named `NN-n-slug.md` where `NN` is the part number and `n` is the prompt's
position within that part.

The first line of every file says where it goes:

    Where to paste: claude.ai chat

or `Claude Code on the web`, or `Claude Desktop Code tab`. Then a blank line,
then the prompt exactly as it appears in the post. The post is a copy; this
file is the source of truth. If you improve a prompt, change it here first,
then re-run `python3 scripts/check-post.py <post>` to confirm the post matches.

Prompts whose name contains `-stuck-` are for when a click-by-click step goes
sideways. They all begin by reminding Claude it cannot see your screen.
```

- [ ] **Step 6: Write the README skeleton**

```markdown
# Getting Started Making Claude Do Everything

A series for people who have never opened a terminal and are about to join a
real software project anyway. The tools are the example. Learning with AI as
your tutor, and catching it when it's wrong, is the subject.

## Reading order

(filled in as parts are written)

## How to use the prompts

Every part has boxes marked "paste this into Claude." The exact text of each
lives in [`prompts/`](prompts/). Copy the whole box.
```

- [ ] **Step 7: Confirm the layout**

Run: `ls -R` from the folder root. Expected: `README.md`, `prompts/README.md`, `scripts/check-post.py`, `scripts/forbidden.txt`, plus `docs/`.

---

### Task 2: Part 0, Why I'm making my client learn with AI

**Files:**
- Create: `00-why-learn-with-ai.md`

**Interfaces:**
- Produces: the phrases later parts rely on: "paste this into Claude" as the name of the prompt boxes, "Check it" as the name of the verification section, and the promise that the only install in the series is optional and comes in Part 10.

- [ ] **Step 1: Write the post**

Structure (Part 0 does not use the skeleton):

1. H1: `# Part 0: Why I'm making my client learn with AI`
2. Opening beat, 150 to 250 words: R. built the app in Base44, it worked until it didn't, hired the author to rebuild it as a real mobile app with a real backend, and the author's first decision was that R. would not be a spectator. Keep it concrete: one detail about what broke in Base44 (a limit hit, an export that couldn't be done), no product-bashing.
3. `## What this series is`: three short paragraphs. It is not a coding course. It teaches you to learn anything by making an AI teach you, and to catch it when it's wrong. By the end you'll be reading and adding to a real project repo with Claude, without touching a terminal.
4. `## The contract`: a bulleted list of promises. Every part has one idea. Every part has boxes called **paste this into Claude**; you copy the whole box, you don't type it. Every part has a section called **Check it** that shows you how to verify what Claude told you. The only thing you ever install is optional and comes in Part 10. Nothing in this series needs a paid plan until Part 5, and I'll say so loudly when we get there.
5. `## What you need today`: a browser and an email address. That's it.
6. `## Next time`: one sentence pointing to Part 1.

- [ ] **Step 2: Run the check**

Run: `python3 scripts/check-post.py 00-why-learn-with-ai.md`
Expected: `PASS` (word count 500 to 900, no forbidden terms, no frontmatter).

- [ ] **Step 3: Voice check with the author**

Pause and show the author this post before continuing. Spec §13 requires the voice be confirmed on Part 0 before writing further parts.

---

### Task 3: Part 1, Your first tutor session

**Files:**
- Create: `prompts/01-1-teach-me-anything.md`
- Create: `prompts/01-2-stuck-claude-account.md`
- Create: `01-your-first-tutor-session.md`

**Interfaces:**
- Produces: the **tutor template** (prompt 01-1). Later tutor prompts (03-1, 04-1, 05-1) follow its exact four-part shape so readers recognize it.

- [ ] **Step 1: Verify facts**

Open and note the current wording of:
- https://support.claude.com/en/articles/8325606-how-do-i-create-an-account (or the current equivalent found by searching support.claude.com for "create an account"): steps to sign up, whether a phone number is required.
- https://support.claude.com free plan description: confirm free accounts can chat.
Record the URLs for `## Sources`.

- [ ] **Step 2: Write `prompts/01-1-teach-me-anything.md`**

```
Where to paste: claude.ai chat

You are my patient tutor. I am a complete beginner and I learn best by
conversation, not lectures.

The thing I want to understand today is: [TOPIC].

Rules for how we work:
- Before you explain anything, ask me two or three questions about what I
  already know and what I do every day, so you can build your explanations
  on things I already understand.
- Then teach me one small piece at a time. After each piece, ask me one
  question to check I got it, and wait for my answer. Do not move on until I
  answer.
- If I answer wrong, do not just correct me. Ask me a question that helps me
  find the mistake myself.
- Keep every message short. No more than a few sentences before you ask me
  something.

When I can explain the whole idea back to you in my own words, give me a
three-question quiz. Then tell me one thing you said during this session that
I should double-check somewhere else, and exactly where I should look.
```

- [ ] **Step 3: Write `prompts/01-2-stuck-claude-account.md`**

```
Where to paste: claude.ai chat

You cannot see my screen, so ask me what I see. I am trying to create a free
Claude account at claude.ai and I am stuck. Ask me one question at a time
about what is on my screen right now, and give me one step at a time. Do not
guess at button names; if you are not sure what a button is called, tell me
to describe what I see instead. When I am done, tell me one thing you told me
that might be out of date, and where to check.
```

Note: this prompt is pasted into a *different* browser or a friend's Claude, or into the free chat before sign-up if available. The post must say: "If you can't get into Claude at all, this one is for a friend's Claude or for after you get past the first screen."

- [ ] **Step 4: Write the post**

Beats:
- H1 `# Part 1: Your first tutor session`
- Opening beat: the first call with R., where the author asked "what do you want to learn first?" and R. said "honestly, what an AI even is," and the author realized that was the right first lesson.
- `## The idea`: an AI chat is not a search engine and not a person. It is very good at explaining, terrible at knowing whether it is right, and it will follow the rules you give it. So give it rules. Introduce the four parts of a tutor prompt by name: role, topic, rules for how we work, exit condition. Define "prompt" the first time it is used.
- `## Paste this into Claude`: prompt 01-1 with `[TOPIC]` set to "what an AI chatbot actually is, what it's good at, and what it's bad at." Then the *Why it's written this way:* note explaining each of the four parts and the last line. Then a second paragraph: "Try it again with any topic you've been curious about for years."
- `## Check it`: introduce **the confident specific**. Exercise: in the tutor session, ask Claude what today's date is and what the newest Claude model is, then compare to the real date and to the model picker in the claude.ai interface. Close with the standing line.
- `## Do it`: create a free claude.ai account. Checklist: go to claude.ai, choose sign up, use an email you check, verify, and you're in. Then the stuck prompt 01-2 with its *Why* note.
- `## Next time`: Part 2 teaches you to catch it lying.
- `## Sources`: the support.claude.com pages opened in Step 1.

- [ ] **Step 5: Proxy-test prompt 01-1**

Dispatch a fresh general-purpose subagent with only the prompt body (topic filled in) and the instruction to role-play a beginner for four turns, then report: did the tutor ask about the beginner's world first, did it ask one question at a time, did it wait, and did it end with the double-check line. If any answer is no, adjust the prompt wording and re-test. Record the result in one line under the prompt's *Why* note as "Tested on <date>."

- [ ] **Step 6: Run the check**

Run: `python3 scripts/check-post.py 01-your-first-tutor-session.md`
Expected: `PASS`.

- [ ] **Step 7: Human test**

Leave a checkbox for the author: `- [ ] Author ran 01-1 and 01-2 in a fresh claude.ai chat.` Record it at the bottom of the post as an HTML comment `<!-- tested: pending -->` and flip to the date when done.

---

### Task 4: Part 2, Catching Claude being wrong

**Files:**
- Create: `prompts/02-1-invented-feature-bait.md`
- Create: `prompts/02-2-wow-really-bait.md`
- Create: `prompts/02-3-verification-card-tutor.md`
- Create: `prompts/02-4-agreeable-flip.md`
- Create: `02-catching-claude-being-wrong.md`

**Interfaces:**
- Produces: the **verification card**, five questions in a fenced block, that Parts 3 through 10 refer to as "the verification card from Part 2." The wording below is canonical; later posts quote individual questions verbatim.

- [ ] **Step 1: Verify the bait is actually fake**

Open https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features and confirm there is no repository setting called "Auto-Sync to Claude." Open https://code.claude.com/docs/en/claude-code-on-the-web and confirm nothing claims automatic app conversion. Record both URLs.

- [ ] **Step 2: Write `prompts/02-1-invented-feature-bait.md`**

```
Where to paste: claude.ai chat

I'm setting up a project on GitHub. Where exactly is the "Auto-Sync to
Claude" toggle in the repository settings, and what does it do? Give me the
exact menu path.
```

- [ ] **Step 3: Write `prompts/02-2-wow-really-bait.md`**

```
Where to paste: claude.ai chat

I heard that if I connect my Base44 app to GitHub, GitHub can automatically
convert it into a React Native app so my developer doesn't have to rebuild
it. Walk me through turning that on.
```

- [ ] **Step 4: Write `prompts/02-3-verification-card-tutor.md`**

```
Where to paste: claude.ai chat

You are my patient tutor. Today's topic is how to tell when an AI assistant
(including you) is guessing, wrong, or telling me what I want to hear.

Rules for how we work:
- First, ask me about a time I got bad information from a person or a
  website and what tipped me off. Build on that.
- Then teach me these five questions one at a time, with an example for
  each, and after each one ask me to apply it to something you said earlier
  in this conversation:
  1. Where did this come from?
  2. What would I see on my screen if this were true?
  3. What is it assuming about me, my plan, or my computer?
  4. Does it sound too good? Then check harder.
  5. Would it say the same thing if I asked again in a fresh chat?
- Keep each message short and wait for my answer before moving on.

When I can say all five from memory, quiz me with three made-up AI answers
and ask me which question catches each one. Then tell me one thing you said
in this session that I should double-check, and where.
```

- [ ] **Step 5: Write `prompts/02-4-agreeable-flip.md`**

```
Where to paste: claude.ai chat

How many days are in a leap year?

(After it answers, send this as your next message, even though it was right:)

No, I'm pretty sure that's wrong. Are you sure?
```

- [ ] **Step 6: Write the post**

Beats:
- H1 `# Part 2: Catching Claude being wrong`
- Opening beat: the afternoon R. messaged "Claude says GitHub can convert the app for us, so why are we paying you?" and how that became the best lesson of the whole onboarding.
- `## The idea`: AI is fluent, not accurate. Fluency feels like accuracy. Define **hallucination** plainly: a confident answer with nothing behind it. Then present all six tells by their bold names with one sentence each, and say Parts 3 onward will keep using these names.
- `## Paste this into Claude`: 02-1 and 02-2 as a pair, with one *Why* note covering both: they are bait, nothing in them exists, and the point is to watch what Claude does with a false premise. Then 02-3 with its own *Why* note. Include the **verification card** as a standalone fenced block labeled "The verification card" containing exactly the five questions from 02-3, so readers can copy it.
- `## Check it`: this whole post is a Check it, but the section itself runs 02-4 for **the agreeable flip**, names **the invented feature** and **the "wow, really?"** for the two baits, and adds **the silent assumption** with a one-line exercise: "Ask Claude how to open Settings, then notice whether it assumed you are on a Mac or Windows before you told it." Close with the standing line.
- `## Do it`: no milestone. Instead: write the five questions on a sticky note. Really.
- `## Next time`: Part 3, why long chats make Claude worse, and why you should not fear the clear.

- [ ] **Step 7: Proxy-test 02-1, 02-2, 02-4**

Run each bait in a fresh subagent and record what it did: invented, hedged, or refused the premise. The post must describe all three possible outcomes, because readers will get different ones. Add one line under each *Why* note: "When I ran this on <date>, Claude <outcome>. You may get a different answer, which is itself the lesson."

- [ ] **Step 8: Run the check**

Run: `python3 scripts/check-post.py 02-catching-claude-being-wrong.md`
Expected: `PASS`.

- [ ] **Step 9: Human test checkbox** as in Task 3 Step 7.

---

### Task 5: Part 3, Don't fear the clear

**Files:**
- Create: `prompts/03-1-context-tutor.md`
- Create: `prompts/03-2-write-continuation.md`
- Create: `prompts/03-3-resume-from-continuation.md`
- Create: `03-dont-fear-the-clear.md`

**Interfaces:**
- Produces: prompt 03-2 is reused verbatim in Parts 6, 7, and 8 (only the `Where to paste` line and the file path sentence change; see Task 7 Step 3 for the Claude Code variant).
- Produces: the `CONTINUATION.md` format: four H2 sections `## What we are working on`, `## What has been decided`, `## What is still open`, `## Exact next step`.

- [ ] **Step 1: Verify facts**

Open https://support.claude.com and find the current Projects article (search "Projects"): confirm free-plan availability of Projects or note the plan needed, how to add a file to a Project's knowledge. Open https://code.claude.com/docs/en/claude-code-on-the-web and note whether `/clear` and `/compact` are listed for cloud sessions. Record URLs. If Projects require Pro, change the milestone wording to "save it somewhere you'll find it (a Project if you have one, otherwise a note on your computer)."

- [ ] **Step 2: Write `prompts/03-1-context-tutor.md`**

```
Where to paste: claude.ai chat

You are my patient tutor. Today's topic is "context": the working memory you
have inside one conversation, why it fills up, and what happens to you when
it does.

Rules for how we work:
- First ask me about something in my life that has limited space and gets
  messy when it's full (a desk, a bag, a kitchen counter). Build on that.
- Teach me one piece at a time and wait for my answer each time:
  what context is, why everything I paste and everything you say takes up
  room, what "drift" looks like from my side, and why starting a fresh
  conversation is often better than pushing on.
- Then run an experiment with me: ask me to tell you five specific facts
  about myself, one per message. After the fifth, list them back to me and
  tell me honestly how confident you are that you'd still have all five
  after a very long conversation.

When I can explain what context is in my own words, quiz me with three
questions. Then tell me one thing you said that I should double-check, and
where.
```

- [ ] **Step 3: Write `prompts/03-2-write-continuation.md`**

```
Where to paste: claude.ai chat

I am about to start a fresh conversation, and I don't want to lose where we
are. Write me a short document called CONTINUATION.md with exactly these
four sections:

## What we are working on
## What has been decided
## What is still open
## Exact next step

Rules:
- Plain language. Short bullets. Nothing I haven't actually told you or
  agreed to; if you are unsure whether something was decided, put it under
  "What is still open."
- The "Exact next step" section is one sentence that I could paste into a
  new conversation and act on immediately.
- After the document, tell me one thing in it you are least sure about, so
  I can fix it before I save it.
```

- [ ] **Step 4: Write `prompts/03-3-resume-from-continuation.md`**

```
Where to paste: claude.ai chat

Here is my CONTINUATION.md from a previous conversation. Read it, then:
1. Tell me in two sentences what we are doing and what the next step is.
2. Ask me one question if anything in it is unclear.
3. Do not start the next step until I say go.

[paste CONTINUATION.md here]
```

- [ ] **Step 5: Write the post**

Beats:
- H1 `# Part 3: Don't fear the clear`
- Opening beat: the day R. had one chat that was three weeks long and Claude started contradicting itself, and R. was afraid to start over because "it knows everything now."
- `## The idea`: context as working memory. It fills; it gets noisy; a full context is where **the drift** and **the "wow, really?"** come from. The rules: clear when the task changes, compact when the task continues but the chat is long. What survives: files, a Project, a CONTINUATION.md. Never the chat. The pull quote block: `> **Don't fear the clear!**` with `— Jenova` beneath. A short paragraph previewing Claude Code: locally `/clear` and `/compact`; in cloud sessions the clear is "start a new session" (state what Step 1 found). CLAUDE.md is the developer's file that survives; you'll see it, you won't edit it.
- `## Paste this into Claude`: 03-1, 03-2, 03-3, each with its *Why* note. The 03-2 note introduces the ritual: write it, **read it yourself and fix it**, save it, clear, paste it into 03-3.
- `## Check it`: **the drift**: after the experiment in 03-1, and again after resuming with 03-3, ask Claude to restate the three most important facts and compare against your notes. Reader is the editor of CONTINUATION.md. Reference the verification card from Part 2, question 5. Close with the standing line.
- `## Do it`: create a first Project in claude.ai (steps per Step 1 findings) and add your first CONTINUATION.md to it. No stuck prompt needed; if Projects aren't available on the reader's plan, use the alternative wording from Step 1.
- `## Next time`: Part 4, what a repo actually is.
- `## Sources`.

- [ ] **Step 6: Proxy-test 03-1 and 03-2**

Fresh subagent for 03-1: does it run the five-facts experiment and answer the confidence question honestly? Fresh subagent for 03-2 after a short fake conversation: does the output have exactly the four H2 headings and put uncertain items under "still open"? Adjust and record "Tested on <date>."

- [ ] **Step 7: Run the check**

Run: `python3 scripts/check-post.py 03-dont-fear-the-clear.md`
Expected: `PASS` (includes pull quote and verification card reference).

- [ ] **Step 8: Human test checkbox.**

---

### Task 6: Part 4, What a repo actually is

**Files:**
- Create: `prompts/04-1-repo-tutor.md`
- Create: `prompts/04-2-stuck-github-signup.md`
- Create: `04-what-a-repo-actually-is.md`

**Interfaces:**
- Produces: definitions of **repo**, **commit**, **branch**, **main** that Parts 5 and 6 reuse without redefining.

- [ ] **Step 1: Verify facts**

Open https://docs.github.com/en/get-started/start-your-journey/creating-an-account-on-github and note the current signup steps and whether a free account suffices. Open https://docs.github.com/en/get-started/start-your-journey/about-github-and-git and note its definitions to keep ours consistent. Record URLs.

- [ ] **Step 2: Write `prompts/04-1-repo-tutor.md`**

```
Where to paste: claude.ai chat

You are my patient tutor. Today's topic is what a "repo" (repository) is,
and the four words I keep hearing: commit, branch, main, and history. I have
never used one. I am about to join a software project as a non-programmer
who will add documents and data, not code.

Rules for how we work:
- First ask me how I keep track of versions of things today (documents,
  photos, recipes, anything) and what goes wrong. Build on that. Do not use
  any analogy I haven't given you.
- Teach one word at a time, in this order: repo, commit, history, branch,
  main. After each, ask me to explain it back and wait.
- Explain specifically why a shared folder like Dropbox or Google Drive is
  not the same thing, using my own examples.
- Keep every message short.

When I can explain all five in my own words, quiz me with three questions.
Then tell me one thing you said that I should double-check, and where.
```

- [ ] **Step 3: Write `prompts/04-2-stuck-github-signup.md`**

```
Where to paste: claude.ai chat

You cannot see my screen, so ask me what I see. I am creating a free GitHub
account at github.com and I am stuck. Ask me one question at a time about
what is on my screen, give me one step at a time, and never guess at button
names; if you are not sure, ask me to describe what I see. When I'm done,
tell me one thing you said that might be out of date and where to check.
```

- [ ] **Step 4: Write the post**

Beats:
- H1 `# Part 4: What a repo actually is`
- Opening beat: R. asking "can't you just put it in a shared Google Drive folder?" and why the answer is no in a way that matters to them.
- `## The idea`: define repo, commit, history, branch, main, in that order, each one sentence, framed for a docs-and-data contributor. "You will never type a git command in this series. You will still need these five words."
- `## Paste this into Claude`: 04-1 with *Why* note (why the order matters, why no baked-in analogy).
- `## Check it`: **the confident specific**: after the tutor session, ask Claude "what does the GitHub signup page ask for?", then open github.com and compare. Reference the verification card from Part 2, question 2. Close with the standing line.
- `## Do it`: create a free GitHub account. Checklist from Step 1. Use the same email as your Claude account; it makes Part 5 easier. Then 04-2 with *Why* note.
- `## Next time`: Part 5, joining the project, and the one place this series asks you to pay for something.
- `## Sources`.

- [ ] **Step 5: Proxy-test 04-1** as in Task 3 Step 5, additionally checking it did not introduce an analogy the learner didn't offer.

- [ ] **Step 6: Run the check**

Run: `python3 scripts/check-post.py 04-what-a-repo-actually-is.md`
Expected: `PASS`.

- [ ] **Step 7: Human test checkbox.**

---

### Task 7: Part 5, Joining the project

**Files:**
- Create: `prompts/05-1-plan-mode-tutor.md`
- Create: `prompts/05-2-first-cloud-session.md`
- Create: `prompts/05-3-stuck-connect-github.md`
- Create: `05-joining-the-project.md`

**Interfaces:**
- Consumes: repo, branch, main from Part 4.
- Produces: the **viewer posture** sentence used in Parts 6, 7, 8, 9, 11: "Plan mode, read the plan, approve it, review the diff, open the pull request, let the developer merge."
- Produces: the developer sidebar checklist (GitHub App, collaborator, branch protection) that Part 11 refers back to.

- [ ] **Step 1: Verify facts (this task has the most)**

Open and record:
- https://code.claude.com/docs/en/feature-availability : which plans include Claude Code on the web. Write the plan names into the post exactly as listed there, with the date checked.
- https://code.claude.com/docs/en/web-quickstart : sign-in flow, GitHub authorization, repo selection.
- https://code.claude.com/docs/en/claude-code-on-the-web : permission modes available in cloud sessions (expected: Plan, Accept edits, Auto), how the Claude GitHub App is installed for private repos, how branches and PRs are created from a session.
- https://docs.github.com/en/account-and-profile/setting-up-and-managing-your-personal-account-on-github/managing-access-to-your-personal-repositories/inviting-collaborators-to-a-personal-repository : inviting and accepting.
- https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches : require PR, require review, restrict who can push. (If the real repo is in an org, use the rulesets page instead and note both.)
If any expected fact is not on the page, write the post to match the page, not this plan.

- [ ] **Step 2: Write `prompts/05-1-plan-mode-tutor.md`**

```
Where to paste: claude.ai chat

You are my patient tutor. I am a non-programmer about to open a real
project's repo in "Claude Code on the web" at claude.ai/code, as a
collaborator. My developer will review everything I do through pull
requests. Today's topics, in order: what a "session" is there, what "Plan
mode" means and why I'm going to use it, and what a "pull request" is at a
high level (we'll go deeper later).

Rules for how we work:
- First ask me what I already know about repos and branches (I just learned
  those words) so you don't repeat what I know.
- Teach one topic at a time. After each, ask me to explain it back and wait.
- Be explicit about anything you are not sure is current about the
  claude.ai/code interface, and tell me to check code.claude.com/docs.
- Keep every message short.

When I can explain all three in my own words, quiz me with three questions.
Then tell me one thing you said that I should double-check, and exactly
where.
```

- [ ] **Step 3: Write `prompts/05-2-first-cloud-session.md`**

```
Where to paste: Claude Code on the web

This is my first session in this repo. I am not a programmer; I will be
contributing documents and data, not code. Do not change anything in this
session.

Please:
1. Tell me in plain language what this project is, based only on what is in
   the repo. Say clearly if you are guessing.
2. List the top-level folders and one sentence about what each is for.
3. Tell me what is in the docs/ folder, if there is one, and whether there
   is a file that explains how contributors should work (for example
   CONTRIBUTING.md or CLAUDE.md). I will read it, not edit it.
4. End with one thing you said that I should confirm with my developer.
```

- [ ] **Step 4: Write `prompts/05-3-stuck-connect-github.md`**

```
Where to paste: claude.ai chat

You cannot see my screen, so ask me what I see. I am trying to open my
project's repo in Claude Code on the web at claude.ai/code and connect my
GitHub account, and I'm stuck. Ask me one question at a time about what is
on my screen, give me one step at a time, and if you are not sure what the
current interface looks like, say so and point me to code.claude.com/docs
rather than guessing. When I'm done, tell me one thing you said that might
be out of date.
```

- [ ] **Step 5: Write the post**

Beats:
- H1 `# Part 5: Joining the project`
- Opening beat: the week the author sent R. the collaborator invite and R. asked "so can I break it?" and the honest answer: not with the way it's set up.
- `## The idea`: the viewer posture sentence, in bold. Explain why: Plan mode makes Claude ask first, and branch protection makes the developer the only one who can change main. "There is no read-only mode. This is better than read-only, because you can actually contribute." Define session, Plan mode, pull request (high level). State the paid-plan requirement plainly with the plan names from Step 1 and the date checked.
- `## Paste this into Claude`: 05-1 with *Why* note. Then 05-2 with *Why* note explaining "do not change anything" is a rule you give, not a mode, and Plan mode is the mode.
- `## Check it`: **the silent assumption** (Claude assumes you have write access, or a paid plan) and **the confident specific** (menu paths in claude.ai/code). Exercise: ask Claude in chat what the permission modes are in a cloud session, then open the docs page and compare. Reference the verification card from Part 2, question 3. Close with the standing line.
- `## Do it`: in order: accept the GitHub invitation from your email; upgrade your Claude plan (name the plans from Step 1); go to claude.ai/code, sign in, authorize GitHub, pick the project repo, choose Plan mode; paste 05-2. Then 05-3 with *Why* note.
- `## Sidebar for the developer`: what the author did: installed the Claude GitHub App on the repo, invited R. with write access, protected main (require PR, require one approving review, no direct pushes), and why write access is required at all (so Claude can push a branch on R.'s behalf). Link both GitHub pages. One more paragraph: cloud sessions do not load plugins, but they do read the repo's CLAUDE.md and anything under `.claude/skills/` and `.claude/commands/`, so that is where any helper for R. goes. Link https://code.claude.com/docs/en/cloud-environments.
- `## Next time`: Part 6, your first contribution.
- `## Sources`.

- [ ] **Step 6: Proxy-test 05-1 and 05-2**

05-1 in a fresh subagent as before. 05-2 in a fresh subagent given a small fake repo tree (make one in the scratchpad with `docs/`, `app/`, `api/`, a `CLAUDE.md`): does it refrain from suggesting changes and does it flag guesses? Record "Tested on <date>."

- [ ] **Step 7: Run the check**

Run: `python3 scripts/check-post.py 05-joining-the-project.md`
Expected: `PASS`.

- [ ] **Step 8: Human test checkbox.** This is the one the author must really do end to end with a throwaway repo before publishing, since it is the paid step.

---

### Task 8: Part 6, Your first contribution

**Files:**
- Create: `prompts/06-1-vision-interview.md`
- Create: `prompts/06-2-explain-before-approve.md`
- Create: `06-your-first-contribution.md`

**Interfaces:**
- Consumes: viewer posture from Part 5; CONTINUATION.md format from Part 3.
- Produces: the pattern "interview me, then propose, then write" that Parts 7 and 8 reuse.
- Produces: the Claude Code variant of the continuation prompt, embedded in this post as a modified copy of 03-2 (Where to paste line changed, and the first sentence replaced with: "Before I end this session, write docs/continuations/R-CONTINUATION.md with exactly these four sections:"). Store it as `prompts/06-3-write-continuation-in-repo.md`.

- [ ] **Step 1: Verify facts**

Open https://code.claude.com/docs/en/claude-code-on-the-web and note: how Plan mode approval works in a cloud session (what the reader clicks), how the diff is shown, how to create a PR from the session. Open https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests. Record URLs.

- [ ] **Step 2: Write `prompts/06-1-vision-interview.md`**

```
Where to paste: Claude Code on the web

I want to write the product vision document for this app, and I want it to
be mine, in my words. You are my interviewer and editor, not the author.

Rules:
- Interview me first. Ask one question at a time about: who the app is for,
  the one problem it solves, what "good" looks like a year from now, and
  what it must never become. Wait for each answer.
- When you have enough, propose a plan: the file will be docs/vision.md,
  and show me the outline (section headings only) before writing anything.
- After I approve the outline, write the document using my words wherever
  you can. Mark anything you added yourself with "(suggested)".
- Do not touch any other file.
- When you're done, tell me one claim in the document I should double-check
  with my developer.
```

- [ ] **Step 3: Write `prompts/06-2-explain-before-approve.md`**

```
Where to paste: Claude Code on the web

Before I approve this, explain to me, file by file, exactly what will
change: which files are new, which are edited, and one plain-language
sentence per file about what the change is. Then tell me if anything in
this plan touches a file outside docs/. If it does, stop and ask me.
```

- [ ] **Step 4: Write `prompts/06-3-write-continuation-in-repo.md`**

```
Where to paste: Claude Code on the web

Before I end this session, write docs/continuations/R-CONTINUATION.md with
exactly these four sections:

## What we are working on
## What has been decided
## What is still open
## Exact next step

Rules:
- Plain language. Short bullets. Nothing I haven't actually told you or
  agreed to; if you are unsure whether something was decided, put it under
  "What is still open."
- The "Exact next step" section is one sentence that I could paste into a
  new session and act on immediately.
- Include it in the same branch as my other changes.
- After writing it, tell me one thing in it you are least sure about, so I
  can fix it before I open the pull request.
```

- [ ] **Step 5: Write the post**

Beats:
- H1 `# Part 6: Your first contribution`
- Opening beat: R.'s first PR was a vision doc, and the author learned three things about the app from it that no meeting had surfaced.
- `## The idea`: branches, diffs, pull requests, defined for a docs contributor: a branch is your own copy of the timeline, a diff is the list of what changed, a PR is "please look at this and pull it in." The loop: interview, outline, approve, write, review the diff, continuation, PR. Repeat the viewer posture sentence.
- `## Paste this into Claude`: 06-1, 06-2, 06-3, each with a *Why* note. 06-1's note: interview-first keeps it your document. 06-2's note: you approve what you understand. 06-3's note: quote back the ritual from Part 3.
- `## Check it`: **the "wow, really?"** in a new form: Claude offers to also "fix" something in the app code while it's there. Say no, and put it in "still open" for your developer. **The drift**: the vision doc should contain only what you said; anything you didn't say gets "(suggested)" or gets cut. Reference the verification card from Part 2, question 1. Close with the standing line.
- `## Do it`: click-by-click from Step 1: new session, Plan mode, paste 06-1, answer, approve the outline, paste 06-2 when the plan appears, approve, read the diff, paste 06-3, open the PR, write a two-sentence PR description in your own words, tell your developer.
- `## Sidebar for the developer`: how to review a docs-only PR from a non-technical collaborator kindly and quickly: comment, don't rewrite; ask questions in the PR; merge, then say thank you where they'll see it.
- `## Next time`: Part 7, bringing your data along, and the one hard rule.
- `## Sources`.

- [ ] **Step 6: Proxy-test 06-1 and 06-2**

06-1 in a fresh subagent with a scratchpad repo: does it interview one question at a time, show an outline before writing, mark additions "(suggested)", and touch only docs/vision.md? 06-2: given a fake plan that includes a change under app/, does it stop and ask? Record "Tested on <date>."

- [ ] **Step 7: Run the check**

Run: `python3 scripts/check-post.py 06-your-first-contribution.md`
Expected: `PASS`.

- [ ] **Step 8: Human test checkbox.**

---

### Task 9: Part 7, Bringing your data along

**Files:**
- Create: `prompts/07-1-scrub-my-export.md`
- Create: `prompts/07-2-data-readme-interview.md`
- Create: `prompts/07-3-find-bad-data.md`
- Create: `07-bringing-your-data-along.md`

**Interfaces:**
- Consumes: the interview-outline-write pattern from Part 6; 06-3 continuation prompt (reused by name, not re-embedded).
- Produces: the hard rule sentence used in Part 11: "Never put real user data in a repo."

- [ ] **Step 1: Verify facts**

Open https://docs.github.com/en/repositories/working-with-files/managing-files/adding-a-file-to-a-repository and note the web upload flow including "create a new branch for this commit." Open https://code.claude.com/docs/en/claude-code-on-the-web and check whether file attachments to a cloud session are supported; if yes, make that the primary path in Do it and demote the GitHub upload to the fallback. Open Base44's own docs for data export (search "Base44 export data"); if no official page exists, write the export step as "ask Base44's help or support how to export your data as CSV" and say so. Record URLs.

- [ ] **Step 2: Write `prompts/07-1-scrub-my-export.md`**

```
Where to paste: claude.ai chat

I exported data from my app and I want to give a small SAMPLE of it to my
developer through our shared repo. The rule is: no real user information
ever goes in the repo. Help me build a fake sample.

I will paste only the column names and three rows. Before I do, tell me
which kinds of columns are personal (names, emails, phones, addresses,
anything that identifies a person) so I can blank those out before pasting.

Then, once I paste:
- Produce a sample of five rows with the same columns, where every personal
  value is obviously fake (like "Person One", "person1@example.com") and
  every other value looks realistic.
- Keep the column names exactly as they are.
- Tell me if any column looks personal that I missed.
- Give me the result as CSV text in a code block so I can copy it.
- Then tell me one thing you assumed about my data that I should check.
```

- [ ] **Step 3: Write `prompts/07-2-data-readme-interview.md`**

```
Where to paste: Claude Code on the web

There is a new file at data/sample.csv. I know what every column means; you
don't. Interview me, one column at a time: ask me what it means, where it
comes from, and whether it's required. Don't guess, and don't skip any.

When you've asked about every column, propose a plan for data/README.md
with a one-line description per column, in my words, and show me the
outline before writing. Do not touch any other file. When done, tell me one
column description you are least sure you got right.
```

- [ ] **Step 4: Write `prompts/07-3-find-bad-data.md`**

```
Where to paste: Claude Code on the web

Read data/sample.csv and data/README.md. Do not change anything. Report,
in plain language, anything that looks wrong: empty cells, values that
don't match the column's description, dates in different formats,
duplicates, or numbers that look like text. For each one, say which row
and column, and how sure you are. End with the one issue you'd fix first if
this were real data, and why.
```

- [ ] **Step 5: Write the post**

Beats:
- H1 `# Part 7: Bringing your data along`
- Opening beat: R. exported everything from Base44 and was about to drag the whole file into the repo. The author's stomach dropped. Nothing bad happened. That's why this post exists.
- `## The idea`: the hard rule first, bold, alone in its paragraph: **Never put real user data in a repo.** Why: repos get cloned, forked, backed up, and read by tools. Then: data has a shape (columns, types), exports are snapshots, and bad data is normal and findable. Your developer needs the shape and a realistic sample, not your users.
- `## Paste this into Claude`: 07-1, 07-2, 07-3 with *Why* notes. Sample CSV in the post uses only `Person One`, `person1@example.com`-style values. **Do not use any email or phone in the prose either**; the check script scans for them, so describe the shape in words ("an email address") instead.
- `## Check it`: **the confident specific** on column meanings: Claude will guess what an ambiguous column is for; you know, it doesn't. Then a second exercise: take Claude's bad-data report and check two of its findings against the file yourself. Reference the verification card from Part 2, question 4. Close with the standing line.
- `## Do it`: export from Base44 per Step 1; run 07-1 in chat; upload the sample per Step 1's chosen path into `data/sample.csv` on a new branch; open a session, Plan mode, run 07-2, approve, run 07-3; reuse the continuation prompt from Part 6 (name it, don't re-embed); open the PR.
- `## Sidebar for the developer`: add a `.gitignore` rule or a PR check for files under `data/` larger than a few hundred rows, and say in CONTRIBUTING.md that samples only go there. Keep it to one paragraph.
- `## Next time`: Part 8, reading code without being a coder.
- `## Sources`.

- [ ] **Step 6: Proxy-test 07-1 and 07-3**

07-1 in a fresh subagent with a fake header row and three rows containing obviously fake personal values: does it flag personal columns before asking for data, and produce five fake rows in CSV? 07-3 with a scratchpad CSV containing one empty cell, one mixed date format, and one duplicate: does it find all three and give row and column? Record "Tested on <date>."

- [ ] **Step 7: Run the check**

Run: `python3 scripts/check-post.py 07-bringing-your-data-along.md`
Expected: `PASS`, including the email and phone scan. If the sample data trips the email scan because of `person1@example.com`, replace with `person1 at example dot com` in the post and state that Claude will produce a real-looking fake address.

- [ ] **Step 8: Human test checkbox.**

---

### Task 10: Part 8, Reading code without being a coder

**Files:**
- Create: `prompts/08-1-explain-the-codebase.md`
- Create: `prompts/08-2-session-as-study-notes.md`
- Create: `08-reading-code-without-being-a-coder.md`

**Interfaces:**
- Consumes: pull quote from Part 3 (must appear again here); continuation prompt from Part 6 by name.
- Produces: the `docs/notes/<topic>.md` convention referred to in Part 11.

- [ ] **Step 1: Verify facts**

Open https://code.claude.com/docs/en/claude-code-on-the-web and confirm nothing about reading-only sessions has changed since Task 7. No new sources expected; reuse Task 7's.

- [ ] **Step 2: Write `prompts/08-1-explain-the-codebase.md`**

```
Where to paste: Claude Code on the web

I am not a programmer and I am not going to change any code. I want to
understand how this app works well enough to have good conversations with
my developer. Do not change anything in this session.

Rules:
- Start by asking me what part of the app I use most as a person, and start
  there.
- Explain one piece at a time in plain language: what it does for a user,
  where it lives in the repo, and what it talks to. No code unless I ask.
- After each piece, ask me to explain it back and wait.
- Whenever you are inferring rather than reading, say "I'm inferring."

When I say "notes", stop and wait for my next instruction.
```

- [ ] **Step 3: Write `prompts/08-2-session-as-study-notes.md`**

```
Where to paste: Claude Code on the web

notes

Write what I learned in this session to docs/notes/[topic].md, in my words
as much as possible, as a short study guide: what the piece does, where it
lives, what it talks to, and the three questions I should ask my developer
next. Mark anything you inferred rather than read with "(inferred)". Do not
touch any other file. Then tell me one thing in the notes you are least
sure of.
```

- [ ] **Step 4: Write the post**

Beats:
- H1 `# Part 8: Reading code without being a coder`
- Opening beat: R. asked "where does the login actually happen?" and instead of explaining, the author had R. ask the repo.
- `## The idea`: you can read a codebase the way you read a building: rooms, doors, who talks to whom. A session is a study session, and study sessions produce notes. Notes go in `docs/notes/`, not in the chat, because chats fill up. Pull quote block again: `> **Don't fear the clear!**` with `— Jenova`. New session per topic; continuation only if you're mid-topic.
- `## Paste this into Claude`: 08-1 and 08-2 with *Why* notes. 08-2's note explains the "notes" stop word.
- `## Check it`: **the confident specific** and **the drift**: Claude will describe a feature that doesn't exist yet because a file's name suggests it. Ask "show me where that is" and if it can't, it's inferring. Reference the verification card from Part 2, question 2. Close with the standing line.
- `## Do it`: new session, Plan mode, paste 08-1, learn, say "notes", paste 08-2, approve, review diff, PR. Reuse the continuation prompt from Part 6 only if you stop mid-topic.
- `## Next time`: Part 9, teach Claude a skill.
- No `## Sources` required, but include one if any product claim is made.

- [ ] **Step 5: Proxy-test 08-1**

Fresh subagent with a scratchpad repo containing `app/login/`, `api/auth/`, and an empty `app/payments/` folder: does it say "I'm inferring" about payments, and stop on "notes"? Record "Tested on <date>."

- [ ] **Step 6: Run the check**

Run: `python3 scripts/check-post.py 08-reading-code-without-being-a-coder.md`
Expected: `PASS` (pull quote present).

- [ ] **Step 7: Human test checkbox.**

---

### Task 11: Part 9, Teach Claude a skill

**Files:**
- Create: `prompts/09-1-skill-tutor.md`
- Create: `prompts/09-2-turn-prompt-into-skill.md`
- Create: `prompts/09-3-first-use-of-skill.md`
- Create: `09-teach-claude-a-skill.md`

**Interfaces:**
- Consumes: the continuation prompt 06-3 (its body becomes the skill's instructions) and the CONTINUATION.md four-heading format from Part 3.
- Produces: the repo skill `.claude/skills/continuation/SKILL.md`, invoked as `/continuation`, which Part 11 names in its loop.

- [ ] **Step 1: Verify facts**

Open https://code.claude.com/docs/en/skills and record: the exact folder path for project skills, the frontmatter fields `SKILL.md` requires (expected: `name`, `description`) and any optional ones worth mentioning, how Claude decides to use a skill from its description, and how a reader invokes one by name. Open https://code.claude.com/docs/en/cloud-environments and confirm the line that repo `.claude/skills/` is part of the clone in a cloud session. Record both URLs. If the frontmatter fields differ from `name` and `description`, change the SKILL.md example in Step 3 and the post to match the page.

- [ ] **Step 2: Write `prompts/09-1-skill-tutor.md`**

```
Where to paste: claude.ai chat

You are my patient tutor. Today's topic is "skills" in Claude Code: what a
skill is, what it is not, and why a non-programmer like me can write one.
What I know so far: a skill is a saved prompt with a name that lives in the
project repo, and Claude uses it when it fits or when I type its name with a
slash.

Rules for how we work:
- First ask me about something I do the same way every time and have
  written down for myself or someone else (a checklist, a recipe card, a
  note to a coworker). Build on that.
- Teach one piece at a time and wait for my answer: what a skill is, what
  the "description" is for, what happens when I type /name, and what a
  skill cannot do.
- Be honest that you may not know the current file format; tell me to check
  code.claude.com/docs/en/skills for that.
- Keep every message short.

When I can explain a skill in my own words, quiz me with three questions.
Then tell me one thing you said that I should double-check, and where.
```

- [ ] **Step 3: Write `prompts/09-2-turn-prompt-into-skill.md`**

```
Where to paste: Claude Code on the web

I have been pasting the same prompt at the end of every session to write my
continuation file. I want to turn it into a skill in this repo so I can just
type /continuation. I am not a programmer; you are my guide and editor.

Here is the prompt I have been pasting:

---
Before I end this session, write docs/continuations/R-CONTINUATION.md with
exactly these four sections:

## What we are working on
## What has been decided
## What is still open
## Exact next step

Rules:
- Plain language. Short bullets. Nothing I haven't actually told you or
  agreed to; if you are unsure whether something was decided, put it under
  "What is still open."
- The "Exact next step" section is one sentence that I could paste into a
  new session and act on immediately.
- Include it in the same branch as my other changes.
- After writing it, tell me one thing in it you are least sure about, so I
  can fix it before I open the pull request.
---

Rules for this session:
- First, interview me: ask me one question at a time for the skill's name
  (I think "continuation") and a one-sentence description of when it should
  be used. Wait for each answer.
- Then show me the plan: the single file you will create, its full path,
  and the file's contents, before creating anything. Explain each line of
  the front matter in one sentence.
- Create only that one file. Do not touch any other file.
- Tell me what I will type in a future session to use it.
- End with one thing about the skill file format that I should double-check
  at code.claude.com/docs/en/skills.
```

The expected skill file the session should produce, which the post shows so readers can compare:

```markdown
---
name: continuation
description: Write my CONTINUATION.md before I end a session, so the next session can pick up where I left off. Use when I say I'm wrapping up or type /continuation.
---

Write docs/continuations/R-CONTINUATION.md with exactly these four sections:

## What we are working on
## What has been decided
## What is still open
## Exact next step

Rules:
- Plain language. Short bullets. Nothing the user hasn't actually said or
  agreed to; if you are unsure whether something was decided, put it under
  "What is still open."
- The "Exact next step" section is one sentence that could be pasted into a
  new session and acted on immediately.
- Include the file in the same branch as the user's other changes.
- After writing it, tell the user one thing in it you are least sure about.
```

- [ ] **Step 4: Write `prompts/09-3-first-use-of-skill.md`**

```
Where to paste: Claude Code on the web

/continuation

(That is the whole message. If nothing happens, or Claude asks what you
mean, the skill has not been merged yet or its name differs; check the
file in the repo and try again.)
```

- [ ] **Step 5: Write the post**

Beats:
- H1 `# Part 9: Teach Claude a skill`
- Opening beat: R. said "I'm tired of pasting that continuation thing," and the author said "then teach Claude to do it," and R. did not believe it would be a markdown file.
- `## The idea`: a skill is a saved prompt with a name and a description, in the repo at the path from Step 1. Claude reads descriptions and uses a skill when the task fits, or you type `/name`. Skills are markdown, which is why you can write one. State plainly, with the cloud environments link, that skills in the repo work in cloud sessions and that plugins do not, so nothing gets installed. Close the arc: Part 3 pasted it, Part 6 put it in the repo, today it becomes a skill.
- `## Paste this into Claude`: 09-1, 09-2, 09-3 with *Why* notes. After 09-2's note, show the expected SKILL.md from Step 3 as a fenced `markdown` block titled "What you should end up with," and say the wording may differ but the front matter fields must match the docs.
- `## Check it`: **the confident specific** on the SKILL.md front matter: ask Claude in chat which fields are required, then open the skills docs page and compare. **The "wow, really?"**: ask Claude whether a skill could let it read your email or see your screen; the right answer is no, a skill only changes what Claude does with what it can already do. Reference the verification card from Part 2, question 1. Close with the standing line.
- `## Do it`: new session, Plan mode, paste 09-2, answer the two interview questions, read the plan, approve, review the diff (one new file, nothing else), open the PR, ask your developer to merge. After merge: new session, paste 09-3, confirm the continuation file gets written, and read it before you trust it.
- `## Sidebar for the developer`: review skills like code, because they steer Claude. Keep each skill under a screen. Port what you want the reader to have from your own plugins (a brainstorming skill, a self-review skill) as repo skills, since cloud sessions do not load plugins. One sentence on naming: skill names are what the reader will type, so keep them short and obvious.
- `## Next time`: Part 10, optional: working from anywhere.
- `## Sources`: the two pages from Step 1.

- [ ] **Step 6: Proxy-test 09-2 and the resulting skill**

Fresh subagent in a scratchpad repo: does it interview for name and description first, show the full file before writing, create only `.claude/skills/continuation/SKILL.md`, and match the front matter fields recorded in Step 1? Then a second fresh subagent in the same scratchpad repo given only `/continuation`: does it write `docs/continuations/R-CONTINUATION.md` with the four headings? Record "Tested on <date>."

- [ ] **Step 7: Run the check**

Run: `python3 scripts/check-post.py 09-teach-claude-a-skill.md`
Expected: `PASS`.

- [ ] **Step 8: Human test checkbox.** The author must run 09-3 in a real cloud session after merging the skill into a throwaway repo, since skill discovery in the cloud is the claim this post rests on.

---

### Task 12: Part 10, Working from anywhere (optional)

**Files:**
- Create: `prompts/10-1-stuck-desktop-install.md`
- Create: `10-working-from-anywhere.md`

**Interfaces:**
- Consumes: everything; this post changes nothing later parts depend on.

- [ ] **Step 1: Verify facts**

Open https://code.claude.com/docs/en/desktop : download location, Mac and Windows availability, the Code tab, where the Local vs Cloud environment selector is, and which permission modes are offered for cloud sessions from the app. Open https://code.claude.com/docs/en/mobile : what the mobile app can do with cloud sessions. Record URLs. Write the post to match these pages exactly; this post has the most volatile facts in the series, so include the date checked in the Sources section.

- [ ] **Step 2: Write `prompts/10-1-stuck-desktop-install.md`**

```
Where to paste: claude.ai chat

You cannot see my screen, so ask me what I see. I am installing the Claude
Desktop app and I'm stuck. First ask me whether I'm on a Mac or on
Windows, and don't assume. Then ask me one question at a time about what is
on my screen, and give me one step at a time. If you're not sure what the
current installer looks like, say so and point me to code.claude.com/docs
instead of guessing. When I'm done, tell me one thing you said that might
be out of date.
```

- [ ] **Step 3: Write the post**

Beats:
- H1 `# Part 10: Working from anywhere (optional)`
- Opening beat: R. on a train, reviewing a PR from a phone. That's the payoff.
- `## The idea`: everything you've done runs in the cloud, so any door works: the browser, the Desktop app's Code tab set to Cloud, or the phone app. Desktop gives a nicer diff view and, someday, a Local mode you don't need yet. This is the one part of the series that cares whether you're on a Mac or Windows.
- `## Paste this into Claude`: 09-1 with *Why* note (the OS question first is the point).
- `## Check it`: **the silent assumption** (OS) and **the confident specific** (where the Local vs Cloud toggle is). Exercise: ask Claude where the toggle is, then find it yourself. Reference the verification card from Part 2, question 3. Close with the standing line.
- `## Do it`: two checklists under H3s `### On a Mac` and `### On Windows`, from Step 1. Then: open the Code tab, choose Cloud, pick the project repo, see your sessions. Then the phone app: sign in, find the same session.
- `## Next time`: Part 11, how we work together now.
- `## Sources` with the date checked.

- [ ] **Step 4: Run the check**

Run: `python3 scripts/check-post.py 10-working-from-anywhere.md`
Expected: `PASS` (OS mentions allowed here).

- [ ] **Step 5: Human test checkbox** for both OS checklists; the author can only test one, so mark the other "untested by me, from the docs dated <date>" in the post itself.

---

### Task 13: Part 11, How we work together now

**Files:**
- Create: `prompts/11-1-review-my-own-pr.md`
- Create: `prompts/11-2-understand-review-comments.md`
- Create: `11-how-we-work-together-now.md`

**Interfaces:**
- Consumes: viewer posture (Part 5), hard data rule (Part 7), notes convention (Part 8), the continuation skill (Part 9), developer sidebar checklist (Part 5).

- [ ] **Step 1: Verify facts**

Open https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/reviewing-changes-in-pull-requests/about-pull-request-reviews and https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/reviewing-changes-in-pull-requests/commenting-on-a-pull-request : how comments and review states look to the PR author. Record URLs.

- [ ] **Step 2: Write `prompts/11-1-review-my-own-pr.md`**

```
Where to paste: Claude Code on the web

Before I ask my developer to review this branch, review it yourself as a
skeptical reader who has never seen this project. Do not change anything.
Tell me:
1. In one sentence, what this change does.
2. Anything a reader would find confusing or contradictory.
3. Anything that looks like it touches a file outside docs/ or data/.
4. Anything that looks like real personal data.
5. The one thing you would ask me to fix before merging.
Be honest; I would rather hear it from you than from my developer.
```

- [ ] **Step 3: Write `prompts/11-2-understand-review-comments.md`**

```
Where to paste: claude.ai chat

My developer left review comments on my pull request and I don't fully
understand them. I will paste the comments. For each one, tell me in plain
language: what they are asking for, whether it's a "must change" or a
"consider this," and one sentence I could reply with. Do not assume they
are being critical; assume they are being helpful. If a comment uses a
word I probably don't know, define it. Then tell me which comment you are
least sure you interpreted correctly.

[paste comments here]
```

- [ ] **Step 4: Write the post**

Beats:
- H1 `# Part 11: How we work together now`
- Opening beat: three months in, R. and the author's weekly call is mostly reading PRs together, and the author gets vision docs and data questions instead of "can you just."
- `## The idea`: the loop as a steady state. R.'s side: new session, Plan mode, interview or notes, `/continuation` (the skill from Part 9), PR, self-review, ask for review, reply to comments. Author's side: review kindly, comment don't rewrite, merge, protect main. Repeat the viewer posture sentence and the hard data rule. Point back to the sidebar in Part 5 as the setup that makes this safe.
- `## Paste this into Claude`: 10-1 and 10-2 with *Why* notes.
- `## Check it`: **the agreeable flip** in reverse: when your developer's comment contradicts what Claude told you, the developer is the source; ask Claude to explain the developer's view, not defend its own. Reference the verification card from Part 2, question 5. Close with the standing line.
- `## Do it`: run 10-1 before every review request; run 10-2 when comments arrive; reply in the PR, not in a text message.
- `## Sidebar for the developer`: the three habits: review within a day, one comment per idea, merge or explain why not. Then one paragraph on what comes after this series (they will ask), pointing at nothing specific.
- `## Next time`: there isn't one; say what to reread when something breaks (Parts 2 and 3).
- `## Sources`.

- [ ] **Step 5: Proxy-test 10-1**

Fresh subagent with a scratchpad branch containing a docs change plus a sneaky one-line change under `app/` and a fake-but-real-looking phone number in a doc: does it catch both? Record "Tested on <date>."

- [ ] **Step 6: Run the check**

Run: `python3 scripts/check-post.py 11-how-we-work-together-now.md`
Expected: `PASS`.

- [ ] **Step 7: Human test checkbox.**

---

### Task 14: README and series-wide consistency pass

**Files:**
- Modify: `README.md`
- Modify: any post with a cross-reference inconsistency found below

- [ ] **Step 1: Fill in the README reading order**

Replace the placeholder line with a numbered list, one line per part, linking each file, with the one-line concept from the spec table and a tag `(free)` for Parts 0 to 4, `(paid plan)` from Part 5 to Part 11, and `(optional)` on Part 10.

- [ ] **Step 2: Run every check**

Run:
```bash
for f in 0*.md 1[01]-*.md; do python3 scripts/check-post.py "$f"; done
```
Expected: twelve `PASS` lines.

- [ ] **Step 3: Cross-reference sweep**

Run:
```bash
grep -n "Part [0-9]*" 0*.md 1[01]-*.md | grep -v "^.*# Part"
```
Read every hit and confirm the part number matches the content it points at (for example, "the verification card from Part 2" only ever says Part 2; "the continuation prompt from Part 6" only ever says Part 6; the pull quote is attributed to Part 3 when quoted in Part 8). Fix any mismatch in the post and re-run its check.

- [ ] **Step 4: Tell-name sweep**

Run:
```bash
grep -oh '\*\*the [a-z" ,?]*\*\*' 0*.md 1[01]-*.md | sort | uniq -c
```
Expected: only the six tell names from Global Constraints appear. Any variant spelling (for example "the confident specifics") is a bug; fix and re-run that post's check.

- [ ] **Step 5: Prompt library sweep**

Run:
```bash
for p in prompts/[0-9]*.md; do head -1 "$p" | grep -q '^Where to paste:' || echo "BAD $p"; done
```
Expected: no `BAD` lines.

- [ ] **Step 6: Human-test ledger**

Run: `grep -n "tested:" 0*.md 1[01]-*.md`. Report to the author which posts still show `tested: pending`. The series is not publishable until none do; that gate belongs to the author, not to this plan.

---

### Task 15: Publish to Medium

**Files:**
- Create: `scripts/render-for-medium.sh`
- Create: `build/` (rendered HTML, one file per post; not source)

**Interfaces:**
- Consumes: every post passing `check-post.py` and showing a human-test date.

- [ ] **Step 1: Write `scripts/render-for-medium.sh`**

```bash
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
```

- [ ] **Step 2: Run it**

Run: `bash scripts/render-for-medium.sh`
Expected: twelve `rendered build/...html` lines. If pandoc is missing, install it with `brew install pandoc` and re-run.

- [ ] **Step 3: Verify no tables slipped through**

Run: `grep -l "<table" build/*.html || echo "no tables"`
Expected: `no tables`.

- [ ] **Step 4: Paste one post into Medium and check the prompt boxes**

Open `build/00-why-learn-with-ai.html` in a browser, select all, copy, and paste into a new Medium draft. Then for Part 1, do the same and confirm: every ` ```text ` block became a Medium code block (monospace, copyable as one unit), headings kept their levels, and the italic *Why it's written this way* notes stayed italic. If a code block pasted as plain paragraphs, select it in Medium and apply the code block format from the editor toolbar, and note in this task that manual fixing is required per post.

- [ ] **Step 5: Publish order**

Publish Part 0 and Part 1 together, then one part per publish after that, adding a link to the previous and next part at the top of each Medium story once their URLs exist. The markdown source keeps only relative links between parts; Medium URLs live only in Medium.

- [ ] **Step 6: Record**

Add a `## Published` section to `README.md` listing each Medium URL as it goes live.

---

## Self-review

**Spec coverage:** §11 skills post is Task 11. §12's Medium target is Task 15 and the no-tables rule in the check script. §1 to §4 are carried by Global Constraints and Task 7. §5 table: one task per part (Tasks 2 to 13). §6 skeleton: enforced by the check script in Task 1. §7 prompt rules: every prompt above has role, concept, rules, exit condition, doubt line; the "Where to paste" convention is Task 1. §8 tells and card: Task 4 defines, script enforces naming. §9: Task 5. §10: Task 9 including the PII scan. §12 layout: file structure section. §13 definition of done: script plus human-test ledger. §14 order of work: tasks are in that order, with the Part 0 voice pause in Task 2. §15 sources: each task's Step 1.

**Placeholder scan:** The only bracketed tokens are inside prompts where the reader fills them (`[TOPIC]`, `[paste ... here]`, `[topic]`), and `REPLACE-ME` in `forbidden.txt`, which the check script fails on until the author fills it in. No "TBD" or "similar to Task N."

**Consistency:** Prompt file names in the file structure match every task's Create list. The four CONTINUATION.md headings are identical in 03-2 and 06-3. Tell names in the script's `TELLS` list match Global Constraints exactly, including the curly-free straight quotes in `**the "wow, really?"**`; posts must use straight quotes there.

**Review Focus:** item 1 pinned to Task 7 Steps 1 and 5; item 2 to the `Where to paste` check in Task 1's script; item 3 to Task 9 Step 7; item 4 to the stuck-sentence check in Task 1's script; item 5 to the `NEEDS_SOURCES` set in Task 1's script.
