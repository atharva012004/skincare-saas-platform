"""
Global exception handlers for the Skincare SaaS Platform.
"""

from __future__ import annotations

import logging

from fastapi import FastAPI, HTTPException, Request, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from sqlalchemy.exc import SQLAlchemyError

from app.shared.constants import ErrorCodes
from app.shared.exceptions import BaseAPIException
from app.shared.response_factory import ResponseFactory
from app.shared.responses import ErrorDetail

logger = logging.getLogger(__name__)


def _request_id(request: Request) -> str | None:
    """
    Return the request ID attached by middleware, when present.
    """

    return getattr(request.state, "request_id", None)


def _http_error_code(status_code: int) -> str:
    """
    Map framework HTTP errors onto the platform error code vocabulary.
    """

    if status_code == status.HTTP_401_UNAUTHORIZED:
        return ErrorCodes.AUTHENTICATION_ERROR
    if status_code == status.HTTP_403_FORBIDDEN:
        return ErrorCodes.AUTHORIZATION_ERROR
    if status_code == status.HTTP_404_NOT_FOUND:
        return ErrorCodes.NOT_FOUND
    if status_code == status.HTTP_409_CONFLICT:
        return ErrorCodes.CONFLICT
    if status_code == status.HTTP_422_UNPROCESSABLE_ENTITY:
        return ErrorCodes.VALIDATION_ERROR
    if status_code >= status.HTTP_500_INTERNAL_SERVER_ERROR:
        return ErrorCodes.INTERNAL_ERROR
    return ErrorCodes.VALIDATION_ERROR


def register_exception_handlers(app: FastAPI) -> None:
    """
    Register all global exception handlers.
    """

    @app.exception_handler(BaseAPIException)
    async def handle_api_exception(
        request: Request,
        exc: BaseAPIException,
    ) -> JSONResponse:
        """
        Handle known application exceptions.
        """

        logger.warning(
            "%s %s -> %s",
            request.method,
            request.url.path,
            exc.error_code,
        )

        response = ResponseFactory.error(
            message=exc.message,
            code=exc.error_code,
            details=exc.details,
            request_id=_request_id(request),
        )

        return JSONResponse(
            status_code=exc.status_code,
            content=response.model_dump(mode="json"),
        )

    @app.exception_handler(RequestValidationError)
    async def handle_validation_error(
        request: Request,
        exc: RequestValidationError,
    ) -> JSONResponse:
        """
        Handle FastAPI request validation errors.
        """

        details = [
            ErrorDetail(
                field=".".join(map(str, error["loc"])),
                message=error["msg"],
            )
            for error in exc.errors()
        ]

        logger.warning(
            "%s %s -> validation_error",
            request.method,
            request.url.path,
        )

        response = ResponseFactory.error(
            message="Request validation failed.",
            code=ErrorCodes.VALIDATION_ERROR,
            details=details,
            request_id=_request_id(request),
        )

        return JSONResponse(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            content=response.model_dump(mode="json"),
        )

    @app.exception_handler(HTTPException)
    async def handle_http_exception(
        request: Request,
        exc: HTTPException,
    ) -> JSONResponse:
        """
        Handle FastAPI HTTP exceptions.
        """

        logger.warning(
            "%s %s -> http_exception (%s)",
            request.method,
            request.url.path,
            exc.status_code,
        )

        response = ResponseFactory.error(
            message=str(exc.detail),
            code=_http_error_code(exc.status_code),
            request_id=_request_id(request),
        )

        return JSONResponse(
            status_code=exc.status_code,
            content=response.model_dump(mode="json"),
            headers=exc.headers,
        )

    @app.exception_handler(SQLAlchemyError)
    async def handle_database_exception(
        request: Request,
        exc: SQLAlchemyError,
    ) -> JSONResponse:
        """
        Handle database-layer failures.
        """

        logger.exception(
            "Database exception on %s %s",
            request.method,
            request.url.path,
            exc_info=exc,
        )

        response = ResponseFactory.error(
            message="A database error occurred.",
            code=ErrorCodes.DATABASE_ERROR,
            request_id=_request_id(request),
        )

        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content=response.model_dump(mode="json"),
        )

    @app.exception_handler(Exception)
    async def handle_unexpected_exception(
        request: Request,
        exc: Exception,
    ) -> JSONResponse:
        """
        Catch any unexpected exception.
        """

        logger.exception(
            "Unhandled exception on %s %s",
            request.method,
            request.url.path,
            exc_info=exc,
        )

        response = ResponseFactory.error(
            message="An unexpected error occurred.",
            code=ErrorCodes.INTERNAL_ERROR,
            request_id=_request_id(request),
        )

        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content=response.model_dump(mode="json"),
        )
