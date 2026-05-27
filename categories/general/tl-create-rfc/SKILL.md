---
name: tl-create-rfc
description: Creates structured Request for Comments (RFC) documents for proposing
  and deciding on significant changes. Use when the user says "write an RFC", "create
  a proposal", "I need to propose a change", ...
license: CC-BY-4.0
tags:
- general
metadata: None
author: Tech Leads Club - github.com/tech-leads-club
version: 1.0.0
---

## Important Notes

- **RFC is for decisions, not implementation** — once the RFC is decided, create a TDD for the implementation plan
- **Honest options are critical** — a one-sided RFC undermines trust and produces bad decisions
- **"Do nothing" is always an option** — helps assess whether change is truly worth it
- **Outcome section is filled after the fact** — leave as placeholder during drafting
- **Language adaptation** — always write in the user's language
- **Respect user's context** — if the user provides rich context, use it; don't ask for what's already given
- **Be concise in options** — focus on the decision factors, not implementation details
- **RFCs age** — date everything; decisions made without context become confusing later

## Example Prompts that Trigger This Skill

### English
- "Write an RFC for migrating our database from MySQL to PostgreSQL"
- "I need an RFC to propose moving from monolith to microservices"
- "Create a request for comments on our on-call rotation policy"
- "Draft an RFC comparing self-hosted vs managed Kafka"
- "I need to get approval to adopt a new design system"

### Portuguese
- "Escreva um RFC para migrar nosso banco de dados"
- "Preciso de um RFC para propor a adoção de uma nova ferramenta"
- "Crie um Request for Comments sobre nossa política de on-call"
- "Quero documentar a decisão de trocar de provedor de cloud"

### Spanish
- "Escribe un RFC para migrar nuestra infraestructura a la nube"
- "Necesito un RFC para proponer un cambio en el proceso de deploy"
- "Crea un Request for Comments sobre la adopción de un nuevo framework"
