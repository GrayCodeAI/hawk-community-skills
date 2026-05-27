---
name: neo-do-competitively
description: Execute tasks through competitive multi-agent generation, meta-judge
  evaluation specification, multi-judge evaluation, and evidence-based synthesis
license: MIT
tags:
- general
argument-hint: Task description and optional output path/criteria
---

[Summary of your evaluation]

## Instructions

Follow your full judge process as defined in your agent instructions!

CRITICAL: Base your evaluation on evidence, not impressions. Quote specific text.

## Output

CRITICAL: You must reply with this exact structured evaluation report format in YAML at the START of your response!
```

CRITICAL: NEVER provide score threshold to judges. Judge MUST not know what threshold for score is, in order to not be biased!!!

**Dispatch:**

```
Use Task tool (3 calls in single message):
  - description: "Judge [1|2|3]: {brief task summary}"
  - prompt: {judge prompt with exact meta-judge specification YAML}
  - model: opus
  - subagent_type: "sadd:judge"
```

### Phase 2.5: Adaptive Strategy Selection (Early Return)

**The orchestrator** (not a subagent) analyzes judge outputs to determine the optimal strategy.

#### Decision Logic

**Step 1: Parse structured headers from judge reply**

Parse the judges reply.
CRITICAL: Do not read reports files itself, it can overflow your context.

**Step 2: Check for unanimous winner**

Compare all three VOTE values:

- If Judge 1 VOTE = Judge 2 VOTE = Judge 3 VOTE (same solution):
  - **Strategy: SELECT_AND_POLISH**
  - **Reason:** Clear consensus - all three judges prefer same solution

**Step 3: Check if all solutions are fundamentally flawed**

If no unanimous vote, calculate average scores:

1. Average Solution A scores: (Judge1_A + Judge2_A + Judge3_A) / 3
2. Average Solution B scores: (Judge1_B + Judge2_B + Judge3_B) / 3
3. Average Solution C scores: (Judge1_C + Judge2_C + Judge3_C) / 3

If (avg_A < 3.0) AND (avg_B < 3.0) AND (avg_C < 3.0):

- **Strategy: REDESIGN**
- **Reason:** All solutions below quality threshold, fundamental approach issues

**Step 5: Default to full synthesis**

If none of the above conditions met:

- **Strategy: FULL_SYNTHESIS**
- **Reason:** Split decision with merit, synthesis needed to combine best elements

#### Strategy 1: SELECT_AND_POLISH

**When:** Clear winner (unanimous votes)

**Process:**

1. Select the winning solution as the base
2. Launch subagent to apply specific improvements from judge feedback
3. Cherry-pick 1-2 best elements from runner-up solutions
4. Document what was added and why

**Benefits:**

- Saves synthesis cost (simpler than full synthesis)
- Preserves proven quality of winning solution
- Focused improvements rather than full reconstruction

**Prompt template:**

```markdown
You are polishing the winning solution based on judge feedback.

<task>
{task_description}
</task>

<winning_solution>
{path_to_winning_solution}
Score: {winning_score}/5.0
Judge consensus: {why_it_won}
</winning_solution>

<runner_up_solutions>
{list of paths to all runner-up solutions}
</runner_up_solutions>

<judge_feedback>
{list of paths to all evaluation reports}
</judge_feedback>

<output>
{final_solution_path}
</output>

Instructions:
Let's work through this step by step to polish the winning solution effectively.

1. Take the winning solution as your base (do NOT rewrite it)
2. First, carefully review all judge feedback to understand what needs improvement
3. Apply improvements based on judge feedback:
   - Fix identified weaknesses
   - Add missing elements judges noted
4. Next, examine the runner-up solutions for standout elements
5. Cherry-pick 1-2 specific elements from runners-up if judges praised them
6. Document changes made:
   - What was changed and why
   - What was added from other solutions

CRITICAL: Preserve the winning solution's core approach. Make targeted improvements only.
```

#### Strategy 2: REDESIGN

**When:** All solutions scored <3.0/5.0 (fundamental issues across the board)

**Process:**

1. Launch new agent to analyze the failure modes and lessons learned. Ask the agent to:
   - Think through step by step: what went wrong with each solution?
   - Analyze common failure modes across all solutions
   - Extract lessons learned (what NOT to do)
   - Identify the root causes of why all approaches failed
   - Generate new task decomposition or constraints based on these insights
2. **Return to Phase 1**, provide to new implementation agents the lessons learned and new constraints.

**Prompt template for new implementation:**

```markdown
You are analyzing why all solutions failed to meet quality standards. And implement new solution based on it.

