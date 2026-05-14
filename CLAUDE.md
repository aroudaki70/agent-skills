# Agent Skills Project

This project contains production-grade engineering skills for AI coding agents.

## Structure
- `skills/` - Skill definitions with SKILL.md and metadata.json
- `agents/` - Specialist agent persona configs (.md format)
- `references/` - Testing, security, performance, accessibility, orchestration
- `hooks/` - Session lifecycle hooks
- `docs/` - Documentation

## Commands
- `/review` - Run code review skill
- `/test` - Run test agent
- `/security` - Run security audit

## Orchestration Rules
- The user (or a slash command) is the orchestrator
- Personas do not invoke other personas
- A persona may invoke skills
- Skills are mandatory hops when an intent matches
