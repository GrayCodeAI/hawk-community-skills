---
name: arezv-agent-workflow-designer
description: Agent Workflow Designer
license: MIT
tags:
- general
---

## Common Pitfalls

- Over-orchestrating tasks solvable by one well-structured prompt
- Missing timeout/retry policies for external-model calls
- Passing full upstream context instead of targeted artifacts
- Ignoring per-step cost accumulation

## Best Practices

1. Start with the smallest pattern that can satisfy requirements.
2. Keep handoff payloads explicit and bounded.
3. Validate intermediate outputs before fan-in synthesis.
4. Enforce budget and timeout limits in every step.