<task>
{task_description}
</task>

<constraints>
{constraints_if_any}
</constraints>

<context>
{relevant_context}
</context>

<failed_solutions>
{list of paths to all candidate solutions}
</failed_solutions>

<evaluation_reports>
{list of paths to all evaluation reports with low scores}
</evaluation_reports>

Instructions:
Let's break this down systematically to understand what went wrong and how to design new solution based on it.

1. First, analyze the task carefully - what is being asked and what are the key requirements?
2. Read through each solution and its evaluation report
3. For each solution, think step by step about:
   - What was the core approach?
   - What specific issues did judges identify?
   - Why did this approach fail to meet the quality threshold?
4. Identify common failure patterns across all solutions:
   - Are there shared misconceptions?
   - Are there missing requirements that all solutions overlooked?
   - Are there fundamental constraints that weren't considered?
5. Extract lessons learned:
   - What approaches should be avoided?
   - What constraints must be addressed?
6. Generate improved guidance for the next iteration:
   - New constraints to add
   - Specific approaches to try - what are the different ways to solve this?
   - Key requirements to emphasize
7. Think through the tradeoffs step by step and choose the approach you believe is best
8. Implement it completely
9. Generate 5 verification questions about critical aspects
10. Answer your own questions:
   - Review solution against each question
   - Identify gaps or weaknesses
11. Revise solution:
   - Fix identified issues
12. Explain what was changed and why

```

#### Strategy 3: FULL_SYNTHESIS (Default)

**When:** No clear winner AND solutions have merit (scores >=3.0)

**Process:** Proceed to Phase 3 (Evidence-Based Synthesis)

### Phase 3: Evidence-Based Synthesis

**Only executed when Strategy 3 (FULL_SYNTHESIS) selected in Phase 2.5**

Launch **1 synthesis agent** (recommended: Opus for quality):

1. Agent receives:
   - **All candidate solutions** (A, B, C)
   - **All evaluation reports** (1, 2, 3)
2. Agent analyzes:
   - Which elements each judge praised (consensus on strengths)
   - Which issues each judge identified (consensus on weaknesses)
   - Where solutions differed in approach
3. Agent produces **final solution** by:
   - **Copying superior sections** when one solution clearly wins
   - **Combining approaches** when hybrid is better
   - **Fixing identified issues** that all judges caught
   - **Documenting decisions** (what was taken from where and why)

**Key principle:** Evidence-based synthesis leverages collective intelligence.

**Prompt template for synthesizer:**

```markdown
You are synthesizing the best solution from competitive implementations and evaluations.

<task>
{task_description}
</task>

<solutions>
{list of paths to all candidate solutions}
</solutions>

<evaluation_reports>
{list of paths to all evaluation reports}
</evaluation_reports>

<output>
{define expected output following such pattern: solution.md based on the task description and context. Result should be a complete solution to the task.}
</output>

Instructions:
Let's think through this synthesis step by step to create the best possible combined solution.

1. First, read all solutions and evaluation reports carefully
2. Map out the consensus:
   - What strengths did multiple judges praise in each solution?
   - What weaknesses did multiple judges criticize in each solution?
3. For each major component or section, think through:
   - Which solution handles this best and why?
   - Could a hybrid approach work better?
4. Create the best possible solution by:
   - Copying text directly when one solution is clearly superior
   - Combining approaches when a hybrid would be better
   - Fixing all identified issues
   - Preserving the best elements from each
5. Explain your synthesis decisions:
   - What you took from each solution
   - Why you made those choices
   - How you addressed identified weaknesses

CRITICAL: Do not create something entirely new. Synthesize the best from what exists.
```

<output>
The command produces different outputs depending on the adaptive strategy selected:

### Outputs (All Strategies)

1. **Candidate solutions:** `{solution-file}.[a|b|c].[ext]` (in specified output location)
2. **Evaluation reports:** `.specs/reports/{solution-name}-{date}.[1|2|3].md`
3. **Resulting solution:** `{output_path}`

### Strategy-Specific Outputs

- SELECT_AND_POLISH: Polished solution based on winning solution
- REDESIGN: Do not stop, return to phase 1 and eventiualy should result in finish at SELECT_AND_POLISH or FULL_SYNTHESIS strategies
- FULL_SYNTHESIS: Synthesized solution combined best from all

### Orcestrator Reply

Once command execution is complete, reply to user with following structure:

```markdown
## Execution Summary

