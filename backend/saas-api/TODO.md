# TODO - PR-006 Merchant REST API

## Step 1: Inspect & Confirm Current State (done)
- Review existing merchant API/router composition and ensure merchants router is included. ✅
- Review current merchant schemas (only request exists) and shared response/pagination conventions. ✅
- Review merchant models/repository/service for missing CRUD + pagination/meta. ✅


## Step 2: Implement Schemas
- Add merchant response schemas (single + list item) and request/query schemas as needed.

## Step 3: Extend Repository Layer
- Implement list with pagination meta: filtering/search/sorting.
- Add total count method(s) consistent with repository style.
- Add soft delete behavior correctness checks (idempotent safe semantics).

## Step 4: Extend Service Layer
- Implement get/update/soft delete/list operations.
- Implement update uniqueness checks only for modified fields.
- Ensure deleted merchants are excluded; soft delete only.

## Step 5: Implement Merchant API Router (CRUD)
- Implement endpoints for create/get/list/update/soft-delete.
- Add request validation via Pydantic.
- Add OpenAPI metadata (summary/description/tags/response models).

## Step 6: Add Dependency/Query Support
- Ensure pagination/filter/search/sort query parameters are parsed safely.

## Step 7: Add Tests
- Repository tests: CRUD, soft delete, constraints behavior, list meta correctness, filter/search/sort.
- Service tests: business rules, duplicate prevention, not found.
- API tests: endpoint contracts, response envelope, validation errors, pagination/filter/search/sort.

## Step 8: Generate API Testing Guide
- Create docs/testing/merchant-api.md per required format.

## Step 9: Quality Gates
- Run: black, ruff, mypy, compileall, pytest.
- Fix all issues until passing.

## Step 10: Docs + Checkpoint
- Update .ai/SESSION.md, .ai/PROJECT_STATE.md, .ai/ROADMAP.md, .ai/CHANGELOG.md, .ai/DECISIONS.md.
- Create git commit: `Phase 6: Merchant REST API completed`.
- Produce PR-006 Completion Report and stop.
