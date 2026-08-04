from typing import List, Optional

from extensions import db
from models.ml_model import MLModel


def create_ml_model(
    name: str,
    description: str,
    price: float,
    model_path: str = "yolov8n.pt",
    is_active: bool = True,
) -> MLModel:
    model = MLModel(
        name=name,
        description=description,
        price=price,
        model_path=model_path,
        is_active=is_active,
    )
    db.session.add(model)
    db.session.commit()
    db.session.refresh(model)
    return model


def get_ml_model_by_id(model_id: int) -> Optional[MLModel]:
    return db.session.get(MLModel, model_id)


def get_active_models() -> List[MLModel]:
    return (
        db.session.query(MLModel)
        .filter_by(is_active=True)
        .order_by(MLModel.id)
        .all()
    )


def get_all_models() -> List[MLModel]:
    return db.session.query(MLModel).order_by(MLModel.id).all()