Original Task: {task_description}

Strategy Used: {strategy} ({reason})

### Results

| Phase                   | Agents | Models   | Status      |
|-------------------------|--------|----------|-------------|
| Phase 1: Competitive Generation + Meta-Judge | 4 (3 generators + 1 meta-judge) | opus x 4 | [Complete / Failed] |
| Phase 2: Multi-Judge Evaluation | 3 | opus x 3 | [Complete / Failed] |
| Phase 2.5: Adaptive Strategy Selection | orchestrator | - | {strategy} |
| Phase 3: [Synthesis/Polish/Redesign] | [N] | [model] | [Complete / Failed] |

Files Created

Final Solution:
- {output_path} - Synthesized production-ready command

Candidate Solutions:
- {solution-file}.[a|b|c].[ext] (Score: [X.X]/5.0)

Evaluation Reports:
- .specs/reports/{solution-file}-{date}.[1|2|3].md (Vote: [Solution A/B/C])

Synthesis Decisions

| Element              | Source           | Rationale   |
|----------------------|------------------|-------------|
| [element]            | Solution [B/A/C] | [rationale] |

```

</output>

## Best Practices

### Meta-Judge + Judge Verification

- **Never skip meta-judge** - Tailored evaluation criteria produce better judgments than generic ones
- **Meta-judge runs once** - Same specification for all 3 judges
- **Include CLAUDE_PLUGIN_ROOT** - Both meta-judge and judges need the resolved plugin root path
- **Meta-judge YAML** - Pass only the meta-judge YAML to judges, do not add any additional text or comments to it!

### Common Pitfalls

- **Using for trivial tasks** - Overhead not justified
- **Vague task descriptions** - Leads to incomparable solutions
- **Insufficient context** - Agents can't produce quality work
- **Forcing synthesis when clear winner exists** - Wastes cost and risks degrading quality
- **Synthesizing fundamentally flawed solutions** - Better to redesign than polish garbage
- **Skipping meta-judge** - Hardcoded criteria are less effective than tailored ones
- **Modifying meta-judge YAML before passing to judges** - Judges must receive exact specification

**Do:**

- Well-defined task with clear constraints
- Rich context for informed decisions
- Trust adaptive strategy selection
- Polish clear winners, synthesize split decisions, redesign failures
- Dispatch meta-judge in parallel with generators for speed

## Examples

### Example 1: API Design (Clear Winner - SELECT_AND_POLISH)

```bash
/do-competitively "Design REST API for user management (CRUD + auth)" \
  --output "specs/api/users.md" \
  --criteria "RESTfulness,security,scalability,developer-experience"
```

**Phase 1 outputs (4 parallel agents):**

- Meta-judge: evaluation specification YAML with 5 criteria dimensions, comparative rubrics
- `specs/api/users.a.md` - Resource-based design with nested routes
- `specs/api/users.b.md` - Action-based design with RPC-style endpoints
- `specs/api/users.c.md` - Minimal design, missing auth consideration

**Phase 2 outputs** (assuming date 2025-01-15, 3 judges using meta-judge specification):

- `.specs/reports/users-api-2025-01-15.1.md`:

  ```
  VOTE: Solution A
  SCORES: A=4.5/5.0, B=3.2/5.0, C=2.8/5.0
  ```

  "Most RESTful, good security"

- `.specs/reports/users-api-2025-01-15.2.md`:

  ```
  VOTE: Solution A
  SCORES: A=4.3/5.0, B=3.5/5.0, C=2.6/5.0
  ```

  "Clean resource design, scalable"

- `.specs/reports/users-api-2025-01-15.3.md`:

  ```
  VOTE: Solution A
  SCORES: A=4.6/5.0, B=3.0/5.0, C=2.9/5.0
  ```

  "Best practices, clear structure"

**Phase 2.5 decision (orchestrator parses headers):**

- Unanimous vote: A, A, A
- Average scores: A=4.5, B=3.2, C=2.8
- Strategy: SELECT_AND_POLISH
- Reason: Unanimous winner with >1.0 point gap

**Phase 3 output:**

- `specs/api/users.md` - Solution A polished with:
  - Added rate limiting documentation (from B)
  - Simplified nested routes (judge feedback)
  - Total cost: 8 agents (4 Phase 1 + 3 judges + 1 polish)

### Example 2: Algorithm Selection (Split Decision - FULL_SYNTHESIS)

```bash
/do-competitively "Design caching strategy for high-traffic API" \
  --output "specs/caching.md" \
  --criteria "performance,memory-efficiency,simplicity,reliability"
