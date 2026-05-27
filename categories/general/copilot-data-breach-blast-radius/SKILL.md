---
name: copilot-data-breach-blast-radius
description: 'Pre-breach impact analysis: inventories sensitive data (PII, PHI, PCI-DSS,
  credentials), traces data flows, scores exposure vectors, and produces a regulatory
  blast radius report with fine ranges s...'
license: MIT
tags:
- general
---

## Reference Files

Load on-demand as needed:

| File | Use When | Content |
|------|----------|---------|
| `references/data-classification.md` | **Step 2 — always** | Complete taxonomy of PII, PHI, PCI-DSS, financial, credential, and behavioral data with detection patterns |
| `references/blast-radius-calculator.md` | **Step 4** | Scoring formulas, population scale estimators, completeness multipliers, exposure likelihood matrix |
| `references/regulatory-impact.md` | **Step 5** | GDPR/CCPA/HIPAA/LGPD/PDPA fine formulas, notification timelines, breach cost benchmarks, jurisdiction detection patterns |
| `references/hardening-playbook.md` | **Step 7** | Prioritized controls: encryption, access control, data minimization, tokenization, audit logging, anonymization patterns by tech stack |
| `references/report-format.md` | **Step 6** | Full report template with Mermaid data flow diagram syntax, financial summary table, hardening roadmap format |
