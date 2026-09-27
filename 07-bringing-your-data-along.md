# Part 7: Bringing your data along

R. exported everything from Base44. All of it: every client, every appointment, every note anyone had ever typed into a text box. It came down as one big spreadsheet file, and R., who had just learned how to upload a file to a repo, was about to drag the whole thing into the project.

My stomach dropped. I typed "WAIT" in all caps, which I try never to do, and then I called.

Nothing bad happened. The file never left R.'s laptop. But it was close enough that I wrote this part the same night, and I'm going to say the rule before I say anything else.

## The idea

**Never put real user data in a repo.**

Not a sample of it, not "just the first hundred rows," not "it's a private repo." Repos get cloned onto laptops, forked, backed up, indexed by tools, and read by AI assistants. A repo is the most durable, most copied thing in a software project. That's the whole point of it, and it's exactly why your users' names and phone numbers can never go in one. Your developer does not need your users. Your developer needs the *shape* of your data, and a realistic fake sample of it.

Three ideas make that possible.

**Data has a shape.** Every export is rows and columns. The columns have names, and each column holds one kind of thing: a date, a number, a yes-or-no, a bit of text. That shape is what your developer needs to build the new database, and it contains no secrets at all. The column called `signup_date` is not private. The dates in it, attached to names, are.

**Exports are snapshots.** The file you download is your data as of that moment. It's not connected to the app. Change something in the app tomorrow and the file won't know. That's fine for a sample. It's important to remember when someone asks "is this current?"

**Bad data is normal, and findable.** Every real export has empty cells, dates in two formats, a duplicate, a number someone typed with a dollar sign. This isn't a failure. It's information your developer needs early, and Claude is good at finding it.

## Paste this into Claude

The first prompt goes in a regular claude.ai chat, with your real export open next to it, before anything touches the repo.

```text
I exported data from my app and I want to give a small SAMPLE of it to my
developer through our shared repo. The rule is: no real user information
ever goes in the repo. Help me build a fake sample.

I will paste only the column names and three rows. Before I do, tell me
which kinds of columns are personal (names, emails, phones, addresses,
anything that identifies a person) so I can blank those out before pasting.

Then, once I paste:
- Produce a sample of five rows with the same columns, where every personal
  value is obviously fake (like "Person One", or an email address at
  example dot com) and every other value looks realistic but is not copied
  from my real rows.
- Keep the column names exactly as they are.
- Tell me if any column looks personal that I missed.
- Give me the result as CSV text in a code block so I can copy it.
- Then tell me one thing you assumed about my data that I should check.
```

*Why it's written this way:* The rule is stated first, to Claude, in the prompt. Then the two-step: Claude tells you which columns are personal *before* you paste anything, so you can blank them out on your side. Even in a chat, the less real data you paste, the better. "Obviously fake" matters: a sample full of realistic-looking names is a sample somebody will one day mistake for real. When Claude writes the fake email addresses, it will produce real-looking ones ending in the standard example domain; that's fine in the sample, and it's why I spelled it out in words here instead of typing one. Tested on 2026-09-27.

The second and third prompts go in a Claude Code session, Plan mode, after the sample file is in the repo (see Do it).

```text
There is a new file at data/sample.csv. I know what every column means; you
don't. Interview me, one column at a time: ask me what it means, where it
comes from, and whether it's required. Don't guess, and don't skip any.

When you've asked about every column, propose a plan for data/README.md
with a one-line description per column, in my words, and show me the
outline before writing. Do not touch any other file. When done, tell me one
column description you are least sure you got right.
```

*Why it's written this way:* Interview, outline, approve, write: the pattern from Part 6, aimed at a data file. "I know what every column means; you don't" is the most important sentence, because it's true, and because Claude will otherwise guess. The result is a README that describes your data in your words, which is the single most useful document you can give a developer.

```text
Read data/sample.csv and data/README.md. Do not change anything. Report,
in plain language, anything that looks wrong: empty cells, values that
don't match the column's description, dates in different formats,
duplicates, or numbers that look like text. For each one, say which row
and column, and how sure you are. End with the one issue you'd fix first if
this were real data, and why.
```

*Why it's written this way:* Report, don't fix. Row and column for every finding, so you can go look. A confidence level for each, so you know which to check first. And the closing question turns a list into a priority. Tested on 2026-09-27.

## Check it

Today's tell is **the confident specific**, on column meanings. Claude will look at a column called `status` and tell you, confidently, that it's the client's account status. Maybe. Or maybe in your app it means whether the appointment is confirmed. You know. It doesn't. In the interview, when Claude proposes a meaning before asking, that's the tell, and your job is to correct it every time.

Second exercise: take Claude's bad-data report and pick two findings. Open the sample file and check them yourself, row and column. Did the empty cell exist? Was the date really in a different format? Claude is usually right about these, and you should know that from having looked, not from having been told.

This is question 4 on the verification card from Part 2: *does it sound too good? Then check harder.* A clean bill of health on a real export is too good.

**Ask for the source, open the source, compare.**

## Do it

1. **Export from Base44.** In your app editor, open Dashboard, then Data, choose the table you want, open the more-actions menu, and choose Export. You get a CSV file. Keep it on your computer. It does not go in the repo.
2. **Build the fake sample.** Open the CSV in a spreadsheet, copy the header row and three rows with the personal cells blanked out, and run the scrub prompt in a chat. Paste the five-row result into a plain-text editor (not a word processor, which adds formatting) and save it as `sample.csv`. If that's fiddly on your machine, skip to the fallback in step 3 and let Claude write the file.
3. **Upload it to the repo on a new branch.** Cloud sessions can't see your laptop, so this step goes through GitHub's website. Open the project repo, go into the `data/` folder (or ask your developer to create it), click **Add file**, then **Upload files**, and drop `sample.csv` in. Write a short commit message. Choose the option to **create a new branch for this commit**, and click **Propose changes**. If the file is tiny, the fallback is to paste the CSV text into a Claude Code session and ask Claude to write it to `data/sample.csv`.
4. **Open a session on that branch.** At claude.ai/code, pick the project repo, switch the branch selector to your new branch, choose Plan mode.
5. Paste the README interview prompt. Answer every column. Approve the plan. Read the diff.
6. Paste the bad-data prompt. Read the report. Check two findings yourself.
7. Run the continuation prompt from Part 6. Then **Create PR**, with a description that says this is a fake sample and what you'd like your developer to look at.

## Sidebar for the developer

Make the rule mechanical. A `.gitignore` entry or a PR check that rejects anything under `data/` beyond a few hundred rows, and one sentence in CONTRIBUTING.md saying that `data/` holds samples only, means the day someone drags the wrong file in, the tool says no before you have to.

## Next time

Part 8: reading code without being a coder. You're going to ask the app how it works, and it's going to tell you.

## Sources

- Exporting a Base44 table as CSV: https://docs.base44.com/Building-your-app/Managing-your-app-data
- Uploading a file through GitHub's website, including the new-branch option: https://docs.github.com/en/repositories/working-with-files/managing-files/adding-a-file-to-a-repository
- Cloud sessions run in an isolated environment that does not see your computer: https://code.claude.com/docs/en/claude-code-on-the-web

<!-- tested: pending -->
