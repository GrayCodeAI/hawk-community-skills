---
name: flow-federation-status
description: "Show federation health — peers, sessions, trust levels, and message metrics"
license: MIT
tags: [general]
allowed-tools: Bash(npx *) mcp__claude-flow__memory_search Read
argument-hint: None
---

Show the current state of the federation.

Steps:
1. `npx -y -p @claude-flow/plugin-agent-federation@latest ruflo-federation status` -- overall health
2. `npx -y -p @claude-flow/plugin-agent-federation@latest ruflo-federation peers` -- list peers with trust levels and scores
3. Summarize: active sessions, messages exchanged, PII redactions, threat detections

Search memory for federation history:
`mcp__claude-flow__memory_search({ query: "federation peer trust", namespace: "federation" })`