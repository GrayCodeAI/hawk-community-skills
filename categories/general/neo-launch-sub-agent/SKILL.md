---
name: neo-launch-sub-agent
description: Launch an intelligent sub-agent with automatic model selection based
  on task complexity, specialized agent matching, Zero-shot CoT reasoning, and mandatory
  self-critique verification
license: MIT
tags:
- general
argument-hint: Task description (e.g., "Implement user authentication" or "Research
  caching strategies") [--model opus|sonnet|haiku] [--agent <agent-name>] [--output
  <path>]
---

### Example 4: Research Task (Opus + Researcher)

**Input:** `/launch-sub-agent Research authentication options for mobile app - evaluate OAuth2, SAML, passwordless`

**Analysis:**

- Task type: Research / comparison
- Complexity: High (comparative analysis, recommendations)
- Output size: Large (comprehensive research)
- Domain match: sdd:researcher

**Selection:** Opus + sdd:researcher agent

**Dispatch:** Task tool with Opus model, sdd:researcher prompt, CoT prefix, critique suffix

## Best Practices

### Context Isolation

- Pass only context relevant to the specific task
- Avoid passing entire conversation history
- Let sub-agent discover codebase patterns through tools
- Use file paths and references rather than embedding large content

### Model Selection

- When in doubt, use Opus (quality over cost)
- Use Haiku only for truly trivial tasks
- Use Sonnet for "grunt work" - needs capability but not genius
- Production code always deserves Opus

### Specialized Agents

- Use when domain expertise clearly improves quality
- Combine with CoT and critique patterns
- Don't force specialization on general tasks

### Quality Gates

- Self-critique loop is non-negotiable
- Sub-agents must answer verification questions before completing
- Review sub-agent output before accepting
