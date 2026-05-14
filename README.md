# Agent Skills

Production-grade engineering skills for AI coding agents.

Skills encode the workflows, quality gates, and best practices that senior engineers use when building software.

## Structure

```
agent-skills/
├── skills/           # Skill definitions (SKILL.md per skill)
├── agents/           # Specialist agent personas
├── references/       # Supplementary checklists
├── hooks/            # Session lifecycle hooks
├── docs/             # Documentation
├── .claude/commands/ # Slash commands for Claude Code
└── .gemini/commands/ # Slash commands for Gemini CLI
```

## Quick Start

Each skill in `skills/` contains a `SKILL.md` with:
- **Overview** – What the skill does
- **When to Use** – Trigger conditions
- **Process** – Step-by-step workflow
- **Common Rationalizations** – Excuses vs. reality
- **Red Flags** – Warning signs
- **Verification** – Exit criteria

## License

MIT
