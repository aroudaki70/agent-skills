---
name: test-agent
description: Guides agents through test strategy, test writing, and coverage analysis. Use when implementing new features that need tests, fixing bugs, or improving test coverage.
---

# Test Agent

## Overview
Provides a systematic approach to testing: test pyramid guidance, test structure, mocking strategies, and coverage analysis. Ensures tests are meaningful, maintainable, and comprehensive.

## When to Use
- Writing tests for new code
- Adding regression tests for bug fixes
- Auditing existing test coverage
- NOT for: one-off exploratory scripts

## Process

### 1. Determine Test Level
- **Unit** (80%): Isolated logic, fast, no I/O
- **Integration** (15%): Module boundaries, external services
- **E2E** (5%): Critical user journeys

### 2. Write Tests (Red-Green-Refactor)
- Write a failing test first (Red)
- Write the minimum code to pass (Green)
- Refactor while keeping tests green

### 3. Follow Best Practices
- DAMP over DRY in tests
- One assertion concept per test
- Descriptive test names: `should_do_X_when_Y`
- Mock external dependencies, not internal logic

### 4. Verify Coverage
- Run tests and confirm all pass
- Check coverage report (aim for 80%+)
- Review untested branches

## Usage

This skill ships a test runner helper:

```bash
bash /mnt/skills/user/test-agent/scripts/run-tests.sh
```

## Common Rationalizations
| Rationalization | Reality |
|---|---|
| "I'll add tests later" | Later never comes; write tests now |
| "This is too simple to test" | Simple code changes over time; tests catch regressions |
| "100% coverage means no bugs" | Coverage measures execution, not correctness |

## Red Flags
- No tests for error paths or edge cases
- Tests that share mutable state
- Over-mocking (testing implementation, not behavior)

## Verification
- [ ] All new code has corresponding tests
- [ ] Tests follow the 80/15/5 pyramid split
- [ ] Coverage meets project threshold
