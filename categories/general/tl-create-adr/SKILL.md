---
name: tl-create-adr
description: Creates Architecture Decision Records (ADRs) to document significant
  architectural choices and their rationale for future team members. Use when the
  user says "write an ADR", "document this decisio...
license: CC-BY-4.0
tags:
- general
metadata: None
author: Tech Leads Club - github.com/tech-leads-club
version: 1.0.0
---

## Important Notes

- **ADRs are immutable** — never edit the decision. Supersede with a new ADR.
- **Short is better** — 200–500 words is ideal. If it needs to be longer, move detail to a linked TDD or RFC.
- **Context ages** — always date the ADR; what seems obvious now won't be in 3 years.
- **Honest consequences** — a one-sided ADR loses credibility. Future engineers will hit the downsides regardless.
- **Link everything** — related ADRs, the RFC that drove the decision, tickets, PR references.
- **Language adaptation** — always write in the user's language.
- **Number sequentially** — check the directory before assigning a number.

## Example Prompts that Trigger This Skill

### English
- "Write an ADR for using PostgreSQL as our primary database"
- "Document our decision to adopt GraphQL"
- "Create an ADR for moving our frontend to Next.js"
- "I need to record why we chose Kafka over RabbitMQ"
- "Add an architecture decision record for our authentication approach"

### Portuguese
- "Escreva um ADR sobre a decisão de usar PostgreSQL"
- "Documente a decisão de adotar GraphQL no projeto"
- "Crie um ADR explicando por que escolhemos Kafka"

### Spanish
- "Escribe un ADR sobre la decisión de usar PostgreSQL"
- "Documenta la decisión de adoptar microservicios"
- "Crea un ADR explicando por qué elegimos Next.js"
