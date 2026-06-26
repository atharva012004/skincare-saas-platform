# CODING_STANDARDS.md

> Enterprise Coding Standards
>
> Every AI assistant MUST follow these standards.
>
> These rules are mandatory.

---

# General Principles

Write code as if it will be maintained by a team of senior engineers.

Code must be

- Readable
- Maintainable
- Testable
- Scalable
- Production Ready

Never optimize for fewer lines.

Always optimize for readability.

---

# Python Version

Python 3.11+

Use modern syntax only.

Examples

✅

```python
value: str | None
```

❌

```python
Optional[str]
```

---

# Typing

Every public function must be fully typed.

Every variable should have an inferable type.

Never use

- Any
- type: ignore
- cast unless absolutely necessary

Prefer Protocol and Generic where appropriate.

Strict mypy compatibility is required.

---

# Naming

Classes

```python
MerchantService
```

Repositories

```python
MerchantRepository
```

Schemas

```python
MerchantCreateRequest
MerchantResponse
```

Variables

```python
merchant_code
created_at
```

Constants

```python
MAX_PAGE_SIZE
DEFAULT_LIMIT
```

Private members

```python
_session
_repository
```

---

# File Naming

Use snake_case.

Examples

```
merchant_service.py

merchant_repository.py

response_factory.py
```

Never

```
MerchantService.py

MerchantRepository.py
```

---

# Class Rules

One responsibility per class.

Prefer composition over inheritance.

Keep classes small.

Never create God classes.

---

# Function Rules

Functions should perform one task.

Target

20–40 lines

Maximum

60 lines

Split large functions into private helper methods.

---

# Docstrings

Every public class

Every public function

Every public module

must have docstrings.

Use Google style.

Example

```python
def create_merchant(
    request: MerchantCreateRequest,
) -> Merchant:
    """
    Create a new merchant.

    Args:
        request:
            Merchant creation request.

    Returns:
        Created merchant.

    Raises:
        ConflictException:
            If merchant already exists.
    """
```

---

# Imports

Always

Standard Library

↓

Third Party

↓

Application

Separate groups with one blank line.

Never use wildcard imports.

---

# Async Rules

Everything touching the database must be async.

Never block the event loop.

Never call synchronous DB APIs.

---

# Repository Rules

Repositories

Only database logic.

Allowed

- SELECT
- INSERT
- UPDATE
- DELETE
- Pagination
- Filtering

Never

- Business logic
- HTTP logic
- Commit
- Rollback

---

# Service Rules

Services contain business logic.

Services

- Validate business rules
- Coordinate repositories
- Handle transactions

Never

- Return HTTP responses
- Raise HTTPException
- Access Request object

---

# Router Rules

Routers must remain thin.

Allowed

- Dependency Injection
- Request validation
- Response serialization

Never

- Business logic
- SQL queries

---

# Response Rules

Every endpoint returns

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

Never return raw dicts.

Never return inconsistent formats.

---

# Exception Rules

Only Services raise

- ValidationException
- ConflictException
- NotFoundException
- ForbiddenException
- UnauthorizedException

Routers never raise business exceptions.

Repositories never translate exceptions.

---

# SQLAlchemy Rules

Use SQLAlchemy 2.0.

Always

```python
Mapped[]

mapped_column()
```

Never use legacy APIs.

---

# Pydantic Rules

Use Pydantic v2.

Separate

Request Schemas

Response Schemas

Internal DTOs

Never reuse request schema as response schema.

---

# Validation Rules

Validation belongs in

1. Pydantic Schema

2. Service

Repositories never validate business rules.

---

# Logging

Never use

```python
print()
```

Use structured logging.

Errors

warning

info

debug

must go through logger.

---

# Testing

Every new feature requires

Unit Tests

Integration Tests

Regression Tests

Test names

```python
test_create_merchant_success()

test_create_merchant_duplicate_email()

test_create_merchant_invalid_slug()
```

---

# Performance

Avoid

N+1 queries.

Always paginate.

Select only required columns.

Index searchable fields.

---

# Security

Never

Hardcode secrets.

Log passwords.

Log tokens.

Return internal exceptions.

Always use environment variables.

---

# Code Review Checklist

Before finishing a PR verify

- No duplicate logic
- No dead code
- No TODO
- No placeholders
- No Any
- No type: ignore
- Correct async usage
- Proper docstrings
- Imports organized
- Architecture preserved

---

# Quality Gates

Every phase must pass

```bash
uv run black .

uv run ruff check .

uv run mypy app

uv run python -m compileall app

uv run pytest
```

If any command fails

Fix the issue

Run again

Never continue until all pass.

---

# Git Rules

One feature

↓

One commit

↓

One PR

Commit style

```
feat(api): implement merchant CRUD

fix(repository): resolve async query issue

refactor(service): simplify merchant validation

test(api): add merchant integration tests
```

---

# AI Instructions

Before changing code

1. Read

AI_CONTEXT.md

PROJECT_STATE.md

ROADMAP.md

ARCHITECTURE.md

CODING_STANDARDS.md

2. Analyze

3. Plan

4. Implement

5. Self Review

6. Fix Issues

7. Update Documentation

8. Stop

Never skip roadmap phases.

Never refactor architecture without approval.

These standards are mandatory for all future implementations.