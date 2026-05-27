---
name: arezv-org-health-diagnostic
description: Cross-functional organizational health check combining signals from all
  C-suite roles. Scores 8 dimensions on a traffic-light scale with drill-down recommendations.
  Use when assessing overall compa...
license: MIT
tags:
- general
metadata: None
version: 1.0.0
author: Alireza Rezvani
category: c-level
domain: organizational-health
updated: 2026-03-05
python-tools: health_scorer.py
frameworks: health-benchmarks
---

## Graceful Degradation

You don't need all metrics to run a diagnostic. The tool handles partial data:
- Missing metric → excluded from score, flagged as "[data needed]"
- Score still valid for available dimensions
- Report flags which gaps to fill for next cycle

## References
- `references/health-benchmarks.md` — benchmarks by stage (Seed, A, B, C)
- `scripts/health_scorer.py` — CLI scoring tool with traffic light output
