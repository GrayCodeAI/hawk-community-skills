---
name: mdc-svelte-5-reactivity-handling
description: "Guidelines for handling reactivity and reactive statements in Svelte 5."
license: MIT
tags: [react]
---

- Prefer runes over reactive declarations ( `$:`) for reactivity, e.g. `bind:value`
- Treat event handlers as properties, simplifying their use.