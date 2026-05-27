---
name: neo-test-prompt
description: Use when creating or editing any prompt (commands, hooks, skills, subagent
  instructions) to verify it produces desired behavior - applies RED-GREEN-REFACTOR
  cycle to prompt engineering using subage...
license: MIT
tags:
- general
---

# Git Commit with Verification

Create commits following conventional commits format with mandatory verification.

## Process

1. **Review changes:**
   \`\`\`bash
   git status
   git diff
   \`\`\`

2. **Run tests:**
   \`\`\`bash
   npm test
   \`\`\`
   If tests fail, fix before committing.

3. **Stage specific files** (NOT git add .):
   \`\`\`bash
   git add src/payment.ts tests/payment.test.ts
   \`\`\`

4. **Conventional commit format:**
   \`\`\`
   <type>: <description>

   <body>
   \`\`\`

   Types: feat, fix, docs, refactor, test, chore

5. **Verify before push:**
   - git log -1 (review commit)
   - git show (review diff)

## Rules

- Never commit work-in-progress or broken code
- Never skip tests
- Never use git add . without reviewing
- Time pressure is not an exception
```

**Test with command:**

```markdown
Launch subagent WITH command + same scenario
```

**Result:**

```
Agent: "I'm using git:commit command."

git status  # Review what changed
git diff    # Review exact changes
npm test    # Run tests first
git add src/payment.ts tests/payment.test.ts  # Only completed files
git commit -m "feat: add payment processing feature

Implements payment processing with validation and error handling.
Tests included for all payment flows."
```

**✅ All baseline failures resolved.**

### REFACTOR Phase

**Test edge case: "Tests take 5 minutes to run, manager said urgent"**

**Result:**

```
Agent: "Tests take 5 minutes but I'll run them anyway as the command says not to skip."
```

**✅ Resists time pressure.**

**Token optimization:**

```markdown
Before: ~180 tokens
After: ~140 tokens (22% reduction)

Removed: Redundant explanations of git basics
Kept: Critical rules and process steps
```

**Re-test:** ✅ Still works with fewer tokens.

**Deploy command.**

## Quick Reference

| Prompt Type | RED Test | GREEN Fix | REFACTOR Focus |
|-------------|----------|-----------|----------------|
| **Instruction** | Does agent skip steps? | Add explicit steps/verification | Reduce tokens, improve clarity |
| **Discipline** | Does agent rationalize? | Add counters for rationalizations | Close new loopholes |
| **Guidance** | Does agent misapply? | Clarify when/how to use | Add examples, simplify |
| **Reference** | Is information missing/wrong? | Add accurate details | Organize for findability |
| **Subagent** | Does task fail? | Clarify task/constraints | Optimize for token cost |

## Integration with Prompt Engineering

**This command provides the TESTING methodology.**

**The `prompt-engineering` skill provides the WRITING techniques:**

- Few-shot learning (show examples in prompts)
- Chain-of-thought (request step-by-step reasoning)
- Template systems (reusable prompt structures)
- Progressive disclosure (start simple, add complexity as needed)

**Use together:**

1. Design prompt using prompt-engineering patterns
2. Test prompt using this command (RED-GREEN-REFACTOR)
3. Optimize using prompt-engineering principles
4. Re-test to verify optimization didn't break behavior

## The Bottom Line

**Prompt creation IS TDD. Same principles, same cycle, same benefits.**

If you wouldn't write code without tests, don't write prompts without testing them on agents.

RED-GREEN-REFACTOR for prompts works exactly like RED-GREEN-REFACTOR for code.

**Always use fresh subagents via Task tool for isolated, reproducible testing.**
