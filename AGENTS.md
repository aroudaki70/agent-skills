# AGENTS.md

This file provides guidance to AI coding agents (Claude Code, Cursor, Copilot, etc.) when working with code in this repository.

## Repository Overview

A collection of agent skills for AI coding assistants. Skills are packaged instructions and scripts that extend agent capabilities.

## Skill-Driven Execution

### Core Rules

- If a task matches a skill, invoke it
- Skills are located in `skills/<skill-name>/SKILL.md`
- Never implement directly if a skill applies
- Always follow the skill instructions exactly

### Intent to Skill Mapping

| Intent | Skill |
|---|---|
| Product discovery / pre-spec validation under uncertainty | `design-sprint` |
| SEO audit / keyword optimization / content optimization | `seo-optimization-agent` |
| Code review | `code-review-agent` |
| Writing tests | `test-agent` |
| Security audit | `security-audit-agent` |

### Lifecycle Mapping

- DISCOVER → `design-sprint` (high uncertainty, validate direction before building)
- DEFINE → `design-sprint` → `seo-optimization-agent` (for content strategy)
- BUILD → `test-agent` (test-driven development)
- VERIFY → `code-review-agent` + `security-audit-agent`
- OPTIMIZE → `seo-optimization-agent` (content and search optimization)
- SHIP → `code-review-agent` (final review pass)

### Orchestration: Personas, Skills, and Commands

Three composable layers:

- **Skills** (`skills/<name>/SKILL.md`) — workflows with steps and exit criteria
- **Personas** (`agents/<role>.md`) — roles with a perspective and output format
- **Slash commands** (`.claude/commands/*.md`) — user-facing entry points

Composition rule: **the user (or a slash command) is the orchestrator. Personas do not invoke other personas.** A persona may invoke skills.

## Creating a New Skill

```
skills/
  {skill-name}/
    SKILL.md              # Required: skill definition
    scripts/              # Optional: executable scripts
      {script-name}.sh
```
