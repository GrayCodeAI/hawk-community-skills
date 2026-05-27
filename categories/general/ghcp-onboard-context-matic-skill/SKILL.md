---
name: ghcp-onboard-context-matic-skill
description: Interactive onboarding tour for the context-matic MCP server. Walks the
  user through what the server does, shows all available APIs, lets them pick one
  to explore, explains it in their project lang...
license: MIT
tags:
- general
---

## Notes for the agent

- If the user picks an API that is not in the `fetch_api` results, tell them it is not currently
  available and offer to continue the tour with one that is.
- All tool calls in this skill are **read-only** — they do not modify the project, install packages,
  or write files unless the user explicitly asks you to proceed with integration.
- When showing code samples from `endpoint_search` or `ask`, present them in fenced code blocks
  with the correct language tag.
