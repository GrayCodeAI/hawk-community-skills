---
name: ghcp-references-pandoc
description: 'Skill: ghcp-references-pandoc'
license: MIT
tags:
- general
---

# Introduction

Document content here...
```

## Filters

### Using Lua Filters

```bash
pandoc --lua-filter=filter.lua input.md -o output.html
```

Example Lua filter (`filter.lua`):

```lua
function Header(el)
  if el.level == 1 then
    el.classes:insert("main-title")
  end
  return el
end
```

### Using Pandoc Filters

```bash
pandoc --filter pandoc-citeproc input.md -o output.html
```

## Batch Conversion

### Bash Script

```bash
#!/bin/bash
for file in *.md; do
  pandoc "$file" -s -o "${file%.md}.html"
done
```

### PowerShell Script

```powershell
Get-ChildItem -Filter *.md | ForEach-Object {
  $output = $_.BaseName + ".html"
  pandoc $_.Name -s -o $output
}
```

## Resources

- [Pandoc User's Guide](https://pandoc.org/MANUAL.html)
- [Pandoc Demos](https://pandoc.org/demos.html)
- [Pandoc FAQ](https://pandoc.org/faqs.html)
- [GitHub Repository](https://github.com/jgm/pandoc)
