# Part 5: Joining the project

The week I sent R. the collaborator invitation, I got a one-line reply within about four minutes: "So can I break it?"

Honest question. Deserves an honest answer. The answer is: not with the way it's set up. Not because I trust R. to be careful, though I do, but because I spent an hour before sending that invitation making sure that carefulness wasn't the thing standing between R. and disaster. The tool was. This part is about what that setup looks like from your side, and the sidebar at the end is what it looks like from mine.

## The idea

Here is how you're going to work in the project repo, for the rest of this series and probably for the rest of the project. Memorize this sentence:

**Plan mode, read the plan, approve it, review the diff, open the pull request, let the developer merge.**

Three words in there are new. A **session** is one conversation with Claude Code, opened on the project repo. Where a claude.ai chat is a conversation about anything, a session is a conversation that can read and change files in the repo. Each session gets its own branch, so nothing you do in one bleeds into another.

**Plan mode** is a setting for the session that makes Claude ask first. In Plan mode, Claude reads files and explores, then proposes a plan of what it would change, and it doesn't touch anything until you approve. You'll read the plan. If it makes sense, you approve. If it doesn't, you say so and Claude plans again. This is the whole difference between "an AI did something to my project" and "I decided what happened to my project."

A **pull request**, or PR, is how your work reaches the real project. When your changes are ready on your branch, you open a pull request, which is a page on GitHub that says "here's what I changed, please look." Your developer reads it, comments, and merges it into main. Part 6 goes deeper.

Now, the safety question. There is no read-only mode in Claude Code. I want to be honest about that. What there is, is better than read-only, because you can actually contribute: Plan mode means Claude asks you before every change, and branch protection on the repo means nobody can change main directly, not you, not Claude on your behalf, not even me without a review. Your work always goes on a branch, and it always waits for a human to pull it in.

Now the part I promised to say loudly. **Claude Code on the web is not on the free plan.** As of the day I checked, the official availability page lists cloud sessions on the Pro, Max, and Team plans, and on Enterprise with a premium seat or a Chat + Claude Code seat. For most readers that means one of two things: you upgrade your own account to Pro, or your developer's organization is on a Team plan and gives you a seat. Ask your developer which. Do it before the steps below, because signing in to claude.ai/code on a free plan gets you a door that doesn't open.

## Paste this into Claude

First, in a regular claude.ai chat, the lesson:

```text
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

*Why it's written this way:* The tutor shape you know. The new rule is the third one: Claude has to say out loud when it isn't sure the interface details are current, and send you to the official docs instead of guessing. Interfaces change. Claude's memory of them doesn't. That rule is a seatbelt. Tested on 2026-09-27.

Second, once you're in, this is the first thing you paste into your first session:

```text
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

*Why it's written this way:* "Do not change anything" is a rule you give Claude, like every other rule in this series. It is not a mode. Plan mode is the mode, and you set it with a dropdown, not a sentence; the sentence is belt-and-suspenders. The rest is a guided tour with a built-in honesty clause ("say clearly if you are guessing") and the usual ending: one thing to confirm with a human who knows. Tested on 2026-09-27.

## Check it

Two tells today. **The silent assumption**: when you ask Claude about claude.ai/code in a chat, it may answer as if you already have write access, or a paid plan, or as if you're a developer. You told it who you are in the prompt above. Notice when it forgets. And **the confident specific**: Claude will give you menu paths and button names for claude.ai/code with total assurance.

Exercise: in a chat, ask Claude, "What permission modes can I choose in a Claude Code cloud session?" Write down what it says. Then open the official page linked under Sources and compare. When I checked, the answer was three: Accept edits, Plan, and Auto. Claude may list those, or list extras that only exist on the desktop, or miss one. This is question 3 on the verification card from Part 2: *what is it assuming about me, my plan, or my computer?*

**Ask for the source, open the source, compare.**

## Do it

In this order. The order matters.

1. **Accept the GitHub invitation.** Your developer added you as a collaborator; GitHub emailed you. Open the email, click accept, sign in to GitHub if asked. You now have access to the project repo.
2. **Sort out your Claude plan.** Either upgrade to Pro in your claude.ai settings, or accept the seat your developer's Team plan sent you. Confirm which with your developer first.
3. **Go to claude.ai/code** and sign in with your Claude account.
4. **Sign in with GitHub** when prompted. You'll be sent to GitHub's authorization page; approve it, and you'll be sent back. If it asks you to install the Claude GitHub App, your developer has already done that on the project repo, so you can skip.
5. **Pick the project repo** from the repository selector below the message box.
6. **Choose Plan mode** from the mode dropdown next to the message box.
7. **Paste the first-session prompt** above. Read what comes back. Read the contributor file it points you to. Don't change anything today.

If you get stuck anywhere in steps 3 through 6, in a regular chat:

```text
You cannot see my screen, so ask me what I see. I am trying to open my
project's repo in Claude Code on the web at claude.ai/code and connect my
GitHub account, and I'm stuck. Ask me one question at a time about what is
on my screen, give me one step at a time, and if you are not sure what the
current interface looks like, say so and point me to code.claude.com/docs
rather than guessing. When I'm done, tell me one thing you said that might
be out of date.
```

*Why it's written this way:* Same stuck-prompt shape as always, with the docs-not-guessing rule added because this interface changes more than most.

## Sidebar for the developer

What I did before sending the invitation, in order:

1. **Installed the Claude GitHub App on the project repo.** A cloud session can only work in a private repo that has the app installed. Install it once on the repo or the organization, and the reader never has to.
2. **Invited R. as a collaborator with write access.** Repo Settings, Collaborators, Add people. Yes, write access. Claude pushes a branch on R.'s behalf, and pushing a branch requires write. Read access would mean no contributions at all.
3. **Protected main.** Under branch protection or a ruleset: require a pull request before merging, require one approving review, and restrict who can push. With that in place, write access means "can create branches and open PRs," not "can change the live project."

One more thing worth knowing before you set anything else up: **cloud sessions do not load plugins.** They do clone the repo, which means they read the repo's `CLAUDE.md` and anything committed under `.claude/skills/` and `.claude/commands/`. So any helper you want your reader to have goes in the repo, not in a plugin. Part 9 makes use of this.

## Next time

Part 6: your first contribution. A real document, on a real branch, in a real pull request, with your name on it.

## Sources

- Which plans include cloud sessions (checked 2026-09-27): https://code.claude.com/docs/en/feature-availability
- Sign-in, GitHub authorization, repo selection, and the three permission modes: https://code.claude.com/docs/en/web-quickstart
- Cloud sessions overview, including the GitHub App requirement for private repos: https://code.claude.com/docs/en/claude-code-on-the-web
- What Plan mode does: https://code.claude.com/docs/en/permission-modes
- What a cloud session reads from the repo, and that it does not install plugins: https://code.claude.com/docs/en/cloud-environments
- Inviting a collaborator: https://docs.github.com/en/account-and-profile/setting-up-and-managing-your-personal-account-on-github/managing-access-to-your-personal-repositories/inviting-collaborators-to-a-personal-repository
- Protecting main: https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches

<!-- tested: pending -->
