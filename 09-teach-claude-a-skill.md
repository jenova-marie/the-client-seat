# Part 9: Teach Claude a skill

"I'm tired of pasting that continuation thing."

Fair. R. had pasted it at the end of every session for three parts. It's a long prompt. So I said, "Then teach Claude to do it," and R. said "how," and I said "it's a file," and R. did not believe me. There was a whole conversation about whether I was simplifying for the non-programmer. I was not. A skill is a markdown file. You've been writing markdown files for four parts now.

## The idea

A **skill** is a saved prompt with a name and a description, stored in the project repo at `.claude/skills/<name>/SKILL.md`. That's the entire definition. The file has a short header at the top, the **front matter**, with the skill's name and a one-line description of when to use it. Under that, the prompt itself.

Two ways it gets used. Claude reads every skill's description at the start of a session and reaches for a skill on its own when your request matches. Or you type `/name`, with a slash, and Claude runs it directly. Either way, a skill doesn't give Claude new abilities. It changes what Claude does with the abilities it already has. It can't read your email. It can't see your screen. It can run a prompt you'd otherwise paste.

Because skills are markdown, you can write one. Because they live in the repo, they go through a pull request like everything else, and your developer reviews them like everything else. And because cloud sessions read the repo's `.claude/skills/` folder, a skill you merge is there in your next session, with nothing installed. The docs are specific about this: plugins do not load in cloud sessions, but project skills committed to the repo do. That's why nothing in this series ever asks you to install anything.

This closes an arc. In Part 3 you pasted the continuation prompt into a chat. In Part 6 you had Claude write it into the repo. Today it becomes a skill, and you never paste it again.

## Paste this into Claude

First, in a regular chat, the lesson:

```text
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

*Why it's written this way:* "What I know so far" gives Claude a starting point so it doesn't restart from zero. The "what a skill cannot do" piece is in the rules on purpose; it's the part people get wrong. And the file-format honesty clause sends you to the docs, because the format is the one thing here most likely to have changed since Claude learned it.

Then, in a Claude Code session, Plan mode:

```text
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

*Why it's written this way:* Interview, plan, approve, write, the loop from Part 6. Claude interviews you for the two things only you can decide, the name and the description, then shows you the whole file before it exists, with each header line explained. One file, nothing else. And the closing line points the double-check at the format, because that's where a stale memory would bite. Tested on 2026-09-27.

What you should end up with:

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

Your wording may differ. The shape shouldn't: a front matter block between two lines of three dashes, then the prompt. When I checked the docs, every front matter field was optional; the description is the one to always include, because it's how Claude decides when to use the skill, and the name defaults to the folder's name if you leave it out.

After your developer merges it, in a fresh session:

```text
/continuation
```

*Why it's written this way:* That is the whole message. One word, and something either happens or it doesn't. If nothing happens, or Claude asks what you mean, the skill hasn't been merged yet or its name differs; check the file in the repo and try again. Tested on 2026-09-27.

## Check it

First, **the confident specific**: in a chat, ask Claude which front matter fields a SKILL.md requires. It will answer with certainty. Then open the skills docs page linked below and compare. When I looked, the honest answer was "none are required, description is recommended." Claude may say something firmer.

Second, **the "wow, really?"**: ask Claude whether a skill could let it read your email or see your screen. The right answer is no. A skill only changes what Claude does with what it can already do. If it says yes, or hedges toward yes, you've caught it.

This is question 1 on the verification card from Part 2: *where did this come from?* For file formats, the answer is always the docs page, never Claude's memory.

**Ask for the source, open the source, compare.**

## Do it

1. New session on the project repo. Plan mode. Paste the skill-building prompt.
2. Answer the two interview questions. "continuation" is a fine name.
3. Read the plan: one new file, full path, full contents. Approve.
4. Read the diff. One new file under `.claude/skills/`. Nothing else.
5. **Create PR.** Ask your developer to merge it.
6. After it's merged: new session, paste the one-word test. Confirm the continuation file gets written. Read it before you trust it.

## Sidebar for the developer

Review skills like code, because they steer Claude. Keep each one under a screen. If there are helpers from your own plugins you want your client to have, a brainstorming skill or a self-review skill, port them as repo skills; cloud sessions don't load plugins, so the repo is the only channel. Skill names are what the reader will type, so keep them short and obvious.

## Next time

Part 10, optional: working from anywhere, including the one install in the whole series.

## Sources

- Skill file location, front matter fields, and slash invocation: https://code.claude.com/docs/en/skills
- Cloud sessions read repo skills and do not install plugins: https://code.claude.com/docs/en/cloud-environments

<!-- tested: pending -->
