# Agent Skills

Production-grade engineering skills for AI coding agents.

Skills encode the workflows, quality gates, and best practices that senior engineers use when building software.

## Project Structure

```
agent-skills/
├── skills/                            # Skill definitions
│   ├── design-sprint/                 # Accelerated discovery sprint (5-phase)
│   │   ├── SKILL.md
│   │   └── nudges.md
│   ├── code-review-agent/             # Systematic code review across five axes
│   │   ├── SKILL.md
│   │   ├── metadata.json
│   │   └── scripts/
│   ├── test-agent/                    # Test strategy and coverage analysis
│   │   ├── SKILL.md
│   │   ├── metadata.json
│   │   └── scripts/
│   └── security-audit-agent/          # OWASP Top 10 security auditing
│       ├── SKILL.md
│       ├── metadata.json
│       └── scripts/
├── agents/                            # Specialist agent personas
│   ├── code-reviewer.md
│   ├── security-auditor.md
│   └── test-engineer.md
├── references/                        # Supplementary checklists
│   ├── testing-patterns.md
│   ├── security-checklist.md
│   ├── performance-checklist.md
│   ├── accessibility-checklist.md
│   └── orchestration-patterns.md
├── hooks/                             # Session lifecycle hooks
├── docs/                              # Documentation
│   └── skill-anatomy.md
├── .claude/commands/                  # Slash commands
├── .gemini/commands/                  # Gemini CLI commands
├── plugin.json                        # Claude Code plugin manifest
├── marketplace.json                   # Plugin marketplace metadata
├── AGENTS.md                          # AI agent guidance
├── CONTRIBUTING.md                    # Contribution guidelines
├── CLAUDE.md                          # Claude Code configuration
└── remote-config/                     # Remote development setup
```

## Skills

| Skill | What It Does | Use When |
|---|---|---|
| `design-sprint` | 5-phase accelerated discovery (Map→Sketch→Decide→Prototype→Validate) | Product discovery, pre-spec validation, high uncertainty |
| `code-review-agent` | Five-axis code review (correctness, security, performance, maintainability, style) | Reviewing PRs, assessing code quality |
| `test-agent` | Test strategy, writing, and coverage following the test pyramid | Writing tests, fixing bugs, improving coverage |
| `security-audit-agent` | OWASP Top 10 security audits, auth review, vulnerability detection | Auditing security, reviewing auth flows |

## Workflow

When uncertainty is high at project start:

```
Discovery: design-sprint → spec-driven-development → planning-and-task-breakdown
```

## Quick Start

Each skill contains a `SKILL.md` with a structured workflow, common rationalizations table, and verification checklist.

## Quick Start

Each skill contains a `SKILL.md` with a structured workflow, common rationalizations table, and verification checklist.

## License

MIT
