# Agent Skills

Production-grade engineering skills for AI coding agents.

Skills encode the workflows, quality gates, and best practices that senior engineers use when building software.

## Commands

| What you're doing | Command | Skill |
|---|---|---|
| Discover what to build | `/discover` | `design-sprint` |
| Review code before merge | `/review` | `code-review-agent` |
| Write and verify tests | `/test` | `test-agent` |
| Audit security | `/security` | `security-audit-agent` |
| Optimize content for search | `/seo` | `seo-optimization-agent` |

## Skills

| Skill | What It Does | Use When |
|---|---|---|
| `design-sprint` | 5-phase accelerated discovery (Map→Sketch→Decide→Prototype→Validate) | Product discovery, pre-spec validation, high uncertainty |
| `code-review-agent` | Five-axis code review (correctness, security, performance, maintainability, style) | Reviewing PRs, assessing code quality |
| `test-agent` | Test strategy, writing, and coverage following the test pyramid | Writing tests, fixing bugs, improving coverage |
| `security-audit-agent` | OWASP Top 10 security audits, auth review, vulnerability detection | Auditing security, reviewing auth flows |
| `seo-optimization-agent` | SEO audit, keyword strategy, optimized HTML generation with Notion integration | Content optimization, search ranking, blog posts |

## Project Structure

```
agent-skills/
├── skills/              # Skill definitions (SKILL.md + metadata.json + scripts/)
├── agents/              # Specialist agent personas (.md)
├── references/          # Supplementary checklists
├── hooks/               # Session lifecycle hooks
├── docs/                # Documentation & setup guides
├── .claude/commands/    # Slash commands for Claude Code
├── .gemini/commands/    # Slash commands for Gemini CLI
├── plugin.json          # Claude Code plugin manifest
├── marketplace.json     # Plugin marketplace metadata
├── AGENTS.md            # AI agent guidance & intent mapping
├── CLAUDE.md            # Claude Code configuration
└── remote-config/       # Remote development setup
```

## How Skills Work

Every skill follows a consistent anatomy:

```yaml
---
name: skill-name
description: What it does + when to use it
---

# Skill Title

## Overview
What this skill does and why it matters

## Process
Step-by-step workflow with numbered steps and checkpoints

## Common Rationalizations
| Excuse | Reality |
|---|---|

## Red Flags
Warning signs that the skill is being violated

## Verification
Checklist of exit criteria with evidence requirements
```

## Quick Start

```bash
# Clone and explore
git clone https://github.com/aroudaki70/agent-skills.git
cd agent-skills

# Browse available skills
ls skills/
cat skills/code-review-agent/SKILL.md
```

## Workflow

High-uncertainty project start:
```
DISCOVER → design-sprint → BUILD (test-agent) → VERIFY (code-review) → SHIP
```

Content optimization:
```
OPTIMIZE → seo-optimization-agent → VERIFY → PUBLISH
```

## License

MIT
