---
name: neo-do-in-parallel
description: Launch multiple sub-agents in parallel to execute tasks across files
  or targets with intelligent model selection, quality-focused prompting, and meta-judge
  → LLM-as-a-judge verification
license: MIT
tags:
- general
argument-hint: Task description [--files "file1.ts,file2.ts,..."] [--targets "target1,target2,..."]
  [--model opus|sonnet|haiku] [--output <path>]
---

### Example 3: Requirement Grouping -- All Independent

**Input:**

```
/do-in-parallel write tests for loan.service.ts, add password recovery feature to auth module and enable caching during dependency loading in github actions.
```

**Orchestrator Analysis:**

```
Phase 2: Task Analysis + Requirement Grouping

1. Task Identification:
   - Task A: "Write tests for src/services/loan.service.ts"
   - Task B: "Add password recovery feature to src/modules/auth/"
   - Task C: "Enable caching during dependency loading in .github/workflows/ci.yml"

2. Requirement Grouping:
   - Task A: INDEPENDENT — test generation for a specific service
   - Task B: INDEPENDENT — new feature in auth module (unrelated to tasks A and C)
   - Task C: INDEPENDENT — CI configuration change (unrelated to tasks A and B)
   - No grouping possible: all 3 tasks are different task types on different targets

3. Agent Count:
   - Meta-judges: 3 (one per task — standard flow)
   - Implementation agents: 3 (one per task)
   - Judges: 3 (one per task)
   - Total: 9 agents (no reduction possible)
```

**Phase 3.5: Meta-Judge Dispatch (3 meta-judges in parallel):**

```
[Meta-judge 1: Independent — loan service tests]
Use Task tool:
  - description: "Meta-judge: write tests for loan.service.ts"
  - prompt:
    ## Task

    Generate an evaluation specification yaml for the following task applied
    to a specific target. You will produce rubrics, checklists, and scoring
    criteria that a judge agent will use to evaluate the implementation
    artifact for this specific target.

    CLAUDE_PLUGIN_ROOT={CLAUDE_PLUGIN_ROOT}

    ## User Prompt as Context
    write tests for loan.service.ts, add password recovery feature to auth
    module and enable caching during dependency loading in github actions.

    ## Target
    Write comprehensive unit tests for src/services/loan.service.ts

    ## Context
    Project uses Jest. Tests should cover all public methods, edge cases,
    and error scenarios for the loan service.

    ## Artifact Type
    code

    ## Instructions
    User prompt is provided as context, you should use it only as reference
    of changes that can occur in the project by other agents. Generate
    evaluation specification ONLY for the loan service test generation.
    Your report will be used to verify only this particular task, not the
    all tasks in the user prompt.
    Return only the final evaluation specification YAML in your response.
  - model: opus
  - subagent_type: "sadd:meta-judge"

[Meta-judge 2: Independent — password recovery feature]
Use Task tool:
  - description: "Meta-judge: add password recovery to auth module"
  - prompt:
    ## Task

    Generate an evaluation specification yaml for the following task applied
    to a specific target. You will produce rubrics, checklists, and scoring
    criteria that a judge agent will use to evaluate the implementation
    artifact for this specific target.

    CLAUDE_PLUGIN_ROOT={CLAUDE_PLUGIN_ROOT}

    ## User Prompt as Context
    write tests for loan.service.ts, add password recovery feature to auth
    module and enable caching during dependency loading in github actions.

    ## Target
    Add password recovery feature to src/modules/auth/ (password reset flow:
    request, token generation, validation, password update)

    ## Context
    Auth module handles authentication. Password recovery requires new
    endpoints, email integration, token management.

    ## Artifact Type
    code

    ## Instructions
    User prompt is provided as context, you should use it only as reference
    of changes that can occur in the project by other agents. Generate
    evaluation specification ONLY for the password recovery feature.
    Your report will be used to verify only this particular task, not the
    all tasks in the user prompt.
    Return only the final evaluation specification YAML in your response.
  - model: opus
  - subagent_type: "sadd:meta-judge"

[Meta-judge 3: Independent — GH Actions caching]
Use Task tool:
  - description: "Meta-judge: enable dependency caching in GitHub Actions"
  - prompt:
    ## Task

    Generate an evaluation specification yaml for the following task applied
    to a specific target. You will produce rubrics, checklists, and scoring
    criteria that a judge agent will use to evaluate the implementation
    artifact for this specific target.

    CLAUDE_PLUGIN_ROOT={CLAUDE_PLUGIN_ROOT}

    ## User Prompt as Context
    write tests for loan.service.ts, add password recovery feature to auth
    module and enable caching during dependency loading in github actions.

    ## Target
    Enable caching during dependency loading in .github/workflows/ci.yml
    (e.g., npm/yarn cache, actions/cache)

    ## Context
    GitHub Actions CI pipeline. Dependency installation step should use
    caching to speed up builds.

    ## Artifact Type
    configuration

    ## Instructions
    User prompt is provided as context, you should use it only as reference
    of changes that can occur in the project by other agents. Generate
    evaluation specification ONLY for enabling dependency caching in GH Actions.
    Your report will be used to verify only this particular task, not the
    all tasks in the user prompt.
    Return only the final evaluation specification YAML in your response.
  - model: opus
  - subagent_type: "sadd:meta-judge"

[All 3 meta-judges launched simultaneously]
```

