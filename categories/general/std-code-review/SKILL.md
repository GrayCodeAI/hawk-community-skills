---
name: std-code-review
description: Run an AI-assisted PR code review using multi-layer lenses with confidence
  scoring.
license: MIT
tags:
- general
metadata: None
triggers: None
keywords: None
---

## Step 7 — Skill Feedback Loop (Mandatory)

For every `BLOCKER` or `MAJOR` finding, answer: "Was there an active skill that should have prevented this?"

1. **YES**: Fix the skill's `SKILL.md` (Anti-Patterns) and `evals/evals.json`.
2. **NO**: If recurring, create a new skill via `common-skill-creator`.

## Output Template

- Findings:
- Verdict:
- Next action:
