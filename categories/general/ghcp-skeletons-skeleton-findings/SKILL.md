---
name: ghcp-skeletons-skeleton-findings
description: 'Skill: ghcp-skeletons-skeleton-findings'
license: MIT
tags:
- general
---

## Threat Coverage Verification

| Threat ID | Finding ID | Status |
|-----------|------------|--------|
[REPEAT: one row per threat from ALL components in 2-stride-analysis.md]
| [FILL: T##.X] | [FILL: FIND-## or —] | [FILL: ✅ Covered (FIND-XX) / ✅ Mitigated (FIND-XX) / 🔄 Mitigated by Platform] |
[END-REPEAT]

<!-- ⛔ POST-TABLE CHECK: Verify Threat Coverage Verification:
  1. Status column uses ONLY these 3 values with emoji prefixes:
     - `✅ Covered (FIND-XX)` — vulnerability needs remediation
     - `✅ Mitigated (FIND-XX)` — team built a control (documented in finding)
     - `🔄 Mitigated by Platform` — external platform handles it
  2. Do NOT use plain text like "Finding", "Mitigated", "Covered" without the emoji
  3. Do NOT use "Needs Review", "Accepted Risk", or "N/A"
  4. Column headers are EXACTLY: `Threat ID | Finding ID | Status` (NOT `Threat | Finding | Status`)
  5. Every threat from 2-stride-analysis.md appears in this table (no missing threats)
  If ANY check fails → FIX NOW. -->
```

**Fixed rules baked into this skeleton:**
- Finding ID: `FIND-` prefix (never `F-`, `F01`, `Finding`)
- Attribute names: `SDL Bugbar Severity`, `Exploitation Prerequisites`, `Exploitability Tier`, `Remediation Effort` (exact — not abbreviated)
- CVSS: starts with `CVSS:4.0/` (never bare vector)
- CWE: hyperlinked (never plain text)
- OWASP: `:2025` suffix (never `:2021`)
- Related Threats: individual hyperlinks (never plain text)
- Sub-sections: `#### Description`, `#### Evidence`, `#### Remediation`, `#### Verification`
- Organized by TIER — no `## Critical Findings` or `## Mitigated` sections
- Exactly 3 tier sections (all mandatory, even if empty with "*No Tier N findings identified.*")
