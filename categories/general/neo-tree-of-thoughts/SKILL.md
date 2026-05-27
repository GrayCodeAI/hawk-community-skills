---
name: neo-tree-of-thoughts
description: Execute tasks through systematic exploration, pruning, and expansion
  using Tree of Thoughts methodology with meta-judge evaluation specifications and
  multi-agent evaluation
license: MIT
tags:
- general
argument-hint: Task description and optional output path/criteria
---

[Summary of your evaluation]

## Instructions

Follow your full judge process as defined in your agent instructions!

CRITICAL: You must reply with this exact structured evaluation report format in YAML at the START of your response!
```

**Dispatch:**

```
Use Task tool:
  - description: "Evaluation Judge {1|2|3}: {brief task summary}"
  - prompt: {evaluation judge prompt with exact meta-judge specification YAML}
  - model: opus
  - subagent_type: "sadd:judge"
```

### Phase 4.5: Adaptive Strategy Selection (Early Return)

**The orchestrator** (not a subagent) analyzes judge outputs to determine the optimal strategy.

#### Decision Logic

**Step 1: Parse structured headers from judge reply**

Parse the judges reply.
CRITICAL: Do not read report files themselves, as they can overflow your context.

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

**Step 4: Default to full synthesis**

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

Let's approach this polishing task methodically to improve without disrupting what works.

**Step 1: Understand why this solution won**
Analyze the winning solution:
- What are its core strengths that judges praised?
- What makes its approach superior to alternatives?
- Which parts should remain untouched?

**Step 2: Catalog improvement opportunities**
From judge feedback, identify:
- Specific weaknesses mentioned (list each one)
- Missing elements judges noted
- Areas where runner-ups were praised

**Step 3: Prioritize changes by impact**
For each improvement opportunity:
- High impact: Directly addresses judge criticism
- Medium impact: Adds praised element from runner-up
- Low impact: Nice-to-have refinement

Focus on high-impact changes first.

**Step 4: Apply improvements surgically**
For each change:
- Locate the specific section to modify
- Make the minimal change needed to address the issue
- Verify the change integrates cleanly with surrounding content

**Step 5: Cherry-pick from runners-up**
Review runner-up solutions for:
- 1-2 specific elements that judges praised
- Elements that complement (not conflict with) the winning approach
- Only incorporate if clearly superior to winning solution's version

**Step 6: Document all changes**
Record:
- What was changed and why (with reference to judge feedback)
- What was added from other solutions (cite source)
- What was intentionally left unchanged

CRITICAL: Preserve the winning solution's core approach. Make targeted improvements only.
```

#### Strategy 2: REDESIGN

**When:** All solutions scored <3.0/5.0 (fundamental issues across the board)

**Process:**
1. Launch new agent to analyze the failure modes and lessons learned
2. **Return to Phase 3** (Expansion), provide to new implementation agents the lessons learned and new constraints

**Note:** If redesign fails twice, escalate to user for guidance.

**Prompt template for new implementation:**

```markdown
You are analyzing why all solutions failed to meet quality standards, to inform a redesign. And implement new solution based on it.


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
{list of paths to all solution files}
Average scores: A={avg_a}/5.0, B={avg_b}/5.0, C={avg_c}/5.0
</failed_solutions>

<evaluation_reports>
{list of paths to all evaluation reports}
All solutions scored below 3.0/5.0 threshold.
</evaluation_reports>

<output>
.specs/research/{solution-name}-{date}.redesign-analysis.md
</output>

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

**Process:** Proceed to Phase 5 (Evidence-Based Synthesis)

### Phase 5: Synthesis (Evidence-Based Combination)

**Only executed when Strategy 3 (FULL_SYNTHESIS) selected in Phase 4.5**

Launch **1 synthesis agent** (recommended: Opus for quality):

1. Agent receives:
   - **All solutions** (from specified output location)
   - **All evaluation reports** (from `.specs/reports/`)
   - **Selection rationale** from pruning phase (from `.specs/research/`)
2. Agent analyzes:
   - **Consensus strengths** (what multiple judges praised)
   - **Consensus weaknesses** (what multiple judges criticized)
   - **Complementary elements** where solutions took different approaches
3. Agent produces **final solution** by:
   - **Copying superior sections** when one solution clearly wins
   - **Combining approaches** when hybrid is better
   - **Fixing identified issues** that judges caught
   - **Documenting decisions** (what was taken from where and why)

**Key principle:** Evidence-based synthesis leverages collective intelligence from exploration and evaluation.

**Prompt template for synthesizer:**

```markdown
You are synthesizing the best solution from explored, pruned, and evaluated implementations.

