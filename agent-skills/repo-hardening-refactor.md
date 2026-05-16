# repo-hardening-refactor

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

