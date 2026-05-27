---
name: ag-issues
description: Interact with GitHub issues - create, list, and view issues.
license: MIT
tags:
- general
allowed-tools: Bash(gh *)
risk: unknown
source: community
metadata: None
author: Shpigford
version: 1.0
---

## Error Handling

If `gh` command fails:
1. Check if user is authenticated: `gh auth status`
2. If not authenticated, inform user to run `gh auth login`
3. Check if in a git repository with a GitHub remote
4. Report specific error message to user

## Important Notes

- **Titles should be succinct** (5-10 words) - if a user provides a long title, help shorten it and move details to body
- **Bodies should be detailed** - encourage users to provide thorough context, steps, and specifics
- Always confirm the issue was created successfully by showing the URL
- For issue bodies, preserve user's formatting and newlines
- If the user provides minimal information, that's okay - create the issue with what they gave
- Use HEREDOC for the body to preserve formatting:
  ```bash
  gh issue create --title "Title" --body "$(cat <<'EOF'
  Body content here
  EOF
  )"
  ```

## Limitations
- Use this skill only when the task clearly matches the scope described above.
- Do not treat the output as a substitute for environment-specific validation, testing, or expert review.
- Stop and ask for clarification if required inputs, permissions, safety boundaries, or success criteria are missing.
