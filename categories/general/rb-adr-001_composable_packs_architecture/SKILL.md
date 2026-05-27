---
name: rb-adr-001_composable_packs_architecture
description: 'Skill: rb-adr-001_composable_packs_architecture'
license: MIT
tags:
- general
---

### Summary of Final Design Decisions

| Feature | Original Proposal | Alternative (Isolation) | Final Hybrid Design | Rationale |
| :--- | :--- | :--- | :--- | :--- |
| **Context/Tools** | Unified `memory/` & `tools/` via merging. | Kept isolated in `packs/`. | **Unified `memory/` & `tools/` via non-destructive merging.** | **This is the core decision.** A unified context is essential for the AI to function as intended. User experience is also far better. |
| **State Management** | `active_profiles.json` | `selection.lock.json` | **`.rulebook/selection.json`** | Adopted clearer naming and a dedicated hidden directory for all framework internals, keeping the project root cleaner. |
| **Metadata** | Implicit (directory name). | `manifest.yaml` | **`manifest.yaml` per pack.** | Excellent idea. Makes the framework more robust, descriptive, and future-proof (for versions, dependencies, etc.). |
| **Documentation** | Not explicitly defined. | `README.md` per ruleset. | **`README.md` per pack.** | Perfect for human-readable setup and usage instructions. Keeps the manifest clean. |
| **Tool Execution** | (Not specified) | Optional `runners/`. | **README-driven setup.** | Correctly identified as over-engineering for v1. Simple instructions in a README are more flexible and transparent. |
| **Rule Composition** | Merged and generated. | Merged into `COMBINED.md`. | **Merged into a single file per assistant.** | Both designs agreed on this. Concatenation is the most reliable method for ensuring rule order is respected by all platforms. |
