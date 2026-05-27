---
name: arezv-incident-response
description: Use when a security incident has been detected or declared and needs
  classification, triage, escalation path determination, and forensic evidence collection.
  Covers SEV1-SEV4 classification, false ...
license: MIT
tags:
- general
---

## Cross-References

| Skill | Relationship |
|-------|-------------|
| [threat-detection](SKILL.md) | Confirmed hunting findings escalate to incident-response for triage and classification |
| [cloud-security](SKILL.md) | Cloud posture findings (IAM compromise, S3 exposure) may trigger incident classification |
| [red-team](SKILL.md) | Red team findings validate detection coverage; confirmed gaps become hunting hypotheses |
| [security-pen-testing](SKILL.md) | Pen test vulnerabilities exploited in the wild escalate to incident-response for active incident handling |
