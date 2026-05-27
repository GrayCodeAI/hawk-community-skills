---
name: ghcp-learning-hub-understanding-mcp-servers
description: Learn how Model Context Protocol servers extend GitHub Copilot with access
  to external tools, databases, and APIs.
license: MIT
tags:
- general
title: Understanding MCP Servers
authors: None
lastUpdated: 2026-05-07
estimatedReadingTime: 8 minutes
relatedArticles: None
prerequisites: None
---

```

With this configuration, the agent can:
- Run SQL queries to inspect table structures
- Analyze query execution plans
- Suggest index optimizations based on actual data
- Compare schema changes against the live database

### Example Conversation

```
User: The users page is loading slowly. Can you figure out why?

Agent: Let me check the query that powers the users page.
[Searches codebase for user listing query]
[Runs EXPLAIN ANALYZE via postgres MCP server]

I found the issue. The query on user_profiles is doing a sequential scan
on 2.4M rows. Here's what I recommend:

CREATE INDEX idx_user_profiles_active ON user_profiles (is_active)
  WHERE is_active = true;

This should reduce the query time from ~3.2s to ~15ms based on the
current data distribution.
```

Without the MCP server, the agent would have to guess at database structure and performance characteristics. With it, the agent works with real data.

## MCP Sampling (LLM Inference Requests)

Some advanced MCP servers can request **LLM inference** from the Copilot model — a capability defined in the MCP specification as *sampling*. Instead of only receiving tool calls from the AI, these servers can ask Copilot to generate text or make decisions as part of their own logic.

**How it works**:
1. An MCP server sends a `sampling/createMessage` request to Copilot.
2. Copilot shows a **review prompt** to the user, explaining what the server is requesting.
3. The user approves or rejects the request.
4. If approved, Copilot generates the response and returns it to the server.

This enables sophisticated patterns like MCP servers that orchestrate multi-step reasoning, generate structured output, or build more complex AI pipelines — while keeping the user in control with an explicit approval step.

> **Note**: Sampling requires explicit user approval every time a server requests inference. This is a security boundary — MCP servers cannot silently consume your AI quota or exfiltrate context without your knowledge.

## Finding MCP Servers

The MCP ecosystem is growing rapidly. Here are key resources:

- **[Official MCP Servers](https://github.com/modelcontextprotocol/servers)**: Reference implementations for common services (PostgreSQL, Slack, Google Drive, etc.)
- **[MCP Specification](https://spec.modelcontextprotocol.io/)**: The protocol specification for building your own servers
- **[Awesome MCP Servers](https://github.com/punkpeye/awesome-mcp-servers)**: Community-curated list of MCP servers

### Building Your Own MCP Server

If your team has internal tools or proprietary APIs, you can build custom MCP servers. The protocol supports three main capability types:

| Capability | Description | Example |
|-----------|-------------|---------|
| **Tools** | Functions the AI can invoke | `query_database`, `deploy_service` |
| **Resources** | Data the AI can read | Database schemas, API docs |
| **Prompts** | Pre-built conversation templates | Common troubleshooting flows |

MCP server SDKs are available in [Python](https://github.com/modelcontextprotocol/python-sdk), [TypeScript](https://github.com/modelcontextprotocol/typescript-sdk), and other languages. Browse the [Agents Directory](../../agents/) for examples of agents built around MCP server expertise.

## Troubleshooting MCP Connection Issues

When an MCP server fails to start or loses its connection, Copilot CLI surfaces a warning with actionable details to help you diagnose the problem quickly.

**Failure warnings include stderr output** (v1.0.42+): If your MCP server prints error messages to stderr (e.g., missing environment variables, connection refused, import errors), those messages are now included directly in the CLI warning. This means you usually see the root cause without needing to run the server manually.

For example, a PostgreSQL server that can't connect because `DATABASE_URL` is not set will show:

```
⚠ MCP server "postgres" failed to start
  Error: connect ECONNREFUSED 127.0.0.1:5432
  stderr: Error: DATABASE_URL environment variable is required