<task>
{task_description}
</task>

<solutions>
{list of paths to all solution files}
</solutions>

<evaluation_reports>
{list of paths to all evaluation reports}
</evaluation_reports>

<selection_rationale>
{path to selection.md explaining why these proposals were chosen}
</selection_rationale>

<output>
{output_path} - The final synthesized solution
</output>

Instructions:

Let's approach this synthesis systematically by first analyzing, then decomposing, then building.

**Step 1: Build the evidence base**
Before synthesizing, gather evidence from judge reports:
- What did multiple judges praise? (consensus strengths)
- What did multiple judges criticize? (consensus weaknesses)
- Where did judges disagree? (areas needing careful analysis)

**Step 2: Decompose into synthesis subproblems**
Break the solution into logical sections or components. For each component:
- Which solution handles this best? (cite evidence)
- Are there complementary elements from multiple solutions?
- What issues were identified that need fixing?

**Step 3: Solve each subproblem**
For each component/section, determine the synthesis strategy:

*Strategy A - Clear winner:* If one solution is clearly superior for this component:
- Copy that section directly
- Document: "Taken from Solution X because [judge evidence]"

*Strategy B - Complementary combination:* If solutions have complementary strengths:
- Identify what each contributes
- Combine carefully, ensuring consistency
- Document: "Combined X from Solution A with Y from Solution B because [rationale]"

*Strategy C - All flawed:* If all solutions have issues in this area:
- Start with the best version
- Apply fixes based on judge criticism
- Document: "Based on Solution X, modified to address [specific issues]"

**Step 4: Integrate and verify consistency**
After synthesizing all components:
- Check that combined elements work together
- Resolve any contradictions between borrowed sections
- Ensure consistent terminology and style

**Step 5: Document synthesis decisions**
Create a synthesis log:
- What you took from each solution (with specific citations)
- Why you made those choices (reference judge feedback)
- How you addressed identified weaknesses
- Any novel combinations or improvements

<example>
**Example synthesis decision for an API design:**

Component: Authentication flow
- Solution A: JWT with refresh tokens (praised for security by 2/3 judges)
- Solution B: Session-based (praised for simplicity by 1 judge, criticized for scalability)
- Solution C: OAuth2 only (criticized as over-engineered for use case)

Decision: Take Solution A's authentication flow directly.
Evidence: Judges 1 and 3 both noted "JWT approach provides good balance of security and statelessness"
Modification: None needed - this section was rated highest across judges.
</example>

**Step 6: Revise your solution**
- Generate 5 verification questions about critical aspects
- Answer your own questions:
   - Review solution against each question
   - Identify gaps or weaknesses
- Revise solution:
   - Fix identified issues
- Explain what was changed and why


CRITICAL:
- Do not create something entirely new - synthesize the best from what exists
- Cite your sources (which solution, which section)
- Explain every major decision
- Address all consensus weaknesses identified by judges
```

<output>
The command produces different outputs depending on the adaptive strategy selected:

### Outputs (All Strategies)

1. **Research directory:** `.specs/research/` (created if not exists)
   - Proposals: `.specs/research/{solution-name}-{date}.proposals.[a|b|c].md` - High-level approaches with probabilities
   - Pruning: `.specs/research/{solution-name}-{date}.pruning.[1|2|3].md` - Judge evaluations and votes
   - Selection: `.specs/research/{solution-name}-{date}.selection.md` - Vote tallies and selected proposals

2. **Expansion outputs:**
   - `solution.a.md`, `solution.b.md`, `solution.c.md` - Full implementations (in specified output location)

3. **Reports directory:** `.specs/reports/` (created if not exists)
   - Evaluation: `.specs/reports/{solution-name}-{date}.[1|2|3].md` - Final judge reports

4. **Resulting solution:** `{output_path}`

### Strategy-Specific Outputs

- **SELECT_AND_POLISH**: Polished solution based on winning solution, with targeted improvements
- **REDESIGN**: Do not stop; return to Phase 3 with lessons learned; eventually finishes at SELECT_AND_POLISH or FULL_SYNTHESIS
- **FULL_SYNTHESIS**: Synthesized solution combining best elements from all solutions
</output>

## Best Practices

### Meta-Judge + Judge Verification

- **Two meta-judges** - Separate specs for pruning (proposals) and evaluation (full solutions)
- **Meta-judges run in parallel with implementation** - Don't block the pipeline; pruning meta-judge runs with Phase 1, evaluation meta-judge runs with Phase 3
- **Include CLAUDE_PLUGIN_ROOT** - Both meta-judges and judges need the resolved plugin root path
- **Meta-judge YAML** - Pass only the YAML to judges, do not modify it

### Common Pitfalls

- **Insufficient exploration** - Agents propose similar approaches
- **Ignoring judge feedback** - Expansion ignores concerns from pruning
- **Vague proposals** - Can't properly evaluate without implementation details
- **Over-exploration** - Too many proposals, evaluation becomes expensive
- **Forcing synthesis when clear winner exists** - Wastes cost and risks degrading quality
- **Synthesizing fundamentally flawed solutions** - Better to redesign than polish garbage

### Recommendations

- **Encourage diverse exploration** - Prompt for different regions of solution space
- **Feed feedback forward** - Expansion agents address pruning concerns
- **Right level of detail** - Proposals have enough detail to evaluate
- **Prune aggressively** - Only expand most promising 3 approaches
- **Trust adaptive strategy selection** - Polish clear winners, synthesize split decisions, redesign failures

## Example: API Design

```bash
/tree-of-thoughts "Design REST API for user management (CRUD + auth)" \
  --output "specs/api/users.md" \
  --criteria "RESTfulness,security,scalability,developer-experience"
