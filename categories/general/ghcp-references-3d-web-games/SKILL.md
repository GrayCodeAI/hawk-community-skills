---
name: ghcp-references-3d-web-games
description: 'Skill: ghcp-references-3d-web-games'
license: MIT
tags:
- general
---

## WebXR

WebXR is the modern web API for building virtual reality (VR) and augmented reality (AR) experiences in the browser. It replaces the deprecated WebVR API.

### What WebXR Is

The WebXR Device API provides access to XR hardware (headsets, controllers) and enables stereoscopic rendering. It captures real-time data including:

- Headset position and orientation
- Controller position, orientation, velocity, and acceleration
- Input events from XR controllers

### Supported Devices

- Meta Quest
- Valve Index
- PlayStation VR (PSVR2)
- Any device with a WebXR-compatible browser

### Core Concepts

Every WebXR experience requires two things:

1. **Real-time positional data** -- the application continuously receives headset and controller positions in 3D space.
2. **Real-time stereoscopic rendering** -- the application renders two slightly offset views (one for each eye) to the headset's display.

### Framework Support

All major 3D web frameworks support WebXR:

- **A-Frame** -- built-in VR mode button; declarative HTML-based scenes automatically work in VR.
- **Three.js** -- provides WebXR integration via `renderer.xr`. See [Three.js VR documentation](https://threejs.org/docs/#manual/en/introduction/How-to-create-VR-content).
- **Babylon.js** -- built-in WebXR support via the XR Experience Helper.

### Related APIs

- **Gamepad API** -- for non-XR controller inputs (gamepads, joysticks).
- **Device Orientation API** -- for detecting device rotation on mobile devices.

### Design Principles

- Prioritize **immersion** over raw graphics quality or gameplay complexity.
- Users must feel like they are *part of the experience*.
- Basic shapes rendered at high, stable frame rates can be more compelling in VR than detailed graphics at unstable frame rates.
- Experimentation is essential; test frequently on actual hardware.

### Practical Tips

- Start with A-Frame for rapid VR prototyping -- its declarative HTML approach gets you to a working VR scene in minutes.
- Use Three.js or Babylon.js when you need more control over rendering and performance.
- Always test on real headsets; the experience is vastly different from desktop preview.
- Maintain a stable, high frame rate (72-90+ FPS) to prevent motion sickness.
- Consult [MDN WebXR Device API](https://developer.mozilla.org/en-US/docs/Web/API/WebXR_Device_API) for the full API reference.
