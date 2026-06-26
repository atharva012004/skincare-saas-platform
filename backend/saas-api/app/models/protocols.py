from __future__ import annotations

import uuid
from datetime import datetime
from typing import Protocol

from sqlalchemy.orm import Mapped


class EntityProtocol(Protocol):
    """
    Protocol implemented by all persistent entities.
    """

    id: Mapped[uuid.UUID]

    is_deleted: Mapped[bool]

    deleted_at: Mapped[datetime | None]
