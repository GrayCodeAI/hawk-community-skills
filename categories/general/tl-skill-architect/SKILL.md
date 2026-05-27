---
name: tl-skill-architect
description: Expert guide for designing and building high-quality skills from scratch
  through structured conversation. Use when someone wants to create a new skill, build
  a skill, design a skill, or asks for he...
license: CC-BY-4.0
tags:
- general
metadata: None
author: Felipe Rodrigues - github.com/felipfr
version: 1.0.0
---

## Conversation Style

- Ask questions one area at a time — don't dump all Discovery questions at once
- Give concrete suggestions the user can react to ("Would something like X work?")
- If the user provides a vague request, propose a specific interpretation and ask
  if it matches their intent
- If the conversation already contains a workflow (user says "turn this into a
  skill"), extract what you can from history FIRST, then fill gaps with questions
- Match the user's technical level — explain terms if they seem non-technical
- Be direct about tradeoffs: if a design choice has a downside, say so

## Important Boundaries

- This skill is for CREATING new skills. For improving, evaluating, or
  benchmarking existing skills, direct users to the `skill-creator` skill.
- Never generate a SKILL.md without completing Discovery and Architecture.
  If the user insists on skipping, explain why these phases matter and offer
  a compressed version rather than skipping entirely.
- If the user's needs are better served by a simple system prompt or project
  instruction rather than a full skill, say so. Not everything needs to be a skill.
