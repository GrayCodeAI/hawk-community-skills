---
name: ghcp-references-testing
description: 'Skill: ghcp-references-testing'
license: MIT
tags:
- general
---

## Project structure

```
MyApp/
├── src/
│   ├── MyApp.AppHost/           # AppHost project
│   ├── MyApp.Api/               # API service
│   ├── MyApp.Worker/            # Worker service
│   └── MyApp.ServiceDefaults/   # Shared defaults
└── tests/
    └── MyApp.Tests/             # Integration tests
        ├── MyApp.Tests.csproj   # References AppHost + Testing package
        └── ApiTests.cs          # Test classes
```

```xml
<!-- MyApp.Tests.csproj -->
<Project Sdk="Microsoft.NET.Sdk">
  <PropertyGroup>
    <TargetFramework>net10.0</TargetFramework>
    <IsAspireTestProject>true</IsAspireTestProject>
  </PropertyGroup>

  <ItemGroup>
    <PackageReference Include="Aspire.Hosting.Testing" Version="*" />
    <PackageReference Include="Microsoft.NET.Test.Sdk" Version="*" />
    <PackageReference Include="xunit" Version="*" />
    <PackageReference Include="xunit.runner.visualstudio" Version="*" />
  </ItemGroup>

  <ItemGroup>
    <ProjectReference Include="..\..\src\MyApp.AppHost\MyApp.AppHost.csproj" />
  </ItemGroup>
</Project>
```
