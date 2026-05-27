---
name: ag-seo-dataforseo
description: 'Skill: ag-seo-dataforseo'
license: MIT
tags:
- general
---

## Available Utility Tools

These DataForSEO tools are available for internal use by the agent but do not have dedicated commands:

- `serp_locations`:Location code lookups for SERP queries
- `serp_youtube_locations`:Location code lookups for YouTube queries
- `kw_data_google_ads_locations`:Location lookups for keyword data
- `kw_data_dfs_trends_demography`:Demographic data for trend analysis
- `kw_data_dfs_trends_subregion_interests`:Subregion interest data for trends
- `kw_data_dfs_trends_explore`:DFS proprietary trends data
- `kw_data_google_trends_categories`:Google Trends category lookups
- `dataforseo_labs_google_keyword_overview`:Quick keyword metrics overview
- `dataforseo_labs_google_historical_serp`:Historical SERP results for a keyword
- `dataforseo_labs_google_serp_competitors`:Competitors for a specific SERP
- `dataforseo_labs_google_keywords_for_site`:Keywords a site ranks for (alternative to ranked)
- `dataforseo_labs_google_page_intersection`:Page-level intersection analysis
- `dataforseo_labs_google_historical_rank_overview`:Historical domain rank data
- `dataforseo_labs_google_historical_keyword_data`:Historical keyword metrics
- `dataforseo_labs_available_filters`:Available filter options for Labs endpoints
- `backlinks_competitors`:Find domains with similar backlink profiles
- `backlinks_bulk_backlinks`:Bulk backlink counts for multiple targets
- `backlinks_bulk_new_lost_referring_domains`:Bulk new/lost referring domains
- `backlinks_bulk_new_lost_backlinks`:Bulk new/lost backlinks
- `backlinks_bulk_ranks`:Bulk rank overview for multiple targets
- `backlinks_bulk_referring_domains`:Bulk referring domain counts
- `backlinks_domain_pages_summary`:Summary of pages on a domain
- `backlinks_domain_pages`:List pages on a domain with backlink data
- `backlinks_page_intersection`:Shared backlink sources at page level
- `backlinks_referring_networks`:Referring network analysis
- `backlinks_timeseries_new_lost_summary`:Track new/lost backlinks over time
- `backlinks_bulk_pages_summary`:Bulk page summaries
- `backlinks_available_filters`:Available filter options for Backlinks endpoints
- `domain_analytics_whois_available_filters`:WHOIS filter options
- `domain_analytics_technologies_available_filters`:Technology detection filter options
- `ai_opt_kw_data_loc_and_lang`:AI optimization keyword data locations/languages
- `ai_optimization_keyword_data_search_volume`:AI-specific keyword volume data
- `ai_optimization_llm_response`:Direct LLM response analysis
- `ai_optimization_llm_mentions_filters`:Available filters for LLM mentions
- `ai_optimization_chat_gpt_scraper_locations`:Available locations for ChatGPT scraper

## Cross-Skill Integration

When DataForSEO MCP tools are available, other claude-seo skills can leverage live data:

- **seo-audit**:Spawn `seo-dataforseo` agent for real SERP, backlink, on-page, and listings data
- **seo-technical**:Use `on_page_instant_pages` / `on_page_lighthouse` for real crawl data, `domain_analytics_technologies_domain_technologies` for stack detection
- **seo-content**:Use `kw_data_google_ads_search_volume`, `dataforseo_labs_bulk_keyword_difficulty`, `dataforseo_labs_search_intent` for real keyword metrics, `content_analysis_summary` for content quality
- **seo-page**:Use `serp_organic_live_advanced` for real SERP positions, `backlinks_summary` for link data
- **seo-geo**:Use `ai_optimization_chat_gpt_scraper` for real ChatGPT visibility, `ai_opt_llm_ment_search` for LLM mention tracking
- **seo-plan**:Use `dataforseo_labs_google_competitors_domain`, `dataforseo_labs_google_domain_intersection`, `dataforseo_labs_bulk_traffic_estimation` for real competitive intelligence

## Error Handling

- **MCP server not connected**: Report that DataForSEO extension is not installed or MCP server is unreachable. Suggest running `./extensions/dataforseo/install.sh`
- **API authentication failed**: Report invalid credentials. Suggest checking DataForSEO API login/password in MCP config
- **Rate limit exceeded**: Report the limit hit and suggest waiting before retrying
- **No results returned**: Report "no data found" for the query rather than guessing. Suggest broadening the query or checking location/language codes
- **Invalid location code**: Report the error and suggest using the locations lookup tool to find the correct code

## Output Formatting

Match existing claude-seo output patterns:
- Use tables for comparative data
- Prioritize issues as Critical > High > Medium > Low
- Include specific, actionable recommendations
- Show scores as XX/100 where applicable
- Note data source as "DataForSEO (live)" to distinguish from static analysis

## Limitations
- Use this skill only when the task clearly matches the scope described above.
- Do not treat the output as a substitute for environment-specific validation, testing, or expert review.
- Stop and ask for clarification if required inputs, permissions, safety boundaries, or success criteria are missing.