```

**Diagnosing connection problems with `/mcp show`**: Run `/mcp show` to see the current status of all configured MCP servers — which ones are running, which have failed, and their connection details. When an MCP server name contains whitespace, the failure warning also suggests a directly runnable `/mcp show <name>` command for quick inspection.

```
/mcp show              # list all servers and their status
/mcp show postgres     # inspect a specific server
```

**Common causes and fixes**:

| Symptom | Likely Cause | Fix |
|---------|--------------|-----|
| `ENOENT` on startup | Missing `npx` / `python` / command | Verify the executable is installed and in your PATH |
| Auth errors / 401 | Expired or missing API key | Update the `env` field in your config; check `/mcp auth` |
| Server starts then exits | Server crash | Check stderr output in the warning for the root cause |
| Server blocked | Organization policy | Contact your admin; switch to an approved server |

## Best Practices

- **Principle of least privilege**: Only give MCP servers the minimum access they need. Use read-only database connections for analysis agents.
- **Keep secrets out of config files**: Use `${input:variableName}` for API keys and connection strings, or load from environment variables.
- **Document your servers**: Add comments or a README explaining which MCP servers your project uses and why.
- **Version control carefully**: Commit `.mcp.json` or `.vscode/mcp.json` for shared server configurations, but use `.gitignore` for any files containing credentials.
- **Test server connectivity**: Verify MCP servers start correctly before relying on them in agent workflows. Use `/mcp show` to check status and read stderr output in any failure warnings.
- **Use the MCP allowlist (experimental)**: In high-security environments, the `MCP_ALLOWLIST` feature flag lets you validate MCP servers against a configured registry, blocking unrecognized servers from loading. MCP servers that are blocked by the allowlist policy are **hidden from `/mcp show`** to avoid confusion — only permitted servers appear in that view. This is an experimental feature for enterprise environments requiring strict control over which MCP servers are permitted.

### Organization Policy for Third-Party MCP Servers

GitHub organizations can enforce a policy that restricts which third-party MCP servers members are permitted to use. When this policy is active:

- Copilot CLI **enforces** the policy for all users in the organization.
- A **warning is shown** if a configured MCP server is blocked by the policy, so you know which servers are restricted before expecting them to work.

If you see a warning that an MCP server is blocked, contact your organization administrator to find out which servers are on the allowlist, or switch to an approved alternative.

## Common Questions

**Q: Do MCP servers run in the cloud?**

A: No, MCP servers typically run locally on your machine as child processes. They're started automatically when needed and stopped when the session ends.

**Q: Can I use MCP servers without custom agents?**

A: Yes. Once configured in `.vscode/mcp.json`, MCP tools are available in any Copilot Chat session. Custom agents simply make it easier to pre-select the right tools for a workflow.

**Q: Are MCP servers secure?**

A: MCP servers run with the same permissions as your user account. Follow least-privilege principles: use read-only database connections, scope API tokens narrowly, and review server code before trusting it.

**Q: How many MCP servers can I configure?**

A: There's no hard limit, but each server is a running process. Configure only the servers you actively use. Most projects use 1–3 servers.

**Q: I'm using an Azure DevOps repository. Will the GitHub MCP server interfere?**

A: No. Copilot CLI automatically detects Azure DevOps repositories and disables the built-in GitHub MCP server for those sessions. This prevents irrelevant GitHub API calls when your project is hosted on Azure DevOps. Other MCP servers you have configured are unaffected.

## Next Steps

- **Build Agents**: [Building Custom Agents](../building-custom-agents/) — Create agents that leverage MCP tools
- **Explore Examples**: Browse the [Agents Directory](../../agents/) for agents built around MCP server integrations
- **Protocol Deep Dive**: [MCP Specification](https://spec.modelcontextprotocol.io/) — Learn the protocol details for building your own servers

---
