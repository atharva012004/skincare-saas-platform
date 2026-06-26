"""Merchant REST API.


This module provides thin HTTP endpoints for merchant management.
All business logic is delegated to :class:`app.services.merchant_service.MerchantService`.
"""

from __future__ import annotations

from fastapi import APIRouter, Depends, Path

from app.dependencies.services import get_merchant_service
from app.schemas.merchant import (
    MerchantCreateRequest,
    MerchantListQuery,
    MerchantResponse,
    MerchantUpdateRequest,
)
from app.services.merchant_service import MerchantService
from app.shared.response_factory import ResponseFactory

# Response wrapper schema is intentionally not used for typing here.
# FastAPI's response_model generics are not compatible with the service layer
# return types during dependency analysis.
from app.shared.responses import ApiResponse, ErrorResponse

router = APIRouter()


def _error_responses() -> dict[int | str, dict[str, object]]:  # type: ignore[type-arg]
    """Centralized OpenAPI error response metadata."""

    # The project uses centralized exception handling which produces a standardized
    # ErrorResponse schema.
    return {
        404: {
            "description": "Not found.",
            "model": ErrorResponse,
        },
        409: {
            "description": "Conflict.",
            "model": ErrorResponse,
        },
        422: {
            "description": "Validation error.",
            "model": ErrorResponse,
        },
        500: {
            "description": "Internal server error.",
            "model": ErrorResponse,
        },
    }


@router.post(
    "/merchants",
    summary="Create a merchant",
    description="Create a new merchant.",
    tags=["Merchants"],
    response_model=ApiResponse[MerchantResponse],
    responses=_error_responses(),
    status_code=201,
)
async def create_merchant(
    request: MerchantCreateRequest,
    service: MerchantService = Depends(get_merchant_service),
) -> ApiResponse[MerchantResponse]:
    """Create a merchant."""

    merchant = await service.create_merchant(request)

    return ResponseFactory.created(
        message="Merchant created successfully.",
        data=MerchantResponse.model_validate(merchant),
    )


@router.get(
    "/merchants",
    summary="List merchants",
    description="List active merchants. Pagination and filtering are applied by the service layer.",
    tags=["Merchants"],
    response_model=ApiResponse[list[MerchantResponse]],
    responses=_error_responses(),
)
async def list_merchants(
    query: MerchantListQuery = Depends(),
    service: MerchantService = Depends(get_merchant_service),
) -> ApiResponse[list[MerchantResponse]]:
    """List merchants."""

    merchants = await service.list_merchants(
        offset=(query.page - 1) * query.page_size,
        limit=query.page_size,
    )

    # Service layer returns a list without pagination metadata in current implementation.
    return ResponseFactory.success(
        message="Merchants fetched successfully.",
        data=[MerchantResponse.model_validate(m) for m in merchants],
    )


@router.get(
    "/merchants/{merchant_id}",
    summary="Get merchant",
    description="Fetch a merchant by its unique identifier.",
    tags=["Merchants"],
    response_model=ApiResponse[MerchantResponse],
    responses=_error_responses(),
)
async def get_merchant(
    merchant_id: str = Path(..., description="Merchant UUID."),
    service: MerchantService = Depends(get_merchant_service),
) -> ApiResponse[MerchantResponse]:
    """Get a merchant by id."""

    merchant = await service.get_merchant(merchant_id)  # type: ignore[arg-type]

    return ResponseFactory.success(
        message="Merchant fetched successfully.",
        data=MerchantResponse.model_validate(merchant),
    )


@router.patch(
    "/merchants/{merchant_id}",
    summary="Update merchant",
    description=(
        "Update a merchant. Note: `merchant_code` and `slug` are immutable and "
        "intentionally excluded from the update payload."
    ),
    tags=["Merchants"],
    response_model=ApiResponse[MerchantResponse],
    responses=_error_responses(),
)
async def update_merchant(
    merchant_id: str = Path(..., description="Merchant UUID."),
    request: MerchantUpdateRequest = None,  # type: ignore[assignment]
    service: MerchantService = Depends(get_merchant_service),
) -> ApiResponse[MerchantResponse]:
    """Patch an existing merchant."""

    merchant = await service.update_merchant(merchant_id, request)  # type: ignore[arg-type]

    return ResponseFactory.updated(
        message="Merchant updated successfully.",
        data=MerchantResponse.model_validate(merchant),
    )


@router.delete(
    "/merchants/{merchant_id}",
    summary="Delete merchant",
    description="Soft-delete a merchant.",
    tags=["Merchants"],
    response_model=ApiResponse[None],
    responses=_error_responses(),
)
async def delete_merchant(
    merchant_id: str = Path(..., description="Merchant UUID."),
    service: MerchantService = Depends(get_merchant_service),
) -> ApiResponse[None]:
    """Soft-delete a merchant."""

    await service.soft_delete_merchant(merchant_id)  # type: ignore[arg-type]

    return ResponseFactory.deleted(
        message="Merchant deleted successfully.",
    )
