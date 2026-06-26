"""
Alembic environment configuration.

Supports asynchronous SQLAlchemy migrations.
"""

from __future__ import annotations

import asyncio
from logging.config import fileConfig

from sqlalchemy.engine import Connection

import app.models  # noqa: F401
from alembic import context
from app.core.config import settings
from app.db.base import Base
from app.db.engine import engine

config = context.config

config.set_main_option(
    "sqlalchemy.url",
    settings.DATABASE_URL,
)

if config.config_file_name is not None:
    fileConfig(config.config_file_name)

target_metadata = Base.metadata


def run_migrations_offline() -> None:
    """
    Run migrations in offline mode.
    """

    context.configure(
        url=settings.DATABASE_URL,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={
            "paramstyle": "named",
        },
        compare_type=True,
        compare_server_default=True,
    )

    with context.begin_transaction():
        context.run_migrations()


def do_run_migrations(
    connection: Connection,
) -> None:
    """
    Execute migrations using an active SQLAlchemy connection.
    """

    context.configure(
        connection=connection,
        target_metadata=target_metadata,
        compare_type=True,
        compare_server_default=True,
    )

    with context.begin_transaction():
        context.run_migrations()


async def run_migrations_online() -> None:
    """
    Run migrations in online mode.
    """

    async with engine.connect() as connection:
        await connection.run_sync(do_run_migrations)


if context.is_offline_mode():
    run_migrations_offline()
else:
    asyncio.run(run_migrations_online())
