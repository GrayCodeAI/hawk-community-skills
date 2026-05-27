---
name: copilot-roundup
description: Generate personalized status briefings on demand. Pulls from your configured
  data sources (GitHub, email, Teams, Slack, and more), synthesizes across them, and
  drafts updates in your own communicat...
license: MIT
tags:
- general
---

## When Something Goes Wrong

### Config seems outdated
If the config references repos that return errors or tools that aren't available, note which sources you couldn't reach and generate from what you could access. At the end, suggest: "Some of your configured sources seem out of date. You might want to re-run roundup-setup to refresh things."

### No config file
Tell the user to run setup first. Don't try to generate without a config.

### User asks for an audience not in the config
If they ask for an audience that isn't defined in the config, offer two options: generate using their default style (best guess), or add the new audience to the config first by running a quick follow-up: ask what this audience cares about, detail level, and any format preferences, then append to the config file.

### User seems unsure how to use roundup
If the user invokes roundup but seems uncertain (vague request, asks "what can you do?", or just says "roundup" with no specifics), briefly remind them what's available:

"Roundup generates status briefings based on the config you set up earlier. Just tell me who it's for and what time period to cover. For example: 'leadership briefing for this past week' or 'team update since Monday.' I'll pull the data and draft it in your style."

Then ask which audience they want to generate for.

### User wants to iterate on the draft
If they want to go back and forth refining, support that. Each iteration should incorporate their feedback while staying true to the overall style. Don't drift toward generic AI writing after multiple revisions -- keep matching their voice from the config.

### User forgot what's configured
If they ask what audiences, sources, or preferences are set up, read the config and give them a quick summary rather than telling them to go find the file. Offer to adjust anything on the spot.
