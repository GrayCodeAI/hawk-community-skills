---
name: ghcp-skeletons-skeleton-assessment
description: 'Skill: ghcp-skeletons-skeleton-assessment'
license: MIT
tags:
- general
---

## Classification Reference

<!-- SKELETON INSTRUCTION: Copy the table below verbatim. Do NOT modify values. Do NOT copy this HTML comment into the output. -->

| Classification | Values |
|---------------|--------|
| **Exploitability Tiers** | **T1** Direct Exposure (no prerequisites) · **T2** Conditional Risk (single prerequisite) · **T3** Defense-in-Depth (multiple prerequisites or infrastructure access) |
| **STRIDE + Abuse** | **S** Spoofing · **T** Tampering · **R** Repudiation · **I** Information Disclosure · **D** Denial of Service · **E** Elevation of Privilege · **A** Abuse (feature misuse) |
| **SDL Severity** | `Critical` · `Important` · `Moderate` · `Low` |
| **Remediation Effort** | `Low` · `Medium` · `High` |
| **Mitigation Type** | `Redesign` · `Standard Mitigation` · `Custom Mitigation` · `Existing Control` · `Accept Risk` · `Transfer Risk` |
| **Threat Status** | `Open` · `Mitigated` · `Platform` |
| **Incremental Tags** | `[Existing]` · `[Fixed]` · `[Partial]` · `[New]` · `[Removed]` (incremental reports only) |
| **CVSS** | CVSS 4.0 vector with `CVSS:4.0/` prefix |
| **CWE** | Hyperlinked CWE ID (e.g., [CWE-306](https://cwe.mitre.org/data/definitions/306.html)) |
| **OWASP** | OWASP Top 10:2025 mapping (e.g., A01:2025 – Broken Access Control) |
```

**Critical format rules baked into this skeleton:**
- `0-assessment.md` is the FIRST row in Report Files (not `0.1-architecture.md`)
- `## Analysis Context & Assumptions` uses `&` (never word "and")
- `---` horizontal rules between EVERY pair of `## ` sections (minimum 6)
- `### Quick Wins` always present (with fallback note if no low-effort findings)
- `### Needs Verification` and `### Finding Overrides` always present (even if empty with `—`)
- References has TWO subsections with THREE-column tables (never flat 2-column)
- ALL metadata values wrapped in backticks
- ALL metadata fields present (Model, Analysis Started, Analysis Completed, Duration)
- Risk Rating heading has NO emojis
- Action Summary has EXACTLY 4 data rows: Tier 1, Tier 2, Tier 3, Total — NO "Mitigated" or "Platform" rows
- Git Commit rows include commit date in parentheses: `SHA` (`date`)
