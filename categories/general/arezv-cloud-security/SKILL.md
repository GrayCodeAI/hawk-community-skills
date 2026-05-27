---
name: arezv-cloud-security
description: Use when assessing cloud infrastructure for security misconfigurations,
  IAM privilege escalation paths, S3 public exposure, open security group rules, or
  IaC security gaps. Covers AWS, Azure, and G...
license: MIT
tags:
- general
---

## Cross-References

| Skill | Relationship |
|-------|-------------|
| [incident-response](../incident-response/SKILL.md) | Critical findings (public S3, privilege escalation confirmed active) may trigger incident classification |
| [threat-detection](../threat-detection/SKILL.md) | Cloud posture findings create hunting targets — over-permissioned roles are likely lateral movement destinations |
| [red-team](../red-team/SKILL.md) | Red team exercises specifically test exploitability of cloud misconfigurations found in posture assessment |
| [security-pen-testing](../security-pen-testing/SKILL.md) | Cloud posture findings feed into the infrastructure security section of pen test assessments |
