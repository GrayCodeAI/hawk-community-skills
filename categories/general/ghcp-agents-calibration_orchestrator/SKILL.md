---
name: ghcp-agents-calibration_orchestrator
description: 'Skill: ghcp-agents-calibration_orchestrator'
license: MIT
tags:
- general
---

## Out of scope for this orchestrator

- Designing the lever change. The operator provides `<lever_change_description>`; you apply it, you don't invent it.
- Modifying the playbook prose (SKILL.md, references/exploration_patterns.md beyond the documented lever change). If the cycle reveals a non-lever defect (e.g., the runner-side "Phase 1 archived as complete with 0-line EXPLORATION.md" finding), document it in the audit's "Cycle Findings" section but don't auto-fix it; that's a separate cycle or a v1.5.7 cleanup item.
- Promoting a Ship verdict to a release tag. The cycle's commit ships the lever change; the release happens separately when v1.5.6 (or whichever version) is ready to ship.
