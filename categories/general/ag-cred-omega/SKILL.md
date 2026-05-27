---
name: ag-cred-omega
description: CISO operacional enterprise para gestao total de credenciais e segredos.
license: MIT
tags:
- general
risk: critical
source: community
date_added: 2026-03-06
author: renat
tools: None
---

## Skills Complementares

| Skill | Integracao |
|-------|-----------|
| **007** | Threat modeling + Red Team — cred-omega cuida de segredos, 007 de arquitetura |
| **instagram** | Protecao de Meta tokens, Graph API secrets |
| **whatsapp-cloud-api** | Protecao de WABA tokens, webhook secrets |
| **telegram** | Protecao de bot tokens |
| **ai-studio-image** | Protecao de Google API keys |
| **stability-ai** | Protecao de Stability API keys |
| **context-agent** | Persistir estado de auditoria entre sessoes |
| **skill-sentinel** | Auditar seguranca das proprias skills |

## Quando Outra Skill Deve Chamar Cred-Omega

Qualquer skill que lide com APIs externas deve consultar cred-omega para:
1. Validar que credenciais estao armazenadas de forma segura
2. Verificar restricoes adequadas
3. Confirmar presenca no registry
4. Verificar rotacao em dia

## Best Practices

- Provide clear, specific context about your project and requirements
- Review all suggestions before applying them to production code
- Combine with other complementary skills for comprehensive analysis

## Common Pitfalls

- Using this skill for tasks outside its domain expertise
- Applying recommendations without understanding your specific context
- Not providing enough project context for accurate analysis

## Related Skills

- `007` - Complementary skill for enhanced analysis

## Limitations
- Use this skill only when the task clearly matches the scope described above.
- Do not treat the output as a substitute for environment-specific validation, testing, or expert review.
- Stop and ask for clarification if required inputs, permissions, safety boundaries, or success criteria are missing.
