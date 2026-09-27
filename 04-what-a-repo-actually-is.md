# Part 4: What a repo actually is

"Can't you just put it in a shared Google Drive folder?"

R. asked me this on a call, gently, the way you ask a contractor whether the fancy thing is really necessary. And it's a fair question. R. had been running a business out of shared folders for years. Documents went in, people edited them, and it mostly worked, except for the time two people edited the same pricing sheet and nobody noticed for a week, and the time a file called `FINAL_v3_real_USE_THIS.docx` turned out not to be the one anyone used.

I said, "Those two things you just told me about? A repo makes them impossible." And then I had to explain what a repo was without a whiteboard, which is what this part is.

## The idea

A **repo**, short for repository, is a folder that remembers. That's the whole thing. It holds your project's files, and it holds every version of every file that has ever existed in it, and who changed what, and when, and why.

You are going to need five words. You will never type a git command in this series. You will still need these five words.

- A **repo** is the project folder that remembers everything. Documents, data, code, all of it, plus the entire history of changes.
- A **commit** is one saved change, with a note saying what it was and why. Not "the file as it is now" but "here's what I changed and here's what I was thinking." Every commit has a name and a timestamp and an author.
- The **history** is the list of every commit, in order, forever. You can go back to any point in it. Nothing is ever really overwritten.
- A **branch** is your own parallel copy of the project where you can make changes without affecting anyone else. You work on the branch, and when your work is ready, it gets folded back in.
- **main** is the branch that everyone agrees is the real one. The live version. Changes only reach main after they've been looked at.

Now the shared-folder question. A shared folder has one version of each file, right now. When you save, the old version is gone, or buried in a version-history menu nobody opens. Two people editing at once make a mess. There's no note explaining why anything changed. A repo has all versions, always; two people can work on two branches at the same time without touching each other; and every change comes with a sentence explaining itself. The difference isn't features. It's that a repo is built around the question "what changed, and why?" and a folder isn't built around any question at all.

For you, as someone who'll be adding documents and data rather than code, this means: you can never break anything permanently. Your work goes on a branch. It reaches main only after your developer has looked at it. If something goes wrong, the history has the version from before. That's not a safety net I'm adding for you. It's how the tool works for everyone.

## Paste this into Claude

Fresh chat.

```text
You are my patient tutor. Today's topic is what a "repo" (repository) is,
and the four words I keep hearing: commit, branch, main, and history. I have
never used one. I am about to join a software project as a non-programmer
who will add documents and data, not code.

Rules for how we work:
- First ask me how I keep track of versions of things today (documents,
  photos, recipes, anything) and what goes wrong. Build on that. Do not use
  any analogy or metaphor I haven't given you, not even a small one like
  "snapshot" or "timeline"; if you need a comparison I haven't offered,
  ask me for one first.
- Teach one word at a time, in this order: repo, commit, history, branch,
  main. After each, ask me to explain it back and wait.
- Explain specifically why a shared folder like Dropbox or Google Drive is
  not the same thing, using my own examples.
- Keep every message short.

When I can explain all five in my own words, quiz me with three questions.
Then tell me one thing you said that I should double-check, and where.
```

*Why it's written this way:* Two things are new here. The order is fixed on purpose: repo, commit, history, branch, main. Each word only makes sense once you have the one before it, and left to itself Claude tends to start with branches, which is like teaching someone to drive by explaining lane changes. And there's a new rule: "do not use any analogy I haven't given you." Every tutorial about repos has a baked-in analogy, trees or timelines or save points, and they're all fine and none of them are yours. The prompt forces Claude to build on whatever you actually do with versions today, which is the thing you'll remember. Small metaphors still sneak in sometimes; when one does, say "use my example instead," and it will. Tested on 2026-09-27, three times; the third wording is the one above.

## Check it

Today's tell is **the confident specific**, and today you check it against a real page.

After the tutor session, still in the same chat, ask Claude: "What does the GitHub signup page ask for?" It will give you a list. It will sound sure. Note the list.

Now open github.com/signup in another tab and look at the actual page. Compare field by field. Claude may be right. It may describe a page from a year ago. It may add a field that isn't there. Whatever you find, you now know something Claude doesn't: what the page looks like today.

This is question 2 on the verification card from Part 2: *what would I see on my screen if this were true?* You looked. That's the whole move.

**Ask for the source, open the source, compare.**

## Do it

Today's milestone: a free GitHub account. Use the same email address you used for Claude. It isn't required, but it makes Part 5 easier, because both accounts will be recognizably you.

1. Go to github.com/signup.
2. Follow the prompts. You'll enter an email address, or you can sign up with a Google or Apple account.
3. Choose a username. This is public and your developer will use it to invite you, so pick something you'd be fine seeing in a work setting.
4. Verify your email. GitHub will send you a message; click the link. This step isn't skippable: without a verified email you can't do basic things like create a repo.
5. A free account is all you need. When GitHub offers you plans, choose free.

If you get stuck, paste this into a regular claude.ai chat:

```text
You cannot see my screen, so ask me what I see. I am creating a free GitHub
account at github.com and I am stuck. Ask me one question at a time about
what is on my screen, give me one step at a time, and never guess at button
names; if you are not sure, ask me to describe what I see. When I'm done,
tell me one thing you said that might be out of date and where to check.
```

*Why it's written this way:* Same shape as the stuck prompt from Part 1, and it always will be: Claude can't see your screen, so it asks first; one step at a time; no guessing at button names; and a closing admission about what might be stale. Signup pages change more often than almost anything else on the internet, so that last line is doing real work here.

## Next time

Part 5: joining the project. Your developer sends an invitation, you accept it, and you open the project repo for the first time. It's also the one place in this series where I ask you to pay for something, and I'll tell you exactly what and why before you click anything.

## Sources

- Creating a GitHub account, including the verified-email requirement: https://docs.github.com/en/get-started/start-your-journey/creating-an-account-on-github
- GitHub's own definitions of repository, commit, branch, and main, which I kept ours consistent with: https://docs.github.com/en/get-started/learning-about-github/github-glossary
- What GitHub and Git are, in their words: https://docs.github.com/en/get-started/start-your-journey/about-github-and-git

<!-- tested: pending -->
