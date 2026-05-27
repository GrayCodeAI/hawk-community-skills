---
name: agc-limitations
description: 'Skill: agc-limitations'
license: MIT
tags:
- general
---

## Summary: Priorities

### Must Address

1. **Tool Discovery at Scale**: Semantic search for > 50 tools
2. **Cost Monitoring**: Cost tracking from day one
3. **Observability**: Logging, metrics, tracing
4. **Security**: Tool-level permissions, human-in-the-loop
5. **MCP Servers**: Deploy in streamable-http mode, NOT Lambda

### Nice to Have

1. **Warm Agent Pools**: Reduce cold starts
2. **Response Caching**: Avoid duplicate LLM calls
3. **Multi-Region**: Deploy close to users

### Can Defer

1. **Advanced Multi-Agent**: Start single agents first
2. **Custom Models**: Use Bedrock initially
3. **Complex Graphs**: Begin with linear workflows
