# ARCHITECTURE.md

> Enterprise Architecture Specification
>
> This document defines the architecture of the Skincare SaaS Platform Backend.
>
> Every AI assistant MUST follow this architecture.
>
> Do not change architectural decisions without explicit approval.

---

# Architecture Style

The project follows **Enterprise Clean Architecture** with strict layer separation.

```
                Client
                   │
                   ▼
        FastAPI API Layer
                   │
                   ▼
        Dependency Injection
                   │
                   ▼
          Service Layer
                   │
                   ▼
        Repository Layer
                   │
                   ▼
     SQLAlchemy Async ORM
                   │
                   ▼
          PostgreSQL Database
```

---

# High Level Folder Structure

```
app/
│
├── api/
├── core/
├── db/
├── dependencies/
├── middleware/
├── models/
├── repositories/
├── schemas/
├── services/
├── shared/
├── tests/
└── utils/
```

Every folder has one responsibility.

---

# Layer Responsibilities

## API Layer

Location

```
app/api/
```

Responsibilities

- Receive HTTP requests
- Validate request body
- Dependency Injection
- Call Services
- Return standardized responses

Never

- Execute SQL
- Contain business logic
- Commit transactions

---

## Dependency Layer

Location

```
app/dependencies/
```

Responsibilities

- Provide database sessions
- Provide services
- Provide repositories
- Provide application settings
- Provide shared infrastructure

Dependencies must be stateless.

---

## Service Layer

Location

```
app/services/
```

Responsibilities

- Business logic
- Validation orchestration
- Transaction management
- Repository coordination

Services may call multiple repositories.

Services own the business rules.

Never

- Return HTTP responses
- Raise HTTPException
- Access FastAPI Request directly

Services raise ApplicationException subclasses.

---

## Repository Layer

Location

```
app/repositories/
```

Responsibilities

- Database access only
- SQLAlchemy queries
- CRUD
- Filtering
- Pagination queries

Repositories never contain business rules.

Repositories never commit transactions.

---

## Models

Location

```
app/models/
```

Rules

Use

Mapped[]

mapped_column()

SQLAlchemy 2.0 only.

No legacy declarative syntax.

---

## Schemas

Location

```
app/schemas/
```

Responsibilities

- Request DTOs
- Response DTOs
- Validation

Never

- Business logic

---

## Shared

Location

```
app/shared/
```

Contains

- Exceptions
- Constants
- Response Factory
- Utilities

Everything inside shared must remain framework-independent where possible.

---

# Dependency Flow

Allowed

```
API

↓

Service

↓

Repository

↓

Database
```

Forbidden

```
Repository

↓

Service
```

Forbidden

```
Repository

↓

API
```

Forbidden

```
Model

↓

Repository
```

Dependencies must always point downward.

---

# Transaction Rules

Repositories

Never commit.

Never rollback.

Services

Own transaction boundaries.

Commit when business operation succeeds.

Rollback on failure.

---

# Exception Flow

Repositories

Raise SQLAlchemy exceptions only.

↓

Services

Convert database errors into ApplicationExceptions.

↓

API

Global exception handlers convert ApplicationExceptions into ErrorResponse.

---

# Response Flow

Controller

↓

ResponseFactory

↓

ApiResponse

↓

JSON

Every endpoint returns the same response envelope.

---

# Validation Flow

Request

↓

Pydantic Schema

↓

Service Validation

↓

Repository

Validation belongs primarily to schemas and services.

---

# Multi-Tenancy

Merchant is the Tenant.

Future entities must include Merchant ownership.

Examples

Merchant

↓

Store

↓

Website

↓

Products

↓

Orders

↓

Customers

Never allow cross-tenant access.

---

# Security Principles

Authentication

External Service

Authorization

Internal

RBAC

Future Phase

Secrets

Never hardcode.

Always use environment variables.

---

# Database Principles

Primary Keys

UUID

Soft Delete

Enabled

Audit Fields

Required

Indexes

Required

Constraints

Required

Relationships

Explicit

Naming

Consistent

---

# API Principles

RESTful

Versioned

```
/api/v1/
```

Standard Responses

No raw dictionaries.

No inconsistent JSON.

OpenAPI

Always documented.

---

# Async Principles

Everything is async by default.

Never block the event loop.

Repositories

Async

Services

Async

Dependencies

Async where applicable.

---

# Logging

Structured logging.

No print().

No debugging statements.

Errors must be logged before returning responses.

---

# Testing Strategy

Unit Tests

Repositories

Services

Utilities

Integration Tests

API

Database

End-to-End

Future

Coverage Goal

90%+

---

# Performance Principles

Avoid N+1 queries.

Use indexes.

Paginate list endpoints.

Select only required columns.

Lazy-load only when appropriate.

---

# Quality Gates

Every PR must pass

```bash
uv run black .

uv run ruff check .

uv run mypy app

uv run python -m compileall app

uv run pytest
```

No phase is complete unless all checks pass.

---

# Definition of Done

A feature is complete only if

- Architecture preserved
- Business logic isolated
- Repository pattern respected
- Strict typing
- Tests updated
- Documentation updated
- Quality gates pass

---

# AI Rules

Every AI assistant must

- Preserve this architecture.
- Never bypass layers.
- Never introduce shortcuts.
- Never duplicate abstractions.
- Never change architectural direction without approval.

If an architectural concern is discovered

STOP

Report

Wait for approval

Only then continue.

This document is the authoritative architecture specification.