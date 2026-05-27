---
name: ghcp-learning-hub-agents-and-subagents
description: Learn how delegated subagents differ from primary agents, when to use
  them, and how to launch them in VS Code and Copilot CLI.
license: MIT
tags:
- general
title: Agents and Subagents
authors: None
lastUpdated: 2026-05-07
estimatedReadingTime: 9 minutes
relatedArticles: None
prerequisites: None
---

```

You can also use `disable-model-invocation: true` to prevent an agent from being used as a subagent unless another coordinator explicitly allows it.

### 3. Prompt for isolated or parallel work

You do not always need to say "run a subagent," but prompts that describe isolated research or parallel tracks make delegation easier. For example:

```text
Analyze this feature in parallel:
1. Research existing code patterns
2. Propose an implementation plan
3. Review likely security risks
Then summarize the findings into one recommendation.
```

### 4. Know the nesting rule

By default, subagents do not keep spawning additional subagents. In VS Code, recursive delegation is controlled by the `chat.subagents.allowInvocationsFromSubagents` setting, which is off by default.

## Launch subagents in Copilot CLI

In GitHub Copilot CLI, the clearest end-user entry point is **`/fleet`**. Fleet acts as an orchestrator that decomposes a larger objective, launches multiple background subagents, respects dependencies, and then synthesizes the final result.

```text
/fleet Update the auth docs, refactor the auth service, and add related tests.
```

For non-interactive execution:

```bash
copilot -p "/fleet Update the auth docs, refactor the auth service, and add related tests." --no-ask-user
```

> **Prompt mode and repo hooks (v1.0.40+)**: When using `copilot -p "..."` (prompt mode), repository hooks are disabled by default for security. If your `/fleet` workflow relies on hooks (e.g., auto-formatting or lint checks after edits), opt in by setting `GITHUB_COPILOT_PROMPT_MODE_REPO_HOOKS=true` before running. See [Automating with Hooks]() for details.

The important behavior is different from a single chat turn:

- the orchestrator plans work items first
- independent tasks can run in parallel
- each subagent gets its own context window
- subagents share the same filesystem, so overlapping writes should be avoided

That makes `/fleet` a practical way to launch subagents even if you are not authoring custom agent files yourself.

### Rubber-duck agent (experimental)

Available in `/experimental` (v1.0.42+), the **rubber-duck agent** applies a novel multi-model pattern: when you're working in a GPT-powered session, the rubber-duck agent internally routes certain requests through Claude to provide a second perspective. The idea is similar to rubber-duck debugging — talking through a problem with a different "listener" often surfaces assumptions or blind spots you didn't notice.

To try it, enable experimental features and then select the rubber-duck agent from the agent picker:

```
/experimental           # toggle experimental features
/agent                  # open the agent picker and select rubber-duck
```

Because it runs as a sub-agent layer rather than replacing your primary model, you keep your current session model and context while the rubber-duck analysis runs in the background.

> **Note**: This is an experimental feature and may change. Provide feedback via `/feedback` if you find it useful.

## Orchestration patterns that work well

### Coordinator and worker

One agent owns the workflow and delegates to narrower specialists such as planner, implementer, and reviewer. This keeps the coordinator lightweight and makes the worker prompts more precise.

### Multi-perspective review

Run parallel subagents for different lenses - correctness, security, code quality, architecture - and combine the results after they finish.

### Research, then act

Use one subagent to gather facts and another to implement with those facts. This pattern is especially helpful when you want the main thread to stay free of exploratory noise.

The built-in **`/research`** command uses this orchestrator/subagent model automatically (v1.0.40+): it spawns an orchestrator that breaks the topic into research threads, runs them in parallel as subagents, and synthesizes the findings into a structured report. This means you get deeper and more reliable results than a single-turn query provides — without having to set up the multi-agent pattern yourself.

## Repository examples you can inspect

This repository already includes a few useful examples of delegation-related syntax:

- [`agents/context7.agent.md`](https://github.com/github/awesome-copilot/blob/main/agents/context7.agent.md) is a concrete example of VS Code-style `handoffs`. It defines a handoff button that can pass work to another agent after research is complete.
- [`agents/rug-orchestrator.agent.md`](https://github.com/github/awesome-copilot/blob/main/agents/rug-orchestrator.agent.md) is a strong coordinator example. It enables the `agent` tool and restricts delegation with `agents: ['SWE', 'QA']`.
- [`agents/gem-orchestrator.agent.md`](https://github.com/github/awesome-copilot/blob/main/agents/gem-orchestrator.agent.md) shows invocation control with `user-invocable` and `disable-model-invocation`, which is useful when deciding whether an orchestrator should be directly selectable, delegatable, or both.
- [`agents/custom-agent-foundry.agent.md`](https://github.com/github/awesome-copilot/blob/main/agents/custom-agent-foundry.agent.md) documents the VS Code `handoffs` shape in its guidance section, which is helpful if you want a template before creating your own coordinator workflow.

## Important platform nuance: handoffs are not universal

VS Code documentation describes both subagents and the `handoffs` frontmatter property. [GitHub's custom agent configuration reference](https://docs.github.com/en/copilot/customizing-copilot/github-copilot-agents/configuration-reference-for-github-copilot-agents), however, notes that `handoffs` and `argument-hint` are currently ignored for Copilot cloud agent on GitHub.com.

That means you should think about delegation features in product-specific terms:

- **VS Code**: supports subagent concepts, allowlists, and handoff-oriented agent composition
- **Copilot CLI**: exposes practical orchestration through commands like `/fleet`
- **GitHub.com coding agent / cloud agent**: supports custom agents, but some VS Code-specific frontmatter is intentionally ignored

If you share agent files across surfaces, document those differences so users know which behaviors are portable and which are editor-specific.

## Common questions

**Do users always invoke subagents directly?**

No. Most of the time the main agent launches them when it decides the task benefits from context isolation or parallelism.

**Can a subagent use a different model or tool set?**

Yes, when the delegated worker is a custom agent with its own frontmatter.

**Are subagents always parallel?**

No. They can run sequentially when one step depends on another, or in parallel when work items are independent.

## Next steps

- Read [Building Custom Agents]() to design coordinator and worker agents.
- Revisit [What are Agents, Skills, and Instructions]() for the broader customization model.
- Keep the [GitHub Copilot Terminology Glossary]() nearby when comparing terminology across products.

---
