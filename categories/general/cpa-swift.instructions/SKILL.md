---
name: cpa-swift.instructions
description: "Skill: cpa-swift.instructions"
license: MIT
tags: [general]
---

# GitHub Copilot Instructions

These instructions define how GitHub Copilot should assist with this project. The goal is to ensure consistent, high-quality code generation aligned with our conventions, stack, and best practices.

## 🧠 Context

- **Project Type**: iOS App / macOS App / CLI Tool / Swift Package
- **Language**: Swift
- **Framework / Libraries**: SwiftUI / UIKit / Combine / Foundation / Vapor / Alamofire
- **Architecture**: MVVM / Clean Architecture / VIPER / Modular

## 🔧 General Guidelines

- Use idiomatic Swift conventions (camelCase, struct over class when possible).
- Prefer `let` over `var` for immutability.
- Use Swift’s optionals and `guard`/`if let` for safe unwrapping.
- Avoid force unwraps (`!`) unless absolutely safe and justified.
- Format using `swift-format` or SwiftLint.
- Document public methods and types using `///` doc comments.
- Leverage value types (structs, enums) and protocol-oriented design.

## 📁 File Structure

Use this structure as a guide when creating or updating files:

```text
Sources/
  App/
    Models/
    Views/
    ViewModels/
    Services/
    Utilities/
    Extensions/
Tests/
  Unit/
  Integration/
Resources/
```

## 🧶 Patterns

### ✅ Patterns to Follow

- Use MVVM for SwiftUI-based UIs.
- Use property wrappers like `@State`, `@ObservedObject`, and `@EnvironmentObject` properly.
- Leverage Combine or async/await for reactive and asynchronous logic.
- Use dependency injection through initializers or protocols.
- Break down views into reusable components.
- Validate user input using model or view model logic.
- Use enums with associated values to manage screen/view state.
- Prefer Swift’s `Codable` for JSON encoding/decoding.

### 🚫 Patterns to Avoid

- Don’t use force unwraps (`!`) unless you’re certain the value is non-nil.
- Avoid putting business logic directly inside views.
- Don’t mix UIKit and SwiftUI unnecessarily.
- Avoid deeply nested views or view models—break them into modules.
- Don’t expose internal state directly—use access control (`private`, `internal`, `public`).
- Avoid hardcoding strings or magic numbers—use constants or localization.

## 🧪 Testing Guidelines

- Use `XCTest` for unit and UI tests.
- Use `@testable import` to access internal modules when needed.
- Write snapshot/UI tests for reusable views or complex components.
- Use mock services conforming to protocols for ViewModel tests.
- Test async behavior using `XCTestExpectation` or `async/await`.

## 🧩 Example Prompts

- `Copilot, create a SwiftUI view that shows a list of users with their names and avatars.`
- `Copilot, write a model struct for a Product with name, price, and optional discount.`
- `Copilot, implement a Combine publisher that fetches data from a URL and decodes JSON.`
- `Copilot, write unit tests for the LoginViewModel using a mock AuthService.`
- `Copilot, define an enum for authentication state with associated values for success and error.`

## 🔁 Iteration & Review

- Review Copilot output for proper Swift idioms and memory safety.
- Refactor large or nested SwiftUI views into reusable components.
- Use Xcode warnings and SwiftLint to catch violations.
- Guide Copilot with comments for complex UI layout or async logic.

## 📚 References

- [The Swift Programming Language Book](https://swift.org/documentation/#the-swift-programming-language)
- [Apple SwiftUI Documentation](https://developer.apple.com/documentation/swiftui)
- [Swift.org API Guidelines](https://swift.org/documentation/api-design-guidelines/)
- [Combine Framework Guide](https://developer.apple.com/documentation/combine)
- [SwiftLint (Linter)](https://realm.github.io/SwiftLint/)
- [Vapor Web Framework](https://docs.vapor.codes/)
- [Alamofire Networking Library](https://github.com/Alamofire/Alamofire)
- [Apple XCTest Framework](https://developer.apple.com/documentation/xctest)
- [Swift Package Manager Docs](https://developer.apple.com/documentation/swift_packages/)