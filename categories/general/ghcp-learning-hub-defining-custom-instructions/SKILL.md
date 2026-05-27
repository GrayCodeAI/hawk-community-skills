---
name: ghcp-learning-hub-defining-custom-instructions
description: Learn how to create persistent, context-aware instructions that guide
  GitHub Copilot automatically across your codebase.
license: MIT
tags:
- general
title: Defining Custom Instructions
authors: None
lastUpdated: 2026-03-22
estimatedReadingTime: 8 minutes
relatedArticles: None
prerequisites: None
---

# Playwright Testing Standards

Write descriptive test names that explain the expected behavior.

## Test Structure

```typescript
test('should display error message when login fails', async ({ page }) => {
  await page.goto('/login');
  await page.fill('#username', 'invalid');
  await page.fill('#password', 'invalid');
  await page.click('#submit');
  
  await expect(page.locator('.error')).toBeVisible();
});
```
````

This instruction applies only to test files, ensuring test-specific context.

## Structuring Instruction Content

### Effective Organization

A well-structured instruction file includes:

1. **Clear title and overview**: What this instruction covers
2. **Specific guidelines**: Actionable rules, not vague suggestions
3. **Code examples**: Working snippets showing correct patterns
4. **Explanations**: Why certain approaches are preferred

### Writing Style Best Practices

- **Be specific**: "Use PascalCase for component names" instead of "name components well"
- **Show examples**: Include working code snippets demonstrating patterns
- **Explain reasoning**: Brief context helps Copilot understand intent
- **Stay concise**: Focus on what matters most; avoid exhaustive documentation

**Example - Vague vs Specific**:

❌ **Vague**: "Handle errors properly"

✅ **Specific**:
````markdown
## Error Handling

Wrap async operations in try-catch blocks and log errors:

```typescript
try {
  const data = await fetchUser(userId);
  return data;
} catch (error) {
  logger.error('Failed to fetch user', { userId, error });
  throw new UserNotFoundError(userId);
}
```
````

## Common Questions

**Q: How many instructions should I create?**

A: Start with 3-5 core instructions covering your most important standards (naming, structure, security). Add more as patterns emerge. Having 10-20 instructions for a medium-sized project is reasonable. Awesome Copilot repository contains over 120 to demonstrate the range of possibilities.

**Q: Do instructions slow down Copilot?**

A: No. Instructions are processed efficiently as part of Copilot's context window. Keep individual files focused (under 500 lines) for best results, and ensure that they are scoped appropriately.

**Q: Can instructions contradict each other?**

A: If multiple instructions apply to the same file, Copilot considers all of them. Avoid contradictions by keeping instructions focused and using specific `applyTo` patterns. More specific patterns take precedence mentally, but it's best to design complementary instructions.

**Q: How do I know if my instructions are working?**

A: Test by asking Copilot to generate code matching your patterns. If it follows your standards without explicit prompting, the instructions are effective. You can also reference the instruction explicitly in chat: "Following the TypeScript standards in my instructions, create a user component."

**Q: Should I document everything in instructions?**

A: No. Instructions are for persistent standards that apply repeatedly. Document one-off decisions in code comments. Use instructions for patterns you want Copilot to follow automatically.

## Best Practices

- **One purpose per file**: Create separate instructions for different concerns (security, testing, styling)
- **Use clear naming**: Name files descriptively: `react-component-standards.instructions.md`, not `rules.instructions.md`
- **Include examples**: Every guideline should have at least one code example
- **Keep it current**: Review instructions when dependencies or frameworks update
- **Test your instructions**: Generate code and verify Copilot follows the patterns
- **Link to documentation**: Reference official docs for detailed explanations
- **Use tables for rules**: Tabular format works well for naming conventions and comparisons

## Common Pitfalls to Avoid

- ❌ **Too generic**: "Write clean code" doesn't give Copilot actionable guidance  
  ✅ **Instead**: Provide specific patterns: "Extract functions longer than 20 lines into smaller, named functions"

- ❌ **Too verbose**: Including entire documentation pages overwhelms the context window  
  ✅ **Instead**: Distill key patterns and link to full documentation

- ❌ **Contradictory rules**: Different instructions suggesting opposite approaches  
  ✅ **Instead**: Design complementary instructions with clear scopes

- ❌ **Outdated patterns**: Instructions referencing deprecated APIs or old versions  
  ✅ **Instead**: Review and update instructions when dependencies change

- ❌ **Missing scope**: Using `applyTo: '**'` for language-specific guidelines  
  ✅ **Instead**: Scope to relevant files: `applyTo: '**/*.py'` for Python-specific rules

## Next Steps

Now that you understand custom instructions, you can:

- **Explore Repository Examples**: Browse [Instructions Directory](../../instructions/) - Over 120 real-world examples covering frameworks, languages, and domains
- **Learn About Skills**: [Creating Effective Skills](../creating-effective-skills/) - Discover when to use skills instead of instructions
- **Understand Agents**: [Building Custom Agents](../building-custom-agents/) - See how agents complement instructions for complex workflows
- **Configuration Basics**: [Copilot Configuration Basics](../copilot-configuration-basics/) - Learn how to organize and manage your customizations

**Suggested Reading Order**:
1. This article (defining custom instructions)
2. [Creating Effective Skills](../creating-effective-skills/) - Learn complementary customization type
3. [Building Custom Agents](../building-custom-agents/) - Decision framework for when to use each type
