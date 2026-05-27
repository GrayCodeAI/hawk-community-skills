---
name: neo-context-engineering
description: Understand the components, mechanics, and constraints of context in agent
  systems. Use when writing, editing, or optimizing commands, skills, or sub-agents
  prompts.
license: MIT
tags:
- general
---

# 50 different review checklists crammed together
```

**Skill Optimization**
Skills load their descriptions by default, so descriptions must be concise:
```markdown
# Good: Concise description
description: Analyze code architecture. Use for design reviews.

# Avoid: Verbose description that wastes context budget
description: This skill provides comprehensive analysis of code
architecture including but not limited to class hierarchies,
dependency graphs, coupling metrics, cohesion analysis...
```

**Sub-Agent Context Design**
When spawning sub-agents, provide focused context:
```markdown
# Coordinator provides minimal handoff:
"Review authentication module for security issues.
Return findings in structured format."

# NOT this verbose handoff:
"I need you to look at the authentication module which is
located in src/auth/ and contains several files including
login.ts, session.ts, tokens.ts... [500 more tokens of context]"
```

## Guidelines

1. Measure before optimizing--know your current state
2. Apply compaction before masking when possible
3. Design for cache stability with consistent prompts
4. Partition before context becomes problematic
5. Monitor optimization effectiveness over time
6. Balance token savings against quality preservation
7. Test optimization at production scale
8. Implement graceful degradation for edge cases
