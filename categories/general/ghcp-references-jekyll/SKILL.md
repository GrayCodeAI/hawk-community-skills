---
name: ghcp-references-jekyll
description: 'Skill: ghcp-references-jekyll'
license: MIT
tags:
- general
---

<article>
  <h1>{{ page.title }}</h1>
  <time>{{ page.date | date: "%B %d, %Y" }}</time>
  {{ content }}
</article>
```

## Plugins

### Common Plugins

```ruby
# Gemfile
group :jekyll_plugins do
  gem 'jekyll-feed'        # RSS feed
  gem 'jekyll-seo-tag'     # SEO meta tags
  gem 'jekyll-sitemap'     # XML sitemap
  gem 'jekyll-paginate'    # Pagination
  gem 'jekyll-archives'    # Archive pages
end
```

### Using Plugins

```yaml
# _config.yml
plugins:
  - jekyll-feed
  - jekyll-seo-tag
  - jekyll-sitemap
```

## Troubleshooting

| Issue | Solution |
|-------|----------|
| Ruby 3.0+ webrick error | `bundle add webrick` |
| Permission denied | Use `--user-install` or rbenv |
| Slow builds | Use `--incremental` |
| Liquid errors | Check for unescaped `{` `}` |
| Encoding issues | Add `encoding: utf-8` to config |
| Plugin not loading | Add to both Gemfile and _config.yml |

## Resources

- [Jekyll Documentation](https://jekyllrb.com/docs/)
- [Liquid Template Language](https://shopify.github.io/liquid/)
- [Kramdown Documentation](https://kramdown.gettalong.org/)
- [GitHub Repository](https://github.com/jekyll/jekyll)
- [Jekyll Themes](https://jekyllthemes.io/)
