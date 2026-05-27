---
name: ghcp-references-retrieval
description: 'Skill: ghcp-references-retrieval'
license: MIT
tags:
- general
---

## Rules

- NEVER fabricate nodes or edges not present in the graph
- NEVER traverse deeper than depth 2
- ALWAYS check the wiki before the graph (wiki-first)
- Always include seed nodes in the result, even if they have no edges
- Prefer edges with higher confidence when pruning
- File valuable answers back into the wiki as topic pages
- Return an empty subgraph (not an error) if no relevant nodes are found
