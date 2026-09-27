# Part 6: Your first contribution

R.'s first pull request was a vision document. Not code, not data: two pages about who the app was for, what it was supposed to fix, and what it must never turn into. I opened it expecting to be polite about it.

I learned three things about the app from that document that had never come up in a meeting. One of them changed how I built the login screen. Another was a sentence under "what it must never become" that I've since quoted to two other clients. R. had been carrying all of this around for two years and nobody had asked in a way that made it come out.

That's what this part is for. Not the mechanics of a pull request, though you'll learn those. The fact that the person who knows the most about the project is usually the one who's never been handed the pen.

## The idea

Three words, defined for someone who adds documents, not code.

A **branch** is your own copy of the project's timeline. You make changes on it; nobody else sees them in main until they're pulled in. Every session you open gets one automatically.

A **diff** is the list of exactly what changed: which files, which lines, what was there before and what's there now. Green for added, red for removed. It's how you and your developer see the same thing without reading the whole document twice.

A **pull request** is the message that says "please look at this and pull it in." It shows the diff, it has a comment thread, and it's where your developer says yes, or asks a question, or asks for a change. Nothing reaches main except through one.

The loop you'll run today, and in every part after this, goes: interview, outline, approve, write, review the diff, continuation, pull request. Claude interviews you. Claude proposes an outline. You approve it. Claude writes. You read the diff. Claude writes your continuation file. You open the PR. Or, in the sentence from Part 5: **Plan mode, read the plan, approve it, review the diff, open the pull request, let the developer merge.**

## Paste this into Claude

All three of these go into a Claude Code session, in Plan mode, on the project repo.

```text
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

*Why it's written this way:* "Interviewer and editor, not the author" is the role, and it's the whole point: interview-first keeps it your document. The four questions are the ones I'd ask you on a call. The outline-before-writing step is where Plan mode earns its keep: you see the shape before anything exists. And "(suggested)" is how you tell, later, which sentences were yours and which Claude helpfully added. The ones it added are the ones to check. Tested on 2026-09-27.

When Claude shows you its plan and asks for approval, paste this before you click anything. If the only choices on screen are buttons, choose the one that says keep planning rather than approving, and then paste it:

```text
Before I approve this, explain to me, file by file, exactly what will
change: which files are new, which are edited, and one plain-language
sentence per file about what the change is. Then tell me if anything in
this plan touches a file outside docs/. If it does, stop and ask me.
```

*Why it's written this way:* You approve what you understand. A plan is a list of files and changes, and until you can say in your own words what each one does, you're not approving, you're clicking. The "outside docs/" line is a tripwire: you're here to write documents, so anything reaching into the app itself is a surprise, and surprises stop the session. Tested on 2026-09-27.

Before you end the session, the continuation ritual from Part 3, now as a file in the repo:

```text
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

*Why it's written this way:* It's the same prompt as Part 3 with one change: instead of pasting the result into a Project, Claude writes it straight into the repo, under a folder named `continuations/` with your initial on the file, so two people's continuations never collide. The ritual is the ritual: **write it, read it yourself and fix it, save it, clear, paste it into the next prompt.** In the repo, "save it" and "clear" become "open the PR" and "start a new session." Don't fear the clear.

## Check it

Two tells, in new outfits.

First, **the "wow, really?"**: somewhere in this session, Claude may offer to also fix something in the app while it's there. A typo in a screen. A setting that "looks wrong." It will sound helpful and it will be tempting. Say no. Put it under "What is still open" in your continuation file for your developer to look at. Documents are your lane today, and the tripwire prompt above exists precisely for this.

Second, **the drift**: read the finished vision document against what you actually said in the interview. Every sentence is either yours, or marked "(suggested)," or it gets cut. Claude drifts toward what a vision document usually says. You want what *you* say.

This is question 1 on the verification card from Part 2: *where did this come from?* For every line in that document, the answer should be "me."

**Ask for the source, open the source, compare.**

## Do it

1. Go to claude.ai/code. Start a new session on the project repo. Choose Plan mode.
2. Paste the interview prompt. Answer the questions, one at a time, in your own words. Short answers are fine.
3. When Claude shows the outline, read it. Ask for changes if you want them. Approve it.
4. When Claude shows its plan and asks for approval, paste the explain-before-approve prompt. Read the answer. Then approve.
5. Claude writes. When it's done, find the diff indicator near the top of the session, the one with green and red numbers. Click it. Read the diff. It should be one new file under `docs/`.
6. Paste the continuation prompt. Read the file it writes. Fix anything it got wrong.
7. Click **Create PR** at the top of the diff view. Write a title and a two-sentence description in your own words: what this is, and what you'd like your developer to look at.
8. Tell your developer the PR exists. That's it. You're done.

## Sidebar for the developer

Reviewing a docs-only PR from a non-technical collaborator is a different job from reviewing code, and it's mostly about tone. Comment, don't rewrite: if a sentence is unclear, ask what they meant, in the PR, on that line. Ask questions rather than issuing corrections; the document is theirs. Merge it. Then say thank you somewhere they'll actually see it, which is probably not the PR. A first contribution that gets a curt "LGTM" and a merge teaches someone that this is a place where their work disappears. A first contribution that gets three curious questions and a thank-you teaches them to come back.

## Next time

Part 7: bringing your data along, and the one hard rule I will never let you break.

## Sources

- How a cloud session shows the plan, the diff, inline comments, and the Create PR button: https://code.claude.com/docs/en/web-quickstart
- What Plan mode does and how approval works: https://code.claude.com/docs/en/permission-modes
- What a pull request is, in GitHub's words: https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests

<!-- tested: pending -->
