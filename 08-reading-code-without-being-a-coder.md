# Part 8: Reading code without being a coder

"Where does the login actually happen?"

R. asked me this on a call, and I opened my mouth to explain, and then I closed it. Because I'd explained it before, twice, and it hadn't stuck, and I finally understood why: I was explaining it the way I understood it, from the inside, and R. needed it explained from the outside, starting at the button R. actually tapped every morning.

So I said, "Ask the repo." And I watched R. open a session and type the question, and twenty minutes later R. explained login back to me, correctly, using a metaphor about the front desk at a hotel that I now use myself.

You don't need to read code to understand a codebase. You need to know how to ask it questions, and how to keep the answers.

## The idea

A codebase is a building. It has rooms (folders), each room is for something, and there are doors between them (one part calls another). You don't need to know how the plumbing works to walk through a building and understand it: this is where people come in, this is where the money is kept, this room talks to that room. That's the level you're after. What does this piece do for a user, where does it live, and what does it talk to.

Why bother, if you're never going to change the code? Because every conversation you have with your developer is about this building, and right now they can see it and you can't. When you know that login lives in one room and talks to a second room that checks passwords, you can ask "is the password check the slow part?" instead of "why is it slow?" You can read a pull request description and know which room it touched. You stop being the person things are explained to and start being the person in the conversation. That's worth an hour a week.

Claude Code can walk you through the building, because it can read every file in the repo. Ask it to start where you start: the part of the app you use most. Ask for one room at a time. Ask it to say when it's guessing.

A session like this is a **study session**, and study sessions produce **notes**. Notes go in the repo, in a folder called `docs/notes/`, one file per topic, because a chat is not a place to keep things. You learned this in Part 3. It's truer here, because a study session is long and dense and exactly the kind of chat that drifts. One session per topic. When the topic changes, start a new session. If you stop mid-topic, the continuation prompt from Part 6 carries you over.

> **Don't fear the clear!**
>
> — Jenova

## Paste this into Claude

Claude Code session, Plan mode, on the project repo.

```text
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

*Why it's written this way:* It's the tutor prompt from Part 1, pointed at a repo. Starting from the part you use most means the first room is one you already know from the inside. "No code unless I ask" keeps it in plain language; you can always ask. The "I'm inferring" rule is the one that matters most: Claude reads files, but it also fills gaps, and you want to know which is which. And the last line sets up a stop word. When you say "notes," Claude stops explaining and waits. Tested on 2026-09-27.

When you've learned enough for one sitting:

```text
notes

Write what I learned in this session to docs/notes/[topic].md, in my words
as much as possible, as a short study guide: what the piece does, where it
lives, what it talks to, and the three questions I should ask my developer
next. Mark anything you inferred rather than read with "(inferred)". Do not
touch any other file. Then tell me one thing in the notes you are least
sure of.
```

*Why it's written this way:* The first word is the stop word, so it lands cleanly even if Claude was mid-thought. Replace `[topic]` with a short name like `login` or `appointments`. The three questions for your developer turn passive learning into your next conversation. "(inferred)" carries the honesty from the session into the file, so future-you knows which parts to trust.

## Check it

Two tells, and they show up together here.

First, **the confident specific**: a folder called `payments` does not mean the app takes payments. It might be empty. It might be a plan. Claude sees the name and may describe a feature that doesn't exist yet, in detail, with confidence. Second, **the drift**: forty minutes into a study session, Claude may blend two rooms together, or describe a door that isn't there.

The move is the same for both. When Claude describes something, ask: "Show me where that is." If it points to a file and quotes it, it read it. If it can't, it's inferring, and it should have said so. Make it say so.

This is question 2 on the verification card from Part 2: *what would I see on my screen if this were true?* In a codebase, the answer is always a file. Ask for the file.

**Ask for the source, open the source, compare.**

## Do it

1. New session on the project repo. Plan mode.
2. Paste the study prompt. Answer the first question honestly: which part of the app do you actually use?
3. Learn one room at a time. Explain each back. Ask "show me where that is" at least once, on purpose.
4. When you've had enough for one topic, type the notes prompt with `[topic]` filled in.
5. Approve the plan. Read the diff: one new file under `docs/notes/`, nothing else.
6. **Create PR.** In the description, say what you learned in one sentence and which of the three questions you most want answered.
7. If you stopped mid-topic and want to pick it up tomorrow, run the continuation prompt from Part 6 before you create the PR. If you finished the topic, you don't need it. New topic, new session.

## Sidebar for the developer

Read the notes files. Not to correct them, though you can, but because they tell you exactly how your client understands the system, in their words, including the parts marked "(inferred)" where they're guessing. Those inferences are the misconceptions you'd otherwise discover six months from now in a tense meeting. Answer the three questions at the bottom of each file in the PR, one comment per question, and you've had the most efficient conversation about your architecture you'll have all month.

## Next time

Part 9: teach Claude a skill. You've been pasting the same continuation prompt for three parts now. Time to stop.

## Sources

- What a cloud session can read and how the diff view works: https://code.claude.com/docs/en/claude-code-on-the-web

<!-- tested: pending -->
