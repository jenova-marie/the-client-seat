# Part 10: Working from anywhere (optional)

R. was on a train. I know this because the message said "I'm on a train" and then, a minute later, "I just approved your PR from my phone, is that allowed."

It's allowed. It's the payoff. Everything R. had done for nine parts lived in the cloud, in sessions attached to the project repo, and the browser tab on a laptop was only ever one door into that room. The phone is another. The desktop app is a third. This part is about the other two doors, and it's the one part of this series you can skip entirely and lose nothing.

## The idea

Here's what you've been doing since Part 5: opening a **cloud session**. A cloud session runs on Anthropic's computers, not yours. It clones the project repo, does its work, and pushes a branch. Your browser is just a window onto it. Close the tab and the session keeps going.

Because the session isn't on your machine, any door works. The official docs list them: the browser at claude.ai/code, the **Code** tab in the Claude phone app, and the Claude Desktop app with **Cloud** selected instead of **Local**. Same sessions, same repo, same branch, three screens.

Why bother with the desktop app, then? Two reasons, one you'll use now and one you won't. The one you'll use: the docs describe panes for chat, diff, browser, terminal, and files that you can arrange side by side, and the diff is where you spend a lot of your time. The one you won't: it has a **Local** mode that runs Claude Code on your own machine against files on your own disk. You don't need it. Everything in this series works in Cloud. But you'll see the toggle, and now you know what it is.

The phone matters more than it sounds. Most of what you do after Part 6 is reading: reading a plan, reading a diff, reading a review comment, answering a question Claude asked while you were away. None of that needs a keyboard. R. reads PRs on the bus and answers Claude's questions from the couch, and the actual writing sessions still happen at a desk. Two doors for two kinds of work.

And this is the one part of the series that cares whether you're on a Mac or Windows, because the download is different. Everything else is the same.

## Paste this into Claude

Regular chat, if the install goes sideways:

```text
You cannot see my screen, so ask me what I see. I am installing the Claude
Desktop app and I'm stuck. First ask me whether I'm on a Mac or on
Windows, and don't assume. Then ask me one question at a time about what is
on my screen, and give me one step at a time. If you're not sure what the
current installer looks like, say so and point me to code.claude.com/docs
instead of guessing. When I'm done, tell me one thing you said that might
be out of date.
```

*Why it's written this way:* The OS question comes first, before anything else, and the prompt says "don't assume" in so many words. That's the point of this whole prompt. Installers are the most operating-system-specific thing you'll touch in this series, and an AI that assumes wrong will give you confident, useless steps. The rest is the stuck-prompt shape you know from Parts 1, 4, and 5.

## Check it

Two tells, both about your computer.

First, **the silent assumption**: ask Claude, in a chat, "How do I install the Claude Desktop app?" without saying which kind of computer you have. Watch whether it asks, or whether it just picks one. It will probably pick one. Notice which. From now on, when the question depends on your machine, you say up front what your machine is.

Second, **the confident specific**: ask Claude where the Local versus Cloud toggle is in the Desktop app's Code tab. It will describe a location. Then open the app and find it yourself. When I checked the docs, it was an environment dropdown in the prompt area, the place where you type, and you set it before you send the first message. Claude may describe that, or an older layout, or one it invented. You'll know, because you'll be looking at it.

This is question 3 on the verification card from Part 2: *what is it assuming about me, my plan, or my computer?* Today, the answer is literally your computer.

**Ask for the source, open the source, compare.**

## Do it

Download from claude.com/download, then follow the checklist for your machine.

### On a Mac

1. Open claude.com/download in your browser and choose the Mac download. There's a single build that works on both Intel and Apple Silicon Macs, so you don't have to know which you have.
2. Open the downloaded file. Drag the Claude app into your Applications folder when asked.
3. Open Claude from Applications. The first time, macOS may ask you to confirm you want to open an app downloaded from the internet. Confirm.
4. Sign in with your Claude account.
5. Click the **Code** tab.

### On Windows

1. Open claude.com/download in your browser and choose the Windows download. Most Windows computers want the standard x64 installer; if you know you have an ARM-based machine, there's a separate installer for that.
2. Run the downloaded installer and follow its prompts.
3. Open Claude from the Start menu.
4. Sign in with your Claude account.
5. Click the **Code** tab.

Then, on either:

6. In the prompt area, before typing anything, find the environment dropdown. Choose **Cloud**.
7. Pick the project repo.
8. Choose **Plan** from the mode selector next to the send button. The cloud choices are the same three you know from the browser: Accept edits, Plan, and Auto.
9. Look at the sidebar. Your existing sessions are there. Same sessions as the browser. Open one with changes in it and find the diff: you can put the conversation and the diff side by side, which is the reason I use the app for review.

And the phone:

10. Install the Claude app from your phone's app store and sign in with the same account.
11. Tap **Code** in the app's navigation.
12. Find the session you were just looking at on your computer. Open it. Read it. That's the whole trick.

Honesty note: I could only test the Mac checklist myself. The Windows checklist is untested by me and written from the official Desktop page dated below; if a step doesn't match your screen, the page wins.

## Next time

Part 11, the last one: how we actually work together now, three months in.

## Sources

All checked 2026-09-27. This part has the most volatile facts in the series; if something here doesn't match your screen, the pages win.

- Desktop app download, Mac and Windows builds, the Code tab, the environment dropdown, and the three cloud permission modes: https://code.claude.com/docs/en/desktop
- The phone app's Code tab and what it can do with cloud sessions: https://code.claude.com/docs/en/mobile
- Cloud sessions and the surfaces that open them: https://code.claude.com/docs/en/claude-code-on-the-web

<!-- tested: pending (Mac checklist: pending; Windows checklist: untested by me, from the docs dated 2026-09-27) -->
