# Part 11: How we work together now

Three months in, our weekly call is mostly reading pull requests together. R. opens one, I open the same one, and we talk about a paragraph in a vision document or a column in a data file or a question at the bottom of a notes page. Sometimes I merge it on the call. Sometimes R. says "actually, let me fix that first" and does, in a session, while I watch.

I get vision documents now. I get data questions with the row number attached. I get "I read the notes on appointments and I think the reminder logic is in the wrong room, is it?" instead of "can you just make the reminders work." I have never had a client relationship like this, and the difference is not that R. learned to code. R. didn't. The difference is that R. learned to learn, and to check.

This part is about what that looks like as a steady state, and how to keep it going after I stop writing.

## The idea

The loop has two sides.

**Your side.** New session, Plan mode. Interview for a document, or a study session for notes. When you're wrapping up, `/continuation`, the skill from Part 9. Read the diff. Before you ask for review, run the self-review prompt below. Open the PR. When comments arrive, run the second prompt, then reply in the PR. Same sentence as always: **Plan mode, read the plan, approve it, review the diff, open the pull request, let the developer merge.** And the rule from Part 7 that never bends: **Never put real user data in a repo.**

**Your developer's side.** Review kindly and quickly. Comment, don't rewrite. Merge, or say why not. Keep main protected. The sidebar in Part 5 is the setup that makes all of this safe, and it's worth rereading once you've lived in it for a while.

What makes it hold isn't goodwill. It's that every step leaves a record in the repo. Your documents in `docs/`, your notes in `docs/notes/`, your continuations in `docs/continuations/`, your samples in `data/`, and every conversation about them in a pull request thread that anyone can reread. Nothing important lives in a chat. Nothing important lives in anyone's memory, including Claude's, including mine.

## Paste this into Claude

Before every review request, in the session on your branch:

```text
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

*Why it's written this way:* "Skeptical reader who has never seen this project" is a role, and it's the opposite of the role Claude has been playing all session, which is why it catches things. Items 3 and 4 are the two tripwires from Parts 6 and 7, run one last time before a human sees the work. Item 5 forces a priority. And the last line gives Claude permission to be blunt, which it otherwise won't be. Tested on 2026-09-27.

When your developer's comments arrive and any of them are confusing, in a regular chat:

```text
My developer left review comments on my pull request and I don't fully
understand them. I will paste the comments. For each one, tell me in plain
language: what they are asking for, whether it's a "must change" or a
"consider this," and one sentence I could reply with. Do not assume they
are being critical; assume they are being helpful. If a comment uses a
word I probably don't know, define it. Then tell me which comment you are
least sure you interpreted correctly.

[paste comments here]
```

*Why it's written this way:* Review comments are written by a person in a hurry, in a vocabulary they forget you don't have. This prompt translates without deciding for you: what's being asked, how firm it is, and a reply you can edit. The "assume they are being helpful" line is there because tone is the first casualty of text, and because they are. The closing line is the doubt habit, aimed at the one interpretation most likely to be wrong.

## Check it

Today's tell is **the agreeable flip**, in reverse.

In Part 2 you watched Claude cave when you pushed back on a right answer. Here's the other side of it. Sometimes your developer's comment will contradict something Claude told you. Claude said the column was optional; your developer says it's required. Claude said the notes file described the login flow correctly; your developer says the flow changed last month.

The developer is the source. Not because developers are always right, but because they can see the running system and Claude is working from a snapshot of the repo and a lot of general knowledge. So don't ask Claude "are you sure?" and don't ask it to defend what it said. Ask it to explain the developer's view: "My developer says this is required. Explain why they might be right." You'll get a better explanation than either of you would have written alone, and you'll have avoided making Claude argue with a human who knows.

This is question 5 on the verification card from Part 2: *would it say the same thing if I asked again in a fresh chat?* When a person who can see the system says otherwise, you already have your answer.

**Ask for the source, open the source, compare.**

## Do it

This one has no milestone. It has habits.

1. Run the self-review prompt before every review request. Every time. It takes a minute and it catches the thing you'd be embarrassed about.
2. Run the comments prompt whenever a review comment confuses you, before you reply.
3. Reply in the PR, on the comment, not in a text message and not on the call. The PR is where the record lives. Click **Resolve conversation** when a thread is done.
4. When something breaks, and something will, go back to Part 2 and Part 3 first. It's almost always a verification problem or a context problem.

## Sidebar for the developer

Three habits on your side. Review within a day; a PR that sits for a week teaches your client that their work goes into a void. One comment per idea, on the line it's about, so each can be resolved on its own. Merge, or say plainly why not; "I'll get to it" is the worst of the three options.

They will ask what comes after this. I don't have a specific answer, and I'm suspicious of anyone who does. What I can say is that a client who can read the repo, write documents into it, bring data safely, ask the codebase questions, and catch an AI being wrong is a client you can build anything with. Where you go from there is between the two of you.

## Next time

There isn't one. When something breaks, reread Part 2 for the tells and Part 3 for the clear. Those two carry almost everything.

## Sources

- How review states (Comment, Approve, Request changes) appear on a pull request: https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/reviewing-changes-in-pull-requests/about-pull-request-reviews
- Commenting on a line, replying, and resolving a conversation: https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/reviewing-changes-in-pull-requests/commenting-on-a-pull-request

<!-- tested: pending -->
