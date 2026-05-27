---
name: agc-idrive-config
description: 'Skill: agc-idrive-config'
license: MIT
tags:
- general
---

## Reading/Writing Plists

**Python** (preferred for complex operations):

```python
import plistlib
with open(path, 'rb') as f:
    data = plistlib.load(f)
# Modify data...
with open(path, 'wb') as f:
    plistlib.dump(data, f, fmt=plistlib.FMT_XML)
```

**plutil** (quick reads):

```bash
plutil -convert xml1 -o - file.plist   # dump to stdout
plutil -lint file.plist                 # validate
```

**defaults** (simple key reads):

```bash
defaults read ~/Library/Application\ Support/IDriveforMac/appDefaultSettings "user@example.com"
```

iDrive uses XML plist format. Always write back as XML (`plistlib.FMT_XML`).
