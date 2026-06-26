# DEVELOPMENT_WORKFLOW.md

> Enterprise AI Development Workflow
>
> This document defines the mandatory workflow for every AI assistant contributing to this repository.
>
> Every implementation must follow this workflow exactly.
>
> Never skip steps.
>
> Never implement multiple roadmap phases in a single task unless explicitly approved.

---

# Development Lifecycle

Every implementation follows this sequence.

```
Analyze

↓

Plan

↓

Approval

↓

Implementation

↓

Self Review

↓

Quality Gates

↓

Documentation Update

↓

Completion Report

↓

Commit

↓

Stop
```

---

# Step 1 — Analyze

Before changing any code

Read

```
.ai/AI_CONTEXT.md

.ai/PROJECT_STATE.md

.ai/ROADMAP.md

.ai/ARCHITECTURE.md

.ai/CODING_STANDARDS.md

.ai/API_SPEC.md

.ai/DATABASE_SPEC.md
```

Understand

- Current architecture
- Current roadmap phase
- Existing implementation
- Dependencies
- Risks

Never start coding before analysis.

---

# Step 2 — Plan

Produce an implementation plan.

The plan must include

- Objective
- Scope
- Files to modify
- Files not to modify
- Risks
- Testing strategy
- Definition of Done

If architecture changes are required

STOP

Wait for approval.

---

# Step 3 — Approval

No implementation begins without approval.

Human approval is required.

Never assume approval.

---

# Step 4 — Implementation

Implement only the approved roadmap phase.

Requirements

- Preserve architecture
- Preserve typing
- Preserve async design
- Preserve repository pattern
- Preserve service layer

Never

- Skip layers
- Introduce shortcuts
- Mix responsibilities

---

# Step 5 — Self Review

Before running checks review

Architecture

Typing

Imports

Naming

Validation

Error Handling

Performance

Security

Documentation

If problems are found

Fix them first.

---

# Step 6 — Quality Gates

Run

```bash
uv run black .

uv run ruff check .

uv run mypy app

uv run python -m compileall app

uv run pytest
```

If any command fails

Fix the issue.

Run again.

Repeat until everything passes.

Never continue with failing checks.

---

# Step 7 — Documentation

If implementation succeeds update

```
PROJECT_STATE.md

ROADMAP.md

CHANGELOG.md

DECISIONS.md
```

Every completed phase updates documentation.

---

# Step 8 — Completion Report

Produce a report.

Template

## Phase

PR-XXX

## Summary

Short description.

## Files Changed

List all modified files.

## Architecture

Confirm architecture preserved.

## Quality Gates

black

ruff

mypy

compileall

pytest

## Risks

Remaining concerns.

## Next Phase

Recommended roadmap phase.

---

# Step 9 — Commit

Commit only after

Quality gates pass.

Commit format

```
feat(api): implement merchant CRUD

fix(repository): resolve duplicate slug query

refactor(service): simplify validation

test(api): add merchant endpoint tests
```

One roadmap phase

↓

One commit

---

# Step 10 — Stop

After completing a roadmap phase

Stop.

Wait for human approval.

Never automatically continue into the next roadmap phase.

---

# Refactoring Policy

Allowed

- Small readability improvements
- Dead code removal
- Import cleanup
- Typing improvements

Not Allowed

- Architectural refactoring
- Folder restructuring
- Renaming public APIs
- Large dependency changes

Without explicit approval.

---

# Error Handling Workflow

If implementation fails

1.

Identify the error.

2.

Fix only the root cause.

3.

Re-run all quality gates.

4.

Verify no regression.

Never hide errors.

Never suppress warnings.

---

# Testing Workflow

Every new feature requires

Unit Tests

↓

Integration Tests

↓

Regression Tests

Tests must

- Be deterministic
- Be isolated
- Avoid external dependencies where possible
- Use fixtures appropriately

---

# Review Checklist

Before marking complete verify

- Scope completed
- No roadmap leakage
- No TODO
- No placeholder code
- No duplicated logic
- No dead imports
- No unused variables
- No Any
- No type: ignore
- Documentation updated
- Quality gates passed

---

# AI Behavior Rules

Every AI assistant must

- Work on one roadmap phase only.
- Never guess requirements.
- Never modify unrelated modules.
- Never change architecture without approval.
- Never continue after a completed phase.
- Always provide a completion report.
- Always update project documentation.

If an unexpected architectural issue is discovered

STOP

Report the issue.

Wait for approval.

Only then continue.

This workflow is mandatory for every implementation in this repository.