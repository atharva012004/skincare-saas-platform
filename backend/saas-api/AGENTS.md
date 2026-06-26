# AGENTS.md

## Enterprise AI Engineering Instructions

This repository is an enterprise-grade multi-tenant SaaS backend.

Every AI assistant (Blackbox, Codex, Claude Code, Cursor, Gemini, ChatGPT, or future coding agents) MUST follow this document before making any modifications.

The repository is the single source of truth.

The chat is NEVER the source of truth.

---

# Startup Procedure (Mandatory)

Every new AI session MUST execute the following steps before writing code.

## Step 1

Read

.ai/AI_CONTEXT.md

.ai/PROJECT_STATE.md

.ai/SESSION.md

.ai/ROADMAP.md

.ai/ARCHITECTURE.md

.ai/CODING_STANDARDS.md

.ai/API_SPEC.md

.ai/DATABASE_SPEC.md

.ai/DEVELOPMENT_WORKFLOW.md

.ai/DECISIONS.md

.ai/CHANGELOG.md

---

## Step 2

Inspect repository

Run

git status

git branch

git log --oneline -10

Compare repository state with SESSION.md.

If mismatch exists

Repository always wins.

Update SESSION.md.

---

## Step 3

Determine

Current Phase

Current Feature

Remaining Tasks

Current Branch

Blocking Issues

Quality Status

---

# Development Rules

Implement ONE roadmap phase only.

Never skip phases.

Never implement future roadmap work.

Never modify unrelated modules.

---

# Architecture Rules

Preserve

Clean Architecture

Repository Pattern

Service Layer

Dependency Injection

Async SQLAlchemy

Strict Typing

Never move business logic into routers.

Never execute SQL inside services.

Never commit inside repositories.

---

# Code Quality Rules

Always

Use type hints

Use async

Use docstrings

Use ResponseFactory

Use ApplicationException

Never

Use Any

Use type: ignore

Leave TODO comments

Leave placeholder implementations

Duplicate business logic

---

# Self Review

Before running tests

Review

Architecture

Typing

Imports

Performance

Security

Validation

Naming

Documentation

Fix every issue before continuing.

---

# Quality Gates

Run until ALL PASS

uv run black .

uv run ruff check .

uv run mypy app

uv run python -m compileall app

uv run pytest

If any command fails

Fix

Run again

Repeat until everything passes.

Never stop with failing quality gates.

---

# API Documentation

Whenever API endpoints are added

Automatically generate

docs/testing/<module>-api.md

Each document must include

Endpoints

Headers

Authentication

Request Body

Query Parameters

Path Parameters

Response

Validation Errors

Conflict Errors

Not Found Errors

Swagger Testing

Postman Testing

Database Verification

---

# Testing

Every feature requires

Repository Tests

Service Tests

API Tests

Integration Tests

Regression Tests

Never ship untested code.

---

# Documentation Updates

Whenever work is completed update

.ai/SESSION.md

.ai/PROJECT_STATE.md

.ai/CHANGELOG.md

.ai/DECISIONS.md

Never skip documentation.

---

# Completion Report

After every roadmap phase report

Summary

Files Changed

Architecture Impact

Endpoints Added

Tests Added

Swagger Testing Guide

Postman Testing Guide

Database Changes

Quality Gate Results

Known Risks

Next Recommended Phase

---

# Stop Conditions

Stop immediately if

Phase complete

Architecture change required

Scope expansion detected

Ambiguous requirements found

Security issue discovered

Produce report

Wait for approval

Never continue automatically.

---

# Definition of Done

A roadmap phase is complete only when

Implementation finished

Quality gates pass

Tests pass

Documentation updated

Testing guide generated

Completion report generated

No architecture violations remain

---

# Project Philosophy

Correctness over speed.

Maintainability over cleverness.

Scalability over shortcuts.

Security over convenience.

Repository is the source of truth.

Always preserve enterprise architecture.
