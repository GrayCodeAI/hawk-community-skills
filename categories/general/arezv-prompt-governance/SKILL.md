---
name: arezv-prompt-governance
description: 'Use when managing prompts in production at scale: versioning prompts,
  running A/B tests on prompts, building prompt registries, preventing prompt regressions,
  or creating eval pipelines for product...'
license: MIT
tags:
- general
---

## Anti-Patterns

| Anti-Pattern | Why It Fails | Better Approach |
|---|---|---|
| Hardcoding prompts in application source code | Prompt changes require code deploys, slowing iteration and coupling concerns | Store prompts in a versioned registry separate from application code |
| Deploying prompt changes without running evals | Silent quality regressions reach users undetected | Gate every prompt change on automated eval pipeline pass before promotion |
| Using a single golden dataset forever | As the product evolves, the golden set drifts from real usage patterns | Review and update the golden dataset quarterly, adding new edge cases from production failures |
| One person owns all prompt knowledge | Bus factor of 1 — when that person leaves, prompt context is lost | Document prompts in a registry with ownership, rationale, and version history |
| A/B testing without a pre-defined success metric | Post-hoc metric selection introduces bias and inconclusive results | Define the primary success metric and sample size requirement before starting the test |
| Skipping rollback capability | A bad prompt in production with no rollback forces an emergency code deploy | Every prompt version promotion must have a one-command rollback to the previous version |

## Related Skills

- **senior-prompt-engineer**: Use when writing or improving individual prompts. NOT for managing prompts in production at scale (that is this skill).
- **llm-cost-optimizer**: Use when reducing LLM API spend. Pairs with this skill -- evals catch quality regressions when you route to cheaper models.
- **rag-architect**: Use when designing retrieval pipelines. Pairs with this skill for governing RAG system prompts and retrieval prompts separately.
- **ci-cd-pipeline-builder**: Use when building CI/CD pipelines. Pairs with this skill for automating eval runs in CI.
- **observability-designer**: Use when designing monitoring. Pairs with this skill for production prompt quality dashboards.
