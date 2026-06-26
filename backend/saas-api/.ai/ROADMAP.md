# ROADMAP.md

> Enterprise Backend Development Roadmap
>
> This document is the single source of truth for project planning.
>
> Every AI assistant MUST follow this roadmap exactly.
>
> Never skip phases.
>
> Never implement a future phase without explicit approval.

---

# Project

Skincare SaaS Platform

Architecture

Enterprise Clean Architecture

Status

🟢 Active Development

---

# Development Principles

Every phase must satisfy the following before completion.

## Planning

- Analyze current implementation.
- Understand dependencies.
- Produce implementation plan.

## Development

- Implement only the approved scope.
- Preserve architecture.
- Reuse existing abstractions.
- No duplicate code.

## Review

Review implementation for

- Architecture violations
- Async correctness
- Typing
- Validation
- Performance
- Naming
- Documentation
- Security

## Verification

Every phase must pass

```bash
uv run black .

uv run ruff check .

uv run mypy app

uv run python -m compileall app

uv run pytest
```

Only after all checks pass is the phase considered complete.

---

# PR-001

## Project Foundation

Status

✅ Completed

Objectives

- Repository structure
- FastAPI project
- Configuration
- Environment
- Logging
- Base modules

Definition of Done

✅ Completed

---

# PR-002

## Domain Models

Status

✅ Completed

Objectives

- Base model
- Mixins
- Merchant model
- Enums
- Relationships foundation

Definition of Done

✅ Completed

---

# PR-003

## Repository Layer

Status

✅ Completed

Objectives

- Generic repository
- Merchant repository
- Async queries
- Repository abstractions

Definition of Done

✅ Completed

---

# PR-004

## Persistence Layer

Status

✅ Completed

Objectives

- Async SQLAlchemy
- Alembic
- Session
- Engine
- Initial migration

Definition of Done

✅ Completed

---

# PR-005

## API Foundation

Status

✅ Completed

Objectives

- Global exception handling
- API response standard
- Dependency providers
- Router composition
- OpenAPI
- Health endpoint
- Infrastructure tests

Definition of Done

✅ Completed

---

# PR-006

# Merchant REST API

Status

🟡 Current Phase

Objectives

Implement complete Merchant Management.

Features

- Create Merchant
- Get Merchant
- List Merchants
- Update Merchant
- Delete Merchant
- Soft Delete
- Restore Merchant (optional if already supported)

Validation

- Email uniqueness
- Merchant code uniqueness
- Slug uniqueness
- Required fields
- Business rules

Query Support

- Pagination
- Filtering
- Searching
- Sorting

Responses

- Standard API Response
- Error Response
- Pagination Response

Business Rules

- Services contain business logic.
- Repositories perform DB operations only.
- Routers remain thin.

Testing

- CRUD tests
- Validation tests
- Pagination tests
- Error handling tests

Definition of Done

- CRUD complete
- Validation complete
- Pagination complete
- Quality gates pass
- Documentation updated

---

# PR-007

## Merchant Users

Status

⬜ Pending

Objectives

- Merchant users
- Roles
- Invitations
- User assignment

---

# PR-008

## Stores

Status

⬜ Pending

Objectives

- Store CRUD
- Merchant mapping
- Validation
- Pagination

---

# PR-009

## Websites

Status

⬜ Pending

Objectives

- Website CRUD
- Domain management
- Publishing status
- Merchant mapping

---

# PR-010

## Authentication Integration

Status

⬜ Pending

Objectives

- Auth-service integration
- JWT validation
- Current user dependency
- Refresh flow

---

# PR-011

## Authorization

Status

⬜ Pending

Objectives

- RBAC
- Permissions
- Policies
- Guards

---

# PR-012

## Audit Logs

Status

⬜ Pending

Objectives

- Entity audit
- User audit
- Change tracking
- History

---

# PR-013

## Background Jobs

Status

⬜ Pending

Objectives

- Scheduler
- Async jobs
- Notifications
- Email tasks

---

# PR-014

## Testing & Coverage

Status

⬜ Pending

Objectives

- Integration tests
- API tests
- Repository tests
- Service tests
- Coverage >90%

---

# PR-015

## Production Readiness

Status

⬜ Pending

Objectives

- Docker
- Monitoring
- Metrics
- Health
- Security
- Performance
- CI/CD
- Deployment

---

# AI Rules

Every AI assistant must

✅ Read AI_CONTEXT.md

✅ Read PROJECT_STATE.md

✅ Read ROADMAP.md

before making changes.

Never implement multiple roadmap phases.

Never skip roadmap phases.

Never refactor architecture without approval.

Never modify unrelated files.

After completing a phase

1. Update PROJECT_STATE.md
2. Update CHANGELOG.md
3. Update DECISIONS.md
4. Stop
5. Wait for approval

This roadmap is authoritative.