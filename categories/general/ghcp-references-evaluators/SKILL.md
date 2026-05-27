---
name: ghcp-references-evaluators
description: 'Skill: ghcp-references-evaluators'
license: MIT
tags:
- general
---

## Custom Evaluators: `create_llm_evaluator`

Factory for custom LLM-as-judge evaluators from prompt templates.

Usage::

    from pixie import create_llm_evaluator

    concise_voice_style = create_llm_evaluator(
        name="ConciseVoiceStyle",
        prompt_template="""
        You are evaluating whether a voice agent response is concise and
        phone-friendly.

        User said: {eval_input}
        Agent responded: {eval_output}
        Expected behavior: {expectation}

        Score 1.0 if the response is concise (under 3 sentences), directly
        addresses the question, and uses conversational language suitable for
        a phone call. Score 0.0 if it's verbose, off-topic, or uses
        written-style formatting.
        """,
    )

### `create_llm_evaluator`

```python
create_llm_evaluator(name: 'str', prompt_template: 'str', *, model: 'str' = 'gpt-4o-mini', client: 'Any | None' = None) -> '_LLMEvaluator'
```

Create a custom LLM-as-judge evaluator from a prompt template.

The template may reference these variables (populated from the
:class:`~pixie.storage.evaluable.Evaluable` fields):

- `{eval_input}` — the evaluable's input data. Single-item lists expand
  to that item's value; multi-item lists expand to a JSON dict of
  `name → value` pairs.
- `{eval_output}` — the evaluable's output data (same rule as
  `eval_input`).
- `{expectation}` — the evaluable's expected output

Args:
name: Display name for the evaluator (shown in scorecard).
prompt_template: A string template with `{eval_input}`,
`{eval_output}`, and/or `{expectation}` placeholders.
model: OpenAI model name (default: `gpt-4o-mini`).
client: Optional pre-configured OpenAI client instance.

Returns:
An evaluator callable satisfying the `Evaluator` protocol.

Raises:
ValueError: If the template uses nested field access like
`{eval_input[key]}` (only top-level placeholders are supported).

### `create_agent_evaluator`

```python
create_agent_evaluator(name: 'str', criteria: 'str') -> '_AgentEvaluator'
```

Create an evaluator whose grading is deferred to a coding agent.

During `pixie test`, agent evaluators are not scored automatically.
Instead, they raise `AgentEvaluationPending` and record a
`PendingEvaluation` with the evaluation criteria. The coding agent
(guided by Step 6) reviews each entry's trace and output, then
grades the pending evaluations.

**When to use**: Quality dimensions that require holistic review of
the LLM trace — tool call correctness, multi-step reasoning quality,
routing decisions — where an automated LLM-as-judge prompt can't
capture the nuance.

**When NOT to use**: Simple text quality checks (use
`create_llm_evaluator` instead), deterministic checks (use heuristic
evaluators), or any criterion that can be scored from input + output
alone without trace context.

Args:
name: Display name for the evaluator (shown in scorecard as ⏳ pending).
criteria: What to evaluate — the grading instructions the agent
will follow when reviewing results. Be specific and actionable.

Returns:
An evaluator callable satisfying the `Evaluator` protocol. Its
`__call__` raises `AgentEvaluationPending` instead of returning an
`Evaluation`.

Example:

```python
from pixie import create_agent_evaluator

ResponseQuality = create_agent_evaluator(
    name="ResponseQuality",
    criteria="The response directly addresses the user's question with "
             "accurate, well-structured information. No hallucinations "
             "or off-topic content.",
)

ToolUsageCorrectness = create_agent_evaluator(
    name="ToolUsageCorrectness",
    criteria="The app called the correct tools in the right order based "
             "on the user's intent. No unnecessary or missed tool calls.",
)
```
