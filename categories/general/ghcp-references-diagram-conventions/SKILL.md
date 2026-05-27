---
name: ghcp-references-diagram-conventions
description: 'Skill: ghcp-references-diagram-conventions'
license: MIT
tags:
- general
---

## STRIDE Analysis — Sidecar Implications

Although sidecars are NOT separate diagram nodes, they DO appear in STRIDE analysis:

- Sidecars with distinct threat surfaces (e.g., MISE auth bypass, Dapr mTLS) get their own `## Component` section in `2-stride-analysis.md`
- The component heading notes which pods they are co-located in
- Threats related to intra-pod communication (localhost bypass, shared namespace) go under the **primary container's** component section
- **Pod Co-location** line in STRIDE template: list co-located sidecars (e.g., "MISE Sidecar, Dapr Sidecar")
