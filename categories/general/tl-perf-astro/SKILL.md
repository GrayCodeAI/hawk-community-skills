---
name: tl-perf-astro
description: Astro-specific performance optimizations for 95+ Lighthouse scores. Covers
  critical CSS inlining, compression, font loading, and LCP optimization. Use when
  optimizing Astro site performance, improv...
license: MIT
tags:
- general
---

<!doctype html>
<html lang="pt-BR">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />

    <!-- Font fallback (prevents FOIT) -->
    <style>
      @font-face {
        font-family: 'Inter';
        font-display: swap;
        src: local('Inter');
      }
    </style>

    <!-- Non-blocking Google Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link
      rel="stylesheet"
      href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap"
      media="print"
      onload="this.media='all'"
    />
    <noscript>
      <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap">
    </noscript>

    <!-- Preload LCP images -->
    <link rel="preload" as="image" href="/hero.png" fetchpriority="high">

    <title>{title}</title>

    <!-- Defer third-party scripts -->
    <script>
      let loaded = false;
      function loadAnalytics() {
        if (loaded) return;
        loaded = true;
        // Load GTM, analytics, etc.
      }
      ['scroll', 'click', 'touchstart'].forEach(e => {
        document.addEventListener(e, loadAnalytics, { once: true, passive: true });
      });
      setTimeout(loadAnalytics, 5000);
    </script>
  </head>
  <body>
    <slot />
  </body>
</html>
```

## Measuring

```bash
npx lighthouse https://your-site.com --preset=perf --form-factor=mobile
```

See also:

- **perf-lighthouse** - Running audits, reading reports, setting budgets
- **perf-web-optimization** - Core Web Vitals, bundle size, caching strategies

## Checklist

- [ ] `astro-critters` installed and configured
- [ ] `@playform/compress` installed and configured
- [ ] Google Fonts use `media="print" onload` pattern
- [ ] Third-party scripts deferred to user interaction
- [ ] LCP images preloaded in `<head>`
