---
name: ghcp-references-analysis-principles
description: 'Skill: ghcp-references-analysis-principles'
license: MIT
tags:
- general
---

## Severity Standards

### SDL Bugbar Severity
Classify each finding per: https://www.microsoft.com/en-us/msrc/sdlbugbar

### CVSS 4.0 Score
Use CVSS v4.0 Base score (0.0-10.0) with vector string.
Reference: https://www.first.org/cvss/v4.0/specification-document

### CWE
Assign Common Weakness Enumeration ID and name.
Reference: https://cwe.mitre.org/

### OWASP
Map to OWASP Top 10:2025 category if applicable (A01-A10).
**ALWAYS use `:2025` suffix** (e.g., `A01:2025`), never `:2021`.
Reference: https://owasp.org/Top10/2025/

### Remediation Effort
- **Low**: Configuration change, flag toggle, or single-file fix
- **Medium**: Multi-file code change, new validation logic, or dependency update
- **High**: Architecture change, new component, or cross-team coordination

### STRIDE Scope Rule
- **External services** (AzureOpenAI, AzureAD, Redis, PostgreSQL) **DO get** STRIDE sections — they are attack surfaces from your system's perspective
- **External actors** (Operator, EndUser) **do NOT get** STRIDE sections — they are threat sources, not targets
- If you have 20 elements and 2 are external actors, you write 18 STRIDE sections

**⚠️ DO NOT include time estimates.** Never add "(hours)", "(days)", "(weeks)", "~1 hour", "~2 hours", or any duration/effort-to-fix estimates anywhere in the output. The effort level (Low/Medium/High) is sufficient.

### Mitigation Type (OWASP-aligned)
- **Redesign**: Eliminate the threat by changing architecture (OWASP: Avoid)
- **Standard Mitigation**: Apply well-known, proven security controls (OWASP: Mitigate)
- **Custom Mitigation**: Implement a bespoke code fix specific to this system (OWASP: Mitigate)
- **Existing Control**: Team already built a control that addresses this threat — document it (OWASP: Fix)
- **Accept Risk**: Acknowledge and document the residual risk (requires justification) (OWASP: Accept)
- **Transfer Risk**: Shift responsibility to user/operator/third-party (e.g., configuration choice, SLA) (OWASP: Transfer)
