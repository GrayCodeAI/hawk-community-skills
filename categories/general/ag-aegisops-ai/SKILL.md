---
name: ag-aegisops-ai
description: Autonomous DevSecOps & FinOps Guardrails. Orchestrates Gemini 3 Flash
  to audit Linux Kernel patches, Terraform cost drifts, and K8s compliance.
license: MIT
tags:
- general
risk: safe
source: community
author: Champbreed
date_added: 2026-03-24
---

## 🔒 Security & Safety Notes

* **Key Management:** Use CI/CD secrets for `GEMINI_API_KEY` in production.
* **Least Privilege:** Test "Hardened" manifests in staging first to ensure no functional regressions.

## Links

+ - **Repository**: https://github.com/Champbreed/AegisOps-AI
+ - **Documentation**: https://github.com/Champbreed/AegisOps-AI#readme

## Limitations
- Use this skill only when the task clearly matches the scope described above.
- Do not treat the output as a substitute for environment-specific validation, testing, or expert review.
- Stop and ask for clarification if required inputs, permissions, safety boundaries, or success criteria are missing.
