---
name: ag-fp-data-transforms
description: Everyday data transformations using functional patterns - arrays, objects,
  grouping, aggregation, and null-safe access
license: MIT
tags:
- general
risk: unknown
source: community
version: 1.0.0
author: Claude
---

## Summary

| Task | Imperative | Functional | Recommendation |
|------|-----------|------------|----------------|
| Transform array elements | for loop with push | `.map()` | Use map |
| Filter array | for loop with condition | `.filter()` | Use filter |
| Accumulate values | for loop with accumulator | `.reduce()` | Use reduce for complex, loop for simple |
| Group by key | for loop with object | `groupBy` utility | Create reusable utility |
| Pick object fields | manual property copy | `pick` utility | Use spread for one-off, utility for repeated |
| Merge objects | property-by-property | spread syntax | Use spread |
| Deep merge | nested conditionals | recursive utility | Use utility or library |
| Null-safe access | `if (x && x.y)` | `?.` or Option | Use `?.` for simple, Option for composition |
| Normalize API data | nested loops | extraction functions | Break into composable functions |

**The functional approach is better when:**
- You need to compose operations
- You want reusable transformations
- You value explicit data flow over implicit state
- Type safety for missing values matters

**The imperative approach is acceptable when:**
- The transformation is a one-off
- The logic is simple and linear
- Performance is critical and you've measured
- The team is more comfortable with it

## Limitations
- Use this skill only when the task clearly matches the scope described above.
- Do not treat the output as a substitute for environment-specific validation, testing, or expert review.
- Stop and ask for clarification if required inputs, permissions, safety boundaries, or success criteria are missing.
