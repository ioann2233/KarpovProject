from datetime import datetime
from typing import Any, Dict, Optional

from models.base import BaseClass, TaskStatus
from models.ml_model import MLModel
from models.prediction import PredictionResult
from models.user import User


class MLTask(BaseClass):
    def __init__(self, task_id: int, user: User, model: MLModel, image_path: str):
        super().__init__(task_id)
        self.user = user
        self.model = model
        self.image_path = image_path
        self.status = TaskStatus.CREATED
        self.completed_at: Optional[datetime] = None
        self.result: Optional[PredictionResult] = None

    def start(self) -> Optional[PredictionResult]:
        if not self.user.subtract_balance(self.model.price):
            self.status = TaskStatus.NOT_ENOUGH_BALANCE
            return None

        # пока в разработке — inference через YOLO
        self.status = TaskStatus.FAILED
        return None

    def get_status(self) -> TaskStatus:
        return self.status

    def get_info(self) -> Dict[str, Any]:
        info = super().get_info()
        info.update({
            "user_id": self.user.id,
            "model_id": self.model.id,
            "status": self.status.value,
            "completed_at": self.completed_at,
        })
        return info
