---
name: ag-apify-ultimate-scraper
description: AI-driven data extraction from 55+ Actors across all major platforms.
  This skill automatically selects the best Actor for your task.
license: MIT
tags:
- general
risk: unknown
source: community
---

#### Multi-Actor Workflows

For complex tasks, chain multiple Actors:

| Workflow | Step 1 | Step 2 |
|----------|--------|--------|
| **Lead enrichment** | `compass/crawler-google-places` → | `vdrmota/contact-info-scraper` |
| **Influencer vetting** | `apify/instagram-profile-scraper` → | `apify/instagram-comment-scraper` |
| **Competitor deep-dive** | `apify/facebook-pages-scraper` → | `apify/facebook-posts-scraper` |
| **Local business analysis** | `compass/crawler-google-places` → | `compass/Google-Maps-Reviews-Scraper` |

#### Can't Find a Suitable Actor?

If none of the Actors above match the user's request, search the Apify Store directly:

```bash
export $(grep APIFY_TOKEN .env | xargs) && mcpc --json mcp.apify.com --header "Authorization: Bearer $APIFY_TOKEN" tools-call search-actors keywords:="SEARCH_KEYWORDS" limit:=10 offset:=0 category:="" | jq -r '.content[0].text'
```

Replace `SEARCH_KEYWORDS` with 1-3 simple terms (e.g., "LinkedIn profiles", "Amazon products", "Twitter").

### Step 2: Fetch Actor Schema

Fetch the Actor's input schema and details dynamically using mcpc:

```bash
export $(grep APIFY_TOKEN .env | xargs) && mcpc --json mcp.apify.com --header "Authorization: Bearer $APIFY_TOKEN" tools-call fetch-actor-details actor:="ACTOR_ID" | jq -r ".content"
```

Replace `ACTOR_ID` with the selected Actor (e.g., `compass/crawler-google-places`).

This returns:
- Actor description and README
- Required and optional input parameters
- Output fields (if available)

### Step 3: Ask User Preferences

Before running, ask:
1. **Output format**:
   - **Quick answer** - Display top few results in chat (no file saved)
   - **CSV** - Full export with all fields
   - **JSON** - Full export in JSON format
2. **Number of results**: Based on character of use case

### Step 4: Run the Script

**Quick answer (display in chat, no file):**
```bash
node --env-file=.env ${CLAUDE_PLUGIN_ROOT}/reference/scripts/run_actor.js \
  --actor "ACTOR_ID" \
  --input 'JSON_INPUT'
```

**CSV:**
```bash
node --env-file=.env ${CLAUDE_PLUGIN_ROOT}/reference/scripts/run_actor.js \
  --actor "ACTOR_ID" \
  --input 'JSON_INPUT' \
  --output YYYY-MM-DD_OUTPUT_FILE.csv \
  --format csv
```

**JSON:**
```bash
node --env-file=.env ${CLAUDE_PLUGIN_ROOT}/reference/scripts/run_actor.js \
  --actor "ACTOR_ID" \
  --input 'JSON_INPUT' \
  --output YYYY-MM-DD_OUTPUT_FILE.json \
  --format json
```

### Step 5: Summarize Results and Offer Follow-ups

After completion, report:
- Number of results found
- File location and name
- Key fields available
- **Suggested follow-up workflows** based on results:

| If User Got | Suggest Next |
|-------------|--------------|
| Business listings | Enrich with `vdrmota/contact-info-scraper` or get reviews |
| Influencer profiles | Analyze engagement with comment scrapers |
| Competitor pages | Deep-dive with post/ad scrapers |
| Trend data | Validate with platform-specific hashtag scrapers |

## Error Handling

`APIFY_TOKEN not found` - Ask user to create `.env` with `APIFY_TOKEN=your_token`
`mcpc not found` - Ask user to install `npm install -g @apify/mcpc`
`Actor not found` - Check Actor ID spelling
`Run FAILED` - Ask user to check Apify console link in error output
`Timeout` - Reduce input size or increase `--timeout`

## Limitations
- Use this skill only when the task clearly matches the scope described above.
- Do not treat the output as a substitute for environment-specific validation, testing, or expert review.
- Stop and ask for clarification if required inputs, permissions, safety boundaries, or success criteria are missing.
