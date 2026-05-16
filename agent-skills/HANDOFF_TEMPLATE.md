# Agent Handoff Template

Use this template whenever one agent hands work to another.

The goal is to reduce ambiguity, prevent scope drift, and keep implementation reviewable.

---

# Task Objective

One sentence describing the exact task.

---

# Scope

## Files allowed to change

- path/to/file
- path/to/file

## Files forbidden to change

- path/to/file
- path/to/file

---

# Constraints

- Maximum files touched:
- Maximum lines changed:
- New dependencies allowed: yes/no
- New top-level modules allowed: yes/no
- Public/private boundary considerations:

---

# Required skill

Primary skill:
- `skill-name`

Optional supporting skill:
- `skill-name`

Why these skills apply:
- One sentence.

---

# Validation requirements

Required checks:

- unit tests
- lint/type checks
- smoke tests
- config validation
- doc link validation

Required commands:

```text
pytest ...
ruff check ...
```

---

# Acceptance criteria

The task is complete only if:

- behavior works as requested
- no unnecessary abstractions were added
- no placeholder code was introduced
- validation checks passed or skipped checks are explained
- documentation matches implementation
- scope boundaries were respected

---

# Explicit non-goals

List adjacent problems that must NOT be solved during this task.

Example:

- Do not redesign service boundaries
- Do not add dashboards
- Do not refactor unrelated modules
- Do not add deployment automation

---

# Review focus for receiving agent

The reviewer should inspect:

- architecture drift
- unnecessary abstractions
- validation gaps
- public/private boundary violations
- evidence quality
- runtime stability implications

---

# Rollback plan

Describe the smallest rollback path if the patch fails.
