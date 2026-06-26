# DATABASE_SPEC.md

> Enterprise Database Specification
>
> This document defines all database design principles, conventions, and constraints for the Skincare SaaS Platform.
>
> Every database model, migration, repository, and service must comply with these rules.

---

# Database

Engine

PostgreSQL

ORM

SQLAlchemy 2.0 Async

Migration Tool

Alembic

Primary Key Strategy

UUID v4

---

# Naming Convention

## Tables

Use snake_case and plural names.

Examples

```
merchants

merchant_users

stores

websites

audit_logs
```

Never use camelCase.

---

## Columns

Use snake_case.

Examples

```
merchant_code

created_at

updated_at

deleted_at

is_deleted
```

---

## Foreign Keys

Format

```
merchant_id

store_id

website_id
```

Never use

```
merchant

merchantId
```

---

# Primary Keys

Every table uses

```
UUID
```

Example

```python
id: Mapped[UUID]
```

Never use integer IDs.

---

# Audit Columns

Every table must contain

```
id

created_at

updated_at
```

Soft deletable entities must also contain

```
deleted_at

is_deleted
```

Audit fields are inherited from BaseModel.

---

# Soft Delete

Delete operations must never physically remove business data.

Instead

```
is_deleted = True

deleted_at = current_timestamp
```

Repositories must exclude deleted records unless explicitly requested.

---

# Relationships

Use explicit SQLAlchemy relationships.

Example

Merchant

↓

Store

↓

Website

Use

```
relationship()
```

with proper

```
back_populates
```

Avoid unnecessary eager loading.

---

# Index Strategy

Create indexes for

Primary Search Fields

```
email

merchant_code

slug

name
```

Foreign Keys

```
merchant_id

store_id

website_id
```

Frequently filtered fields

```
status

subscription_plan

country

created_at
```

Composite indexes should be used when query patterns justify them.

---

# Unique Constraints

Examples

Merchant

```
email

merchant_code

slug
```

Store

```
merchant_id + store_name
```

Website

```
domain
```

Always enforce uniqueness at the database level.

---

# Nullable Columns

Only allow NULL when business logic requires it.

Prefer explicit defaults over nullable fields.

---

# Default Values

Prefer server-side defaults where appropriate.

Examples

```
created_at

updated_at

is_deleted
```

Never calculate timestamps in multiple places.

---

# Enums

Use PostgreSQL enums through SQLAlchemy.

Never use free-form strings for controlled values.

Example

```
MerchantStatus

SubscriptionPlan

UserRole
```

---

# Multi-Tenant Rules

Merchant is the tenant.

Every tenant-owned table must include

```
merchant_id
```

Examples

```
stores

websites

products

orders

customers
```

Never allow cross-tenant queries.

Repositories must always filter by tenant where applicable.

---

# Transactions

Repositories

Never commit.

Never rollback.

Services

Own transaction boundaries.

One business operation equals one transaction.

---

# Alembic Rules

Every schema change requires a migration.

Migration names must be descriptive.

Examples

```
create_merchants_table

add_store_indexes

add_subscription_plan

create_websites_table
```

Never edit an applied migration.

Create a new revision instead.

---

# Performance Guidelines

Avoid

- N+1 queries
- SELECT *
- Unindexed filtering
- Large OFFSET pagination for massive datasets

Prefer

- Indexed lookups
- LIMIT/OFFSET for moderate datasets
- Cursor pagination if needed in future phases
- Explicit column selection when appropriate

---

# Data Integrity

Enforce

- Foreign keys
- Unique constraints
- Check constraints
- NOT NULL where required

Business rules should exist in both

- Database constraints
- Service validation

---

# Security

Never store

- Plain-text passwords
- Secrets
- API keys without encryption

Sensitive data must be encrypted or delegated to the authentication service.

---

# Testing

Every migration should be verified.

Repository tests must validate

- CRUD
- Constraints
- Soft delete
- Relationships
- Pagination
- Filtering

---

# Review Checklist

Before merging database changes

- Naming follows convention
- UUID primary keys used
- Audit fields present
- Soft delete implemented
- Foreign keys defined
- Indexes added
- Constraints enforced
- Alembic migration generated
- Quality gates pass

---

# AI Instructions

Every new model and migration must follow this specification.

Never introduce inconsistent naming.

Never bypass the repository layer.

Never modify existing migrations that have already been applied.

Database integrity always takes precedence over convenience.