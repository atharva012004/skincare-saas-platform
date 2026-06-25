"""
Centralized application logging.

This module configures Structlog for the entire application and provides
a consistent logger interface across all modules.
"""

from __future__ import annotations

import logging
import sys
from typing import cast

import structlog
from structlog.typing import FilteringBoundLogger

_CONFIGURED = False


def configure_logging() -> None:
    """
    Configure application logging.

    Safe to call multiple times.
    """

    global _CONFIGURED

    if _CONFIGURED:
        return

    logging.basicConfig(
        level=logging.INFO,
        format="%(message)s",
        stream=sys.stdout,
    )

    structlog.configure(
        processors=[
            structlog.contextvars.merge_contextvars,
            structlog.processors.TimeStamper(fmt="iso", utc=True),
            structlog.stdlib.add_log_level,
            structlog.processors.StackInfoRenderer(),
            structlog.processors.format_exc_info,
            structlog.dev.ConsoleRenderer(),
        ],
        logger_factory=structlog.stdlib.LoggerFactory(),
        wrapper_class=structlog.stdlib.BoundLogger,
        cache_logger_on_first_use=True,
    )

    _CONFIGURED = True


def get_logger(name: str) -> FilteringBoundLogger:
    """
    Return a configured Structlog logger.
    """

    configure_logging()
    return cast(FilteringBoundLogger, structlog.get_logger(name))
