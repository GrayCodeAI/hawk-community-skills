---
name: ag-mcp-builder-ms
description: Use this skill when building MCP servers to integrate external APIs or
  services, whether in Python (FastMCP) or Node/TypeScript (MCP SDK).
license: MIT
tags:
- general
risk: unknown
source: community
date_added: 2026-02-27
---

# Reference Files

## 📚 Documentation Library

Load these resources as needed during development:

### Core MCP Documentation (Load First)
- **MCP Protocol**: Start with sitemap at `https://modelcontextprotocol.io/sitemap.xml`, then fetch specific pages with `.md` suffix
- 📋 MCP Best Practices - Universal MCP guidelines including:
  - Server and tool naming conventions
  - Response format guidelines (JSON vs Markdown)
  - Pagination best practices
  - Transport selection (streamable HTTP vs stdio)
  - Security and error handling standards

### Microsoft MCP Documentation (For Azure/Foundry)
- 🔷 Microsoft MCP Patterns - Microsoft-specific patterns including:
  - Azure MCP Server architecture (48+ Azure services)
  - C#/.NET command implementation patterns
  - Remote MCP with Foundry Agent Service
  - Authentication (Entra ID, OBO flow, Managed Identity)
  - Testing infrastructure with Bicep templates

### SDK Documentation (Load During Phase 1/2)
- **Python SDK**: Fetch from `https://raw.githubusercontent.com/modelcontextprotocol/python-sdk/main/README.md`
- **TypeScript SDK**: Fetch from `https://raw.githubusercontent.com/modelcontextprotocol/typescript-sdk/main/README.md`
- **Microsoft MCP SDK**: See Microsoft MCP Patterns for C#/.NET

### Language-Specific Implementation Guides (Load During Phase 2)
- 🐍 Python Implementation Guide - Complete Python/FastMCP guide with:
  - Server initialization patterns
  - Pydantic model examples
  - Tool registration with `@mcp.tool`
  - Complete working examples
  - Quality checklist

- ⚡ TypeScript Implementation Guide - Complete TypeScript guide with:
  - Project structure
  - Zod schema patterns
  - Tool registration with `server.registerTool`
  - Complete working examples
  - Quality checklist

- 🔷 Microsoft MCP Patterns - Complete C#/.NET guide with:
  - Command hierarchy (BaseCommand → GlobalCommand → SubscriptionCommand)
  - Naming conventions (`{Resource}{Operation}Command`)
  - Option handling with `.AsRequired()` / `.AsOptional()`
  - Azure Functions remote MCP deployment
  - Live test patterns with Bicep

### Evaluation Guide (Load During Phase 4)
- ✅ Evaluation Guide - Complete evaluation creation guide with:
  - Question creation guidelines
  - Answer verification strategies
  - XML format specifications
  - Example questions and answers
  - Running an evaluation with the provided scripts

## Limitations
- Use this skill only when the task clearly matches the scope described above.
- Do not treat the output as a substitute for environment-specific validation, testing, or expert review.
- Stop and ask for clarification if required inputs, permissions, safety boundaries, or success criteria are missing.
