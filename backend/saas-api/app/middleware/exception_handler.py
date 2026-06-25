"""
Global exception handlers for the Skincare SaaS Platform.
"""

from __future__ import annotations

import logging

from fastapi import FastAPI, HTTPException, Request, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from app.shared.constants import ErrorCodes
from app.shared.exceptions import BaseAPIException
from app.shared.response_factory import ResponseFactory
from app.shared.responses import ErrorDetail

logger = logging.getLogger(__name__)


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
            request_id=getattr(request.state, "request_id", None),
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
            request_id=getattr(request.state, "request_id", None),
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
            code=ErrorCodes.INTERNAL_ERROR,
            request_id=getattr(request.state, "request_id", None),
        )

        return JSONResponse(
            status_code=exc.status_code,
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
            request_id=getattr(request.state, "request_id", None),
        )

        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content=response.model_dump(mode="json"),
        )
