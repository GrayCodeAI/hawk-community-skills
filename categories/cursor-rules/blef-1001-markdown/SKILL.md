---
name: blef-1001-markdown
description: Always use for writing or updating Markdown files to ensure consistent
  formatting and readability across documentation
license: MIT
tags:
- cursor-rules
alwaysApply: false
---

graph TD
    A[Start] --> B{Decision}
    B -->|Yes| C[Process 1]
    B -->|No| D[Process 2]
    C --> E[End]
    D --> E
  ```

</example>

<example type="invalid">

  ```mermaid
  graph TD
  A-->B
  B-->C
  ```

  ❌ No title, unclear labels, no context.

</example>

## Examples

<example>

  ```md
  # Heading  

  > 🚨 **Warning:** Important detail.

  ```

  ✅ Proper headings, callouts, and spacing.

</example>

<example type="invalid">

  ❌ No headings.
  ❌ Inline code block missing triple backticks.

</example>
