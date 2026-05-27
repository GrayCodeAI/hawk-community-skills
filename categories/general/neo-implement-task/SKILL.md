---
name: neo-implement-task
description: Implement a task with automated LLM-as-Judge verification for critical
  steps
license: MIT
tags:
- general
argument-hint: Task file [options] (e.g., "add-validation.feature.md --continue --human-in-the-loop")
---

## Appendix A: Verification Specifications Reference

This appendix documents how verification is specified in task files. During Phase 2 (Execute Steps), you will reference these specifications to understand how to verify each artifact.

### How Task Files Define Verification

Task files define verification requirements in `#### Verification` sections within each implementation step. These sections specify:

### Required Elements

1. **Level**: Verification complexity
   - `None` - Simple operations (mkdir, delete) - skip verification
   - `Single Judge` - Non-critical artifacts - 1 judge, threshold 4.0/5.0
   - `Panel of 2 Judges` - Critical artifacts - 2 judges, median voting, threshold 4.0/5.0 or 4.5/5.0
   - `Per-Item Judges` - Multiple similar items - 1 judge per item, parallel execution

2. **Artifact(s)**: Path(s) to file(s) being verified
   - Example: `src/decision/decision.service.ts`, `src/decision/tests/decision.service.spec.ts`

3. **Threshold**: Minimum passing score
   - Typically 4.0/5.0 for standard quality
   - Sometimes 4.5/5.0 for critical components

4. **Rubric**: Weighted criteria table (see format below)

5. **Reference Pattern** (Optional): Path to example of good implementation
   - Example: `src/app.service.ts` for NestJS service patterns

### Rubric Format

Rubrics in task files use this markdown table format:

```markdown
| Criterion | Weight | Description |
|-----------|--------|-------------|
| [Name 1]  | 0.XX   | [What to evaluate] |
| [Name 2]  | 0.XX   | [What to evaluate] |
| ...       | ...    | ...         |
```

**Requirements:**

- Weights MUST sum to 1.0
- Each criterion has a clear, measurable description
- Typically 3-6 criteria per rubric

**Example:**

```markdown
| Criterion | Weight | Description |
|-----------|--------|-------------|
| Type Correctness | 0.35 | Types match specification exactly |
| API Contract Alignment | 0.25 | Aligns with documented API contract |
| Export Structure | 0.20 | Barrel exports correctly expose all types |
| Code Quality | 0.20 | Follows project TypeScript conventions |
```

### Scoring Scale

When judges evaluate artifacts, they use this 5-point scale for each criterion:

- **1 (Poor)**: Does not meet requirements
  - Missing essential elements
  - Fundamental misunderstanding of requirements

- **2 (Below Average)**: Multiple issues, partially meets requirements
  - Some correct elements, but significant gaps
  - Would require substantial rework

- **3 (Adequate)**: Meets basic requirements
  - Functional but minimal
  - Room for improvement in quality or completeness

- **4 (Good)**: Meets all requirements, few minor issues
  - Solid implementation
  - Minor polish could improve it

- **5 (Excellent)**: Exceeds requirements
  - Exceptional quality
  - Goes beyond what was asked
  - Could serve as reference implementation

### Using Verification Specs During Execution

**During Phase 2 (Execute Steps):**

1. After a sdd:developer agent completes implementation
2. Read the step's `#### Verification` section in the task file
3. Extract: Level, Artifact paths, Threshold, Rubric, Reference Pattern
4. Launch appropriate judge agent(s) based on Level
5. Provide judges with: Artifact path, Rubric, Threshold, Reference Pattern
6. Aggregate judge results and determine PASS/FAIL
7. If FAIL, launch sdd:developer agent to fix issues and re-verify

**Example Verification Section in Task File:**

```markdown
#### Verification

**Level:** Panel of 2 Judges with Aggregated Voting
**Artifact:** `src/decision/decision.service.ts`, `src/decision/tests/decision.service.spec.ts`

**Rubric:**

| Criterion | Weight | Description |
|-----------|--------|-------------|
| Routing Logic | 0.20 | Correctly routes by customerType |
| Drip Feed Implementation | 0.25 | 2% random approval for rejected New customers only |
| Response Formatting | 0.20 | Correct decision outcome, triggeredRules preserved, ISO 8601 timestamp |
| Testability | 0.15 | Injectable randomGenerator enables deterministic testing |
| Test Coverage | 0.20 | Unit tests cover approval, rejection, drip feed, routing, timestamp |

**Reference Pattern:** NestJS service patterns, ZenEngineService API
```

This specification tells you to:

- Launch 2 judge agents in parallel
- Have them evaluate both service and test files
- Use the 5-criterion rubric with specified weights
- Do not pass threshold to judges, only use it to compare it with the average score of the judges
- Reference existing NestJS patterns for comparison
