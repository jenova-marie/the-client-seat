# "Getting Started Making Claude Do Everything" — Series Design

**Date:** 2026-09-26
**Author:** Jenova (with Claude)
**Status:** approved design, ready for planning

## 1. Purpose

A twelve-part (0 through 11) blog tutorial that teaches a non-technical reader how to use AI as
a tutor to educate themselves on any subject, and how to recognize when the AI
is wrong. The worked example is real: onboarding a remote client onto the
rebuild of their Base44 app as an Expo app, API, and cloud backend, so they can
contribute design docs, vision docs, and data files to the project repo through
Claude Code on the web.

The tools are the example. Self-education with AI, and verification of what AI
says, is the subject.

## 2. Reader

- Total non-technical. Has never opened a terminal and may not know what a
  repo is.
- Has used Base44 or similar no-code tools, so understands "an app I made."
- Any OS. The series is browser-first and never depends on Mac vs Windows,
  with one named exception: Part 10 (optional Desktop app install) has separate
  Mac and Windows checklists.
- Prototypical reader is the author's client, anonymized as **"R."** The app is
  always "the app." The repo is always "the project repo."

## 3. Voice

First person, the author's own persona: warm, sparkly, a little queer-fem-tech-
queen, zero condescension. The reader is "you." The author tells the real story
of onboarding R. with names and identifying details removed.

Pull quote, attributed to Jenova, introduced in Part 3 and quoted back in
Part 8 when sessions become study notes:

> **Don't fear the clear!**

## 4. Delivery path being taught

Claude Code on the web (cloud sessions), with the **"viewer" posture**
defined as: work in Plan mode, read the plan Claude proposes, approve it,
review the diff, open a pull request, and let the developer merge. There is no
enforced read-only mode. Plan mode makes Claude ask first; branch protection
and PR review make the developer the only one who can change `main`.

Bootstrap milestones, in order:

1. Free claude.ai account. This is all Parts 1 through 4 need.
2. GitHub account.
3. Developer sidebar (not reader tasks): install the Claude GitHub App on the
   project repo, add the reader as a collaborator with write access, and
   protect `main` so that changes require a reviewed pull request and the
   reader cannot merge their own work.
4. Reader accepts the collaborator invitation, upgrades to Pro or takes a seat
   on the developer's Team plan, signs in at claude.ai/code with GitHub, opens
   the repo, and selects Plan mode. Pro is needed here because Claude Code on
   the web is not on the free plan (re-verify at writing time).
5. Contributions land as branches and pull requests that the developer
   reviews and merges.

Explicitly out of scope: `gh` CLI, cloning, terminals, SSH remotes, Cowork mode.
Claude Desktop appears only as an optional later post (Part 10).

## 5. Series structure (approach B: concept-first, milestone-paced)

Each part teaches one concept via paste-in prompts. The setup milestone is the
reward for understanding the concept. Verification is a recurring section in
every part.

| # | File | Working title | Concept | Milestone |
|---|------|---------------|---------|-----------|
| 0 | `00-why-learn-with-ai.md` | Why I'm making my client learn with AI | The series contract: paste-this prompts, the verification habit | none |
| 1 | `01-your-first-tutor-session.md` | Your first tutor session | How to ask AI to teach you and quiz you back | Free claude.ai account |
| 2 | `02-catching-claude-being-wrong.md` | Catching Claude being wrong | Hallucinations, assumptions, invented features, "wow, really?", cross-checking | none; the immune system |
| 3 | `03-dont-fear-the-clear.md` | Don't fear the clear | Context: what it is, why it fills, clear vs compact, the CONTINUATION.md ritual | First claude.ai Project with a CONTINUATION.md |
| 4 | `04-what-a-repo-actually-is.md` | What a repo actually is | Version control, history, branches, why not Dropbox | GitHub account |
| 5 | `05-joining-the-project.md` | Joining the project | Collaborators, the Claude GitHub App, Plan mode as "viewer" | Pro or Team seat, connected at claude.ai/code, repo open |
| 6 | `06-your-first-contribution.md` | Your first contribution | Branches, diffs, pull requests | Vision doc in `docs/`, first PR |
| 7 | `07-bringing-your-data-along.md` | Bringing your data along | Data shapes, exports, spotting bad data, never real user data in a repo | Scrubbed Base44 sample uploaded via GitHub web into `data/`, second PR |
| 8 | `08-reading-code-without-being-a-coder.md` | Reading code without being a coder | Asking the codebase questions, sessions as study notes | none |
| 9 | `09-teach-claude-a-skill.md` | Teach Claude a skill | A skill is a saved prompt with a name, living in the repo; Claude uses it by description or by `/name` | `.claude/skills/continuation/SKILL.md` in the repo, third PR |
| 10 | `10-working-from-anywhere.md` | Working from anywhere (optional) | Desktop app Code tab, Local vs Cloud toggle, mobile app | Desktop installed |
| 11 | `11-how-we-work-together-now.md` | How we work together now | The PR review loop between developer and client | ongoing |

