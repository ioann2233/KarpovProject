from datetime import datetime
from enum import Enum
from typing import Any, Dict


class TaskStatus(Enum):
    CREATED = "created"
    RUNNING = "running"
    COMPLETED = "completed"
    NOT_ENOUGH_BALANCE = "not enough balance"
    FAILED = "failed"


class BaseClass:
    def __init__(self, entity_id: int):
        self._id = entity_id
        self.created_at = datetime.now()

    @property
    def id(self) -> int:
        return self._id

    def get_info(self) -> Dict[str, Any]:
        return {"id": self._id, "created_at": self.created_at}
