---
name: mdc-soup-cell-to-region-mapping-rules
description: "Rules for mapping soup cells to regions in the cellular automata simulation. This rule focuses on efficient mapping and updating strategies."
license: MIT
tags: [cursor-rules]
---

- Implement Soup Cell to Region Mapping:
  - Develop a system to efficiently map each soup cell to its corresponding region. This mapping is crucial for quick lookups during simulation.
  - Create a separate array where each element represents a soup cell and contains the index or reference to its associated region.
  - Implement functions to update this mapping whenever the region grid size changes. Ensure that this mapping system is optimized for performance, as it will be frequently accessed during the simulation.