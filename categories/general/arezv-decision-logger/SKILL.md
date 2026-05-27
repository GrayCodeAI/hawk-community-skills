---
name: arezv-decision-logger
description: Two-layer memory architecture for board meeting decisions. Manages raw
  transcripts (Layer 1) and approved decisions (Layer 2). Use when logging decisions
  after a board meeting, reviewing past decis...
license: MIT
tags:
- general
metadata: None
version: 1.0.0
author: Alireza Rezvani
category: c-level
domain: decision-memory
updated: 2026-03-05
python-tools: scripts/decision_tracker.py
---

## References
- `templates/decision-entry.md` — single entry template with field rules
- `scripts/decision_tracker.py` — CLI parser, overdue tracker, conflict detector
