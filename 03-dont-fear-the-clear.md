# Part 3: Don't fear the clear

R. had one chat. One. It was three weeks long. It had the vision for the app in it, and the list of screens, and a long argument about whether "clients" or "customers" was the right word, and a recipe for lemon bars that had wandered in one evening, and somewhere around week two Claude started contradicting itself. It would say the app had four main screens, then five. It forgot a decision R. had been very clear about and cheerfully argued the opposite.

I said, "Start a new chat." R. looked at me like I'd suggested burning the house down. "But it *knows everything now.*"

It didn't. That was the problem. This part is about why, and about the ritual that makes starting over feel like nothing.

## The idea

Every conversation with Claude has a **context**: the working memory it has for that one chat. Everything you type goes in. Everything Claude says goes in. Every file you paste goes in. That's how it remembers what you said two messages ago, and it's wonderful, right up until it fills.

Context has a size limit. When a chat gets long, two things happen. First, old material gets summarized or dropped to make room, so the early decisions blur. Second, even before the limit, a crowded context gets noisy: there's so much in there that Claude starts reaching for the wrong part of it. From your side, this looks like **the drift**: Claude forgets what you said early on, restates it slightly wrong, then builds on the wrong version. It's also where a lot of **the "wow, really?"** answers come from, because a confused Claude is a confident Claude with worse material.

Two rules, and they're simple:

- **Clear when the task changes.** New topic, new chat. Lemon bars do not belong in the vision document.
- **Compact when the task continues but the chat is long.** Summarize what matters, carry that forward, drop the rest.

What survives a clear? Not the chat. Never the chat. What survives is anything you've put somewhere else: a file, a Project in claude.ai, or the small document this part is going to teach you to write, called `CONTINUATION.md`. If it matters, it goes in a file. If it's only in the chat, it's already half gone.

> **Don't fear the clear!**
>
> — Jenova

A quick preview of where this is going. In a few parts you'll be using Claude Code, the version of Claude that works inside your project. Run on your own computer, it has two commands for exactly this: `/clear` wipes the context, and `/compact` summarizes it and keeps going. In the cloud sessions you'll actually be using, `/compact` works, and the official docs say `/clear` does not: your clear is simply starting a new session from the sidebar. Same idea, different button. You'll also see a file called `CLAUDE.md` in the project. That's your developer's file, the one that survives every clear because it's part of the project itself. You'll read it. You won't edit it.

## Paste this into Claude

First, the lesson. Fresh chat.

```text
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

*Why it's written this way:* Role, topic, rules, exit, same as always. The new move is the experiment in the third rule: Claude has to demonstrate its own memory and then rate it honestly. Asking an AI to describe its own limits is one of the few times it tends to be refreshingly candid, and hearing it from Claude lands differently than hearing it from me. Tested on 2026-09-27.

Second, the ritual. When you're in any chat that matters and you're about to clear, paste this:

```text
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

*Why it's written this way:* Four fixed headings, so every continuation you ever write looks the same and you can find things fast. The rule about "nothing I haven't actually told you" is the anti-drift clause: anything Claude isn't sure was decided goes under "still open," not "decided." And here's the ritual, in order: **write it, read it yourself and fix it, save it, clear, paste it into the next prompt.** The reading step is not optional. You are the editor of this document, not Claude. If it says you decided something you didn't, fix it before you save. Tested on 2026-09-27.

Third, the resume. Fresh chat, first message:

```text
Here is my CONTINUATION.md from a previous conversation. Read it, then:
1. Tell me in two sentences what we are doing and what the next step is.
2. Ask me one question if anything in it is unclear.
3. Do not start the next step until I say go.

[paste CONTINUATION.md here]
```

*Why it's written this way:* Two sentences back to you is a check that Claude actually read it. One question surfaces anything ambiguous before it turns into drift. And "don't start until I say go" keeps you in charge of the first move in the new chat.

## Check it

Today's tell is **the drift**, and you get to catch it twice.

First, after the experiment in the tutor session: scroll up, find the five facts you actually typed, and compare them against the list Claude gave back. Did it get all five? Did it subtly rephrase one? Now imagine that chat is three weeks long.

Second, after you resume with your CONTINUATION.md in a fresh chat: ask Claude to restate the three most important facts about what you're working on. Compare against the document you wrote. Anything missing or bent is drift you caught before it cost you anything.

This is question 5 on the verification card from Part 2: *would it say the same thing if I asked again in a fresh chat?* The continuation ritual is how you make the answer yes.

**Ask for the source, open the source, compare.**

## Do it

Today's milestone: the thing that survives the clear.

1. Go to claude.ai/projects, or find Projects in the left sidebar. Projects are available on the free plan; you can have up to five.
2. Click **New Project** in the upper right. Name it after your app. Add a one-line description.
3. Run the continuation prompt in whatever chat you've been using most, read the result, fix anything wrong, and copy it.
4. Back in your Project, find the knowledge area on the right side and click the plus sign to add content. Paste your CONTINUATION.md there, or save it as a text file and upload it.
5. Start a new chat inside the Project. Paste the resume prompt. Watch Claude pick up where you left off.

If Projects aren't available to you for any reason, the ritual still works: save it somewhere you'll find it (a note on your computer is fine), and paste it in by hand.

## Next time

Part 4: what a repo actually is, why it isn't a shared folder, and why that difference is the reason you'll never lose your work again.

## Sources

- Projects are available on the free plan, up to five: https://support.claude.com/en/articles/9517075-what-are-projects
- Creating a Project and adding knowledge: https://support.claude.com/en/articles/9519177-how-can-i-create-and-manage-projects
- Which context commands work in cloud sessions (`/compact` yes, `/clear` no, start a new session instead): https://code.claude.com/docs/en/claude-code-on-the-web

<!-- tested: pending -->
