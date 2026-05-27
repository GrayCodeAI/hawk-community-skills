---
name: ghcp-references-incremental-orchestrator
description: 'Skill: ghcp-references-incremental-orchestrator'
license: MIT
tags:
- general
---

## Summary: Phase-by-Phase Checklist

| Phase | Action | Success Criteria |
|-------|--------|-----------------|
| 0 | Setup, validate inputs, worktree | All inputs exist, worktree accessible |
| 1 | Load old inventory skeleton | All arrays populated, metrics match |
| 2 | Per-component change detection | Every component has a `change_status` |
| 3 | Scan for new components | New components identified, missed components flagged |
| 4 | Generate all report files | 8-9 files written to output folder |
| 5 | Verification (standard + incremental) | All checks pass or escalated to Needs Verification |
