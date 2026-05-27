---
name: ag-task-intelligence
description: Protocolo de Inteligência Pré-Tarefa — ativa TODOS os agentes relevantes
  do ecossistema ANTES de executar qualquer tarefa solicitada pelo usuário.
license: MIT
tags:
- general
risk: none
source: community
date_added: 2026-03-06
author: renat
tools: None
---

## Exemplo De Briefing Completo

**Tarefa do usuário:** "Crie uma skill para integração com Stripe"

```
BRIEFING PRÉ-EXECUÇÃO — Skill: stripe-integration
════════════════════════════════════════════════════

CONTEXTO COLETADO (3 agentes consultados):
  • 007: CRÍTICO — API keys do Stripe NÃO devem ir para SKILL.md ou git.
    Usar variáveis de ambiente (.env). Webhooks precisam validação HMAC-SHA256.
  • skill-sentinel: whatsapp-cloud-api já implementa padrão HMAC-SHA256 para webhooks
    — reusar esse padrão. Skill deve seguir estrutura: config.py + client.py + SKILL.md.
  • agent-orchestrator: 3 skills similares (whatsapp, telegram, instagram) como referência
    de arquitetura. Nenhuma conflita com Stripe.

PLANO DE EXECUÇÃO:
  1. Criar estrutura de diretórios (~2min) — base para os demais arquivos
  2. Escrever SKILL.md com workflow (~5min) — define comportamento do agente
  3. Criar config.py com variáveis de ambiente (~3min) — sem hardcode de keys
  4. Criar stripe_client.py com autenticação (~10min) — métodos principais
  5. Criar webhook_handler.py com HMAC-SHA256 (~5min) — reusar padrão whatsapp
  6. Instalar via skill-installer (~2min) — validação + registro
  7. Gerar ZIP (~1min) — para backup/upload manual

TEMPO TOTAL: ~28min | CONFIANÇA: Alta
(estrutura clara, dependências conhecidas, sem APIs externas incertas)

PROBLEMAS PRÉ-RESOLVIDOS:
  ✅ API key exposta → .env obrigatório, .gitignore configurado
  ✅ YAML inválido → validar antes de instalar
  ✅ Webhook sem autenticação → HMAC-SHA256 incluído no plano

PONTOS DE VERIFICAÇÃO:
  [ ] Após SKILL.md: yaml.safe_load não levanta exceção
  [ ] Após config.py: sem strings hardcoded de credenciais
  [ ] Final: skill-installer valida os 10 checks

ROLLBACK PLAN:
  → Se skill-installer falhar: pasta em /tmp/stripe-skill-backup/
  → Se ZIP corrompido: reconstruir com build_ecosystem.py
════════════════════════════════════════════════════
```

## Best Practices

- Provide clear, specific context about your project and requirements
- Review all suggestions before applying them to production code
- Combine with other complementary skills for comprehensive analysis

## Common Pitfalls

- Using this skill for tasks outside its domain expertise
- Applying recommendations without understanding your specific context
- Not providing enough project context for accurate analysis

## Related Skills

- `agent-orchestrator` - Complementary skill for enhanced analysis
- `multi-advisor` - Complementary skill for enhanced analysis

## Limitations
- Use this skill only when the task clearly matches the scope described above.
- Do not treat the output as a substitute for environment-specific validation, testing, or expert review.
- Stop and ask for clarification if required inputs, permissions, safety boundaries, or success criteria are missing.
