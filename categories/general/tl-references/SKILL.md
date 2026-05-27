---
name: tl-references
description: 'Skill: tl-references'
license: MIT
tags:
- general
---

<Image
  src={hero}
  loading="eager"
  decoding="sync"
  alt="Hero"
/>
```

## Debugging LCP

```javascript
// Identify LCP element
new PerformanceObserver((entryList) => {
  const entries = entryList.getEntries()
  const lastEntry = entries[entries.length - 1]

  console.log('LCP:', {
    element: lastEntry.element,
    time: lastEntry.startTime,
    size: lastEntry.size,
    url: lastEntry.url,
    renderTime: lastEntry.renderTime,
    loadTime: lastEntry.loadTime,
  })
}).observe({ type: 'largest-contentful-paint', buffered: true })
```

## Common issues

| Issue                    | Impact      | Fix                        |
| ------------------------ | ----------- | -------------------------- |
| No preload for LCP image | +500-1000ms | Add `<link rel="preload">` |
| Large unoptimized image  | +300-800ms  | Compress, use WebP/AVIF    |
| Render-blocking CSS      | +200-500ms  | Inline critical CSS        |
| Slow TTFB                | +300-2000ms | CDN, edge caching          |
| Client-rendered content  | +500-2000ms | SSR/SSG                    |
