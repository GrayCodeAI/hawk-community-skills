---
name: ghcp-references-code-blocks-to-html
description: 'Skill: ghcp-references-code-blocks-to-html'
license: MIT
tags:
- general
---

## Diagrams (Conceptual Parsing)

### Markdown

````md
```mermaid
graph TD
  A --> B
```
````

### Parsed HTML

```html
<pre><code class="language-mermaid">
graph TD
  A --> B
</code></pre>
```

## Closing Notes

* No `language-*` class appears here because **no language identifier** was provided.
* The inner triple backticks are preserved **as literal text** inside `<code>`.
