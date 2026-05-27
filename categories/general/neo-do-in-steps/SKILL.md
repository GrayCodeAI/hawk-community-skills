---
name: neo-do-in-steps
description: Execute complex tasks through sequential sub-agent orchestration with
  intelligent model selection, meta-judge → LLM-as-a-judge verification
license: MIT
tags:
- general
argument-hint: Task description (e.g., "Refactor UserService class and update all
  consumers")
---

```

**Key Insight:** Complex tasks with dependencies benefit from sequential execution where each step operates in a fresh context while receiving only the relevant outputs from previous steps. **Per-step meta-judge evaluation specifications** ensure tailored evaluation criteria specific to each step's requirements, while running in parallel with implementation for speed. **External judge verification** catches blind spots that self-critique misses, while the **iteration loop** (reusing the same step's meta-judge spec) ensures quality before proceeding. This prevents both context pollution and error propagation.
