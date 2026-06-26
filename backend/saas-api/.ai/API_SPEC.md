# API_SPEC.md

> Enterprise API Specification
>
> This document defines all API conventions for the Skincare SaaS Platform Backend.
>
> Every endpoint MUST follow these specifications.

---

# API Versioning

Current Version

```
/api/v1
```

Future versions

```
/api/v2
```

Never expose unversioned APIs.

---

# REST Principles

Resources use plural nouns.

Examples

```
GET     /merchants
POST    /merchants

GET     /stores
POST    /stores

GET     /websites
POST    /websites
```

---

# HTTP Methods

GET

Retrieve resources.

POST

Create resources.

PUT

Replace entire resource.

PATCH

Partial update.

DELETE

Soft delete.

Never use GET for mutations.

---

# Standard Success Response

Every successful endpoint returns

```json
{
    "success": true,
    "message": "Operation completed successfully.",
    "data": {},
    "meta": {}
}
```

---

# Standard Error Response

```json
{
    "success": false,
    "message": "Validation failed.",
    "error": {
        "code": "VALIDATION_ERROR",
        "details": []
    },
    "meta": {}
}
```

---

# Pagination Response

```json
{
    "success": true,
    "message": "Merchants retrieved successfully.",
    "data": [],
    "meta": {
        "page": 1,
        "page_size": 20,
        "total_items": 120,
        "total_pages": 6
    }
}
```

---

# Pagination Rules

Default Page

```
1
```

Default Page Size

```
20
```

Maximum Page Size

```
100
```

---

# Filtering

Supported Query Parameters

```
status

merchant_type

category

country
```

Never implement filtering inside routers.

Filtering belongs in repositories.

---

# Searching

Search Parameter

```
search=
```

Search fields

- Merchant Name
- Merchant Code
- Email
- Slug

Search logic belongs in repositories.

---

# Sorting

Parameter

```
sort_by

sort_order
```

Allowed Orders

```
asc

desc
```

Default

```
created_at desc
```

---

# Resource URLs

Merchant

```
GET /merchants/{merchant_id}
```

Store

```
GET /stores/{store_id}
```

Website

```
GET /websites/{website_id}
```

Always use UUIDs.

---

# Status Codes

200 OK

Successful retrieval.

201 Created

Resource created.

204 No Content

Successful delete.

400 Bad Request

Invalid request.

401 Unauthorized

Authentication required.

403 Forbidden

Permission denied.

404 Not Found

Resource missing.

409 Conflict

Duplicate resource.

422 Validation Error

Request validation.

500 Internal Server Error

Unexpected error.

---

# Validation

Validate

- Path Parameters
- Query Parameters
- Request Body

Business validation belongs in Services.

---

# OpenAPI

Every endpoint must include

- Summary
- Description
- Tags
- Response Model
- Error Responses

---

# Tags

Health

Merchants

Stores

Websites

Authentication

Administration

System

---

# Idempotency

GET

Idempotent

PUT

Idempotent

PATCH

Idempotent where possible

DELETE

Soft Delete

POST

Not idempotent

---

# Security

Authentication

Bearer JWT

Authorization

RBAC

Future Phase

Never expose internal exception messages.

---

# API Review Checklist

Every endpoint must

- Use dependency injection
- Use response models
- Use exception handlers
- Use ResponseFactory
- Return ApiResponse
- Be documented
- Be typed
- Be tested

---

# AI Instructions

Every new endpoint must follow this specification.

Do not introduce new response formats.

Do not bypass ResponseFactory.

Do not implement business logic inside routers.