**Phase 5: Implementation Dispatch (3 agents in parallel, after meta-judges complete):**

```
[Implementation 1: loan service tests]
Use Task tool:
  - description: "Parallel: write tests for loan.service.ts"
  - prompt:
    ## Reasoning Approach
    Let's think step by step.
    Before taking any action, think through the problem systematically:
    1. "Let me first understand what is being asked for this specific target..."
    2. "Let me analyze this specific target..."
    3. "Let me plan my approach..."
    Work through each step explicitly before implementing.

    <task>Write comprehensive unit tests for the loan service</task>
    <target>src/services/loan.service.ts</target>
    <constraints>
    - Work ONLY on the specified target
    - Create test file co-located with the service
    - Cover all public methods, edge cases, and error scenarios
    - Follow existing test patterns in the project
    </constraints>
    <output>
    Create test file for the loan service.
    CRITICAL: At the end of your work, provide a "Summary" section containing:
    - Files modified (full paths)
    - Key changes (3-5 bullet points)
    - Any decisions made and rationale
    </output>

    ## Self-Critique Verification (MANDATORY)
    Before submitting, verify your work:
    1. Re-read the original task and confirm every requirement is addressed
    2. Check that all tests follow existing patterns in the project
    3. Verify no unrelated files were modified
    4. Confirm the Summary section is complete and accurate
  - model: sonnet

[Implementation 2: password recovery]
Use Task tool:
  - description: "Parallel: add password recovery feature to auth module"
  - prompt:
    ## Reasoning Approach
    [standard CoT prefix]

    <task>Add password recovery feature to the auth module</task>
    <target>src/modules/auth/</target>
    <constraints>
    - Work ONLY on the auth module
    - Implement password reset request, token generation, validation,
      and password update
    - Follow existing auth module patterns
    - Do NOT modify unrelated modules
    </constraints>
    <output>
    Implement password recovery feature.
    CRITICAL: At the end of your work, provide a "Summary" section.
    </output>

    ## Self-Critique Verification (MANDATORY)
    [standard self-critique suffix]
  - model: opus

[Implementation 3: GH Actions caching]
Use Task tool:
  - description: "Parallel: enable dependency caching in GitHub Actions"
  - prompt:
    ## Reasoning Approach
    [standard CoT prefix]

    <task>Enable caching during dependency loading in CI pipeline</task>
    <target>.github/workflows/ci.yml</target>
    <constraints>
    - Work ONLY on the CI workflow file
    - Add dependency caching (npm/yarn cache or actions/cache)
    - Do NOT modify other workflow steps beyond what is necessary
    </constraints>
    <output>
    Update CI workflow with dependency caching.
    CRITICAL: At the end of your work, provide a "Summary" section.
    </output>

    ## Self-Critique Verification (MANDATORY)
    [standard self-critique suffix]
  - model: sonnet

[All 3 launched simultaneously]
```