Part 0 is the prologue. It is shorter than the rest and does not follow the
post skeleton: it has an opening beat, the series contract (what "paste this"
means, why every post has a Check it section, how to read the series), and a
Next time line. No concept section, no prompts, no milestone.

## 6. Post skeleton

Every part uses the same shape, in this order:

1. **Opening beat** (100–200 words). A moment from the real project.
2. **The idea.** One concept in plain language. Every jargon word is defined
   the first time it appears. Framed as why it matters to the reader, not to
   developers.
3. **Paste this into Claude.** One to three prompts in fenced code blocks,
   each designed to make Claude teach interactively. A short note under each
   prompt explains why it is written that way.
4. **Check it.** The verification ritual for this part: one concrete thing to
   cross-check, one trap to try on purpose, and the tell that shows Claude is
   guessing.
5. **Do it.** The setup milestone as a click-by-click checklist, with a
   "paste this if you get stuck" prompt instead of screenshots.
6. **Sidebar for the developer.** Only where needed. What the author had to do
   on their side.
7. **Next time.** One sentence linking forward.

Length: 1,200 to 1,800 words per post including prompts. Part 0 may be shorter.

## 7. Prompt design rules

Every paste-in prompt follows these rules:

- **Four parts:** a role ("you are my patient tutor"), the concept, an
  interaction rule (ask one question at a time, wait for my answer, do not
  move on until I have it), and an exit condition ("when I can explain it back
  in my own words, give me a three-question quiz").
- **Pulls from the reader's world.** The prompt tells Claude to ask what the
  reader already knows and build the analogy from that. No baked-in analogies.
- **Honest about being a prompt.** The note under each prompt explains the
  design so the reader learns prompt writing by osmosis.
- **Never does the setup for the reader.** Prompts explain and coach; the
  reader clicks. Posts say plainly that Claude in a chat cannot see the
  reader's screen.
- **Ends with a "make it doubt itself" line.** For example: "At the end, tell
  me one thing you said that I should double-check, and where to check it."
- **Tested.** Each prompt is run once in a fresh session before the post
  ships, and adjusted until it behaves. Parts 1 through 4 are tested in a new
  claude.ai chat conversation. Parts 5 through 8 are tested in a new Claude
  Code on the web session against a throwaway repo. Part 9 is tested in the
  Desktop app Code tab.

Every prompt is stored as its own file under `prompts/` and embedded in the
post by copy. The `prompts/` file is the source of truth.

## 8. The verification thread

Part 2 is the dedicated post. Every part's **Check it** section advances the
same skill using a small set of named **tells**, introduced one or two at a
time and referred back to by name:

- **The confident specific.** Exact menu names, button labels, or version
  numbers with no hedging. Check against the official page.
- **The invented feature.** Ask about something that does not exist and see
  whether Claude invents it. Part 2 does this on purpose with a fake GitHub
  setting.
- **The "wow, really?"** A claim that sounds amazing and plausible but cannot
  be true ("GitHub will convert your Base44 app to React Native for you,"
  "Claude can log into your account and set this up"). The tell is the feeling
  of delight. The more it sounds like exactly what you wanted to hear, the
  harder you check. Part 2 baits one live.
- **The silent assumption.** Claude answers as if you are on Mac, on a paid
  plan, or a developer. Learn to state your situation up front.
- **The drift.** Long conversations where Claude forgets what you said early
  on. Learn to restate context. Leads directly into Part 3.
- **The agreeable flip.** Push back on a correct answer and watch Claude cave.
  "Are you sure?" is not verification.

Standing habit that closes every **Check it**: **ask for the source, open the
source, compare.** Sources for this series are always official docs:
claude.ai help center, code.claude.com docs, docs.github.com. Each post links
the exact pages it depends on.

Part 2 gives the reader a **verification card**: five questions to ask before
acting on anything an AI says. Later posts refer back to it by name.

1. Where did this come from? (Ask for the source. Open it.)
2. What would I see on my screen if this were true?
3. What is it assuming about me, my plan, or my computer?
4. Does it sound too good? Then check harder.
5. Would it say the same thing if I asked again in a fresh chat?

## 9. Part 3 detail: Don't fear the clear

- **Concept.** Context is Claude's working memory for one conversation. It
  fills up, gets noisy, and a full context is where drift, forgotten
  instructions, and "wow, really?" answers come from.
- **Taught by prompt.** A session where the reader watches context fill, then
  asks Claude to summarize what it still remembers and compares that to what
  they actually said.
- **The rules.** Clear when the task changes. Compact when the task continues
  but the chat is long. Anything worth keeping goes into a file or a project
  doc, never "remembered" by the chat. Taught first in claude.ai chat (new
  conversation, Projects), then previewed for Claude Code. In Claude Code the
  equivalents are `/clear` and `/compact` in local sessions; in cloud sessions
  the reader's equivalent of clear is starting a new session. Re-verify which
  commands cloud sessions support at writing time. CLAUDE.md is mentioned as
  the developer's file that survives, and the reader is told not to edit it.
- **The CONTINUATION.md ritual.** The practical half of "don't fear the
  clear." Before clearing, the reader pastes a prompt that has Claude write a
  short `CONTINUATION.md`: what we are working on, what has been decided, what
  is still open, and the exact next step. The reader saves it (in the Project,
  and later in the repo). After clearing, the first message of the new
  conversation is "Here is my CONTINUATION.md, pick up from here" with the file
  pasted or attached. The prompt for writing it is stored in `prompts/` and
  reused by name in Parts 6, 7, and 8, where it becomes a file Claude Code
  writes into the repo itself at `docs/continuations/<name>-CONTINUATION.md`,
  one file per collaborator, so two people's continuations never collide.
  In Part 9 the prompt becomes a repo skill, so the reader never pastes it
  again.
- **Check it.** Two checks. First, read the CONTINUATION.md before clearing
  and fix anything Claude got wrong or left out; the reader is the editor,
  not the chat. Second, after a compact or a continuation, ask Claude to
  restate the three most important facts and check them against your notes.
- **Milestone.** Create a first claude.ai Project as "the thing that survives
  the clear," and save a first `CONTINUATION.md` into it.

## 10. Part 7 detail: Bringing your data along

- **Concept.** Data has a shape (rows, columns, types), exports are snapshots
  not live links, and bad data is normal and findable.
- **Hard rule, stated before anything else.** Never put real user data in a
  repo. The reader exports from Base44, then has Claude help them build a
  small scrubbed sample: a handful of rows, real column names, fake values.
  Names, emails, phone numbers, addresses, and anything identifying are
  replaced, not merely trimmed. The developer sidebar explains why (repos get
  cloned, forked, and backed up).
- **Mechanism.** The cloud sandbox cannot see the reader's laptop. The taught
  path is GitHub's web upload ("Add file" then "Upload files") into `data/`
  on a new branch, which also teaches the GitHub UI. Fallback for small
  samples: paste the CSV text into the Claude Code session and have Claude
  write the file. Re-verify at writing time whether claude.ai/code supports
  attaching files directly; if it does, that becomes the primary path.
- **Prompts.** One that interviews the reader about what each column means and
  writes `data/README.md`; one that scans the sample for bad data (empty
  cells, inconsistent formats, duplicates) and reports without fixing.
- **Check it.** The "confident specific" on column meanings: Claude will guess
  what an ambiguous column means. The reader knows the app; Claude does not.

## 11. Part 9 detail: Teach Claude a skill

- **Concept.** A skill is a saved prompt with a name and a one-line
  description, stored in the repo at `.claude/skills/<name>/SKILL.md`. Claude
  reads the descriptions and uses a skill when the task matches, or the
  reader calls it by `/name`. Skills are markdown, so a docs contributor can
  write one. This is the reader's first file that changes how Claude behaves.
- **Why here.** It closes the continuation arc: Part 3 pastes the prompt,
  Part 6 writes the file into the repo, Part 9 turns the prompt into a skill.
- **Prompts.** A chat tutor on what a skill is and is not; a Claude Code
  session that interviews the reader for the skill's name and description,
  shows the plan, writes only `.claude/skills/continuation/SKILL.md`; a
  first-use test in a fresh session after merge.
- **Check it.** The "confident specific" on the SKILL.md format: Claude will
  state frontmatter fields with confidence; check them against the skills
  docs page. The "wow, really?": a skill cannot give Claude abilities it does
  not have (reading your email, seeing your screen); it only changes what
  Claude does with abilities it already has.
- **Milestone.** Third PR: the continuation skill. After merge, run it in a
  fresh session and confirm it writes the continuation file.
- **Developer sidebar.** Review skills like code, because they steer Claude.
  Keep them small. Port the parts of any plugin you want the reader to have
  (for example a brainstorming skill) as repo skills, since cloud sessions
  do not load plugins.

## 12. File layout

```
claude-do-everything/
  README.md                          series index, reading order, one-line summaries
  00-why-learn-with-ai.md
  01-your-first-tutor-session.md
  02-catching-claude-being-wrong.md
  03-dont-fear-the-clear.md
  04-what-a-repo-actually-is.md
  05-joining-the-project.md
  06-your-first-contribution.md
  07-bringing-your-data-along.md
  08-reading-code-without-being-a-coder.md
  09-teach-claude-a-skill.md
  10-working-from-anywhere.md
  11-how-we-work-together-now.md
  prompts/                           one .md per paste-in prompt, named NN-n-slug.md
                                     (NN = part, n = prompt number within the part)
  docs/superpowers/specs/            this spec
```

Plain markdown. No frontmatter. Source of truth stays here.

**Publishing target: Medium.** Medium does not accept markdown, so each post
is rendered to HTML and pasted into the Medium editor as rich text, then each
prompt box is checked to confirm it landed as a Medium code block. Because of
this, posts contain no markdown tables (Medium has none); the README's table
is fine because it is not published. Medium's "Import a story" tool is not
used, since it strips line breaks inside code blocks.

**Developer-side tooling note.** Cloud sessions do not load plugins, so
anything the developer wants the reader to have in Claude Code (a continuation
command, a self-review skill) is committed into the repo under `.claude/`
(skills, commands, CLAUDE.md), which cloud sessions do honor. Developer
sidebars in Parts 5, 6, 9, and 11 may mention this; the reader never installs
anything.

## 13. Definition of done (per post)

- Follows the skeleton in section 6, 1,200 to 1,800 words (Part 0 excepted).
- Every prompt lives in `prompts/` and has been run once in a fresh Claude
  session.
- Every product claim links to an official doc page that was actually opened
  while writing.
- Client and repo anonymized per section 2.
- Voice per section 3 throughout.
- Names the tells it uses, per section 8, and links back to the verification
  card.
- Part 7 only: the sample data in the post and in `data/` contains no real
  user records.

## 14. Order of work

1. This spec.
2. `README.md` and Part 0, so the voice can be checked early.
3. Parts 1 through 11 in order, one at a time, with a review pause after each.

## 15. Reference pages the series depends on

- https://code.claude.com/docs/en/claude-code-on-the-web
- https://code.claude.com/docs/en/web-quickstart
- https://code.claude.com/docs/en/desktop
- https://code.claude.com/docs/en/mobile
- https://code.claude.com/docs/en/remote-control
- https://code.claude.com/docs/en/feature-availability
- https://code.claude.com/docs/en/skills
- https://code.claude.com/docs/en/cloud-environments
- https://support.claude.com (plans, Projects, account creation)
- https://docs.github.com (account creation, collaborator invitations,
  branch protection rules, uploading files via the web, pull requests)

Facts to re-verify at writing time for each post, since they change: which
plans include Claude Code on the web, which permission modes and slash
commands exist in cloud sessions, whether cloud sessions accept file
attachments, and the exact Local vs Cloud toggle location in the Desktop Code
tab.
