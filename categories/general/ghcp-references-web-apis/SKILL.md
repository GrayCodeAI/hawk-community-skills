---
name: ghcp-references-web-apis
description: 'Skill: ghcp-references-web-apis'
license: MIT
tags:
- general
---

## XMLHttpRequest

### What It Is

`XMLHttpRequest` (XHR) is a built-in browser API for making HTTP requests to servers without reloading the page. Despite its name, it can retrieve any data type -- JSON, binary (ArrayBuffer, Blob), plain text, XML, and HTML. It has been largely superseded by the Fetch API for new code, but remains widely used and fully supported.

### Why It Matters for Games

- **Asset loading**: Retrieve game assets (images, audio, JSON level data, binary model files) asynchronously without blocking the game loop.
- **Binary data support**: Set `responseType` to `"arraybuffer"` or `"blob"` to load binary assets directly into typed arrays for WebGL or Web Audio.
- **Progress tracking**: The `progress` event reports download progress, enabling loading bars.
- **Server communication**: Submit scores, authenticate players, fetch leaderboards, and synchronize game state with backend services.
- **Web Worker compatible**: XHR can be used inside Web Workers for background asset loading.

### Key Methods

| Method | Description |
|--------|-------------|
| `open(method, url, async?)` | Initialize a request (GET, POST, etc.) |
| `send(body?)` | Send the request; `body` can be string, FormData, ArrayBuffer, Blob |
| `setRequestHeader(name, value)` | Set an HTTP header (call after `open`, before `send`) |
| `abort()` | Cancel an in-progress request |
| `getResponseHeader(name)` | Retrieve a specific response header value |

### Key Properties

| Property | Description |
|----------|-------------|
| `response` | The response body as the type specified by `responseType` |
| `responseType` | Expected response format: `""`, `"text"`, `"json"`, `"arraybuffer"`, `"blob"`, `"document"` |
| `status` | HTTP status code (200, 404, etc.) |
| `readyState` | Request lifecycle state (0 = UNSENT through 4 = DONE) |
| `timeout` | Milliseconds before the request auto-aborts |
| `withCredentials` | Whether to include cookies in cross-origin requests |

### Events

| Event | Description |
|-------|-------------|
| `load` | Request completed successfully |
| `error` | Request failed |
| `progress` | Periodic progress updates during download |
| `abort` | Request was aborted |
| `readystatechange` | `readyState` changed |

### Code Example

```javascript
// Load a JSON level file
function loadLevel(url) {
  return new Promise((resolve, reject) => {
    const xhr = new XMLHttpRequest();
    xhr.open("GET", url);
    xhr.responseType = "json";

    xhr.onload = () => {
      if (xhr.status === 200) {
        resolve(xhr.response);
      } else {
        reject(new Error(`Failed to load level: ${xhr.status}`));
      }
    };
    xhr.onerror = () => reject(new Error("Network error"));
    xhr.send();
  });
}

// Load a binary asset with progress tracking
function loadBinaryAsset(url, onProgress) {
  return new Promise((resolve, reject) => {
    const xhr = new XMLHttpRequest();
    xhr.open("GET", url);
    xhr.responseType = "arraybuffer";

    xhr.onprogress = (event) => {
      if (event.lengthComputable && onProgress) {
        onProgress(event.loaded / event.total);
      }
    };

    xhr.onload = () => {
      if (xhr.status === 200) {
        resolve(xhr.response); // ArrayBuffer
      } else {
        reject(new Error(`Failed to load asset: ${xhr.status}`));
      }
    };
    xhr.onerror = () => reject(new Error("Network error"));
    xhr.send();
  });
}

// Usage
loadLevel("levels/level1.json").then(data => initLevel(data));
loadBinaryAsset("models/tank.bin", pct => updateLoadingBar(pct))
  .then(buf => parseModel(new Float32Array(buf)));
```

### Note on Fetch API

For new projects, the **Fetch API** (`fetch()`) is generally preferred over XHR. It provides a cleaner promise-based interface, supports streaming via `ReadableStream`, and integrates well with async/await. However, XHR remains relevant when you need progress events on uploads or require broader compatibility with legacy codebases.
