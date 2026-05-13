# Contributing

Thanks for your interest in contributing prompts!

## Guidelines

## **Naming Proposal**

| Type        | Prefix              | Purpose                                                                                       |
| ----------- | ------------------- | --------------------------------------------------------------------------------------------- |
| **rule**    | `rule-<name>.mdc`   | Define coding standards, best practices, and naming conventions.                              |
| **agent**   | `agent-<task>.mdc`  | Automate multi-step processes like setting up Dependencies, configuring ESLint, or deploying. |
| **feature** | `add-<feature>.mdc` | Add new components or modify existing parts of a project.                                     |

# Adding a prompt

- Create a folder under `prompts/<your-starter-name>`.
- Add a aiprompt.json file.
  ```json
  [
    {
      "name": "<name> (required)",
      "description": "<description> (required)",
      "type": "agent",
      "slug": "<slug> (required)",
      "development_process": ["plan", "design", "implement", "test", "deploy"],
      "dev_categories": ["backend", "frontend", "api", "documentation", "db"],
      "tags": ["automation", "setup", "agentic"],
      "techStack": {
        "framework": "next",
        "service": "supabase"
      },
      "author": {
        "name": "<name> (required)",
        "url": "<url> (optional)",
        "avatar": "<url> (optional)"
      },
      "model": ["reasoning", "chat"],
      "version": "1.0",
      "files": ["myrule.md"]
    }
  ]
  ```

or define multiple

  ```json
  [
  {
    "name": "<name> (required)",
    "description": "<description> (required)",
    ...
  },
  {
    "name": "<name> (required)",
    "description": "<description> (required)",
    ...
  },
  ]
```


- Add one or more `.mdc` files with your rules.
- For `.mdc` files, please include YAML front-matter. Here is an example:
  ```yaml
  ---
  description: "Short summary"
  globs: "*.ts,*.js,*.jsx,*.tsx"
  ---

## Submit a Pull Request

- Fork the repo, create a branch, add your rule(s), and submit a PR.

