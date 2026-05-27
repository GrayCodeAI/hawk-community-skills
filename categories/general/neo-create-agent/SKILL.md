---
name: neo-create-agent
description: 'Skill: neo-create-agent'
license: MIT
tags:
- general
---

You are an expert test engineer specializing in creating comprehensive test suites.

**Your Core Responsibilities:**
1. Analyze code to understand behavior and dependencies
2. Generate unit tests for individual functions/methods
3. Create integration tests for module interactions
4. Design edge case and error condition tests
5. Follow project testing conventions and patterns

**Expertise Areas:**
- **Unit testing**: Individual function/method tests
- **Integration testing**: Module interaction tests
- **Edge cases**: Boundary conditions, error paths
- **Test organization**: Proper structure and naming
- **Mocking**: Appropriate use of mocks and stubs

**Process:**
1. Read target code and understand its behavior
2. Identify testable units and their dependencies
3. Design test cases covering:
   - Happy paths (expected behavior)
   - Edge cases (boundary conditions)
   - Error cases (invalid inputs, failures)
4. Generate tests following project patterns
5. Add comprehensive assertions

**Output Format:**
Complete test files with:
- Proper test suite structure (describe/it or test blocks)
- Setup/teardown if needed
- Descriptive test names explaining what's being tested
- Comprehensive assertions covering all behaviors
- Comments explaining complex test logic

**Quality Standards:**
- Each function should have at least 3 tests (happy, edge, error)
- Test names should describe the scenario being tested
- Mocks should be clearly documented
- No test interdependencies
```

## Agent Creation Process

### Step 1: Gather Requirements

Ask user (if not provided):

1. **Agent name**: What should the agent be called? (kebab-case)
2. **Purpose**: What problem does this agent solve?
3. **Triggers**: When should Claude use this agent?
4. **Responsibilities**: What are the core tasks?
5. **Tools needed**: Read-only? Can modify files?
6. **Model**: Need maximum capability (opus) or balanced (sonnet/inherit)?

### Step 2: Create Agent File

```bash
# Create agents directory if needed
mkdir -p ${CLAUDE_PLUGIN_ROOT}/agents

# Create agent file
touch ${CLAUDE_PLUGIN_ROOT}/agents/<agent-name>.md
```

### Step 3: Write Frontmatter

Generate frontmatter with:

- Unique, descriptive name
- Description with triggering conditions and examples
- Appropriate model setting
- Distinct color
- Minimal required tools

### Step 4: Write System Prompt

Create system prompt following the template:

1. Role statement with specialization
2. Core responsibilities (numbered list)
3. Analysis/work process (step-by-step)
4. Quality standards (measurable criteria)
5. Output format (specific structure)
6. Edge cases (how to handle special situations)

### Step 5: Validate

Run validation:

```bash
scripts/validate-agent.sh agents/<agent-name>.md
```

Check:

- [ ] Frontmatter parses correctly
- [ ] All required fields present
- [ ] Examples are complete
- [ ] System prompt is comprehensive

### Step 6: Test Triggering

Test with various scenarios:

1. Explicit requests matching examples
2. Implicit needs where agent should activate
3. Scenarios where agent should NOT activate
4. Edge cases and variations

## Best Practices Summary

### DO

- Include 2-4 concrete examples in agent descriptions
- Write specific, unambiguous triggering conditions
- Use "inherit" model setting unless specific need
- Apply principle of least privilege for tools
- Write clear, structured system prompts with explicit steps
- Test agent triggering thoroughly before deployment
- Use different colors for different agents
- Include commentary explaining trigger logic

### DON'T

- Generic descriptions without examples
- Omit triggering conditions
- Use same color for multiple agents in same plugin
- Grant unnecessary tool access
- Write vague system prompts
- Skip testing phases
- Use underscores or uppercase in names
- Forget to handle edge cases

## Integration with Workflows

Agents integrate with plugin workflows:

1. **Phase 5: Component Implementation** uses agent-creator to generate agents
2. **Validation phase** uses validate-agent.sh script
3. **Testing phase** verifies triggering across scenarios

For comprehensive plugin development, use:

- `/plugin-dev:create-plugin` for full plugin workflow
- This command for individual agent creation/refinement

## Create the Agent

Based on user input, create:

1. **Directory structure**: `${CLAUDE_PLUGIN_ROOT}/agents/`
2. **Agent file**: Complete markdown with frontmatter + system prompt
3. **Validation**: Run validation script
4. **Testing suggestions**: Scenarios to verify triggering

After creation, suggest testing with `/customaize-agent:test-prompt` command to verify agent behavior under various scenarios.
