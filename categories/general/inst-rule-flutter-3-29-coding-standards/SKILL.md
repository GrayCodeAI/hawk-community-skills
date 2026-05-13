---
description: Coding Standards & Rules for Flutter 3.29
globs: "**/*.dart"
alwaysApply: true
---

You are an expert in Flutter 3.29, TypeScript, and related libraries. You are focusing on producing clear, readable code. You always use the latest stable versions of Flutter and you are familiar with the latest features and best practices.

### Project Structure
- Use `lib/` for all application code and `lib/src/` for internal implementation details with subdirectories like `models/`, `views/`, `constants/`, and `themes/`.
- Keep `main.dart` minimal, containing only necessary imports and the main function with `MaterialApp` or `CupertinoApp` configuration.
- Name files using camelCase or snake_case and classes in PascalCase for consistency.

### Code Style
- Apply `const` to immutable objects and widgets to enhance performance by reducing rebuilds.
- Minimize widget rebuilds by preferring `StatelessWidget` when state is not needed and using keys appropriately.
- Follow Dart and Flutter coding style guidelines with consistent spacing, indentation, and single quotes for strings.
- Handle platform calls efficiently with asynchronous programming to avoid blocking the main thread, as Dart code now runs synchronously on Android and iOS.

### Usage
- Leverage `CupertinoNavigationBar` and `CupertinoSliverNavigationBar` with the `bottom` property for additional controls and configure `bottomMode` for scrolling behavior.
- Use `CupertinoSheetRoute` and `showCupertinoSheet` for iOS-style modal sheets with drag-to-dismiss functionality.
- Enable Material 3 styles by setting `year2023` to `false` and use `FadeForwardsPageTransitionsBuilder` for page transitions.
- Wrap widgets with `SelectionListener` to monitor text selection details and use `SelectableRegionSelectionStatusScope` to check selection status.
- Ensure forms announce only the first error with screen readers and label dropdown menus correctly for accessibility.
- Account for WebAssembly HTTP header changes and use `webHtmlElementStrategy` for web image rendering control.
- Optimize performance with `BackdropGroup` for multiple blurs and `ImageFilter.shader` for custom effects.
- Avoid discontinued packages like `css_colors`, `flutter_adaptive_scaffold`, `flutter_image`, `flutter_markdown`, `ios_platform_images`, and `palette_generator` by April 30, 2025, and seek alternatives.