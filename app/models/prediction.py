from extensions import db
from models.base import BaseModel


class PredictionResult(BaseModel):
    __tablename__ = "prediction_results"

    task_id = db.Column(db.Integer, db.ForeignKey("ml_tasks.id"), unique=True, nullable=False)
    predictions = db.Column(db.JSON, nullable=False, default=list)

    task = db.relationship("MLTask", back_populates="result", uselist=False)

    def show(self) -> list:
        return self.predictions or []

    def count_objects(self) -> int:
        return len(self.show())

    def find_class(self, class_name: str) -> list:
        return [obj for obj in self.show() if obj.get("class") == class_name]

    def get_info(self) -> dict:
        info = super().get_info()
        info.update({
            "task_id": self.task_id,
            "predictions_count": self.count_objects(),
        })
        return info

    def __repr__(self) -> str:
        return f"<PredictionResult id={self.id} task_id={self.task_id}>"
