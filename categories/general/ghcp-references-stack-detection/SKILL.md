---
name: ghcp-references-stack-detection
description: 'Skill: ghcp-references-stack-detection'
license: MIT
tags:
- general
---

## Docker Base Image → Runtime

If no manifest file is present but a `Dockerfile` exists, the `FROM` line reveals the runtime:

| FROM line pattern | Runtime |
|------------------|---------|
| `FROM node:X` | Node.js X |
| `FROM python:X` | Python X |
| `FROM golang:X` | Go X |
| `FROM eclipse-temurin:X` | Java X (Eclipse Temurin JDK) |
| `FROM mcr.microsoft.com/dotnet/aspnet:X` | .NET X |
| `FROM ruby:X` | Ruby X |
| `FROM rust:X` | Rust X |
| `FROM alpine` (alone) | Check what's installed via `RUN apk add` |
