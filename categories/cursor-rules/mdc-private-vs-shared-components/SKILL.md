---
name: mdc-private-vs-shared-components
description: "Rules for determining if a component should be private or shared, and where to place them based on their use-case."
license: MIT
tags: [cursor-rules]
---

- Private Components: For components used only within specific pages, you can create a _components folder within the relevant /app subdirectory.
- Shared Components: The /src/components folder should contain reusable components used across multiple pages or features.