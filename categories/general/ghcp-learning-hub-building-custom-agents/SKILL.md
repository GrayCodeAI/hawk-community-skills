---
name: ghcp-learning-hub-building-custom-agents
description: Learn how to create specialized GitHub Copilot agents with custom personas,
  tool integrations, and domain expertise.
license: MIT
tags:
- general
title: Building Custom Agents
authors: None
lastUpdated: 2026-05-05
estimatedReadingTime: 10 minutes
relatedArticles: None
prerequisites: None
---

```

The agent can then query your database, analyze query plans, and suggest optimizations—all within the conversation. For setup details, see [Understanding MCP Servers](../understanding-mcp-servers/).

## Best Practices

### Writing Effective Agent Personas

- **Be specific about expertise**: "Expert in React 18+ with TypeScript" beats "Frontend developer"
- **Define the working style**: Should the agent ask clarifying questions or make assumptions? Should it be concise or thorough?
- **Include guardrails**: What should the agent never do? ("Never modify production configuration files directly")
- **Provide examples**: Show the output format you expect (review comments, code patterns, etc.)

### Choosing the Right Model

| Scenario | Recommended Model |
|----------|-------------------|
| Complex reasoning, security review | Claude Sonnet 4 or higher |
| Code generation, refactoring | GPT-4.1 |
| Quick analysis, simple tasks | Claude Haiku or GPT-4.1-mini |
| Large codebase understanding | Models with larger context windows |

### Organizing Agents in Your Repository

```
.github/
└── agents/
    ├── security-reviewer.agent.md
    ├── api-designer.agent.md
    ├── terraform-expert.agent.md
    └── release-manager.agent.md
```

Keep agents focused—one persona per file. If you find an agent trying to do too many things, split it into multiple agents or extract common tasks into skills that agents can invoke.

## Common Questions

**Q: How do I select a custom agent?**

A: In VS Code, open Copilot Chat and use the agent picker dropdown at the top of the chat panel. Your custom agents appear alongside built-in options. You can also `@mention` an agent by name.

In Copilot CLI, custom agents are discoverable via the agent picker inside a session. Clients that integrate with Copilot CLI using the **Agent Coordination Protocol (ACP)** can also list available custom agents and switch between them programmatically via the `agent` session configuration option (v1.0.40+). This allows tools like Zed, Neovim plugins, and CI pipelines driving Copilot via ACP to surface the agent picker and switch agents without requiring a slash command. ACP clients also receive the agent's **live plan** as it works through multi-step tasks (v1.0.40+), so they can display real-time progress to their users without waiting for each turn to complete.

**Q: Can agents use skills?**

A: Yes. Agents can discover and invoke skills during a conversation based on the user's intent. Skills extend what an agent can do without bloating the agent's own instructions.

**Q: How many agents should a repository have?**

A: Start with 2–3 agents for your most common workflows. Add more as patterns emerge. Typical teams have 3–8 agents covering areas like code review, infrastructure, testing, and documentation.

**Q: Can I use an agent with the Copilot coding agent?**

A: Yes. When you assign an issue to Copilot, you can specify which agent should handle it. The agent's persona and tool access apply to the autonomous coding session. See [Using the Copilot Coding Agent](../using-copilot-coding-agent/) for details.

**Q: Should agents include code examples?**

A: Yes, when defining output format or coding patterns. Show what you expect the agent to produce—review formats, code structure, commit message style, etc.

## Common Pitfalls

- ❌ **Too broad**: "You are a software engineer" — no focus or guardrails
  ✅ **Instead**: Define specific expertise, review criteria, and output format

- ❌ **No tools specified**: Agent can't search code or run commands
  ✅ **Instead**: Declare the tools the agent needs in frontmatter

- ❌ **Conflicting with instructions**: Agent says "use tabs" but instructions say "use spaces"
  ✅ **Instead**: Agents should complement instructions, not contradict them

- ❌ **Monolithic agent**: One agent that handles security, testing, docs, and deployment
  ✅ **Instead**: Create focused agents and let them invoke shared skills

## Next Steps

- **Explore Repository Examples**: Browse the [Agents Directory](../../agents/) for production agent definitions
- **Connect External Tools**: [Understanding MCP Servers](../understanding-mcp-servers/) — Give agents access to databases, APIs, and more
- **Automate with Coding Agent**: [Using the Copilot Coding Agent](../using-copilot-coding-agent/) — Run agents autonomously on issues
- **Add Reusable Tasks**: [Creating Effective Skills](../creating-effective-skills/) — Build tasks agents can discover and invoke

---
