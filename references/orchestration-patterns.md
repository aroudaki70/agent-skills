# Orchestration Patterns

## Endorsed Patterns

### 1. Direct Invocation
Single persona, single perspective, single artifact.

```
user -> code-reviewer -> report -> user
```

**Use when:** the work is one perspective on one artifact.

### 2. Single-Persona Slash Command
A slash command that wraps one persona with the project's skills.

```
/review -> code-reviewer (with code-review-agent skill) -> report
```

### 3. Parallel Fan-Out with Merge
Multiple personas operate on the same input concurrently.

```
                    +-> code-reviewer    -+
/ship -> fan out  --+-> security-auditor -+-> merge -> go/no-go
                    +-> test-engineer    -+
```

**Use when:** sub-tasks are independent, each benefits from its own context.

### 4. Sequential Pipeline (User-Driven)
The user runs commands in order, carrying context between them.

```
/spec -> /plan -> /build -> /test -> /review -> /ship
```

## Anti-Patterns

- **Router persona** — a persona that decides which other persona to call (wasteful, no domain value)
- **Persona calling persona** — defeats single-perspective design, loses context in hand-off
- **Deep persona trees** — each layer adds latency and tokens with no decision value
