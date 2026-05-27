---
name: copilot-azure-architecture-autopilot
description: 'Skill: copilot-azure-architecture-autopilot'
license: MIT
tags:
- general
When to use this skill: None
---

## Phase Transition Rules

- Each Phase reads and follows the instructions in its corresponding `references/*.md` file
- When transitioning between Phases, always inform the user about the next step
- Do not skip Phases (especially the what-if between Phase 3 → Phase 4)
- **🚨 Required condition for Phase 1 → Phase 2 transition**: `01_arch_diagram_draft.html` must have been generated using the embedded diagram engine and shown to the user. **Do not proceed to Bicep generation without a diagram.** Completing spec collection alone does not mean Phase 1 is done — Phase 1 includes diagram generation + user confirmation.
- Modification request after deployment → return to Phase 1, not Phase 0 (Delta Confirmation Rule)

## Service Coverage & Fallback

### Optimized Services
Microsoft Foundry, Azure OpenAI, AI Search, ADLS Gen2, Key Vault, Microsoft Fabric, Azure Data Factory, VNet/Private Endpoint, AML/AI Hub

### Other Azure Services
All supported — MS Docs are automatically consulted to generate at the same quality standard.
**Do not send messages that cause user anxiety such as "out of scope" or "best-effort".**

### Stable vs Dynamic Information Handling

| Category | Handling Method | Examples |
|----------|----------------|---------|
| **Stable** | Reference files first | `isHnsEnabled: true`, PE triple set |
| **Dynamic** | **Always fetch MS Docs** | API version, model availability, SKU, region |

## Quick Reference

| File | Role |
|------|------|
| `references/phase0-scanner.md` | Existing resource scan + relationship inference + diagram |
| `references/phase1-advisor.md` | Interactive architecture design + fact checking |
| `references/bicep-generator.md` | Bicep code generation rules |
| `references/bicep-reviewer.md` | Code review checklist |
| `references/phase4-deployer.md` | validate → what-if → deploy |
| `references/service-gotchas.md` | Required properties, PE mappings |
| `references/azure-dynamic-sources.md` | MS Docs URL registry |
| `references/azure-common-patterns.md` | PE/security/naming patterns |
| `references/ai-data.md` | AI/Data service guide |
