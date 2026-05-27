---
name: neo-propose-hypotheses
description: Execute complete FPF cycle from hypothesis generation to decision
license: MIT
tags:
- general
argument-hint:
- problem-statement
allowed-tools: Task, Read, Write, Bash, AskUserQuestion
---

## Completion

Workflow complete when:
- [ ] `.fpf/` directory structure exists
- [ ] Context recorded in `.fpf/context.md`
- [ ] Hypotheses generated, verified, validated, and audited
- [ ] DRR created in `.fpf/decisions/`
- [ ] Final summary presented to user

**Artifacts Created**:
- `.fpf/context.md` - Problem context
- `.fpf/knowledge/L0/*.md` - Initial hypotheses
- `.fpf/knowledge/L1/*.md` - Verified hypotheses
- `.fpf/knowledge/L2/*.md` - Validated hypotheses
- `.fpf/knowledge/invalid/*.md` - Rejected hypotheses
- `.fpf/evidence/*.md` - Evidence files
- `.fpf/decisions/*.md` - Design Rationale Record
