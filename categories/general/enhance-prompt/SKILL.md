---
name: enhance-prompt
description: Transforms vague UI ideas into polished, Stitch-optimized prompts. Enhances
  specificity, adds UI/UX keywords, injects design system context, and structures
  output for better generation results.
license: MIT
tags:
- general
allowed-tools: None
---

💡 **Tip:** For consistent designs across multiple screens, create a DESIGN.md 
file using the `design-md` skill.
```

### Example 2: Feature Request → Targeted Edit

**User input:**
> "add a search bar"

**Enhanced output:**
```markdown
Add a search bar to the header navigation.

**Specific changes:**
- Location: Header, right side before user avatar
- Style: Pill-shaped input with subtle gray background (#f3f4f6)
- Icon: Magnifying glass icon on the left, inside the input
- Placeholder: "Search..." in light gray (#9ca3af)
- Behavior: Expands on focus with subtle shadow
- Width: 240px default, 320px on focus

**Context:** This is a targeted edit. Make only this change while preserving all existing elements.
```

## Tips for Best Results

1. **Be specific early** — Vague inputs need more enhancement
2. **Match the user's intent** — Don't over-design if they want simple
3. **Keep it structured** — Numbered sections help Stitch understand hierarchy
4. **Include the design system** — Consistency is key for multi-page projects
5. **One change at a time for edits** — Don't bundle unrelated changes
