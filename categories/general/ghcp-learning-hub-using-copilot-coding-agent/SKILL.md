---
name: ghcp-learning-hub-using-copilot-coding-agent
description: Learn how to use GitHub Copilot coding agent to autonomously work on
  issues, generate pull requests, and automate development tasks.
license: MIT
tags:
- general
title: Using the Copilot Coding Agent
authors: None
lastUpdated: 2026-04-28
estimatedReadingTime: 12 minutes
relatedArticles: None
prerequisites: None
---

When creating database migrations, follow this process:

1. Run `./scripts/check-schema.sh` to validate current state
2. Create a new migration file following the naming convention: `YYYYMMDD_description.sql`
3. Always include a rollback section
4. Test the migration against a local database before committing
```

### Skills vs Instructions vs Agents

| Feature | Instructions | Skills | Custom Agents |
|---------|-------------|--------|---------------|
| When loaded | Always (matching file patterns) | Automatically when relevant | When explicitly selected |
| Best for | Coding standards, style guides | Specialized task guidance | Role-based personas |
| Can include scripts | No | Yes | No (but can reference skills) |
| Scope | File-pattern based | Task-based | Session-wide |

> **Tip**: Browse the [Skills Directory]() for ready-to-use skills you can add to your repository. Each skill includes a `SKILL.md` and any bundled assets needed.

## Leveraging Community Resources

This repository provides a curated collection of agents, skills, and hooks designed for the coding agent. Here's how to use them:

### Adding Agents from This Repo

1. Browse the [Agents Directory]() for agents matching your needs
2. Copy the `.agent.md` file into your repository's `.github/agents/` directory
3. The agent will be available in the dropdown when assigning work to the coding agent

### Adding Skills from This Repo

1. Browse the [Skills Directory]() for specialized skills
2. Copy the entire skill folder into your repository's `.github/skills/` directory
3. The coding agent will automatically use the skill when it's relevant to a task

### Adding Hooks from This Repo

1. Browse the [Hooks Directory]() for automation hooks
2. Copy the `hooks.json` content into a file in `.github/hooks/` in your repository
3. Copy any referenced scripts alongside it
4. The hooks will run automatically during coding agent sessions

> **Example workflow**: Combine a `test-specialist` agent with a `database-migrations` skill and a linting hook. Assign an issue to the coding agent using the test-specialist agent — it will automatically pick up the migrations skill when relevant, and the hook ensures all code is formatted before completion.

## Remote Control

You can connect to and steer a running coding agent session from a local Copilot CLI terminal using **remote control**. This lets you observe the agent's progress, send follow-up prompts, and redirect its work in real time — without waiting for it to open a PR first.

### Starting a Remote-Controlled Session

Launch a session that registers with GitHub for remote access:

```bash
copilot --remote
```

Or open a remote control tab from inside an existing session, and check or toggle its state:

```
/remote             # show current remote control status
/remote on          # enable remote control and register with GitHub
/remote off         # disable remote control for this session
```

The **Remote** tab in the CLI shows all active coding agent tasks from the repository. Select a task to connect and begin sending steering messages.

### Resuming from the Session Picker

Remote sessions also appear in the `--resume` picker, so you can reconnect to a coding agent session you were previously controlling without needing to know the session ID:

```bash
copilot --resume
```

### Why Use Remote Control?

| Scenario | Benefit |
|----------|---------|
| Long-running tasks | Monitor progress without waiting for the final PR |
| Mid-course corrections | Redirect the agent if it heads in the wrong direction |
| Interactive refinement | Provide clarification and feedback as the agent works |
| No PR required | You can steer tasks that haven't yet opened a pull request |

> **Note**: Remote control replaces the earlier "steering" feature. If you see references to steering in older documentation, remote control is the updated equivalent.

## Hooks and the Coding Agent

Hooks are especially valuable with the coding agent because they provide deterministic guardrails for autonomous work:

- **`preToolUse`**: Approve or deny tool executions — block dangerous commands and enforce security policies
- **`postToolUse`**: Format code, run linters, and validate changes after edits
- **`agentStop`**: Run final checks (e.g., full lint pass) when the agent finishes responding
- **`sessionStart`**: Log the start of autonomous sessions for governance
- **`sessionEnd`**: Send notifications when the agent finishes

See [Automating with Hooks]() for configuration details.

## Best Practices

### Setting Up for Success

- **Invest in `copilot-setup-steps.yml`**: A reliable setup means the agent can build and test confidently. If tests are flaky, the agent will struggle.
- **Add comprehensive instructions**: The agent reads your `.github/instructions/` files. The more context you provide about patterns and conventions, the better the output.
- **Create skills for repeatable tasks**: If your team frequently does a specific type of work (migrations, API endpoints, test suites), create a skill with step-by-step guidance the agent can follow automatically.
- **Use custom agents for specialized roles**: Create focused agent profiles for different types of work — a security reviewer, a test specialist, or an infrastructure expert.
- **Define hooks for formatting**: Hooks ensure the agent's code meets your style requirements automatically, reducing review friction.

### Choosing the Right Tasks

The coding agent excels at:
- ✅ Well-defined feature implementations with clear acceptance criteria
- ✅ Bug fixes with reproducible steps
- ✅ Adding tests to existing code
- ✅ Refactoring with specific goals (extract function, rename, etc.)
- ✅ Documentation updates based on code changes

It's less suited for:
- ❌ Ambiguous design decisions that need team discussion
- ❌ Large architectural changes spanning many files
- ❌ Tasks requiring access to external systems not in the dev environment
- ❌ Performance optimization without clear metrics

### Security Considerations

- The coding agent works in an isolated environment—it can't access your local machine
- It can only modify code in its branch—it can't push to main or deploy
- All changes go through PR review before merging
- Use hooks to enforce security scanning on every commit
- Scope repository permissions appropriately

## Common Questions

**Q: How long does the coding agent take?**

A: Typically 5–30 minutes depending on the complexity of the task and the size of the codebase. You'll receive a notification when the PR is ready.

**Q: Can I use the coding agent with private repositories?**

A: Yes. The coding agent works with both public and private repositories where GitHub Copilot is enabled.

**Q: What if the agent gets stuck?**

A: The agent has built-in timeouts. If it can't make progress, it will open a PR with what it has and explain what it couldn't resolve. You can then comment with guidance or take over manually.

**Q: Can I assign multiple issues at once?**

A: Yes. The coding agent can work on multiple issues in parallel, each in its own branch. Use Mission Control on GitHub.com to track all active agent sessions.

**Q: Does the coding agent use my custom agents and skills?**

A: Yes. You can specify which agent to use when assigning work — the coding agent adopts that agent's persona, tools, and guardrails. Skills are loaded automatically when the agent determines they're relevant to the task, based on the skill's description.

## Next Steps

- **Set Up Your Environment**: Create `.github/copilot-setup-steps.yml` for your project
- **Create Skills**: [Creating Effective Skills]() — Build skills the coding agent can use automatically
- **Add Guardrails**: [Automating with Hooks]() — Ensure code quality in autonomous sessions
- **Build Custom Agents**: [Building Custom Agents]() — Create specialized agents for the coding agent to use
- **Explore Configuration**: [Copilot Configuration Basics]() — Set up repository-level customizations
- **Browse Community Resources**: Explore the [Agents](), [Skills](), and [Hooks]() directories for ready-to-use resources

---
