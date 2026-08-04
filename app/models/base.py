from datetime import datetime
from enum import Enum

from extensions import db


class TaskStatus(str, Enum):
    CREATED = "created"
    RUNNING = "running"
    COMPLETED = "completed"
    NOT_ENOUGH_BALANCE = "not enough balance"
    FAILED = "failed"


class BaseModel(db.Model):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    def get_info(self) -> dict:
        return {"id": self.id, "created_at": self.created_at}
