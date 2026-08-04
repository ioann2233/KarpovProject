from extensions import db
from models.base import BaseModel


class Transaction(BaseModel):
    __tablename__ = "transactions"

    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False, index=True)
    amount = db.Column(db.Float, nullable=False)
    transaction_type = db.Column(db.String(50), nullable=False)
    task_id = db.Column(db.Integer, db.ForeignKey("ml_tasks.id"), nullable=True)

    user = db.relationship("User", back_populates="transactions")
    task = db.relationship("MLTask", back_populates="transactions")

    def get_info(self) -> dict:
        info = super().get_info()
        info.update({
            "user_id": self.user_id,
            "username": self.user.username if self.user else None,
            "type": self.transaction_type,
            "amount": self.amount,
            "task_id": self.task_id,
        })
        return info

    def __repr__(self) -> str:
        return (
            f"<Transaction id={self.id} type={self.transaction_type} "
            f"amount={self.amount} user_id={self.user_id}>"
        )
