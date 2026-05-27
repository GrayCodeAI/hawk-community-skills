---
name: ghcp-references-algorithms
description: 'Skill: ghcp-references-algorithms'
license: MIT
tags:
- general
---

## Quick Reference Table

| Algorithm / Concept | Primary Use Case | Complexity |
|---|---|---|
| Bresenham's Line | Grid raycasting, line of sight | O(max(dx, dy)) per ray |
| AABB Overlap | Fast collision detection | O(1) per pair |
| Circle Overlap | Round collider detection | O(1) per pair |
| Separating Axis Theorem | Convex polygon collision | O(n) per pair (n = edges) |
| Spatial Hashing | Broad-phase collision culling | O(1) average lookup |
| Euler Integration | Simple physics stepping | O(1) per body per step |
| Verlet Integration | Constraint-based physics | O(1) per body per step |
| Impulse Resolution | Collision response | O(iterations * contacts) |
| Vector Normalization | Direction extraction | O(1) |
| Dot Product | Angle/projection queries | O(1) |
| Cross Product | Perpendicularity / winding | O(1) |
| Reflection | Bounce / ricochet | O(1) |
