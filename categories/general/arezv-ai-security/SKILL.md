---
name: arezv-ai-security
description: Use when assessing AI/ML systems for prompt injection, jailbreak vulnerabilities,
  model inversion risk, data poisoning exposure, or agent tool abuse. Covers MITRE
  ATLAS technique mapping, injection...
license: MIT
tags:
- general
---

## Cross-References

| Skill | Relationship |
|-------|-------------|
| [threat-detection](SKILL.md) | Anomaly detection in LLM inference API logs can surface model inversion attacks and systematic prompt injection probing |
| [incident-response](SKILL.md) | Confirmed prompt injection exploitation or data extraction from a model should be classified as a security incident |
| [cloud-security](SKILL.md) | LLM API keys and model endpoints are cloud resources — IAM misconfiguration enables unauthorized model access (AML.T0012) |
| [security-pen-testing](SKILL.md) | Application-layer security testing covers the web interface and API layer; ai-security covers the model and agent layer |
