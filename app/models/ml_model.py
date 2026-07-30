from typing import Any, Dict, List

from models.base import BaseClass

# from ultralytics import YOLO  # пока в разработке


class MLModel(BaseClass):
    def __init__(
        self,
        model_id: int,
        name: str,
        description: str,
        price: float,
        model_path: str = "yolov8n.pt",
    ):
        super().__init__(model_id)
        self.name = name
        self.description = description
        self.price = price
        self.model_path = model_path
        # self._model = YOLO(model_path)  # пока в разработке

    def predict(self, image_path: str) -> List[Dict[str, Any]]:
        raise NotImplementedError("ML inference пока в разработке")

    def get_info(self) -> Dict[str, Any]:
        info = super().get_info()
        info.update({
            "name": self.name,
            "description": self.description,
            "price": self.price,
        })
        return info
