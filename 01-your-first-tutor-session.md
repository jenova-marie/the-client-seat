# Part 1: Your first tutor session

On our first real call, after the contract and the timeline and the part where I explain that "backend" is not a body part, I asked R. the question I ask every client: "What do you want to learn first?"

I expected "how the new app will look." Maybe "what a database is." R. thought about it and said, "Honestly? What an AI even is. Everyone keeps telling me to use it and I nod and I have no idea what's actually happening."

I almost laughed, and then I didn't, because it was the right answer. R. was about to spend months working alongside an AI. Of course the first lesson should be about the thing doing the teaching. So that's where we started, and that's where you start too.

## The idea

An AI chat is not a search engine. A search engine finds pages that already exist and hands them to you. An AI chat writes new sentences, one word at a time, that are shaped like a good answer. Usually they *are* a good answer. Sometimes they're a beautifully shaped wrong one. We'll spend all of Part 2 on that.

It's also not a person, even though talking to it feels like talking to one. It doesn't know you. It doesn't remember yesterday unless you remind it. It has no idea whether what it just said is true.

Here's what it is very, very good at: explaining. It can take any idea and explain it to you at your level, in your words, using the things you already understand, and it never gets tired of you asking again. That's a tutor. A tutor who happens to be terrible at knowing when they're wrong, so you'll learn to check.

One more thing that matters more than anything else in this series: **it follows the rules you give it.** If you say "ask me one question at a time and wait," it will. If you say "don't explain anything until you've asked what I already know," it won't. So give it rules.

The text you paste into Claude to start a conversation is called a **prompt**. That's the whole definition: a prompt is what you say to it. Every prompt in this series has four parts, and I want you to learn their names, because you'll be writing your own soon:

1. **The role.** Who Claude is in this conversation. "You are my patient tutor."
2. **The topic.** What you want to understand today.
3. **The rules for how we work.** How the conversation should go. One question at a time. Wait for me. Don't move on until I answer.
4. **The exit condition.** How you'll both know you're done. "When I can explain it back in my own words, quiz me."

That's it. Role, topic, rules, exit. Everything else is decoration.

## Paste this into Claude

Open claude.ai, start a new chat, and paste this whole box. Don't retype it; copy it. If you don't have an account yet, skip to **Do it** below, then come back.

```text
You are my patient tutor. I am a complete beginner and I learn best by
conversation, not lectures.

The thing I want to understand today is: what an AI chatbot actually is,
what it's good at, and what it's bad at.

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

*Why it's written this way:* The first line is the **role**, and "patient" is doing real work there; it changes the tone of everything after. The second paragraph is the **topic**. The bulleted list is the **rules**, and notice that the first rule forbids Claude from explaining anything until it has asked about your life. That's on purpose. An explanation built on what you already know sticks; one built on somebody else's analogy slides right off. The last paragraph is the **exit condition**, plus the line I want you to put at the end of every prompt you ever write: tell me one thing to double-check, and where. That line is Claude admitting, on the record, that it might be wrong. Make it a habit and Part 2 will be easy. Tested on 2026-09-27.

Then try it again with any topic you've been curious about for years. Change the sentence after "The thing I want to understand today is:" and leave everything else alone. Compound interest. How vaccines work. Why the sky is blue. Whatever you've been nodding along to at dinner parties.

## Check it

Here's your first **tell**, the name I'll use in every part for a sign that Claude might be guessing: **the confident specific**. An exact name, an exact number, an exact date, delivered with total confidence and no hedging. Confident specifics are where AI is most often wrong, precisely because they sound so sure.

Try this inside your tutor session, right in the middle of the lesson:

1. Ask Claude: "What is today's date?"
2. Ask Claude: "What is the newest Claude model?"
3. Now look at the actual date on your phone. Then look at the model picker in the claude.ai interface, usually a small dropdown near the message box, and see which model is selected and what others are listed.

Compare. Claude may get the date right, or it may guess from when its training ended. It may name a model that's no longer the newest, or hedge and say it can't be sure. Any of those outcomes is fine. The lesson is that you had a way to check, and you used it. Claude answered from memory; you answered from the screen in front of you.

**Ask for the source, open the source, compare.**

## Do it

Today's milestone: a free Claude account.

1. Go to claude.ai in your browser.
2. Choose the sign-up option. You can continue with an email address, or with a Google account if you'd rather; those are the two options the help center lists.
3. Use an email you actually check, because you'll need to verify it.
4. Claude will ask for a phone number that can receive a text message. This isn't optional; Anthropic requires it for every new account, and it has to be a real mobile number, not an internet phone number or a landline. Enter the code they text you.
5. You're in. You'll land in a chat window with a message box at the bottom. That's where prompts go.

You do not need to pay for anything. The free plan lets you chat, and that's all Parts 1 through 4 use.

If you get stuck, this is your first "paste this if you get stuck" prompt. Since it's about creating an account, you'll need somewhere to paste it: a friend's Claude, or your own chat once you get past the first screen. If you can't get into Claude at all, this one is for a friend's Claude or for after you get past the first screen.

```text
You cannot see my screen, so ask me what I see. I am trying to create a free
Claude account at claude.ai and I am stuck. Ask me one question at a time
about what is on my screen right now, and give me one step at a time. Do not
guess at button names; if you are not sure what a button is called, tell me
to describe what I see instead. When I am done, tell me one thing you told me
that might be out of date, and where to check.
```

*Why it's written this way:* The very first sentence is the most important one, and every stuck prompt in this series starts with it: **Claude cannot see your screen.** It will happily describe a button that isn't there unless you tell it to ask you first. "One step at a time" stops it from dumping a ten-step list you'll lose your place in. And the last line is our double-check habit again, aimed at the thing most likely to be stale: interface details.

## Next time

Part 2, where I bait Claude into inventing a feature that doesn't exist, on purpose, so you can watch exactly what it looks like when it lies to you.

## Sources

- Phone verification is required for every new account: https://support.claude.com/en/articles/8287232-verify-your-phone-number
- Getting started and the age requirement: https://support.claude.com/en/articles/8114491-get-started-with-claude
- Signing in with email or Google: https://support.claude.com/en/articles/13189465-log-in-to-your-claude-account
- What the free plan includes (chat on web, desktop, and mobile): https://www.claude.com/pricing
- Creating a GitHub account (you'll need this in Part 4, not today): https://docs.github.com/en/get-started/start-your-journey/creating-an-account-on-github

<!-- tested: pending -->
