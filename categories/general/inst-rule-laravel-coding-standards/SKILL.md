---
description: Coding Standards & Rules for Laravel 11
globs: **/*.php
---

You are a senior Laravel 11 developer with extensive expertise in modern Laravel development, PHP, and web development best practices.

# Project Structure
- Place domain-driven services in app/Services/ to encapsulate business logic and promote thin controllers. Example: app/Services/Billing/SubscriptionService.php
- Store repositories in app/Repositories/ for data access abstraction with clear interfaces in app/Contracts/
- Organize API resource classes in app/Http/Resources/ for consistent API transformations
- Keep form request validation classes in app/Http/Requests/ for robust input validation
- Place event classes in app/Events/ and listeners in app/Listeners/ for event-driven features

# Laravel 11 Features
- Use the new Precognition feature for form validation without submitting. Example: $response = Precognition::validate($request)
- Implement Laravel Pennant for feature flags and A/B testing. Example: Feature::for($user)->active('new-billing')
- Utilize the new Rate Limiting improvements with Redis. Example: RateLimiter::for('api', fn () => Limit::perMinute(60))
- Use the enhanced Prompts CLI for interactive command building
- Implement the new Folio page-based routing for simpler route organization

# Controllers
- Use invokable controllers for single-action endpoints. Example: CreateSubscriptionController
- Implement resource controllers with Laravel's new API resource improvements
- Utilize controller middleware groups for common authentication and validation
- Keep controllers focused on request handling, delegating business logic to services

# Models
- Use Laravel's new Prunable trait for automatic model pruning
- Implement the new HasUuids trait for UUID primary keys
- Use model observers for complex event handling
- Implement the new WithoutTimestamps trait when timestamps are not needed
- Utilize the new HasFactory trait improvements for testing

# Services & Repositories
- Implement Laravel's new service provider improvements for better dependency injection
- Use the new Laravel Container improvements for service resolution
- Implement repository caching with Laravel's new cache improvements
- Utilize the new batch processing features for handling large datasets

# Middleware
- Use the new middleware priority system for proper execution order
- Implement rate limiting middleware with the new Redis improvements
- Utilize the new sanctum improvements for API authentication
- Use the new PreventRequestsDuringMaintenance middleware effectively

# Database & Eloquent
- Use the new database query builder improvements for better performance
- Implement the new full-text search capabilities in MySQL/PostgreSQL
- Utilize database transactions with the new automatic deadlock handling
- Use the new relationship loading improvements for better performance
- Implement the new enum casting features for better type safety

# Testing
- Use the new Pest test framework improvements
- Implement parallel testing with the new test improvements
- Use the new HTTP test response assertions
- Implement the new time manipulation helpers for testing
- Utilize the new database testing improvements

# API Development
- Use API resources with the new conditional attribute loading
- Implement API rate limiting with the new Redis improvements
- Use the new API versioning features effectively
- Implement the new API documentation improvements with OpenAPI
- Utilize the new API authentication improvements with Sanctum

# Performance Optimization
- Use the new query caching improvements for better performance
- Implement the new lazy loading improvements for collections
- Utilize the new Redis caching improvements
- Use the new queue improvements for background processing
- Implement the new model pruning features for database optimization

# Security
- Use the new password hashing improvements
- Implement the new CSRF protection improvements
- Utilize the new XSS protection features
- Use the new input sanitization improvements
- Implement the new authentication rate limiting

# SEO
- Use Laravel's new sitemap generation features
- Implement meta tags using the new view component improvements
- Utilize the new URL generation features for better SEO
- Use the new robots.txt improvements
- Implement the new canonical URL features