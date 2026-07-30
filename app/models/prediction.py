from typing import Any, Dict, List

from models.base import BaseClass


class PredictionResult(BaseClass):
    def __init__(self, task_id: int, predictions: List[Dict[str, Any]]):
        super().__init__(task_id)
        self._predictions = predictions

    def show(self) -> List[Dict[str, Any]]:
        return self._predictions

    def count_objects(self) -> int:
        return len(self._predictions)

    def find_class(self, class_name: str) -> List[Dict[str, Any]]:
        return [obj for obj in self._predictions if obj["class"] == class_name]

    def get_info(self) -> Dict[str, Any]:
        info = super().get_info()
        info["predictions_count"] = self.count_objects()
        return info
