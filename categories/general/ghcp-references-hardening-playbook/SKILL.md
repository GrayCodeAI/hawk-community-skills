---
name: ghcp-references-hardening-playbook
description: 'Skill: ghcp-references-hardening-playbook'
license: MIT
tags:
- general
---

## Blast Radius Reduction by Control Applied

When reporting the hardening roadmap, use these estimates:

| Control Applied | Blast Radius Reduction | Justification |
|----------------|----------------------|---------------|
| Fix all IDOR vulnerabilities | 80–90% | Most breach scenarios exploit authorization flaws |
| Field encryption for T1 data | 75–85% | Encrypted data is useless without KMS key |
| Remove PII from logs | 40–60% | Log access is often less controlled than DB access |
| Tokenize payment data | 95% for card data | Standard PCI-DSS compliance eliminates card data scope |
| Rate limit data endpoints | 30–50% | Limits scale of automated harvesting attacks |
| Data retention enforcement | 20–40% | Reduces "data lake" effect — less data to steal |
| Audit logging + anomaly detection | 0% prevention, but -60% detection time | Breaches are caught faster |
| Pseudonymization of analytics | 60–70% for analytics data | Analytics data decoupled from identity |
| Architecture: separate analytics from PII | 50–70% | Breach of analytics store has no PII value |
