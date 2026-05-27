---
name: ghcp-skeletons-skeleton-stride-analysis
description: 'Skill: ghcp-skeletons-skeleton-stride-analysis'
license: MIT
tags:
- general
---

[REPEAT: one section per component — do NOT include sections for external actors (Operator, EndUser)]

## [FILL: ComponentName]

**Trust Boundary:** [FILL: boundary name]
**Role:** [FILL: brief description]
**Data Flows:** [FILL: DF##, DF##, ...]
**Pod Co-location:** [FILL: sidecars if K8s, or "N/A" if not K8s]

### STRIDE-A Analysis

#### Tier 1 — Direct Exposure (No Prerequisites)

| ID | Category | Threat | Prerequisites | Affected Flow | Mitigation | Status |
|----|----------|--------|---------------|---------------|------------|--------|
[REPEAT: threat rows or "*No Tier 1 threats identified.*"]
| [FILL: T##.X] | [FILL: Spoofing/Tampering/Repudiation/Information Disclosure/Denial of Service/Elevation of Privilege/Abuse] | [FILL] | [FILL] | [FILL: DF##] | [FILL] | [FILL: Open/Mitigated/Platform] |
[END-REPEAT]

#### Tier 2 — Conditional Risk

| ID | Category | Threat | Prerequisites | Affected Flow | Mitigation | Status |
|----|----------|--------|---------------|---------------|------------|--------|
[REPEAT: threat rows or "*No Tier 2 threats identified.*"]
| [FILL] | [FILL] | [FILL] | [FILL] | [FILL] | [FILL] | [FILL] |
[END-REPEAT]

#### Tier 3 — Defense-in-Depth

| ID | Category | Threat | Prerequisites | Affected Flow | Mitigation | Status |
|----|----------|--------|---------------|---------------|------------|--------|
[REPEAT: threat rows or "*No Tier 3 threats identified.*"]
| [FILL] | [FILL] | [FILL] | [FILL] | [FILL] | [FILL] | [FILL] |
[END-REPEAT]

#### Categories Not Applicable

| Category | Justification |
|----------|---------------|
[REPEAT: one row per N/A STRIDE category — use "Abuse" not "Authorization" for the A category]
| [FILL: Spoofing/Tampering/Repudiation/Information Disclosure/Denial of Service/Elevation of Privilege/Abuse] | [FILL: 1-sentence justification] |
[END-REPEAT]

<!-- ⛔ POST-COMPONENT CHECK: Verify this component:
  1. Category column uses full names (not abbreviations like 'S', 'T', 'DoS')
  2. 'A' category is 'Abuse' (NEVER 'Authorization')
  3. Status column uses ONLY: Open, Mitigated, Platform
  4. All 3 tier sub-sections present (even if empty with '*No Tier N threats*')
  5. N/A table present for any STRIDE categories without threats
  If ANY check fails → FIX NOW before moving to next component. -->

[END-REPEAT]
```

**STRIDE + Abuse Cases — the 7 categories are EXACTLY:**
Spoofing | Tampering | Repudiation | Information Disclosure | Denial of Service | Elevation of Privilege | Abuse

**Note:** The first 6 are standard STRIDE. "Abuse" is a supplementary category for business logic misuse (workflow manipulation, feature exploitation, API abuse). It is NOT "Authorization" — authorization issues belong under Elevation of Privilege (E).

**Valid Status values:** `Open` | `Mitigated` | `Platform` — NO other values permitted.
