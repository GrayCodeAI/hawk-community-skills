---
name: arezv-fda-consultant-specialist
description: FDA regulatory consultant for medical device companies. Provides 510(k)/PMA/De
  Novo pathway guidance, QSR (21 CFR 820) compliance, HIPAA assessments, and device
  cybersecurity. Use when user mention...
license: MIT
tags:
- general
---

## Resources

### scripts/

| Script | Purpose |
|--------|---------|
| `fda_submission_tracker.py` | Track 510(k)/PMA/De Novo submission milestones and timelines |
| `qsr_compliance_checker.py` | Assess 21 CFR 820 compliance against project documentation |
| `hipaa_risk_assessment.py` | Evaluate HIPAA safeguards in medical device software |

### references/

| File | Content |
|------|---------|
| `fda_submission_guide.md` | 510(k), De Novo, PMA submission requirements and checklists |
| `qsr_compliance_requirements.md` | 21 CFR 820 implementation guide with templates |
| `hipaa_compliance_framework.md` | HIPAA Security Rule safeguards and BAA requirements |
| `device_cybersecurity_guidance.md` | FDA cybersecurity requirements, SBOM, threat modeling |
| `fda_capa_requirements.md` | CAPA process, root cause analysis, effectiveness verification |

### Usage Examples

```bash
# Track FDA submission status
python scripts/fda_submission_tracker.py /path/to/project --type 510k

# Assess QSR compliance
python scripts/qsr_compliance_checker.py /path/to/project --section 820.30

# Run HIPAA risk assessment
python scripts/hipaa_risk_assessment.py /path/to/project --category technical
```
