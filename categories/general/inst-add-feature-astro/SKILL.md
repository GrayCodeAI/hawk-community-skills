---
name: inst-add-feature-astro
description: Framework-specific patterns for adding features to Astro 4 applications
license: MIT
tags:
- general
---

<head>
  <title>{frontmatter.title}</title>
  <meta name="description" content={frontmatter.description} />
  <meta property="og:image" content={frontmatter.image} />
  <link rel="canonical" href={new URL(Astro.url.pathname, Astro.site)} />
</head>
```

# Dos
- Use Content Collections for feature data
- Implement View Transitions properly
- Use Islands Architecture effectively
- Configure SSR appropriately
- Handle server integration properly

# Donts
- Don't skip schema validation
- Avoid unnecessary client hydration
- Don't bypass transition system
- Don't ignore SSR capabilities
- Don't misuse server features
