---
name: tl-core-web-vitals
description: Optimize Core Web Vitals (LCP, INP, CLS) for better page experience and
  search ranking. Use when asked to "improve Core Web Vitals", "fix LCP", "reduce
  CLS", "optimize INP", "page experience optimi...
license: MIT
tags:
- general
metadata: None
author: web-quality-skills
version: 1.0
---

## Framework quick fixes

### Next.js

```jsx
// LCP: Use next/image with priority
import Image from 'next/image'
;<Image src="/hero.jpg" priority fill alt="Hero" />

// INP: Use dynamic imports
const HeavyComponent = dynamic(() => import('./Heavy'), { ssr: false })

// CLS: Image component handles dimensions automatically
```

### React

```jsx
// LCP: Preload in head
;<link rel="preload" href="/hero.jpg" as="image" fetchpriority="high" />

// INP: Memoize and useTransition
const [isPending, startTransition] = useTransition()
startTransition(() => setExpensiveState(newValue))

// CLS: Always specify dimensions in img tags
```

### Vue/Nuxt

```vue
<!-- LCP: Use nuxt/image with preload -->
<NuxtImg src="/hero.jpg" preload loading="eager" />

<!-- INP: Use async components -->
<component :is="() => import('./Heavy.vue')" />

<!-- CLS: Use aspect-ratio CSS -->
<img :style="{ aspectRatio: '16/9' }" />
```

## References

- [web.dev LCP](https://web.dev/articles/lcp)
- [web.dev INP](https://web.dev/articles/inp)
- [web.dev CLS](https://web.dev/articles/cls)
- [Performance skill](SKILL.md)
