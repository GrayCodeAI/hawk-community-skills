---
name: ghcp-assets-simple-2d-engine
description: 'Skill: ghcp-assets-simple-2d-engine'
license: MIT
tags:
- general
---

## Design Advantages

| Feature | Benefit |
|---------|---------|
| Grid-based collision | O(1) lookup per check, no broad-phase needed |
| Dual coordinates | Sub-pixel smooth rendering with integer collision |
| Per-axis collision | Simple logic, naturally handles corners |
| Ratio-based velocity | Resolution-independent movement |
| Friction multiplier | Tunable feel per surface type |
| Cell overflow while-loops | Handles multi-cell movement safely |