**Phase 5.2: Judge Dispatch (3 judges in parallel, after ALL implementors complete):**

```
[Judge 1: loan service tests — independent spec]
Use Task tool:
  - description: "Judge: loan.service.ts tests"
  - prompt:
    You are evaluating an implementation artifact for target
    src/services/loan.service.ts against an evaluation specification
    produced by the meta judge.

    CLAUDE_PLUGIN_ROOT={CLAUDE_PLUGIN_ROOT}

    ## User Prompt
    write tests for loan.service.ts, add password recovery feature to auth
    module and enable caching during dependency loading in github actions.

    ## Target
    src/services/loan.service.ts

    ## Evaluation Specification
    ```yaml
    {EXACT spec YAML from loan service meta-judge}
    ```

    ## Implementation Output
    {Summary from loan service test implementation agent}

    ## Instructions
    User prompt is provided as context, you should use it only as reference
    of changes that can occur in the project by other agents. Evaluate ONLY
    the test generation for loan.service.ts.
    Follow your full judge process as defined in your agent instructions!

    ## Output
    CRITICAL: You must reply with this exact structured evaluation report
    format in YAML at the START of your response!
  - model: opus
  - subagent_type: "sadd:judge"

[Judge 2: password recovery — independent spec]
Use Task tool:
  - description: "Judge: auth password recovery"
  - prompt:
    You are evaluating an implementation artifact for target
    src/modules/auth/ against an evaluation specification produced
    by the meta judge.

    CLAUDE_PLUGIN_ROOT={CLAUDE_PLUGIN_ROOT}

    ## User Prompt
    [original user prompt]

    ## Target
    src/modules/auth/ (password recovery feature)

    ## Evaluation Specification
    ```yaml
    {EXACT spec YAML from password recovery meta-judge}
    ```

    ## Implementation Output
    {Summary from password recovery implementation agent}

    ## Instructions
    User prompt is provided as context, you should use it only as reference
    of changes that can occur in the project by other agents. Evaluate ONLY
    the password recovery feature.
    Follow your full judge process as defined in your agent instructions!

    ## Output
    CRITICAL: You must reply with this exact structured evaluation report
    format in YAML at the START of your response!
  - model: opus
  - subagent_type: "sadd:judge"

[Judge 3: GH Actions caching — independent spec]
Use Task tool:
  - description: "Judge: GitHub Actions dependency caching"
  - prompt:
    You are evaluating an implementation artifact for target
    .github/workflows/ci.yml against an evaluation specification produced
    by the meta judge.

    CLAUDE_PLUGIN_ROOT={CLAUDE_PLUGIN_ROOT}

    ## User Prompt
    [original user prompt]

    ## Target
    .github/workflows/ci.yml (dependency caching)

    ## Evaluation Specification
    ```yaml
    {EXACT spec YAML from GH Actions caching meta-judge}
    ```

    ## Implementation Output
    {Summary from GH Actions caching implementation agent}

    ## Instructions
    User prompt is provided as context, you should use it only as reference
    of changes that can occur in the project by other agents. Evaluate ONLY
    the dependency caching in GitHub Actions.
    Follow your full judge process as defined in your agent instructions!

    ## Output
    CRITICAL: You must reply with this exact structured evaluation report
    format in YAML at the START of your response!
  - model: opus
  - subagent_type: "sadd:judge"

[All 3 judges launched simultaneously]
```

**Result:**

| Target | Grouping | Model | Judge Score | Retries | Status |
|--------|----------|-------|-------------|---------|--------|
| src/services/loan.service.ts | Independent | sonnet | 4.1/5.0 | 0 | SUCCESS |
| src/modules/auth/ | Independent | opus | 4.3/5.0 | 0 | SUCCESS |
| .github/workflows/ci.yml | Independent | sonnet | 4.0/5.0 | 0 | SUCCESS |

