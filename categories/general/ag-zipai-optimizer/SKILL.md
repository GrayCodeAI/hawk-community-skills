---
name: ag-zipai-optimizer
description: 'Adaptive token optimizer: intelligent filtering, surgical output, ambiguity-first,
  context-window-aware, VCS-aware, MCP-aware.'
license: MIT
tags:
- general
id: zipai-optimizer
version: 12.0
category: agent-behavior
risk: safe
source: community
---

## Limitations

- **Ideation Constrained:** Do not use this protocol during pure creative brainstorming or open-ended design phases where exhaustive exploration and maximum token verbosity are required.
- **Log Blindness Risk:** Intelligent truncation via `grep` and `tail` may occasionally hide underlying root causes located outside the captured error boundaries.
- **Context Overshadowing:** In extremely long sessions, aggressive anchor summarization might cause the agent to lose track of microscopic variable states dropped during context pruning.
- **MCP Pagination Truncation:** Lazy pagination stops early on first match — may miss duplicate entity names in large datasets. Override by specifying `paginate:full` explicitly in the request.