```

**Phase 1 outputs** (assuming date 2025-01-15):
- `.specs/research/users-api-2025-01-15.proposals.a.md` - 6 approaches from Agent A
- `.specs/research/users-api-2025-01-15.proposals.b.md` - 6 approaches from Agent B
- `.specs/research/users-api-2025-01-15.proposals.c.md` - 6 approaches from Agent C

**Phase 1.5 output** (runs in parallel with Phase 1):
- Pruning Meta-judge (Opus, `sadd:meta-judge`) generates pruning evaluation specification YAML

**Phase 2 outputs** (3 judges with pruning meta-judge spec):
- `.specs/research/users-api-2025-01-15.pruning.1.md` - Top 3: Resource-based REST, Pure REST, Monolithic
- `.specs/research/users-api-2025-01-15.pruning.2.md` - Top 3: Pure REST, Hybrid (services), Resource-based REST
- `.specs/research/users-api-2025-01-15.pruning.3.md` - Top 3: Resource-based REST, REST+GraphQL hybrid, Pure REST
- `.specs/research/users-api-2025-01-15.selection.md` - Selected: Resource-based REST (8 pts), Pure REST (7 pts), Monolithic (4 pts)

**Phase 3 outputs:**
- `specs/api/users.a.md` - Full resource-based design with nested routes
- `specs/api/users.b.md` - Flat REST design with simple endpoints
- `specs/api/users.c.md` - Monolithic API with service-oriented internals

**Phase 3.5 output** (runs in parallel with Phase 3):
- Evaluation Meta-judge (Opus, `sadd:meta-judge`) generates evaluation specification YAML

**Phase 4 outputs** (3 judges with evaluation meta-judge spec):
- `.specs/reports/users-api-2025-01-15.1.md`:
  ```
  VOTE: Solution A
  SCORES: A=4.2/5.0, B=3.8/5.0, C=3.4/5.0
  ```
  "Prefers A for RESTfulness, criticizes C complexity"

- `.specs/reports/users-api-2025-01-15.2.md`:
  ```
  VOTE: Solution B
  SCORES: A=3.9/5.0, B=4.1/5.0, C=3.5/5.0
  ```
  "Prefers B for simplicity, criticizes A deep nesting"

- `.specs/reports/users-api-2025-01-15.3.md`:
  ```
  VOTE: Solution A
  SCORES: A=4.3/5.0, B=3.6/5.0, C=3.2/5.0
  ```
  "Prefers A for discoverability, criticizes B lack of structure"

**Phase 4.5 decision (orchestrator parses headers):**
- Split votes: A, B, A (no unanimous winner)
- Average scores: A=4.1, B=3.8, C=3.4 (all >=3.0)
- Strategy: FULL_SYNTHESIS
- Reason: Split decision with merit, synthesis needed

**Phase 5 output (synthesis):**
- `specs/api/users.md` - Resource-based structure (from A), max 2-level nesting (from B), internal services (from C)

</output>