**Overall:** 3/3 completed. Total Agents: 9 (3 meta-judges + 3 implementations + 3 judges). No grouping reduction possible for fully independent tasks.

## Best Practices

### Target Selection

- **Be specific:** List exact files when possible
- **Use globs carefully:** Review expanded list before confirming
- **Limit scope:** 10-15 targets max per batch for manageability
- **Group by similarity:** Similar targets benefit from consistent patterns

### Model Selection Guidelines

| Scenario | Model | Reason |
|----------|-------|--------|
| Security analysis | Opus | Critical reasoning required |
| Architecture decisions | Opus | Quality over speed |
| Simple refactoring | Haiku | Fast, sufficient |
| Documentation generation | Haiku | Mechanical task |
| Code review per file | Sonnet | Balanced capability |
| Test generation | Sonnet | Extensive but patterned |

### Meta-Judge + Judge Verification

- **Requirement grouping first** - Before dispatching any meta-judges, analyze tasks for repeatable, shared, or independent grouping to minimize total agents
- **One meta-judge per group or independent task** - Repeatable groups share one reusable spec, shared groups share one combined spec, independent tasks get their own spec
- **Batch meta-judges first** - Launch all meta-judges in parallel (regardless of grouping type), then launch implementors
- **Reuse spec on retries** - Each group/target's evaluation specification stays constant across retries; only the implementation changes
- **Parse only headers from judge** - Don't read full reports to avoid context pollution
- **Include CLAUDE_PLUGIN_ROOT** - Both meta-judge and judge need the resolved plugin root path
- **Target-specific YAML** - Pass only the relevant meta-judge YAML to its judge, do not add any additional text or comments to it!
- **Shared group retries** - Only re-launch the specific failing implementation agent(s), not the entire group

### Judge Selection

| Implementation Model | Judge Model | Rationale |
|---------------------|-------------|-----------|
| Opus | Opus | Critical work needs strong verification |
| Sonnet | Opus | Tailored evaluation requires strong reasoning |
| Haiku | Opus | Verify simple work with strong evaluation |

**Guideline:** Judges always use Opus for consistent, high-quality evaluation across all targets.

### Context Isolation

- **Minimal context:** Each sub-agent gets only what it needs
- **No cross-references:** Don't tell Agent A about Agent B's target
- **Let them discover:** Sub-agents read files to understand patterns
- **File system as truth:** Changes are coordinated through the filesystem
- **Track pre-existing changes** - Pass context about prior modifications to each agent's judge to prevent attribution confusion between pre-existing and current changes

### Quality Assurance

- **Three-layer verification:** Self-critique (internal) + Target-specific meta-judge specification (structured) + Judge (external)
- **Self-critique first:** Implementation agents verify own work before submission
- **Target-specific meta-judge specification:** Each target gets tailored rubrics that account for its unique characteristics, producing more precise evaluation criteria
- **External judge second:** Independent judge applies target-specific meta-judge specification mechanically — catches blind spots self-critique misses
- **Iteration loop:** Retry with feedback until passing or max retries
- **Isolated failures:** One target failing doesn't affect others
- **Review the summary:** Check for failed or partial completions
- **Run tests after:** Parallel changes may have subtle interactions
- **Commit atomically:** All changes from one batch = one commit

#### Error Handling

| Failure Type | Description | Recovery Action |
|--------------|-------------|-----------------|
| **Recoverable** | Judge found issues, retry available | Retry with judge feedback (max 3 per target) |
| **Approach Failure** | The approach for this target is wrong | Escalate to user with options |
| **Foundation Issue** | Requirements unclear or impossible | Escalate to user for clarification |
| **Max Retries Exceeded** | Target failed after 3 retries | Mark failed, continue other targets, report at end |

**Critical Rules:**
- NEVER continue past max retries without user input
- NEVER try to "fix forward" without addressing judge issues
- NEVER skip judge verification
- STOP and report if context is missing (don't guess)
- ISOLATE failures - one target failing doesn't stop others
