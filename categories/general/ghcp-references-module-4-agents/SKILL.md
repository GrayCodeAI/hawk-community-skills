---
name: ghcp-references-module-4-agents
description: 'Skill: ghcp-references-module-4-agents'
license: MIT
tags:
- general
---

# Agent Instructions
Your detailed behavior instructions here.
```

## Agent orchestration patterns

1. **Fan-out exploration** — Launch multiple `explore` agents in parallel to answer different questions simultaneously
2. **Pipeline** — `explore` → understand → `general-purpose` → implement → `code-review` → verify
3. **Specialist handoff** — Identify task → `/agent` to pick specialist → review with `/fleet` or `/tasks`

Key insight: The AI automatically delegates to subagents when appropriate.
