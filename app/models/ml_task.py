from datetime import datetime

from extensions import db
from models.base import BaseModel, TaskStatus


class MLTask(BaseModel):
    __tablename__ = "ml_tasks"

    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False, index=True)
    model_id = db.Column(db.Integer, db.ForeignKey("ml_models.id"), nullable=False)
    image_path = db.Column(db.String(500), nullable=False)
    status = db.Column(db.String(50), default=TaskStatus.CREATED.value, nullable=False)
    completed_at = db.Column(db.DateTime, nullable=True)

    user = db.relationship("User", back_populates="tasks")
    model = db.relationship("MLModel", back_populates="tasks")
    result = db.relationship(
        "PredictionResult",
        back_populates="task",
        uselist=False,
        cascade="all, delete-orphan",
    )
    transactions = db.relationship("Transaction", back_populates="task", lazy="select")

    def start(self):
        if not self.user.subtract_balance(self.model.price):
            self.status = TaskStatus.NOT_ENOUGH_BALANCE.value
            return None

        self.status = TaskStatus.FAILED.value
        self.completed_at = datetime.utcnow()
        return None

    def get_status(self) -> TaskStatus:
        try:
            return TaskStatus(self.status)
        except ValueError:
            return TaskStatus.FAILED

    def get_info(self) -> dict:
        info = super().get_info()
        info.update({
            "user_id": self.user_id,
            "model_id": self.model_id,
            "image_path": self.image_path,
            "status": self.status,
            "completed_at": self.completed_at,
        })
        return info

    def __repr__(self) -> str:
        return f"<MLTask id={self.id} status={self.status} user_id={self.user_id}>"
