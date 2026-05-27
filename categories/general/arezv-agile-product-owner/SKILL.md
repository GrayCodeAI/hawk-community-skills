---
name: arezv-agile-product-owner
description: Agile product ownership for backlog management and sprint execution.
  Covers user story writing, acceptance criteria, sprint planning, and velocity tracking.
  Use for writing user stories, creating a...
license: MIT
tags:
- general
not_for: Kanban-only workflows, waterfall project planning, general task management,
  non-Scrum agile frameworks (SAFe, LeSS) without adaptation
triggers: None
---

## Sprint Metrics

Track sprint health and team performance.

### Key Metrics

| Metric | Formula | Target |
|--------|---------|--------|
| Velocity | Points completed / sprint | Stable ±10% |
| Commitment Reliability | Completed / Committed | >85% |
| Scope Change | Points added or removed mid-sprint | <10% |
| Carryover | Points not completed | <15% |

### Velocity Tracking

```
Sprint 1: 25 points
Sprint 2: 28 points
Sprint 3: 30 points
Sprint 4: 32 points
Sprint 5: 29 points
------------------------
Average Velocity: 28.8 points
Trend: Stable

Planning: Commit to 24-26 points
```

### Definition of Done

Story is complete when:

- [ ] Code complete and peer reviewed
- [ ] Unit tests written and passing
- [ ] Acceptance criteria verified
- [ ] Documentation updated
- [ ] Deployed to staging environment
- [ ] Product Owner accepted
- [ ] No critical bugs remaining

## Related Skills

- **Scrum Master** (`project-management/scrum-master/`) — Velocity data and sprint ceremonies complement backlog management
- **Product Manager Toolkit** (`product-team/product-manager-toolkit/`) — RICE prioritization feeds backlog ordering
