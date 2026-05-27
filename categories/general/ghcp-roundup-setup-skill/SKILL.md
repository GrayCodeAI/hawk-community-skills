---
name: ghcp-roundup-setup-skill
description: Interactive onboarding that learns your communication style, audiences,
  and data sources to configure personalized status briefings. Paste in examples of
  updates you already write, answer a few que...
license: MIT
tags:
- general
---

## Edge Cases

### User doesn't have examples to paste
If they say they don't have any recent examples, pivot: "No worries. Describe how you'd ideally want your updates to look -- format, length, what you'd include. I'll work from that description instead."

Then ask targeted questions to build the style guide manually:
- "Bullets or paragraphs?"
- "How long -- a few lines or a full page?"
- "Formal or conversational?"
- "What sections or categories of information would you include?"

### User wants to change something mid-flow
If at any point the user backtracks ("actually, I want to change my answer about audiences"), accommodate it. Adjust your notes and move on. Don't restart from the beginning.

### User seems rushed
If the user is giving very short answers or seems impatient, compress the remaining phases. Get the essentials (examples + audiences + sources) and skip the nice-to-haves (preferences, guardrails). You can always add those later by editing the config.

### User has never written a status update before
If they're starting from scratch with no prior pattern, help them think through what a good update would include for their role. Ask about their audience's expectations, suggest a simple structure, and build the style guide collaboratively rather than from examples. Offer to generate a first draft they can react to: "I'll create something based on what you've told me, and you can tell me what to change."

### Config file already exists
If `~/.config/roundup/config.md` already exists, ask before overwriting: "You already have a roundup config. Want to start fresh, or keep your current setup?" If they want to keep it, offer to open it for manual editing instead.
