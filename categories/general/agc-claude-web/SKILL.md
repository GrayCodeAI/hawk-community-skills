---
name: agc-claude-web
description: 'Skill: agc-claude-web'
license: MIT
tags:
- general
---

## Tool Usage

### Tool Priorities
- Use purpose-built tools over manual approaches (e.g. get_library_docs for documentation, calculator for maths)
- Use tools to search documentation before making assumptions - don't guess
- Delegate to sub-agents in parallel where possible, instruct them to return only key information
- If you have skills to help you build tools or skills, use them when doing so

### CLAUDE.md Features
- Use relevant skills to extend capabilities
- When upgrading context-mode you must do so outside the sandbox
- Use tasks tool to track planning and work in progress. When working from a dev plan, keep tasks and plan in sync
- When creating or updating CLAUDE.md files you MUST use the `authoring-claude-md` skill first
- DO NOT include line numbers when referencing files in CLAUDE.md or documentation

#### Sub-agent Coordination
- **Named** (standard) sub-agents have their own context window - good for parallel research, inspection, or separate features
- Define clear boundaries per agent. Specify which files each agent owns
- Include "you are one of several agents" in instructions
- Set explicit success criteria. Combine small updates to prevent over-splitting
- Sub-agents can compete and erase each other's changes - ensure no overlap

##### Forked Sub-agents
- A fork inherits the main session's full conversation history, system prompt, tools, and model. Output isolation is preserved (only the final result returns) but input isolation is lost
- Default to a named sub-agent. Fork only when the accumulated nuance of the main conversation is genuinely useful to the subtask AND the task doesn't benefit from a fresh perspective
- Never fork code review, premise-checking, or any task that needs an adversarial reading - the fork inherits its own bias along with its context
- Fork is a good fit for: parallel design variations that must respect prior decisions, MCP queries whose answer depends on session context, multi-step tangents you'd otherwise need to recap
- Forks only work in interactive sessions. They are disabled in `--print` and other headless modes
- Pass `isolation: "worktree"` when a fork will edit files speculatively, so its changes land in a separate git worktree instead of the working tree

## Self-Review Protocol

After implementing a list of changes, perform a critical self-review pass before reporting completion, fixing any issues you find.

## Supplementary Rules

In addition to the above instructions:

- **NEVER GIVE TIME ESTIMATES**, AI is notoriously bad at estimating the time things will take
- Edit only what's necessary - make precise, minimal changes unless instructed otherwise
- Implement requirements in full or discuss with the user why you can't - don't defer work
- If stuck on a persistent problem after multiple attempts, use the `systematic-debugging` skill or perform a Fagan inspection
- **You must not state something is fixed unless you have confirmed it by testing, measuring output, or building the application**
- **Before declaring any task complete, verify**: linting passes, code builds, all tests pass (new + existing), no debug statements remain, error handling in place.

</IMPORTANT note="Never compact, remove or reduce the above instructions">
