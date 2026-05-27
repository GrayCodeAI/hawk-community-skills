---
name: mdc-region-structure-definition-rules
description: "Rules for defining the structure of regions in the cellular automata simulation. These rules specify the data structure needed for regions."
license: MIT
tags: [cursor-rules]
---

- Define the Region Structure:
  - Create a comprehensive data structure to represent each region. This structure should be flexible enough to accommodate various parameters that can influence the behavior of soup cells within that region. Consider including:
    - Obstacle
    - Directional influence (for each cardinal direction)
    - Randomness factor
    - Temperature
    - Energy level
    - Any other relevant parameters
  - Ensure that each parameter is represented by an appropriate data type, typically using floating-point numbers for continuous values or integers for discrete states. This structure will be the foundation of your region system, so design it with extensibility in mind.