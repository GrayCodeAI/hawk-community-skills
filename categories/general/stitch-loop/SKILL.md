---
name: stitch-loop
description: 'Skill: stitch-loop'
license: MIT
tags:
- general
---

A competitive achievements page showing developer badges and milestones.

**DESIGN SYSTEM (REQUIRED):**
[Copy the entire design system block from .stitch/DESIGN.md]

**Page Structure:**
1. Header with title and navigation
2. Badge grid showing unlocked/locked states
3. Progress bars for milestone tracking
```

## File Structure Reference

```
project/
├── .stitch/
│   ├── metadata.json   # Stitch project & screen IDs (persist this!)
│   ├── DESIGN.md       # Visual design system (from design-md skill)
│   ├── SITE.md         # Site vision, sitemap, roadmap
│   ├── next-prompt.md  # The baton — current task
│   └── designs/        # Staging area for Stitch output
│       ├── {page}.html
│       └── {page}.png
└── site/public/        # Production pages
    ├── index.html
    └── {page}.html
```

### `.stitch/metadata.json` Schema

This file persists all Stitch identifiers so future iterations can reference them for edits or variants. Populate it by calling `[prefix]:get_project` after creating a project or generating screens.

```json
{
  "name": "projects/6139132077804554844",
  "projectId": "6139132077804554844",
  "title": "My App",
  "visibility": "PRIVATE",
  "createTime": "2026-03-04T23:11:25.514932Z",
  "updateTime": "2026-03-04T23:34:40.400007Z",
  "projectType": "PROJECT_DESIGN",
  "origin": "STITCH",
  "deviceType": "MOBILE",
  "designTheme": {
    "colorMode": "DARK",
    "font": "INTER",
    "roundness": "ROUND_EIGHT",
    "customColor": "#40baf7",
    "saturation": 3
  },
  "screens": {
    "index": {
      "id": "d7237c7d78f44befa4f60afb17c818c1",
      "sourceScreen": "projects/6139132077804554844/screens/d7237c7d78f44befa4f60afb17c818c1",
      "x": 0,
      "y": 0,
      "width": 390,
      "height": 1249
    },
    "about": {
      "id": "bf6a3fe5c75348e58cf21fc7a9ddeafb",
      "sourceScreen": "projects/6139132077804554844/screens/bf6a3fe5c75348e58cf21fc7a9ddeafb",
      "x": 549,
      "y": 0,
      "width": 390,
      "height": 1159
    }
  },
  "metadata": {
    "userRole": "OWNER"
  }
}
```

| Field | Description |
|-------|-------------|
| `name` | Full resource name (`projects/{id}`) |
| `projectId` | Stitch project ID (from `create_project` or `get_project`) |
| `title` | Human-readable project title |
| `designTheme` | Design system tokens: color mode, font, roundness, custom color, saturation |
| `deviceType` | Target device: `MOBILE`, `DESKTOP`, `TABLET` |
| `screens` | Map of page name → screen object. Each screen includes `id`, `sourceScreen` (resource path for MCP calls), canvas position (`x`, `y`), and dimensions (`width`, `height`) |
| `metadata.userRole` | User's role on the project (`OWNER`, `EDITOR`, `VIEWER`) |

## Orchestration Options

The loop can be driven by different orchestration layers:

| Method | How it works |
|--------|--------------|
| **CI/CD** | GitHub Actions triggers on `.stitch/next-prompt.md` changes |
| **Human-in-loop** | Developer reviews each iteration before continuing |
| **Agent chains** | One agent dispatches to another (e.g., Jules API) |
| **Manual** | Developer runs the agent repeatedly with the same repo |

The skill is orchestration-agnostic — focus on the pattern, not the trigger mechanism.

## Design System Integration

This skill works best with the `design-md` skill:

1. **First time setup**: Generate `.stitch/DESIGN.md` using the `design-md` skill from an existing Stitch screen
2. **Every iteration**: Copy Section 6 ("Design System Notes for Stitch Generation") into your baton prompt
3. **Consistency**: All generated pages will share the same visual language

## Common Pitfalls

- ❌ Forgetting to update `.stitch/next-prompt.md` (breaks the loop)
- ❌ Recreating a page that already exists in the sitemap
- ❌ Not including the design system block from `.stitch/DESIGN.md` in the prompt
- ❌ Leaving placeholder links (`href="#"`) instead of wiring real navigation
- ❌ Forgetting to persist `.stitch/metadata.json` after creating a new project

## Troubleshooting

| Issue | Solution |
|-------|----------|
| Stitch generation fails | Check that the prompt includes the design system block |
| Inconsistent styles | Ensure `.stitch/DESIGN.md` is up-to-date and copied correctly |
| Loop stalls | Verify `.stitch/next-prompt.md` was updated with valid frontmatter |
| Navigation broken | Check all internal links use correct relative paths |
