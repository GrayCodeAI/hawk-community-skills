---
name: arezv-strategic-alignment
description: Cascades strategy from boardroom to individual contributor. Detects and
  fixes misalignment between company goals and team execution. Covers strategy articulation,
  cascade mapping, orphan goal detec...
license: MIT
tags:
- general
metadata: None
version: 1.0.0
author: Alireza Rezvani
category: c-level
domain: strategic-alignment
updated: 2026-03-05
python-tools: alignment_checker.py
frameworks: alignment-playbook
---

## Key Questions for Alignment

- "Ask your newest team member: what is the most important thing the company is trying to achieve right now?"
- "Which company OKR does your team's top priority support? Can you trace the connection?"
- "When Team A and Team B both hit their goals, does the company always win? Are there scenarios where they don't?"
- "What changed in how your team works since the last strategy update?"
- "Name a decision made last week that was influenced by the company strategy."

## Red Flags

- Teams consistently hit goals while company misses targets
- Cross-functional projects take 3x longer than expected (coordination failure)
- Strategy updated quarterly but team priorities don't change
- "That's a leadership problem, not our problem" attitude at the team level
- New initiatives announced without connecting them to existing OKRs
- Department heads optimize for headcount or budget rather than company outcomes

## Integration with Other C-Suite Roles

| When... | Work with... | To... |
|---------|-------------|-------|
| New strategy is set | CEO + COO | Cascade into quarterly rocks before announcing |
| OKR cycle starts | COO | Run cross-team conflict check before finalizing |
| Team consistently misses goals | CHRO | Diagnose: capability gap or alignment gap? |
| Silo identified | COO | Design shared metrics or cross-functional OKRs |
| Post-M&A | CEO + Culture Architect | Detect strategy conflicts between merged entities |

## Detailed References
- `scripts/alignment_checker.py` — Automated OKR alignment analysis (orphans, conflicts, coverage)
- `references/alignment-playbook.md` — Cascade techniques, quarterly alignment check, common patterns
