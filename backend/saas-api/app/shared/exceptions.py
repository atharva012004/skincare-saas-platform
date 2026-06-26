"""
Enterprise exception hierarchy.
"""

from __future__ import annotations

from http import HTTPStatus

from app.shared.constants import ErrorCodes
from app.shared.responses import ErrorDetail


class BaseAPIException(Exception):
    """Base API exception."""

    status_code: int = HTTPStatus.INTERNAL_SERVER_ERROR
    error_code: str = ErrorCodes.INTERNAL_ERROR

    def __init__(
        self,
        message: str,
        *,
        details: list[ErrorDetail] | None = None,
    ) -> None:
        self.message = message
        self.details = details or []
        super().__init__(message)


class ValidationException(BaseAPIException):
    status_code = HTTPStatus.BAD_REQUEST
    error_code = ErrorCodes.VALIDATION_ERROR


class AuthenticationException(BaseAPIException):
    status_code = HTTPStatus.UNAUTHORIZED
    error_code = ErrorCodes.AUTHENTICATION_ERROR


class AuthorizationException(BaseAPIException):
    status_code = HTTPStatus.FORBIDDEN
    error_code = ErrorCodes.AUTHORIZATION_ERROR


class NotFoundException(BaseAPIException):
    status_code = HTTPStatus.NOT_FOUND
    error_code = ErrorCodes.NOT_FOUND


class ConflictException(BaseAPIException):
    status_code = HTTPStatus.CONFLICT
    error_code = ErrorCodes.CONFLICT


class BusinessException(BaseAPIException):
    status_code = HTTPStatus.UNPROCESSABLE_ENTITY
    error_code = ErrorCodes.BUSINESS_ERROR


class DatabaseException(BaseAPIException):
    status_code = HTTPStatus.INTERNAL_SERVER_ERROR
    error_code = ErrorCodes.DATABASE_ERROR
