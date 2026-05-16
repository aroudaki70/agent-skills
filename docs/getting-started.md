# Getting Started with Agent Skills

## Overview

This repository contains production-grade agent skills following the Agent Skills format. Each skill is a structured workflow with steps, verification gates, and anti-rationalization tables.

## Quick Start

```bash
# Clone the repo
git clone https://github.com/aroudaki70/agent-skills.git
cd agent-skills

# Explore available skills
ls skills/
```

## Using Skills

### Claude Code
Skills auto-discover via `plugin.json`. Invoke with slash commands:

```
/review   → code-review-agent
/security → security-audit-agent
/test     → test-agent
/seo      → seo-optimization-agent
```

### OpenCode
Intent-driven: describe what you need and the agent maps to the right skill.

### Via AGENTS.md
The `AGENTS.md` file provides intent-to-skill mapping for all agents.

## Workflow

When starting a new project with uncertainty:

```
DISCOVER → design-sprint → DEFINE → BUILD (test-agent) → VERIFY (code-review + security) → SHIP
```

For content projects:

```
OPTIMIZE → seo-optimization-agent → BUILD → VERIFY → SHIP
```

## Adding a New Skill

1. Create `skills/<skill-name>/SKILL.md` with YAML frontmatter
2. Add optional `scripts/` directory
3. Update `AGENTS.md` with intent mapping
4. Create a slash command in `.claude/commands/`
