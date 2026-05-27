---
name: copilot-autoresearch
description: Autonomous iterative experimentation loop for any programming task. Guides
  the user through defining goals, measurable metrics, and scope constraints, then
  runs an autonomous loop of code changes, ...
license: MIT
tags:
- general
compatibility: Requires git. The project must be a git repository. Requires terminal
  access to run commands.
metadata: None
author: luiscantero
inspired-by: https://github.com/karpathy/autoresearch
---

## Quick Reference

### Results TSV Format

Tab-separated, 5 columns:

```
experiment	commit	metric	status	description
0	a1b2c3d	0.997900	baseline	unmodified code
1	b2c3d4e	0.993200	keep	increase learning rate to 0.04
2	c3d4e5f	1.005000	discard	switch to GeLU activation
3	d4e5f6g	0.000000	crash	double model width (OOM)
```

### Git Workflow

- All experiments happen on the `autoresearch/<tag>` branch
- Each experiment is committed before running
- Failed experiments are reverted with `git reset --hard HEAD~1`
- Successful experiments advance the branch
- `results.tsv` and `run.log` stay untracked (added to `.git/info/exclude`)

### Key Principles

1. **Measure everything**: No experiment without a measurement.
2. **Revert failures**: The branch only advances on improvements.
3. **Stay autonomous**: Never stop to ask. Think harder if stuck.
4. **Keep it simple**: Complexity is a cost. Weigh it against gains.
5. **Log everything**: The TSV is the research journal.
