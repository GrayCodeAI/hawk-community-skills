---
name: mdc-openai
description: This guide provides definitive, actionable best practices for developing
  with the OpenAI API, covering prompt engineering, robust client usage, agent design,
  and testing.
license: MIT
tags:
- ai-ml
---

Text 3: {user_text}
Keywords 3:"""

response = client.chat.completions.create(
    model="gpt-4o",
    messages=[{"role": "user", "content": few_shot_prompt}]
)
```

#### 2.1.6 Role/Persona and Constraints

Define the AI's role and explicitly state what it should *not* do.

❌ **BAD**: Only negative constraints
```python
system_message = "DO NOT MENTION PRICES. DO NOT BE OVERLY FORMAL."
```

✅ **GOOD**: Clear role, positive instructions, and specific constraints
```python
system_message = """You are a friendly, helpful customer support agent for a SaaS product.
Your goal is to diagnose user issues and suggest solutions.
NEVER ask for Personally Identifiable Information (PII) like passwords or credit card numbers.
Instead, refer users to our secure help portal at `https://support.example.com/security`.
"""
```

### 2.2 Agent Design

For building autonomous agents, follow OpenAI's "Practical Guide to Building Agents" framework.

#### 2.2.1 Core Components

Agents require:
1.  **Model**: The LLM for reasoning and decision-making.
2.  **Tools**: External functions/APIs the agent can use.
3.  **Instructions**: Explicit guidelines and guardrails.

#### 2.2.2 Function Calling

Use function calling for agents to reliably interact with external tools and APIs. Define tools with clear schemas.

```python
from openai import OpenAI
import json

client = OpenAI()

def get_current_weather(location: str, unit: str = "fahrenheit") -> str:
    """Get the current weather in a given location"""
    # In a real app, this would call an external weather API
    if "san francisco" in location.lower():
        return json.dumps({"location": location, "temperature": "72", "unit": unit})
    return json.dumps({"location": location, "temperature": "unknown"})

tools = [
    {
        "type": "function",
        "function": {
            "name": "get_current_weather",
            "description": "Get the current weather in a given location",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "description": "The city and state, e.g. San Francisco, CA",
                    },
                    "unit": {"type": "string", "enum": ["celsius", "fahrenheit"]},
                },
                "required": ["location"],
            },
        },
    }
]

def run_agent_with_tool(user_message: str):
    messages = [{"role": "user", "content": user_message}]
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=messages,
        tools=tools,
        tool_choice="auto", # Let the model decide if it needs to call a tool
    )
    response_message = response.choices[0].message

    if response_message.tool_calls:
        tool_call = response_message.tool_calls[0]
        function_name = tool_call.function.name
        function_args = json.loads(tool_call.function.arguments)
        
        if function_name == "get_current_weather":
            function_response = get_current_weather(**function_args)
            messages.append(response_message) # Extend conversation with assistant's reply
            messages.append(
                {
                    "tool_call_id": tool_call.id,
                    "role": "tool",
                    "name": function_name,
                    "content": function_response,
                }
            )
            second_response = client.chat.completions.create(
                model="gpt-4o",
                messages=messages,
            )
            return second_response.choices[0].message.content
    return response_message.content

# Example usage:
# print(run_agent_with_tool("What's the weather like in San Francisco?"))
```

#### 2.2.3 Guardrails and Workflow Orchestration

Implement explicit guardrails (e.g., input validation, content moderation, safety checks) and design clear workflows. For complex tasks, split into smaller, orchestratable agents (Manager Pattern).

### 2.3 Code Generation (Codex)

When using models for code generation, provide ample context and verification steps.

#### 2.3.1 Clear Code Pointers

Include specific file paths, greppable identifiers, or full stack traces to narrow the model's focus.

#### 2.3.2 Verification Steps

Ask the model to include steps to reproduce an issue, validate a feature, or run tests/linters. This improves output quality.

```python
code_gen_prompt = """
Refactor the `calculate_total` function in `src/utils.py` to use `Decimal` for currency calculations to avoid floating-point inaccuracies.
Ensure all existing unit tests in `tests/test_utils.py` still pass after your changes.
Provide the updated `src/utils.py` file and the command to run the tests.
"""
```

## 3. Performance Considerations

### 3.1 Model Choice

Balance model capability with cost and latency. Start with `gpt-4o` for prototyping, then consider `gpt-3.5-turbo` for simpler tasks where cost/speed is critical.

### 3.2 Token Usage

Be concise. Avoid sending unnecessary context or overly verbose prompts. Every token costs money and adds latency.

### 3.3 Streaming Responses

For user-facing applications, use streaming responses to improve perceived latency.

```python
def stream_response(prompt: str):
    stream = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}],
        stream=True,
    )
    for chunk in stream:
        if chunk.choices[0].delta.content is not None:
            print(chunk.choices[0].delta.content, end="")
    print() # Newline at the end
```

## 4. Common Pitfalls and Gotchas

*   **Hardcoding API Keys**: Security vulnerability. Use environment variables.
*   **Vague Prompts**: Leads to inconsistent, irrelevant, or hallucinated outputs. Be specific.
*   **Ignoring System Message**: The system message is your primary control for persona and behavior. Use it.
*   **Parsing Freeform Text**: Unreliable. Always use `response_format={"type": "json_object"}` for structured data.
*   **Over-reliance on Single-Turn Prompts**: For complex, multi-step tasks, design agents with tool use and iterative reasoning.

## 5. Error Handling

Implement robust error handling, especially for API calls.

### 5.1 API Exceptions

Catch specific OpenAI API exceptions and implement retry logic.

```python
from openai import OpenAI, APIError, RateLimitError, AuthenticationError
import time

def safe_api_call(prompt: str, retries: int = 3) -> str | None:
    for i in range(retries):
        try:
            response = client.chat.completions.create(
                model="gpt-4o",
                messages=[{"role": "user", "content": prompt}]
            )
            return response.choices[0].message.content
        except RateLimitError:
            delay = 2 ** i  # Exponential backoff
            print(f"Rate limit hit. Retrying in {delay} seconds...")
            time.sleep(delay)
        except AuthenticationError:
            print("Authentication failed. Check your API key.")
            return None
        except APIError as e:
            print(f"OpenAI API error: {e}")
            return None
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return None
    print("Max retries exceeded.")
    return None
```

## 6. Request/Response Patterns

### 6.1 Chat Completions API

This is the primary endpoint for most LLM interactions. Always use the `messages` array for conversational context.

### 6.2 Structured Output (JSON Mode)

For any task requiring data extraction or structured responses, enforce JSON output.

```python
response = client.chat.completions.create(
    model="gpt-4o",
    response_format={"type": "json_object"},
    messages=[
        {"role": "system", "content": "You are a JSON-generating assistant."},
        {"role": "user", "content": "Generate a JSON object with 'name' and 'age' for a person named 'Alice' who is 30."}
    ]
)
data = json.loads(response.choices[0].message.content)
# data will be {'name': 'Alice', 'age': 30}
```

## 7. Rate Limiting

The `openai` Python client includes built-in retry logic for rate limits. However, for high-throughput applications, implement custom exponential backoff and jitter, or use a dedicated rate-limiting library.

## 8. Testing Approaches

Treat prompts and LLM interactions as critical code.

### 8.1 Prompts as Code

Version control your prompts alongside your application code.

### 8.2 Unit-Style Tests (Evals)

Write tests for your prompt outputs. Define expected outcomes and evaluate model responses against them.

```python
# test_summarizer.py
import pytest
from your_app import get_response_good # Assuming get_response_good uses your structured prompt

@pytest.mark.parametrize("input_text, expected_keywords", [
    ("The quick brown fox jumps over the lazy dog.", ["fox", "dog", "jumps"]),
    ("OpenAI released GPT-4o, a new multimodal model.", ["OpenAI", "GPT-4o", "multimodal model"]),
])
def test_keyword_extraction(input_text, expected_keywords):
    # This assumes get_response_good is adapted for keyword extraction with JSON output
    prompt = f"""Extract 3-5 keywords from the following text as a JSON array.
    Text: \"\"\"{input_text}\"\"\"
    Example: ["keyword1", "keyword2"]
    """
    response_json_str = get_response_good(prompt)
    actual_keywords = json.loads(response_json_str)
    
    assert isinstance(actual_keywords, list)
    assert len(actual_keywords) >= 3 # Check length
    for keyword in expected_keywords:
        assert any(keyword.lower() in actual.lower() for actual in actual_keywords) # Check for presence
```

### 8.3 Iterative Refinement

Continuously test, analyze outputs, and refine your prompts and model parameters. Use OpenAI's Evals framework or similar tools for systematic evaluation.
