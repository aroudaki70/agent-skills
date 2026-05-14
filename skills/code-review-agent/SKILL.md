---
name: code-review-agent
description: Guides agents through systematic code review across five axes. Use when reviewing pull requests, assessing code quality before merge, or enforcing team coding standards.
---

# Code Review Agent

## Overview
Performs structured code review across five key axes: correctness, security, performance, maintainability, and style. Ensures reviews are consistent, thorough, and actionable.

## When to Use
- Reviewing a pull request before merge
- Assessing code quality in an existing codebase
- Enforcing team coding standards and best practices
- NOT for: reviewing generated code that won't be merged

## Process

### 1. Understand the Change
- Read the diff and any associated PR description
- Identify the scope and intent of the change
- Check for related tests, docs, or issues

### 2. Five-Axis Review
| Axis | Focus |
|---|---|
| Correctness | Logic errors, edge cases, race conditions |
| Security | OWASP Top 10, input validation, auth |
| Performance | Algorithmic complexity, N+1 queries, bundle size |
| Maintainability | Naming, cohesion, coupling, duplication |
| Style | Project conventions, formatting, consistency |

### 3. Write Review Comments
- Label each comment: `Nit`, `Optional`, `FYI`, or `Blocking`
- For each blocking issue: explain the problem, suggest a fix, cite a source
- Keep total change review under ~400 lines per session

### 4. Verify
- Confirm all `Blocking` comments are addressed
- Check that tests still pass
- Approve or request changes

## Usage

This skill ships a review helper script:

```bash
git diff | bash /mnt/skills/user/code-review-agent/scripts/review.sh
```

## Common Rationalizations
| Rationalization | Reality |
|---|---|
| "I'll just focus on correctness" | Security and maintainability are equally important for production code |
| "This is a small change, it's fine" | Small changes can introduce large bugs; review them properly |
| "The tests pass so it must be correct" | Tests only cover what they test; review for untested paths |

## Red Flags
- Reviewing more than 400 lines at once without context
- No comments on public APIs or interfaces
- All comments are style nits with no substance

## Verification
- [ ] All five axes were evaluated
- [ ] Blocking issues are resolved before merge
- [ ] Test suite passes
