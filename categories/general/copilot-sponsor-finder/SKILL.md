---
name: copilot-sponsor-finder
description: Find which of a GitHub repository's dependencies are sponsorable via
  GitHub Sponsors. Uses deps.dev API for dependency resolution across npm, PyPI, Cargo,
  Go, RubyGems, Maven, and NuGet. Checks npm...
license: MIT
tags:
- general
---

## Critical Rules

1. **NEVER present unverified links.** Fetch every URL before showing it. 5 verified links > 20 guessed links.
2. **NEVER guess from training knowledge.** Always check — funding pages change over time.
3. **Always be encouraging, never shaming.** Frame results positively — celebrate what IS funded, and treat unfunded deps as an opportunity, not a failing. Not every project needs or wants financial sponsorship.
4. **Lead with action.** The "🎯 Ways to Give Back" section is the primary output — bare clickable URLs, grouped by destination.
5. **Use deps.dev as primary resolver.** Fall back to registry APIs only if deps.dev is unavailable.
6. **Always use GitHub MCP tools** (`get_file_contents`), `web_fetch`, and `web_search` — never clone or shell out.
7. **Be efficient.** Batch API calls, deduplicate repos, check each owner's `.github` repo only once.
8. **Focus on GitHub Sponsors.** Most actionable platform — show others but prioritize GitHub.
9. **Deduplicate by maintainer.** Group to show real impact of sponsoring one person.
10. **Show the actionable minimum.** Tell users the fewest sponsorships to support the most deps.
11. **Minimize intermediate output.** Don't announce each batch. Collect all data, then output one cohesive report.
