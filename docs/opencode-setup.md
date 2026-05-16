# OpenCode Setup

OpenCode uses a skill-driven execution model. This repo provides skills that auto-map to your workflow.

## How It Works

OpenCode reads `AGENTS.md` for intent-to-skill mapping. When you describe a task, OpenCode:

1. Evaluates the request against the intent mapping
2. Invokes the matching skill via the `skill` tool
3. Follows the skill workflow strictly

## Available Mappings

| Intent | Skill |
|---|---|
| "discover what to build" → | `design-sprint` |
| "optimize this content for SEO" → | `seo-optimization-agent` |
| "review this code" → | `code-review-agent` |
| "test this feature" → | `test-agent` |
| "audit security" → | `security-audit-agent` |

## Lifecycle

- DISCOVER → `design-sprint`
- BUILD → `test-agent`
- VERIFY → `code-review-agent` + `security-audit-agent`
- OPTIMIZE → `seo-optimization-agent`

## Core Rules

- If a task matches a skill, invoke it
- Skills are in `skills/<skill-name>/SKILL.md`
- Never implement directly if a skill applies
- Always follow the skill instructions exactly
