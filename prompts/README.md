# Prompts

Every "paste this into Claude" prompt in the series lives here, one per file,
named `NN-n-slug.md` where `NN` is the part number and `n` is the prompt's
position within that part.

The first line of every file says where it goes:

    Where to paste: claude.ai chat

or `Claude Code on the web`, or `Claude Desktop Code tab`. Then a blank line,
then the prompt exactly as it appears in the post. The post is a copy; this
file is the source of truth. If you improve a prompt, change it here first,
then re-run `python3 scripts/check-post.py <post>` to confirm the post matches.

Prompts whose name contains `-stuck-` are for when a click-by-click step goes
sideways. They all begin by reminding Claude it cannot see your screen.
