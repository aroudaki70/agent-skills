# Agent Skills Project

This project contains production-grade engineering skills for AI coding agents.

## Structure
- `skills/` - Skill definitions with SKILL.md and metadata.json
- `agents/` - Specialist agent persona configs (.md format)
- `references/` - Testing, security, performance, accessibility, orchestration
- `hooks/` - Session lifecycle hooks
- `docs/` - Documentation

## Skills by Phase

**Discover:** design-sprint

**Define:** idea-refine, spec-driven-development

**Plan:** planning-and-task-breakdown

**Build:** incremental-implementation, test-driven-development, frontend-ui-engineering, api-and-interface-design

**Verify:** debugging-and-error-recovery

**Review:** code-review-and-quality, security-and-hardening

**Ship:** shipping-and-launch

## Commands
- `/review` - Run code review skill
- `/test` - Run test agent
- `/security` - Run security audit
- `/discover` *(planned)* - Run design-sprint

Planned wrapper (not implemented yet): `/discover` (optional alias `/sprint`) as a convenience entry point to `design-sprint`. Until then, rely on intent mapping in `AGENTS.md`.

## Orchestration Rules
- The user (or a slash command) is the orchestrator
- Personas do not invoke other personas
- A persona may invoke skills
- Skills are mandatory hops when an intent matches
