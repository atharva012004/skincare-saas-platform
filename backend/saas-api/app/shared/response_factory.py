"""
Factory for building standard API responses.
"""

from __future__ import annotations

from typing import TypeVar

from app.shared.responses import (
    ApiResponse,
    ErrorDetail,
    ErrorInfo,
    ErrorResponse,
    PaginationMeta,
    ResponseMeta,
)

T = TypeVar("T")


class ResponseFactory:
    """
    Factory responsible for creating API responses.
    """

    @staticmethod
    def success(
        *,
        message: str,
        data: T | None = None,
        request_id: str | None = None,
    ) -> ApiResponse[T]:
        return ApiResponse(
            message=message,
            data=data,
            meta=ResponseMeta(
                request_id=request_id,
            ),
        )

    @staticmethod
    def created(
        *,
        message: str,
        data: T | None = None,
        request_id: str | None = None,
    ) -> ApiResponse[T]:
        return ResponseFactory.success(
            message=message,
            data=data,
            request_id=request_id,
        )

    @staticmethod
    def updated(
        *,
        message: str,
        data: T | None = None,
        request_id: str | None = None,
    ) -> ApiResponse[T]:
        return ResponseFactory.success(
            message=message,
            data=data,
            request_id=request_id,
        )

    @staticmethod
    def deleted(
        *,
        message: str,
        request_id: str | None = None,
    ) -> ApiResponse[None]:
        return ApiResponse(
            message=message,
            meta=ResponseMeta(
                request_id=request_id,
            ),
        )

    @staticmethod
    def paginated(
        *,
        message: str,
        data: T,
        page: int,
        page_size: int,
        total_items: int,
        total_pages: int,
        request_id: str | None = None,
    ) -> ApiResponse[T]:
        return ApiResponse(
            message=message,
            data=data,
            meta=ResponseMeta(
                request_id=request_id,
                pagination=PaginationMeta(
                    page=page,
                    page_size=page_size,
                    total_items=total_items,
                    total_pages=total_pages,
                ),
            ),
        )

    @staticmethod
    def error(
        *,
        message: str,
        code: str,
        details: list[ErrorDetail] | None = None,
        request_id: str | None = None,
    ) -> ErrorResponse:
        return ErrorResponse(
            message=message,
            error=ErrorInfo(
                code=code,
                details=details or [],
            ),
            meta=ResponseMeta(
                request_id=request_id,
            ),
        )
