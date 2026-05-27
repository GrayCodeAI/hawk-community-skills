---
name: copilot-github-copilot-starter
description: Set up complete GitHub Copilot configuration for a new project based
  on technology stack
license: MIT
tags:
- general
---

# Planning mode instructions
You are in planning mode. Your task is to generate an implementation plan for a new feature or for refactoring existing code.
Don't make any code edits, just generate a plan.

The plan consists of a Markdown document that describes the implementation plan, including the following sections:

* Overview: A brief description of the feature or refactoring task.
* Requirements: A list of requirements for the feature or refactoring task.
* Implementation Steps: A detailed list of steps to implement the feature or refactoring task.
* Testing: A list of tests that need to be implemented to verify the feature or refactoring task.
```

## Execution Steps

1. **Gather project information** - Ask the user for technology stack, project type, and development style if not provided
2. **Research awesome-copilot patterns**:
   - Use the fetch tool to explore awesome-copilot directories
   - Check instructions: https://github.com/github/awesome-copilot/tree/main/instructions
   - Check agents: https://github.com/github/awesome-copilot/tree/main/agents (especially for matching expert agents)
   - Check skills: https://github.com/github/awesome-copilot/tree/main/skills
   - Document all sources for attribution comments
3. **Create the directory structure**
4. **Generate main copilot-instructions.md** with project-wide standards
5. **Create language-specific instruction files** using awesome-copilot references with attribution
6. **Generate reusable skills** tailored to project needs
7. **Set up specialized agents**, fetching from awesome-copilot where applicable (especially for expert engineer agents matching the tech stack)
8. **Create the GitHub Actions workflow for Coding Agent** (`copilot-setup-steps.yml`) — skip if user does not use GitHub Actions
9. **Validate** all files follow proper formatting and include necessary frontmatter

## Post-Setup Instructions

After creating all files, provide the user with:

1. **VS Code setup instructions** - How to enable and configure the files
2. **Usage examples** - How to use each skill and agent
3. **Customization tips** - How to modify files for their specific needs
4. **Testing recommendations** - How to verify the setup works correctly

## Quality Checklist

Before completing, verify:
- [ ] All authored Copilot markdown files have proper YAML frontmatter where required
- [ ] Language-specific best practices are included
- [ ] Files reference each other appropriately using Markdown links
- [ ] Skills and agents include relevant descriptions; include MCP/tool-related metadata only when the target Copilot environment actually supports or requires it
- [ ] Instructions are comprehensive but not overwhelming
- [ ] Security and performance considerations are addressed
- [ ] Testing guidelines are included
- [ ] Documentation standards are clear
- [ ] Code review standards are defined

## Workflow Template Structure (only if GitHub Actions is used)

The `copilot-setup-steps.yml` workflow MUST follow this exact format and KEEP IT SIMPLE:

```yaml
name: "Copilot Setup Steps"
on:
  workflow_dispatch:
  push:
    paths:
      - .github/workflows/copilot-setup-steps.yml
  pull_request:
    paths:
      - .github/workflows/copilot-setup-steps.yml
jobs:
  # The job MUST be called `copilot-setup-steps` or it will not be picked up by Copilot.
  copilot-setup-steps:
    runs-on: ubuntu-latest
    permissions:
      contents: read
    steps:
      - name: Checkout code
        uses: actions/checkout@v5
      # Add ONLY basic technology-specific setup steps here
```

**KEEP WORKFLOWS SIMPLE** - Only include essential steps:

**Node.js/JavaScript:**
```yaml
- name: Set up Node.js
  uses: actions/setup-node@v4
  with:
    node-version: "20"
    cache: "npm"
- name: Install dependencies
  run: npm ci
- name: Run linter
  run: npm run lint
- name: Run tests
  run: npm test
```

**Python:**
```yaml
- name: Set up Python
  uses: actions/setup-python@v4
  with:
    python-version: "3.11"
- name: Install dependencies
  run: pip install -r requirements.txt
- name: Run linter
  run: flake8 .
- name: Run tests
  run: pytest
```

**Java:**
```yaml
- name: Set up JDK
  uses: actions/setup-java@v4
  with:
    java-version: "17"
    distribution: "temurin"
- name: Build with Maven
  run: mvn compile
- name: Run tests
  run: mvn test
```

**AVOID in workflows:**
- ❌ Complex configuration setups
- ❌ Multiple environment configurations
- ❌ Advanced tooling setup
- ❌ Custom scripts or complex logic
- ❌ Multiple package managers
- ❌ Database setup or external services

**INCLUDE only:**
- ✅ Language/runtime setup
- ✅ Basic dependency installation
- ✅ Simple linting (if standard)
- ✅ Basic test running
- ✅ Standard build commands
