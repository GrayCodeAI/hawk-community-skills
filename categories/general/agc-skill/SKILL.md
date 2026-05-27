---
name: agc-skill
description: Use when working with AWS Strands Agents SDK or Amazon Bedrock AgentCore
  platform for building AI agents. Provides architecture guidance, implementation
  patterns, deployment strategies, observabili...
license: MIT
tags:
- general
---

## Key Takeaways

1. **MCP servers MUST use streamable-http, NEVER Lambda**
2. **Use semantic search for > 15 tools**
3. **Always implement conversation management**
4. **Multi-agent costs multiply 5-10x** (track from day one)
5. **Set timeout limits everywhere**
6. **Error handling in tools is non-negotiable**
7. **Lambda for stateless, AgentCore for interactive**
8. **AgentCore Observability and Evaluations for production**
9. **Start simple, evolve complexity**
10. **Security by default**
11. **Separate config from code**
