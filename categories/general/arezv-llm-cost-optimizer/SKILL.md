---
name: arezv-llm-cost-optimizer
description: 'Use proactively whenever LLM API costs come up -- or should. Triggers
  include: ''my AI costs are too high'', ''optimize token usage'', ''which model should
  I use'', ''LLM spend is out of control'', ''implem...'
license: MIT
tags:
- general
---

## Anti-Patterns

| Anti-Pattern | Why It Fails | Better Approach |
|---|---|---|
| Using the largest model for every request | 80%+ of requests are simple tasks a smaller model handles equally well, wasting 5–10x on cost | Implement a routing layer that classifies complexity and selects the cheapest adequate model |
| Optimizing prompts without measuring first | You cannot know what to optimize without per-feature spend visibility | Instrument token logging and cost-per-request before any changes |
| Caching by exact string match only | Minor phrasing differences cause cache misses on semantically identical queries | Use embedding-based semantic caching with a cosine similarity threshold |
| Setting a single global max_tokens | Some endpoints need 2,000 tokens, others need 50 -- a global cap either wastes or truncates | Set max_tokens per endpoint based on measured p95 output length |
| Ignoring system prompt size | A 3,000-token system prompt sent on every request is a hidden cost multiplier | Use prompt caching for static system prompts; strip unnecessary instructions |
| Treating cost optimization as a one-time project | Model pricing changes, traffic patterns shift, new features launch -- costs drift | Set up continuous cost monitoring with weekly spend reports and anomaly alerts |
| Compressing prompts to the point of ambiguity | Over-compressed prompts cause hallucination or low-quality output, requiring retries | Compress filler and redundant context; preserve all task-critical instructions |
