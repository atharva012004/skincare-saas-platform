"""
Backward compatible logging module.
"""

from app.core.observability import (
    configure_logging,
    get_logger,
)

__all__ = [
    "configure_logging",
    "get_logger",
]