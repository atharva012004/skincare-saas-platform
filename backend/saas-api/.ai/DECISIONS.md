# DECISIONS.md

> Architecture Decision Record (ADR)
>
> This document records important architectural and technical decisions made throughout the project.
>
> Every significant design decision must be documented here before implementation proceeds.
>
> Decisions are immutable. Never rewrite history. If a decision changes, create a new ADR that supersedes the previous one.

---

# ADR-001

## Title

Adopt Enterprise Clean Architecture

## Status

Accepted

## Date

2026-06-26

## Context

The platform is expected to grow into a multi-tenant enterprise SaaS with multiple services, domains, and integrations.

A layered architecture is required to ensure maintainability, scalability, and long-term development.

## Decision

Use the following architecture:

```
API

↓

Dependency Injection

↓

Service Layer

↓

Repository Layer

↓

SQLAlchemy

↓

PostgreSQL
```

## Consequences

Positive

- High maintainability
- Clear separation of concerns
- Easier testing
- Easier onboarding
- Better scalability

Negative

- Slightly more boilerplate

---

# ADR-002

## Title

Repository Pattern

## Status

Accepted

## Context

Business logic and persistence must remain independent.

## Decision

Repositories perform only database operations.

Repositories never contain business rules.

Repositories never commit or rollback transactions.

Services own transaction boundaries.

## Consequences

Positive

- Easier testing
- Cleaner business logic
- Database abstraction

---

# ADR-003

## Title

Service Layer Owns Business Logic

## Status

Accepted

## Context

Business rules must remain independent of HTTP and persistence.

## Decision

Services

- Validate business rules
- Coordinate repositories
- Manage transactions

Services never

- Return HTTP responses
- Raise HTTPException

## Consequences

Positive

- Framework independence
- Better testability
- Reusable business logic

---

# ADR-004

## Title

Standard API Response Envelope

## Status

Accepted

## Context

Inconsistent API responses increase frontend complexity.

## Decision

Every endpoint returns

Success

```json
{
  "success": true,
  "message": "...",
  "data": {},
  "meta": {}
}
```

Errors

```json
{
  "success": false,
  "message": "...",
  "error": {},
  "meta": {}
}
```

No endpoint may return a custom response format.

---

# ADR-005

## Title

Async-First Backend

## Status

Accepted

## Context

The application is IO-bound and database-heavy.

## Decision

Use

- FastAPI
- Async SQLAlchemy
- Async repositories
- Async services

Avoid synchronous database access.

---

# ADR-006

## Title

UUID Primary Keys

## Status

Accepted

## Decision

Every table uses UUID primary keys.

Integer IDs are prohibited.

---

# ADR-007

## Title

Soft Delete Strategy

## Status

Accepted

## Decision

Business entities are never physically deleted.

Soft delete uses

- is_deleted
- deleted_at

Repositories exclude deleted rows by default.

---

# ADR-008

## Title

Merchant is the Tenant Boundary

## Status

Accepted

## Context

The platform supports multiple independent merchants.

## Decision

Merchant represents the tenant.

Every tenant-owned entity must reference merchant_id.

Cross-tenant data access is prohibited.

---

# ADR-009

## Title

Authentication Service Separation

## Status

Accepted

## Context

Authentication has different scaling and security requirements.

## Decision

Authentication remains an external Node.js + Prisma service.

The FastAPI backend consumes authenticated identity and authorization data.

Authentication logic is not duplicated.

---

# ADR-010

## Title

Strict Typing Policy

## Status

Accepted

## Decision

The project follows strict typing.

Disallowed

- Any
- type: ignore
- Untyped public APIs

Every public function must be fully typed.

---

# ADR-011

## Title

Quality Gates are Mandatory

## Status

Accepted

## Decision

No roadmap phase is complete unless all quality gates pass.

Required

```bash
uv run black .

uv run ruff check .

uv run mypy app

uv run python -m compileall app

uv run pytest
```

Implementation must stop until failures are resolved.

---

# ADR-012

## Title

One Roadmap Phase Per Implementation

## Status

Accepted

## Decision

Each implementation must target exactly one roadmap phase.

No roadmap leakage is allowed.

Future phases require explicit approval.

---

# ADR-013

## Title

AI Documentation is the Source of Truth

## Status

Accepted

## Context

Multiple AI assistants (Blackbox, Codex, ChatGPT, Claude, Gemini) may contribute to this repository.

## Decision

The `.ai/` directory is the authoritative source of project context.

Every AI assistant must read:

- AI_CONTEXT.md
- PROJECT_STATE.md
- ROADMAP.md
- ARCHITECTURE.md
- CODING_STANDARDS.md
- API_SPEC.md
- DATABASE_SPEC.md
- DEVELOPMENT_WORKFLOW.md
- DECISIONS.md

before making changes.

---

# Future ADRs

Every new architectural decision must follow this template:

## ADR-XXX

Title

Status

Date

Context

Decision

Consequences

Related PR

Supersedes (if applicable)

---

This document preserves the architectural history of the project.

Do not modify existing ADRs.

Append new decisions only.