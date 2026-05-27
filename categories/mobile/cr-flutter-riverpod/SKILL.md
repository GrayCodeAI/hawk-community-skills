---
name: cr-flutter-riverpod
description: Cursor rules for flutter-riverpod
license: MIT
tags:
- cursor-rules
- tested
domain: engineering
version: 1.0
author: PatrickJS/awesome-cursorrules
---

## Project Structure

Please implement following this directory structure:

lib/features/products/
├── data/
│   ├── models/
│   │   ├── product_dto.dart
│   │   └── product_category_dto.dart
│   └── product_repository.dart
├── presentation/
│   ├── screens/
│   │   ├── product_list_screen.dart
│   │   └── product_details_screen.dart
│   ├── controllers/
│   │   └── product_list_controller.dart
│   ├── widgets/
│       └── product_card.dart
├── domain/
│   ├── models/
│   │   ├── product.dart
│   │   └── product_category.dart
│   └── get_products_use_case.dart
└── shared/
    └── models/
        └── address.dart

## Placement Rules

### Flutter Project Structure Placement Rules

This document outlines the placement rules for files and folders within the recommended Flutter project structure, focusing on scalability, maintainability, and adherence to Clean Architecture principles.

#### Top-Level Structure

lib/
├── features/
├── models/
├── providers/
├── routes/
├── core/
├── app.dart
└── main.dart

*   **lib/**: Contains all Dart code.
*   **features/**: Feature-specific code.
*   **models/**: Global models (use sparingly).
*   **providers/**: Global providers (minimize use).
*   **routes/**: App navigation.
*   **core/**: Core app logic (networking, errors, DI).
*   **app.dart**: Root widget.
*   **main.dart**: Entry point.

#### features/ Structure

lib/features/
└── <feature_name>/
├── data/
│   ├── models/
│   └── <feature_name>_repository.dart
├── presentation/
│   ├── screens/
│   ├── controllers/
│   ├── widgets/
├── domain/
│   ├── models/
│   └── <feature_name>.dart
├── use_cases/
└── shared/
└── models/

*   **<feature_name>/**: A feature (e.g., authentication, products).
*   **data/**: Data access.
    *   **models/**: Data Transfer Objects (DTOs).
    *   **<feature_name>_repository.dart**: Data access logic.
*   **presentation/**: UI.
    *   **screens/**: UI screens (<feature_name>_<screen_name>_screen.dart).
    *   **controllers/**: State management (<feature_name>_controller.dart).
    *   **widgets/**: Feature-specific widgets (<widget_name>.dart).
*   **domain/**: Business logic.
    *   **models/**: Domain models.
    *   **<feature_name>.dart**: Main entity.
*   **use_cases/**: User interactions (<use_case_name>.dart).
*   **shared/models/**: Models shared between *related* features.

#### shared/ (Top-Level) Structure

lib/shared/
├── providers/
├── widgets/
├── models/
└── services/

*   **providers/**: Providers shared across *unrelated* features.
*   **widgets/**: Widgets shared across *unrelated* features.
*   **models/**: Models shared across *unrelated* features (use cautiously).
*   **services/**: Utility classes.

#### models/ (Top-Level) Structure

lib/models/
└── <model_name>.dart

*   Global models (use sparingly).

#### providers/ (Top-Level) Structure

lib/providers/
└── <provider_name>.dart

*   Global providers (minimize use).

#### core/ Structure

lib/core/
├── network/
│   └── api_client.dart
├── errors/
│   └── exceptions.dart
└── di/
└── injection.dart

*   **network/**: Networking code.
*   **errors/**: Error handling.
*   **di/**: Dependency injection.

## Naming Conventions

*   **Files:** snake_case (e.g., product_list_screen.dart).
*   **Classes:** PascalCase (e.g., ProductListScreen).
*   **Variables/Functions:** camelCase (e.g., productList).

## Key Principles

*   **Feature Isolation:** Self-contained feature code.
*   **Separation of Concerns:** Separate data, logic, and UI.
*   **Single Responsibility:** One purpose per class/file.
*   **DRY:** Avoid code duplication.
*   **Prefer Feature-Specific:** Prioritize feature-level placement.

Please adhere to the above content when executing tasks.
