---
name: ag-go-rod-master
description: Comprehensive guide for browser automation and web scraping with go-rod
  (Chrome DevTools Protocol) including stealth anti-bot-detection patterns.
license: MIT
tags:
- general
risk: safe
source: https://github.com/go-rod/rod
date_added: 2026-02-27
---

## Best Practices

- ✅ **ALWAYS use `stealth.MustPage(browser)`** instead of `browser.MustPage()` for real-world sites.
- ✅ **ALWAYS `defer browser.MustClose()`** immediately after connecting.
- ✅ Use the error-returning API (not `Must*`) in production code.
- ✅ Set explicit timeouts with `.Timeout()` — never rely on defaults for production.
- ✅ Use `browser.MustIncognito().MustPage()` for isolated sessions.
- ✅ Use `PagePool` for concurrent scraping instead of spawning unlimited pages.
- ✅ Use `MustWaitStable()` before clicking elements that might be animating.
- ✅ Use `MustWaitRequestIdle()` after actions that trigger AJAX calls.
- ✅ Use `launcher.New().Headless(false).Devtools(true)` for debugging.
- ❌ **NEVER** use `time.Sleep()` for waiting — use Rod's built-in wait methods.
- ❌ **NEVER** create a new `Browser` per task — create one Browser, use multiple `Page` instances.
- ❌ **NEVER** use `browser.MustPage()` for production scraping — use `stealth.MustPage()`.
- ❌ **NEVER** ignore errors in production — always handle them explicitly.
- ❌ **NEVER** forget to defer-close browsers, pages, and hijack routers.

## Common Pitfalls

- **Problem:** Element not found even though it exists on the page.
  **Solution:** The element may be inside an iframe or shadow DOM. Use `page.MustSearch()` instead of `page.MustElement()` — it searches across all iframes and shadow DOMs.

- **Problem:** Click doesn't work because the element is animating.
  **Solution:** Call `el.MustWaitStable()` before `el.MustClick()`.

- **Problem:** Bot detection despite using stealth.
  **Solution:** Combine `stealth.MustPage()` with: randomized viewport sizes, realistic User-Agent strings, human-like input delays between keystrokes, and random idle behaviors (scroll, hover).

- **Problem:** Browser process leaks (zombie processes).
  **Solution:** Always `defer browser.MustClose()`. Rod uses [leakless](https://github.com/ysmood/leakless) to kill zombies after main process crash, but explicit cleanup is preferred.

- **Problem:** Timeout errors on slow pages.
  **Solution:** Use chained context: `page.Timeout(30 * time.Second).MustWaitLoad()`. For AJAX-heavy pages, use `MustWaitRequestIdle()` instead of `MustWaitLoad()`.

- **Problem:** HijackRequests router not intercepting requests.
  **Solution:** You must call `go router.Run()` after setting up routes, and `defer router.MustStop()` for cleanup.

## Limitations

- **CAPTCHAs:** Rod does not include CAPTCHA solving. External services (2captcha, etc.) must be integrated separately.
- **Extreme Anti-Bot:** While `go-rod/stealth` handles common detection (WebDriver, plugin fingerprints, WebGL), extremely strict systems (some Cloudflare configurations, Akamai Bot Manager) may still detect automation. Additional measures (residential proxies, human-like behavioral patterns) may be needed.
- **DRM Content:** Cannot interact with DRM-protected media (e.g., Widevine).
- **Resource Usage:** Each browser instance consumes significant RAM (~100-300MB+). Use `PagePool` and limit concurrency on memory-constrained systems.
- **Extensions in Headless:** Chrome extensions do not work in headless mode. Use `Headless(false)` with XVFB for server environments.
- **Platform:** Requires a Chromium-compatible browser. Does not support Firefox or Safari.

## Documentation References

- [Official Documentation](https://go-rod.github.io/) — Guides, tutorials, FAQ
- [Go API Reference](https://pkg.go.dev/github.com/go-rod/rod) — Complete type and method documentation
- [go-rod/stealth](https://github.com/go-rod/stealth) — Anti-bot detection plugin
- [Examples (source)](https://github.com/go-rod/rod/blob/main/examples_test.go) — Official example tests
- [Rod vs Chromedp Comparison](https://github.com/nichochar/go-rod.github.io/blob/main/lib/examples/compare-chromedp) — Migration reference
- [Chrome DevTools Protocol Docs](https://chromedevtools.github.io/devtools-protocol/) — Underlying protocol reference
- [Chrome CLI Flags Reference](https://peter.sh/experiments/chromium-command-line-switches) — Launcher flag documentation
- `references/api-reference.md` — Quick-reference cheat sheet
