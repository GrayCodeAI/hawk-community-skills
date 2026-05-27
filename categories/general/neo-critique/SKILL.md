---
name: neo-critique
description: Comprehensive multi-perspective review using specialized judges with
  debate and consensus building
license: MIT
tags:
- general
argument-hint: Optional file paths, commits, or context to review (defaults to recent
  changes)
---

*Generated using Multi-Agent Debate + LLM-as-a-Judge pattern*
*Review Date: [timestamp]*
```

## Important Guidelines

1. **Be Objective**: Base assessments on evidence, not preferences
2. **Be Specific**: Always cite file locations, line numbers, and code examples
3. **Be Constructive**: Frame criticism as opportunities for improvement
4. **Be Balanced**: Acknowledge both strengths and weaknesses
5. **Be Actionable**: Provide concrete recommendations with examples
6. **Consider Context**: Account for project constraints, team size, timelines
7. **Avoid Bias**: Don't favor certain patterns/styles without justification

## Usage Examples

```bash
# Review recent work from conversation
/critique

# Review specific files
/critique src/feature.ts src/feature.test.ts

# Review with specific focus
/critique --focus=security

# Review a git commit
/critique HEAD~1..HEAD
```

## Notes

- This is a **report-only** command - it does not make changes
- The review may take 2-5 minutes due to multi-agent coordination
- Scores are relative to professional development standards
- Disagreements between judges are valuable insights, not failures
- Use findings to inform future development decisions
