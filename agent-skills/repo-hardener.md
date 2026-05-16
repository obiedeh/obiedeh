---
name: repo-hardener
description: Reduce bloat, duplication, dead code, stale documentation, unnecessary abstractions, and AI-generated repo sprawl. Use when a repo audit is requested, when an agent has produced a series of changes that need consolidation, when CI flags untouched files, or when documentation has drifted from code. Use this skill instead of production-architecture-reviewer when the question is "is this clean" rather than "is this safe to deploy".
---

# repo-hardener

Use when reducing bloat, duplication, dead code, stale docs, unnecessary abstractions, or
AI-generated repo sprawl.

## Refactor Rules

- Prefer deletion or consolidation before adding new files.
- Keep public docs concise and non-sensitive.
- Preserve existing behavior unless the task explicitly changes it.
- Avoid wrapper classes and helper modules that do not remove real complexity.

## Checks

- Search for duplicate helpers, stale references, and unused configs.
- Verify tests still target behavior, not implementation trivia.
- Keep diffs reviewable and scoped.

## Output

List removed or simplified surface area, validation run, and remaining entropy risks.
