# AI_CONTEXT.md

> Master Project Context for AI Assistants
>
> Every AI assistant working on this repository MUST read this file before making any changes.

---

# Project Information

## Project Name

Skincare SaaS Platform

## Repository

Enterprise Multi-Tenant SaaS Platform

## Primary Language

Python 3.11+

## Framework

FastAPI

## Database

PostgreSQL

## ORM

SQLAlchemy 2.0 Async

## Migration

Alembic

## Validation

Pydantic v2

## Authentication

External Authentication Service (Node.js + Prisma)

## Architecture

Enterprise Clean Architecture

Repository Pattern

Service Layer

Dependency Injection

SOLID Principles

Async First

Strict Typing

---

# Project Goal

Build a production-ready enterprise-grade multi-tenant SaaS platform for skincare merchants.

The backend must be scalable, maintainable, secure, and easy to extend.

This repository is NOT a tutorial project.

Every implementation must be production quality.

---

# Tech Stack

Backend

- FastAPI
- SQLAlchemy Async
- PostgreSQL
- Alembic
- Pydantic v2

Authentication

- Node.js
- Express
- Prisma
- PostgreSQL

Frontend (Future)

- Next.js
- React
- TypeScript
- TailwindCSS

Infrastructure

- Docker
- Docker Compose

---

# Architecture

Client

↓

FastAPI

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

---

# Layer Responsibilities

## API Layer

Responsible for

- Request parsing
- Validation
- Dependency injection
- Response serialization

Never

- Business logic
- SQL queries

---

## Service Layer

Responsible for

- Business rules
- Transactions
- Validation orchestration
- Repository coordination

Never

- HTTPException
- SQL queries
- FastAPI dependencies

---

## Repository Layer

Responsible for

- Database operations

Never

- Business logic
- HTTP logic

Repositories never commit transactions.

Services own transactions.

---

## Models

Use

Mapped[]

mapped_column()

SQLAlchemy 2.0 syntax only.

---

# Coding Standards

Always

- Strict typing
- Docstrings
- Async functions
- Dependency Injection
- Repository Pattern
- Service Layer

Never

- Any
- type: ignore
- TODO
- Placeholder implementations
- Duplicate logic

---

# Response Standard

Every endpoint returns

{
    "success": true,
    "message": "...",
    "data": {},
    "meta": {}
}

Errors return

{
    "success": false,
    "message": "...",
    "error": {},
    "meta": {}
}

Never return inconsistent response formats.

---

# Exception Rules

Services raise

ApplicationException

Derived exceptions

- ValidationException
- NotFoundException
- ConflictException
- UnauthorizedException
- ForbiddenException
- InternalServerException

Routers never raise business exceptions.

---

# Database Rules

Primary Keys

UUID

Soft Delete

Required

Audit Fields

Required

Created At

Updated At

Deleted At

Indexes

Create indexes for

- Email
- Merchant Code
- Slug
- Foreign Keys

---

# Multi-Tenancy

Merchant is the tenant.

Every future business entity belongs to a merchant.

Never violate tenant isolation.

---

# Current Project Status

Completed

✅ Project Foundation

✅ Configuration

✅ Logging

✅ Database Layer

✅ SQLAlchemy Async

✅ Repository Layer

✅ Merchant Domain Model

✅ Merchant Repository

✅ Merchant Service

✅ Alembic

✅ Initial Migration

✅ API Foundation

Pending

⬜ Merchant REST API

⬜ Merchant Users

⬜ Stores

⬜ Websites

⬜ Authentication Integration

⬜ Authorization

⬜ Audit Logs

⬜ Background Jobs

⬜ Production Readiness

---

# Quality Gates

Every phase must pass

uv run black .

uv run ruff check .

uv run mypy app

uv run python -m compileall app

uv run pytest

Never continue if quality gates fail.

---

# Development Workflow

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

Fix Issues

↓

Quality Gates

↓

Completion Report

↓

Commit

↓

Next Phase

Never skip steps.

---

# Git Rules

Current Branch

Feature branch only.

Never merge to main automatically.

Never rewrite history.

One commit per completed phase.

---

# Definition of Done

A phase is complete only when

- Scope completed
- Code reviewed
- No placeholders
- No TODOs
- No duplicated logic
- Quality gates pass
- Documentation updated

---

# AI Instructions

Every AI assistant MUST

Read this file first.

Preserve architecture.

Work on one roadmap phase only.

Never implement future roadmap phases.

Never refactor architecture without approval.

If an architectural issue is found

STOP

Report

Wait for approval

Only then proceed.

This document is the authoritative project context.
