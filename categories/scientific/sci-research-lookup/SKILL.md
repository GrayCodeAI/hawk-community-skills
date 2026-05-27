---
name: sci-research-lookup
description: Look up current research information using parallel-cli search (primary,
  fast web search), the Parallel Chat API (deep research), or Perplexity sonar-pro-search
  (academic paper searches). Automatic...
license: MIT license
tags:
- scientific
allowed-tools: Read Write Edit Bash
compatibility: parallel-cli required (primary); PARALLEL_API_KEY and OPENROUTER_API_KEY
  optional for deep/academic backends
metadata: None
skill-author: K-Dense Inc.
---

## Summary

This skill serves as the primary research interface with intelligent tri-backend routing:

- **parallel-cli search** (default): Fast, cost-effective web search with academic source prioritization via the parallel-web skill
- **Parallel Chat API** (`core` model): Deep, exhaustive multi-source synthesis (on explicit request only)
- **Perplexity sonar-pro-search**: Academic-specific paper searches only
- **Automatic routing**: Detects query type and routes to the optimal backend
- **Manual override**: Force any backend when needed
- **Academic prioritization**: Two-search pattern ensures scholarly sources surface for scientific queries