```

**Phase 1 outputs (4 parallel agents):**

- Meta-judge: evaluation specification YAML with 4 criteria dimensions, comparative rubrics
- `specs/caching.a.md` - Redis with LRU eviction
- `specs/caching.b.md` - Multi-tier cache (memory + Redis)
- `specs/caching.c.md` - CDN + application cache

**Phase 2 outputs** (assuming date 2025-01-15, 3 judges using meta-judge specification):

- `.specs/reports/caching-2025-01-15.1.md`:

  ```
  VOTE: Solution B
  SCORES: A=3.8/5.0, B=4.2/5.0, C=3.9/5.0
  ```

  "Best performance, complex"

- `.specs/reports/caching-2025-01-15.2.md`:

  ```
  VOTE: Solution A
  SCORES: A=4.0/5.0, B=3.9/5.0, C=3.7/5.0
  ```

  "Simple, reliable, proven"

- `.specs/reports/caching-2025-01-15.3.md`:

  ```
  VOTE: Solution C
  SCORES: A=3.6/5.0, B=4.0/5.0, C=4.1/5.0
  ```

  "Global reach, cost-effective"

**Phase 2.5 decision (orchestrator parses headers):**

- Split votes: B, A, C (no consensus)
- Average scores: A=3.8, B=4.0, C=3.9
- Score gap: 4.0 - 3.9 = 0.1 (<1.0 threshold)
- Strategy: FULL_SYNTHESIS
- Reason: Split decision, all solutions >=3.0, no clear winner

**Phase 3 output:**

- `specs/caching.md` - Hybrid approach:
  - Multi-tier architecture (from B)
  - Simple LRU policy (from A)
  - CDN for static content (from C)
  - Total cost: 8 agents (4 Phase 1 + 3 judges + 1 synthesis)

### Example 3: Authentication Design (All Flawed - REDESIGN)

```bash
/do-competitively "Design authentication system with social login" \
  --output "specs/auth.md" \
  --criteria "security,user-experience,maintainability"
```

**Phase 1 outputs (4 parallel agents):**

- Meta-judge: evaluation specification YAML with 3 criteria dimensions, comparative rubrics
- `specs/auth.a.md` - Custom OAuth2 implementation
- `specs/auth.b.md` - Session-based with social providers
- `specs/auth.c.md` - JWT with password-only auth

**Phase 2 outputs** (assuming date 2025-01-15, 3 judges using meta-judge specification):

- `.specs/reports/auth-2025-01-15.1.md`:

  ```
  VOTE: Solution A
  SCORES: A=2.5/5.0, B=2.2/5.0, C=2.3/5.0
  ```

  "Security risks, reinventing wheel"

- `.specs/reports/auth-2025-01-15.2.md`:

  ```
  VOTE: Solution B
  SCORES: A=2.4/5.0, B=2.8/5.0, C=2.1/5.0
  ```

  "Sessions don't scale, missing requirements"

- `.specs/reports/auth-2025-01-15.3.md`:

  ```
  VOTE: Solution C
  SCORES: A=2.6/5.0, B=2.5/5.0, C=2.3/5.0
  ```

  "No social login, security concerns"

**Phase 2.5 decision (orchestrator parses headers):**

- Split votes: A, B, C (no consensus)
- Average scores: A=2.5, B=2.5, C=2.2 (ALL <3.0)
- Strategy: REDESIGN
- Reason: All solutions below 3.0 threshold, fundamental issues

- Do not stop, return to phase 1 and eventiualy should result in finish at SELECT_AND_POLISH or FULL_SYNTHESIS strategies
</output>
