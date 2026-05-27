---
name: tl-subagent-creator
description: Guide for creating AI subagents with isolated context for complex multi-step
  workflows. Use when users want to create a subagent, specialized agent, verifier,
  debugger, or orchestrator that require...
license: MIT
tags:
- general
---

You are a code review expert.

When invoked:

1. Analyze the code changes
2. Check readability, performance, patterns, error handling
3. Identify code smells and potential bugs
4. Suggest specific improvements

Report:
**✅ Approved / ⚠️ Approved with caveats / ❌ Changes needed**

**Issues Found:**

- **[Severity]** [Location]: [Issue]
  - Suggestion: [How to fix]
```

## Best Practices

### ✅ DO

- **Write focused subagents**: One clear responsibility
- **Invest in the description**: Determines when to delegate
- **Keep prompts concise**: Direct and specific
- **Share with team**: Version control subagent definitions
- **Test the description**: Check correct subagent is triggered

### ❌ AVOID

- **Vague descriptions**: "Use for general tasks" gives no signal
- **Prompts too long**: 2000 words don't make it smarter
- **Too many subagents**: Start with 2-3 focused ones

## Quality Checklist

Before finalizing:

- [ ] Description is specific about when to delegate
- [ ] Name uses kebab-case
- [ ] One clear responsibility (not generic)
- [ ] Prompt is concise but complete
- [ ] Instructions are actionable
- [ ] Output format is well defined
- [ ] Model configuration appropriate

## Output Messages

When creating a subagent:

```
✅ Subagent created successfully!

📁 Location: .agent/subagents/[name].md
🎯 Purpose: [brief description]
🔧 How to invoke:
   - Automatic: Agent delegates when it detects [context]
   - Explicit: /[name] [instruction]

💡 Tip: Include keywords like "use proactively" to encourage delegation.
```
