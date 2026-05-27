---
name: cpa-java.instructions
description: "Skill: cpa-java.instructions"
license: MIT
tags: [general]
---

# GitHub Copilot Instructions

These instructions define how GitHub Copilot should assist with this project. The goal is to ensure consistent, high-quality code generation aligned with our conventions, stack, and best practices.

## 🧠 Context

- **Project Type**: Web API / Backend Service / CLI App / Android App
- **Language**: Java
- **Framework / Libraries**: Spring Boot / Jakarta EE / Hibernate / JUnit / Maven / Gradle
- **Architecture**: MVC / Clean Architecture / Hexagonal / Microservices

## 🔧 General Guidelines

- Use Java-idiomatic patterns and follow standard conventions (JavaBeans, package structure).
- Use proper access modifiers (`private` by default).
- Always include null checks and use Optional where appropriate.
- Prefer `final` for variables that don't change.
- Format using `google-java-format` or IDE rules.
- Favor readability, testability, and separation of concerns.

## 📁 File Structure

Use this structure as a guide when creating or updating files:

```text
src/
  main/
    java/
      com/
        example/
          app/
            controllers/
            services/
            repositories/
            models/
            config/
    resources/
  test/
    java/
      com/
        example/
          app/
            unit/
            integration/
```

## 🧶 Patterns

### ✅ Patterns to Follow

- Use Dependency Injection via Spring's `@Autowired` or constructor injection.
- Apply standard annotations like `@Service`, `@Repository`, `@RestController`.
- Use DTOs for request/response payloads.
- Validate inputs with `@Valid` and Bean Validation (`javax.validation`).
- Handle exceptions using `@ControllerAdvice`.
- Log using `slf4j` and parameterized logging.
- Organize code by feature/module.
- Write clear Javadoc for public classes and methods.

### 🚫 Patterns to Avoid

- Don’t use field injection (`@Autowired` directly on fields).
- Avoid exposing entities directly to the client—use DTOs.
- Don’t hardcode values—use `application.properties` or `@Value`.
- Avoid God classes or putting too much logic in controllers.
- Don’t catch and ignore exceptions—handle or rethrow them.
- Avoid static utility classes for anything other than pure helpers.

## 🧪 Testing Guidelines

- Use `JUnit 5` and `Mockito` for unit testing.
- Use `@SpringBootTest` for integration tests.
- Follow Arrange-Act-Assert structure.
- Mock external dependencies using `@MockBean` or `@Mock`.
- Test validation, edge cases, and exception flows.

## 🧩 Example Prompts

- `Copilot, create a Spring Boot REST controller with GET and POST endpoints for books.`
- `Copilot, write a JPA repository interface for querying users by email.`
- `Copilot, define a DTO with validation annotations for user registration.`
- `Copilot, write a JUnit test for the OrderService.createOrder method using Mockito.`
- `Copilot, configure application.properties for PostgreSQL and enable debug logging.`

## 🔁 Iteration & Review

- Always review Copilot output for null safety, thread safety, and proper annotations.
- Use comments above the cursor to guide Copilot’s intent.
- Refactor repetitive or over-engineered output.
- Run linting (`Checkstyle`, `SpotBugs`, `PMD`) and formatting tools.

## 📚 References

- [Spring Boot Documentation](https://docs.spring.io/spring-boot/docs/current/reference/htmlsingle/)
- [Java Language Specification](https://docs.oracle.com/javase/specs/)
- [Java Code Conventions (Oracle)](https://www.oracle.com/java/technologies/javase/codeconventions-contents.html)
- [Google Java Style Guide](https://google.github.io/styleguide/javaguide.html)
- [JUnit 5 Documentation](https://junit.org/junit5/docs/current/user-guide/)
- [Mockito Documentation](https://site.mockito.org/)
- [Bean Validation (Jakarta)](https://jakarta.ee/specifications/bean-validation/)
- [SLF4J Logging](http://www.slf4j.org/manual.html)