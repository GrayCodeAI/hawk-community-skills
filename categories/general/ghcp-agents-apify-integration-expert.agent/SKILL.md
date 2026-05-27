---
name: ghcp-agents-apify-integration-expert.agent
description: Expert agent for integrating Apify Actors into codebases. Handles Actor
  selection, workflow design, implementation across JavaScript/TypeScript and Python,
  testing, and production-ready deployment.
license: MIT
tags:
- general
mcp-servers: None
apify: None
type: http
url: https://mcp.apify.com
headers: None
Authorization: Bearer $APIFY_TOKEN
Content-Type: application/json
tools: None
---

## 6. Access output fields

```python
dataset = client.dataset(run["defaultDatasetId"])
items = dataset.list_items().get("items", [])

for i, item in enumerate(items[:5]):
    url = item.get("url", "N/A")
    title = item.get("title", "No title")
    print(f"{i+1}. {title}")
    print(f"    URL: {url}")
```
