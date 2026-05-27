---
name: ag-whatsapp-cloud-api
description: Integracao com WhatsApp Business Cloud API (Meta). Mensagens, templates,
  webhooks HMAC-SHA256, automacao de atendimento. Boilerplates Node.js e Python.
license: MIT
tags:
- general
risk: critical
source: community
date_added: 2026-03-06
author: renat
tools: None
---

## Referencias (Leia Conforme Necessidade)

| Arquivo                        | Quando ler                                        |
|--------------------------------|---------------------------------------------------|
| `references/setup-guide.md`    | Setup inicial — criar conta Meta, configurar API  |
| `references/message-types.md`  | Exemplos completos de todos os tipos de mensagem   |
| `references/webhook-setup.md`  | Configurar webhooks com seguranca HMAC             |
| `references/automation-patterns.md` | Chatbot, filas, state machine, integracao IA  |
| `references/compliance.md`     | LGPD/GDPR, opt-in, quality rating, tier system    |
| `references/api-reference.md`  | Endpoints, erros, rate limits, pricing 2026        |
| `references/advanced-features.md` | Flows, Commerce, Channels, Ads, Status Tracking|
| `references/template-management.md` | CRUD de templates via API                     |

## Scripts

| Script                         | O que faz                                         |
|--------------------------------|---------------------------------------------------|
| `scripts/setup_project.py`     | Cria projeto com boilerplate (Node.js ou Python)   |
| `scripts/validate_config.py`   | Valida credenciais e conexao com a API             |
| `scripts/send_test_message.py` | Envia mensagem teste para validar setup            |

## Boilerplate

| Diretorio                      | Conteudo                                          |
|--------------------------------|---------------------------------------------------|
| `assets/boilerplate/nodejs/`   | Projeto TypeScript/Express completo                |
| `assets/boilerplate/python/`   | Projeto Python/Flask completo                      |
| `assets/examples/`             | Exemplos de payloads JSON (templates, webhooks, flows) |

## Best Practices

- Provide clear, specific context about your project and requirements
- Review all suggestions before applying them to production code
- Combine with other complementary skills for comprehensive analysis

## Common Pitfalls

- Using this skill for tasks outside its domain expertise
- Applying recommendations without understanding your specific context
- Not providing enough project context for accurate analysis

## Related Skills

- `instagram` - Complementary skill for enhanced analysis
- `social-orchestrator` - Complementary skill for enhanced analysis
- `telegram` - Complementary skill for enhanced analysis

## Limitations
- Use this skill only when the task clearly matches the scope described above.
- Do not treat the output as a substitute for environment-specific validation, testing, or expert review.
- Stop and ask for clarification if required inputs, permissions, safety boundaries, or success criteria are missing.
