---
name: ghcp-references-vuln-categories
description: 'Skill: ghcp-references-vuln-categories'
license: MIT
tags:
- general
---

## 7. Path Traversal
```python
# VULNERABLE
filename = request.args.get('file')
with open(f'/var/uploads/{filename}') as f:  # ../../../../etc/passwd

# SAFE
filename = os.path.basename(request.args.get('file'))
safe_path = os.path.join('/var/uploads', filename)
if not safe_path.startswith('/var/uploads/'):
    abort(400)
```
