---
name: ghcp-references-hugo
description: 'Skill: ghcp-references-hugo'
license: MIT
tags:
- general
---

Content here...
```

## Templates

### Base Template (_default/baseof.html)

```html
<!DOCTYPE html>
<html>
<head>
  <title>{{ .Title }} | {{ .Site.Title }}</title>
  {{ partial "head.html" . }}
</head>
<body>
  {{ partial "header.html" . }}
  <main>
    {{ block "main" . }}{{ end }}
  </main>
  {{ partial "footer.html" . }}
</body>
</html>
```

### Single Page (_default/single.html)

```html
{{ define "main" }}
<article>
  <h1>{{ .Title }}</h1>
  <time>{{ .Date.Format "January 2, 2006" }}</time>
  {{ .Content }}
</article>
{{ end }}
```

### List Page (_default/list.html)

```html
{{ define "main" }}
<h1>{{ .Title }}</h1>
{{ range .Pages }}
  <article>
    <h2><a href="{{ .Permalink }}">{{ .Title }}</a></h2>
    <p>{{ .Summary }}</p>
  </article>
{{ end }}
{{ end }}
```

## Shortcodes

### Built-in Shortcodes

```markdown
{{< figure src="/images/photo.jpg" title="My Photo" >}}

{{< youtube dQw4w9WgXcQ >}}

{{< gist user 12345 >}}

{{< highlight go >}}
fmt.Println("Hello")
{{< /highlight >}}
```

### Custom Shortcode (layouts/shortcodes/alert.html)

```html
<div class="alert alert-{{ .Get "type" | default "info" }}">
  {{ .Inner | markdownify }}
</div>
```

Usage:

```markdown
{{< alert type="warning" >}}
**Warning:** This is important!
{{< /alert >}}
```

## Content Organization

### Page Bundles

```
content/
├── posts/
│   └── my-post/           # Page bundle
│       ├── index.md       # Content
│       └── image.jpg      # Resources
└── _index.md              # Section page
```

### Accessing Resources

```html
{{ $image := .Resources.GetMatch "image.jpg" }}
{{ with $image }}
  <img src="{{ .RelPermalink }}" alt="...">
{{ end }}
```

## Hugo Pipes (Asset Processing)

### SCSS Compilation

```html
{{ $styles := resources.Get "scss/main.scss" | toCSS | minify }}
<link rel="stylesheet" href="{{ $styles.RelPermalink }}">
```

### JavaScript Bundling

```html
{{ $js := resources.Get "js/main.js" | js.Build | minify }}
<script src="{{ $js.RelPermalink }}"></script>
```

## Taxonomies

### Configure

```toml
[taxonomies]
  tag = 'tags'
  category = 'categories'
```

### Use in Front Matter

```markdown
+++
tags = ['go', 'hugo']
categories = ['tutorials']
+++
```

### List Taxonomy Terms

```html
{{ range .Site.Taxonomies.tags }}
  <a href="{{ .Page.Permalink }}">{{ .Page.Title }} ({{ .Count }})</a>
{{ end }}
```

## Multilingual Sites

```toml
defaultContentLanguage = 'en'

[languages]
  [languages.en]
    title = 'My Site'
    weight = 1
  [languages.es]
    title = 'Mi Sitio'
    weight = 2
```

## Troubleshooting

| Issue | Solution |
|-------|----------|
| Page not found | Check `baseURL` configuration |
| Theme not loading | Verify theme path in config |
| Raw HTML not showing | Set `unsafe = true` in goldmark config |
| Slow builds | Use `--templateMetrics` to debug |
| Module errors | Run `hugo mod tidy` |
| CSS not updating | Clear browser cache or use fingerprinting |

## Resources

- [Hugo Documentation](https://gohugo.io/documentation/)
- [Hugo Themes](https://themes.gohugo.io/)
- [Hugo Discourse](https://discourse.gohugo.io/)
- [GitHub Repository](https://github.com/gohugoio/hugo)
- [Quick Reference](https://gohugo.io/quick-reference/)
