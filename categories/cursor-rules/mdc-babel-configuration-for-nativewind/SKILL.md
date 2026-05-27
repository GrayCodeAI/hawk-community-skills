---
name: mdc-babel-configuration-for-nativewind
description: "Specifies the correct Babel configuration for NativeWind to ensure proper processing and avoid conflicts."
license: MIT
tags: [cursor-rules]
---

- Babel configuration for NativeWind:
  - Include 'nativewind/babel' in the plugins array.
  - Avoid using jsxImportSource in presets.
  - Ensure 'react-native-reanimated/plugin' follows 'nativewind/babel'.