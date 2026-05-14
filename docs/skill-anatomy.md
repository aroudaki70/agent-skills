# Skill Anatomy

Every skill lives in its own directory under `skills/`:

```
skills/
  skill-name/
    SKILL.md           # Required: The skill definition
    metadata.json      # Required: Agent metadata for discovery
```

## SKILL.md Format

### Frontmatter (Required)
```yaml
---
name: skill-name-with-hyphens
description: Guides agents through [task/workflow]. Use when [specific trigger conditions].
---
```

### Standard Sections
- **Overview** – What the skill does and why it matters
- **When to Use** – Triggering conditions and exclusions
- **Process** – Step-by-step workflow
- **Common Rationalizations** – Excuses agents use to skip steps, with rebuttals
- **Red Flags** – Warning signs of incorrect application
- **Verification** – Exit criteria with evidence requirements

### Writing Principles
1. Process over knowledge — steps, not facts
2. Specific over general — "Run `npm test`" beats "verify the tests"
3. Evidence over assumption — every checkbox requires proof
4. Anti-rationalization — every skip-worthy step needs a rebuttal
