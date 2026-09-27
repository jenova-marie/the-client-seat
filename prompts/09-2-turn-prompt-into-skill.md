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
