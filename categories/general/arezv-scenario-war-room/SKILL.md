---
name: arezv-scenario-war-room
description: Cross-functional what-if modeling for cascading multi-variable scenarios.
  Unlike single-assumption stress testing, this models compound adversity across all
  business functions simultaneously. Use w...
license: MIT
tags:
- general
metadata: None
version: 1.0.0
author: Alireza Rezvani
category: c-level
domain: strategic-planning
updated: 2026-03-05
python-tools: scenario_modeler.py
frameworks: scenario-planning
---

## Common Scenarios by Stage

**Seed:**
- Co-founder leaves + product misses launch
- Funding runs out + bridge terms unfavorable

**Series A:**
- Miss ARR target + fundraise delayed
- Key customer churns + competitor raises

**Series B:**
- Market contraction + burn multiple spikes
- Lead investor wants pivot + team resists

## Integration with C-Suite Roles

| Scenario Type | Primary Roles | Cascade To |
|--------------|---------------|------------|
| Revenue miss | CRO, CFO | CMO (pipeline), COO (cuts), CHRO (layoffs) |
| Key person departure | CHRO, COO | CTO (if eng), CRO (if sales) |
| Fundraise failure | CFO, CEO | COO (runway extension), CHRO (hiring freeze) |
| Security breach | CISO, CTO | CEO (comms), CFO (cost), CRO (customer impact) |
| Market shift | CEO, CPO | CMO (repositioning), CRO (new segments) |
| Competitor move | CMO, CRO | CPO (roadmap response), CEO (strategy) |

## References
- `references/scenario-planning.md` — Shell methodology, pre-mortem, Monte Carlo, cascade frameworks
- `scripts/scenario_modeler.py` — CLI tool for structured scenario modeling
