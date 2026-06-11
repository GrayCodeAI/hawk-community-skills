#!/usr/bin/env python3
"""Scan contributed skills for hardcoded credentials.

A contribution registry merges third-party content; a leaked key in a merged
skill is a realistic incident. This sweep flags high-confidence credential
signatures across each skill's text files and reports the offending file + line.

It runs in warning mode by default (exit 0) so it can be introduced without
breaking CI on the security/malware-analysis skills that legitimately contain
token-shaped example strings. Pass --strict to fail the build on findings, and
ratchet to that once the corpus is known clean.
"""
import argparse
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
CATEGORIES_DIR = REPO_ROOT / "categories"

# Extensions worth scanning inside a contributed skill directory.
SCAN_SUFFIXES = {".md", ".py", ".sh", ".bash", ".js", ".ts", ".json", ".yaml", ".yml", ".env", ".txt"}

# Files larger than this are skipped (with a warning): credential leaks live
# in source/config files, not multi-megabyte bulk content, and scanning them
# dominates runtime over a ~12k-skill corpus.
MAX_SCAN_SIZE = 2 * 1024 * 1024  # 2MB

# High-confidence credential signatures. Each entry: (name, compiled regex).
# Patterns target real key shapes (provider prefixes, AWS access keys, PEM
# private-key headers, explicit bearer tokens) rather than generic high-entropy
# strings, to keep the false-positive rate low.
SECRET_PATTERNS = [
    ("AWS access key id", re.compile(r"\bAKIA[0-9A-Z]{16}\b")),
    ("OpenAI/Stripe-style secret key", re.compile(r"\bsk-[A-Za-z0-9]{32,}\b")),
    ("Google API key", re.compile(r"\bAIza[0-9A-Za-z_\-]{35}\b")),
    ("GitHub token", re.compile(r"\bgh[pousr]_[A-Za-z0-9]{36,}\b")),
    ("Slack token", re.compile(r"\bxox[baprs]-[A-Za-z0-9-]{10,}\b")),
    ("Private key block", re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH |DSA |PGP )?PRIVATE KEY-----")),
    ("Explicit bearer token", re.compile(r"\bBearer\s+[A-Za-z0-9._\-]{20,}\b")),
    ("Generic assigned api key", re.compile(r"""(?i)\b(?:api[_-]?key|secret|password|token)\b\s*[:=]\s*['"][A-Za-z0-9._\-]{16,}['"]""")),
]

# Substrings that mark a match as an obvious placeholder/example, not a real
# leak. Lines containing any of these are ignored.
PLACEHOLDER_MARKERS = (
    "example", "placeholder", "your-", "your_", "xxxx", "...", "<", "redacted",
    "dummy", "sample", "sk-test", "sk_test", "changeme", "fake", "replace",
    "env[", "getenv", "os.environ", "${", "{{",
)


def _looks_placeholder(line: str) -> bool:
    low = line.lower()
    return any(m in low for m in PLACEHOLDER_MARKERS)


def scan_file(path: Path) -> list[tuple[int, str, str]]:
    """Return (line_no, pattern_name, snippet) findings for one file."""
    findings = []
    try:
        text = path.read_text(encoding="utf-8", errors="ignore")
    except OSError:
        return findings
    for i, line in enumerate(text.splitlines(), start=1):
        if _looks_placeholder(line):
            continue
        for name, rx in SECRET_PATTERNS:
            if rx.search(line):
                snippet = line.strip()
                if len(snippet) > 120:
                    snippet = snippet[:117] + "..."
                findings.append((i, name, snippet))
                break  # one finding per line is enough
    return findings


def iter_skill_files():
    if not CATEGORIES_DIR.exists():
        return
    for cat in sorted(CATEGORIES_DIR.iterdir()):
        if not cat.is_dir():
            continue
        for skill_dir in sorted(cat.iterdir()):
            if not skill_dir.is_dir():
                continue
            for f in sorted(skill_dir.rglob("*")):
                if f.is_file() and f.suffix.lower() in SCAN_SUFFIXES:
                    yield f


def main():
    parser = argparse.ArgumentParser(description="Scan skills for hardcoded secrets")
    parser.add_argument("--strict", action="store_true", help="exit non-zero when secrets are found")
    args = parser.parse_args()

    total = 0
    for f in iter_skill_files():
        for line_no, name, snippet in scan_file(f):
            rel = f.relative_to(REPO_ROOT)
            print(f"  ⚠ {rel}:{line_no}: possible {name}: {snippet}")
            total += 1

    if total == 0:
        print("✓ No hardcoded secrets detected")
        return

    print(f"\n{'✗' if args.strict else '⚠'} {total} possible secret(s) found.")
    print("  Secrets must come from environment variables, never hardcoded.")
    if args.strict:
        sys.exit(1)
    print("  (warning mode — pass --strict to fail CI)")


if __name__ == "__main__":
    main()
