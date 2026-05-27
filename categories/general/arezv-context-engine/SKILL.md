---
name: arezv-context-engine
description: Loads and manages company context for all C-suite advisor skills. Reads
  ~/.claude/company-context.md, detects stale context (>90 days), enriches context
  during conversations, and enforces privacy/a...
license: MIT
tags:
- general
metadata: None
version: 1.0.0
author: Alireza Rezvani
category: c-level
domain: orchestration
updated: 2026-03-05
frameworks: context-loading, anonymization, context-enrichment
---

## References
- `references/anonymization-protocol.md` — detailed rules for stripping sensitive data before external calls
