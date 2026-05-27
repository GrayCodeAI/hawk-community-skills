---
name: ghcp-references-output-formats
description: 'Skill: ghcp-references-output-formats'
license: MIT
tags:
- general
---

## Enumeration Reference

All reports MUST use these exact values. Do NOT abbreviate, substitute, or invent alternatives.

**Component Types:** `process` | `data_store` | `external_service` | `external_interactor`

**Boundary Kinds (TMT-aligned):** `MachineBoundary` | `NetworkBoundary` | `ClusterBoundary` | `ProcessBoundary` | `PrivilegeBoundary` | `SandboxBoundary`

**Exploitability Tiers:** `Tier 1` (Direct Exposure — no prerequisites) | `Tier 2` (Conditional Risk — single prerequisite) | `Tier 3` (Defense-in-Depth — multiple prerequisites)

**STRIDE + Abuse Categories:** `S` Spoofing | `T` Tampering | `R` Repudiation | `I` Information Disclosure | `D` Denial of Service | `E` Elevation of Privilege | `A` Abuse

**SDL Bugbar Severity:** `Critical` | `Important` | `Moderate` | `Low`

**Remediation Effort:** `Low` | `Medium` | `High`

**Mitigation Type (OWASP-aligned):** `Redesign` | `Standard Mitigation` | `Custom Mitigation` | `Existing Control` | `Accept Risk` | `Transfer Risk`

**Threat Status:** `Open` | `Mitigated` | `Platform`

**Finding Change Status (incremental):** `Still Present` | `Fixed` | `New` | `New (Code)` | `New (Previously Unidentified)` | `Removed`

**OWASP Top 10:2025 suffix:** Always `:2025` (e.g., `A01:2025 – Broken Access Control`)
- [ ] Quick Wins, Needs Verification, Finding Overrides subsections present
- [ ] Deployment pattern documented (K8s operator vs standalone)
- [ ] All metadata values in backticks

**Also verify (applies to ALL files):** No leaked directives (⛔, RIGID, NON-NEGOTIABLE in output), no time estimates, no nested output folders. See `verification-checklist.md` Phase 0 for the full common deviation list.
