---
name: agc-keybindings
description: 'Skill: agc-keybindings'
license: MIT
tags:
- general
---

## Keybinding Tips

### Remove All Default Bindings
```
keybind = clear
```

### Vim-style Navigation
```
keybind = ctrl+h=goto_split:left
keybind = ctrl+j=goto_split:down
keybind = ctrl+k=goto_split:up
keybind = ctrl+l=goto_split:right
```

### tmux-style Leader Key
```
keybind = ctrl+a>c=new_tab
keybind = ctrl+a>n=next_tab
keybind = ctrl+a>p=previous_tab
keybind = ctrl+a>|=new_split:right
keybind = ctrl+a>-=new_split:down
keybind = ctrl+a>z=toggle_split_zoom
keybind = ctrl+a>x=close_surface
```

### Global Quick Terminal
```
keybind = global:super+backquote=toggle_quick_terminal
```
**macOS:** Requires Accessibility permissions
**Linux:** Requires XDG Desktop Portal (KDE 5.27+, GNOME 48+)
