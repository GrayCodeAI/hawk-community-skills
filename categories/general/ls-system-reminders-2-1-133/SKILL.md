---
name: ls-system-reminders-2-1-133
description: 'Skill: ls-system-reminders-2-1-133'
license: MIT
tags:
- general
---

## Sub-agent System Reminders

Sub-agents (Explore, File Search, Plan, Code Guide, Status Line) receive their own context via system-reminders in their first user message, with a slimmer structure:

```xml
<system-reminder>
As you answer the user's questions, you can use the following context:
# claudeMd
{{claude_md_content}}

# memory
Contents of MEMORY.md from {{memory_directory}}:
{{memory_index_content}}

# userEmail
The user's email address is {{user_email}}.

# currentDate
Today's date is {{YYYY/MM/DD}}.
</system-reminder>
```

Sub-agents do NOT receive:

- The Skills List (main-agent only — sub-agents can't invoke skills directly).
- The MCP Server Instructions (only main agent and File Search agent).
- The Auto Mode reminder (sub-agents inherit the parent's permission mode but don't re-emit the directive).
- The Plan Mode Active / Plan File Exists reminders.
