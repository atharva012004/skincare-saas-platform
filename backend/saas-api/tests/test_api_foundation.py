from __future__ import annotations

import os
from typing import Annotated, Any

os.environ.setdefault("DATABASE_URL", "postgresql+asyncpg://user:pass@localhost/test")
os.environ.setdefault("AUTH_SERVICE_URL", "http://localhost:3001")
os.environ.setdefault("JWT_SECRET", "test-secret")
os.environ["DEBUG"] = "false"

import pytest
from fastapi import Depends, FastAPI, HTTPException
from fastapi.testclient import TestClient
from sqlalchemy.exc import SQLAlchemyError

from app.api.v1 import health as health_module
from app.dependencies.config import get_app_settings
from app.dependencies.repositories import get_merchant_repository
from app.main import create_app
from app.middleware.exception_handler import register_exception_handlers
from app.shared.exceptions import ConflictException

SettingsDependency = Annotated[Any, Depends(get_app_settings)]
RepositoryDependency = Annotated[Any, Depends(get_merchant_repository)]


def test_openapi_registers_health_endpoint() -> None:
    app = create_app()

    schema = app.openapi()
    tag_names = {tag["name"] for tag in schema["tags"]}

    assert "/api/v1/health" in schema["paths"]
    assert schema["info"]["title"]
    assert "Health" in tag_names


def test_health_reports_healthy_database(monkeypatch: pytest.MonkeyPatch) -> None:
    async def healthy_database() -> bool:
        return True

    monkeypatch.setattr(health_module, "check_database_connection", healthy_database)

    response = TestClient(create_app()).get("/api/v1/health")

    assert response.status_code == 200
    assert response.json()["message"] == "Platform healthy"
    assert response.json()["data"]["database"] == "healthy"


def test_health_reports_degraded_database(monkeypatch: pytest.MonkeyPatch) -> None:
    async def unhealthy_database() -> bool:
        return False

    monkeypatch.setattr(health_module, "check_database_connection", unhealthy_database)

    response = TestClient(create_app()).get("/api/v1/health")

    assert response.status_code == 200
    assert response.json()["message"] == "Platform degraded"
    assert response.json()["data"]["database"] == "unhealthy"


def test_application_exception_handler_uses_standard_error_shape() -> None:
    app = FastAPI()
    register_exception_handlers(app)

    @app.get("/conflict")
    async def conflict() -> None:
        raise ConflictException("Already exists.")

    response = TestClient(app).get("/conflict")

    assert response.status_code == 409
    assert response.json()["success"] is False
    assert response.json()["error"]["code"] == "conflict"


def test_http_exception_handler_maps_not_found_code() -> None:
    app = FastAPI()
    register_exception_handlers(app)

    @app.get("/missing")
    async def missing() -> None:
        raise HTTPException(status_code=404, detail="Missing.")

    response = TestClient(app).get("/missing")

    assert response.status_code == 404
    assert response.json()["error"]["code"] == "not_found"


def test_database_exception_handler_uses_database_error_code() -> None:
    app = FastAPI()
    register_exception_handlers(app)

    @app.get("/database")
    async def database_error() -> None:
        raise SQLAlchemyError("Connection failed.")

    response = TestClient(app).get("/database")

    assert response.status_code == 500
    assert response.json()["error"]["code"] == "database_error"


def test_dependency_providers_are_available() -> None:
    app = FastAPI()

    app.dependency_overrides[get_merchant_repository] = lambda: "repository"

    @app.get("/settings")
    async def settings_endpoint(
        settings: SettingsDependency,
    ) -> dict[str, str]:
        return {"name": settings.APP_NAME}

    @app.get("/repository")
    async def repository_endpoint(
        repository: RepositoryDependency,
    ) -> dict[str, str]:
        return {"repository": repository}

    assert TestClient(app).get("/settings").json()["name"]
    assert TestClient(app).get("/repository").json() == {"repository": "repository"}
