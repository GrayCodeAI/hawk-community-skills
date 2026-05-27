---
name: minimax-slide-making-skill
description: 'Implement single-slide PowerPoint pages with PptxGenJS. Use when writing
  or fixing slide JS files: dimensions, positioning, text/image/chart APIs, styling
  rules, and export expectations for native ...'
license: MIT
tags:
- general
---

## QA (Required)

**Assume there are problems. Your job is to find them.**

Your first render is almost never correct. Approach QA as a bug hunt, not a confirmation step. If you found zero issues on first inspection, you weren't looking hard enough.

### Content QA

```bash
python -m markitdown slide-XX-preview.pptx
```

Check for missing content, typos, wrong order.

**Check for leftover placeholder text:**

```bash
python -m markitdown slide-XX-preview.pptx | grep -iE "xxxx|lorem|ipsum|placeholder"
```

If grep returns results, fix them before declaring success.

### Verification Loop

1. Generate slide → Extract text with `python -m markitdown slide-XX-preview.pptx` → Review content
2. **List issues found** (if none found, look again more critically)
3. Fix issues
4. **Re-verify** — one fix often creates another problem
5. Repeat until verification reveals no new issues

**Do not declare success until you've completed at least one fix-and-verify cycle.**

---
