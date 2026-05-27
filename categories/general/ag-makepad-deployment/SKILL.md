---
name: ag-makepad-deployment
description: 'Skill: ag-makepad-deployment'
license: MIT
tags:
- general
---

## Troubleshooting

### Missing Resources

If app crashes with missing resources:
1. Check `resources` array in Cargo.toml includes all Makepad resources
2. Verify `before-packaging-command` runs successfully
3. Check `./dist/resources/` contains expected files

### iOS Provisioning

For iOS device deployment:
1. Create empty app in Xcode with same org/app identifiers
2. Run on physical device once to generate provisioning profile
3. Note the profile path, certificate fingerprint
4. Use `--profile`, `--cert`, `--device` flags

### Android SDK Issues

```bash
# Reinstall toolchain with full NDK
cargo makepad android install-toolchain --full-ndk
```

## Reference Files

- `references/platform-troubleshooting.md` - Platform-specific deployment issues
- `references/makepad-packaging-action.md` - GitHub Actions packaging reference
- `community/dora-studio-package-workflow.md` - Dora Studio CI packaging example

## External References

- [cargo-packager docs](https://docs.crabnebula.dev/packager/)
- [robius-packaging-commands](https://github.com/project-robius/robius-packaging-commands)
- [cargo-makepad](https://github.com/makepad/makepad)
- [makepad-packaging-action](https://github.com/marketplace/actions/makepad-packaging-action)

## Limitations
- Use this skill only when the task clearly matches the scope described above.
- Do not treat the output as a substitute for environment-specific validation, testing, or expert review.
- Stop and ask for clarification if required inputs, permissions, safety boundaries, or success criteria are missing.
