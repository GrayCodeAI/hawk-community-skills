---
name: bmad-orchestrator
description: Orchestrates BMAD workflows for structured AI-driven development. Routes
  work across Analysis, Planning, Solutioning, and Implementation phases.
license: MIT
tags:
- bmad
- orchestrator
- workflow
- planning
- implementation
allowed-tools: Read Write Bash Grep Glob
metadata: None
platforms: Claude, Gemini, Codex, OpenCode
keyword: bmad
version: 1.1.0
source: user-installed skill
---

[[BMAD Plans]]

# PRD: myapp
...
```

### Quick Reference

| Phase | Document | Gate Command |
|-------|----------|--------------|
| Phase 1 → 2 | Product Brief | `bash scripts/phase-gate-review.sh docs/product-brief-*.md` |
| Phase 2 → 3 | PRD / Tech Spec | `bash scripts/phase-gate-review.sh docs/prd-*.md` |
| Phase 3 → 4 | Architecture | `bash scripts/phase-gate-review.sh docs/architecture-*.md` |
| Phase 4 done | Sprint Plan | `bash scripts/phase-gate-review.sh docs/sprint-status.yaml` |
