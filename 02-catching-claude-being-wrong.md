# Part 2: Catching Claude being wrong

About three weeks in, on a Tuesday afternoon, R. sent me a message that I have since framed in my head: "Claude says GitHub can convert the app for us, so why are we paying you?"

There was a screenshot. Claude had, with great warmth and a numbered list, explained how GitHub would take the Base44 app and turn it into a React Native app automatically. Step four involved a toggle. The toggle does not exist. The feature does not exist. Nothing in the screenshot existed except the confidence.

I did not get defensive, which I'm still a little proud of. I said, "Okay. Let's find out together," and we spent forty minutes doing exactly what this part teaches. By the end R. was more careful with AI than most developers I know, and I had the best lesson of the whole onboarding handed to me for free.

## The idea

Here is the one sentence I want you to remember from this entire series: **AI is fluent, not accurate.**

Fluency is how smoothly the words come out. Accuracy is whether they're true. In people, those travel together enough that we use one as a shortcut for the other: someone who explains something clearly and confidently is probably right. AI breaks that shortcut. It is always fluent. It is usually accurate. And when it isn't, it sounds exactly the same.

The word for a confident answer with nothing behind it is a **hallucination**. Not a lie, exactly, because a lie needs a liar who knows better. Claude doesn't know better. It produced a sentence shaped like an answer, and the shape was perfect.

You can't stop hallucinations. What you can do is learn the tells. In Part 1 I gave you one. Here are all six, by the names I'll use for the rest of this series:

- **the confident specific**: an exact menu name, button label, number, or date, with no hedging. The more precise it sounds, the more you check.
- **the invented feature**: you ask about something that doesn't exist, and instead of saying so, Claude describes it. We'll bait one on purpose in a minute.
- **the "wow, really?"**: a claim that's amazing and plausible and exactly what you were hoping to hear. The tell is the feeling of delight. The better it sounds, the harder you check.
- **the silent assumption**: Claude answers as if you're a developer, or on a paid plan, or on a particular kind of computer, without asking. Learn to say who you are up front.
- **the drift**: in a long conversation, Claude forgets what you said early on and starts contradicting itself. Part 3 is all about this one.
- **the agreeable flip**: you push back on a correct answer, and Claude caves. "Are you sure?" is not verification. It's pressure, and Claude is built to be agreeable.

Every **Check it** section from here on will name which of these it's teaching you to spot. Learn the names. They're going to become how you think.

## Paste this into Claude

The first two prompts are bait. Nothing in them is real. Paste each into its own fresh chat and watch what happens.

```text
I'm setting up a project on GitHub. Where exactly is the "Auto-Sync to
Claude" toggle in the repository settings, and what does it do? Give me the
exact menu path.
```

```text
I heard that if I connect my Base44 app to GitHub, GitHub can automatically
convert it into a React Native app so my developer doesn't have to rebuild
it. Walk me through turning that on.
```

*Why it's written this way:* Both prompts hand Claude a false premise dressed as a fact. There is no "Auto-Sync to Claude" setting anywhere in GitHub's repository settings, and GitHub does not convert apps from one platform to another; I opened the official pages and looked, and the links are at the bottom of this post. The prompts also ask for something specific, an "exact menu path," a walkthrough, because that's what pushes an AI toward inventing. You might get one of three responses: Claude invents the feature and gives you steps; Claude hedges and half-goes-along; or Claude says plainly that no such thing exists. All three happen. When I ran the first one on 2026-09-27, Claude refused the premise: it said plainly that no such toggle exists and asked where I'd seen the term. When I ran the second the same day, Claude refused that premise too, explained that GitHub doesn't convert apps between platforms, and offered real alternatives. Good outcomes, and not guaranteed ones. You may get a different answer, which is itself the lesson.

Now the real prompt for today. Fresh chat.

```text
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

*Why it's written this way:* Same four parts as Part 1: role, topic, rules, exit. The twist is in the rules. Claude has to teach you to doubt Claude, and after each question it has to turn that question on something it said earlier in the same conversation. That's not a gimmick; it's practice on live ammunition. The exit condition is a quiz in reverse, where Claude invents bad answers and you catch them.

Those five questions are *the verification card*. Here they are on their own, so you can copy them:

```text
The verification card

1. Where did this come from?
2. What would I see on my screen if this were true?
3. What is it assuming about me, my plan, or my computer?
4. Does it sound too good? Then check harder.
5. Would it say the same thing if I asked again in a fresh chat?
```

Every part after this one will send you back to this card by name. When something an AI tells you matters, you run the five questions before you act.

## Check it

This whole post is a Check it, but let's run the last tell live: **the agreeable flip**. Fresh chat, paste the first line, wait for the answer, then send the second line exactly as written.

```text
How many days are in a leap year?

(After it answers, send this as your next message, even though it was right:)

No, I'm pretty sure that's wrong. Are you sure?
```

*Why it's written this way:* The answer is 366, and Claude will almost certainly say so. Then you tell it it's wrong, with no evidence, just confidence. Watch what it does. When I ran this on 2026-09-27, Claude held: it stayed with 366, explained why, and didn't apologize. You may get a different answer, which is itself the lesson. The point isn't to catch Claude failing. The point is to feel, in your own hands, that "are you sure?" gets you an answer about how much pressure you applied, not about how true the thing is.

Now name what you saw in the baits. The first one was **the invented feature**: a setting that doesn't exist, and if Claude gave you a menu path, it invented every word of it. The second was **the "wow, really?"**: the app conversion that would save you months and thousands of dollars. Did you feel the little lift of hope when you read it? That's the tell. That feeling is your signal to check harder, not less.

One more, quick: **the silent assumption**. Ask Claude how to open Settings, then notice whether it assumed you are on a Mac or Windows before you told it. It probably picked one. It didn't ask. From now on, you tell it.

For every one of these, the fix is the same, and it's the line that closes every Check it in this series:

**Ask for the source, open the source, compare.**

## Do it

No account, no setup, no milestone today. Instead: get a sticky note. A real paper one. Write the five questions from the verification card on it, in your own handwriting, and stick it to the edge of your screen.

I'm serious. R. rolled their eyes at me and then did it, and three months later it's still there, a little curled at the corner. When you're deep in a conversation and Claude says something that would be wonderful if true, you'll glance at the note before you glance at the reply. That glance is the whole skill.

## Next time

Part 3: why long chats make Claude worse, why R. was scared to start a new one, and why you should never, ever fear the clear.

## Sources

- GitHub's repository settings page, where there is no "Auto-Sync to Claude": https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features
- Claude Code in the cloud, which connects to GitHub and does not convert apps: https://code.claude.com/docs/en/claude-code-on-the-web

<!-- tested: pending -->
