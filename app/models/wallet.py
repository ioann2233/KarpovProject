from extensions import db
from models.base import BaseModel


class Wallet(BaseModel):
    __tablename__ = "wallets"

    owner_id = db.Column(db.Integer, db.ForeignKey("users.id"), unique=True, nullable=False)
    balance = db.Column(db.Float, default=0.0, nullable=False)

    owner = db.relationship("User", back_populates="wallet", uselist=False)

    def add_balance(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Введенная сумма должна быть положительной")
        self.balance += amount

    def subtract_balance(self, amount: float) -> bool:
        if amount <= 0:
            raise ValueError("Введенная сумма должна быть положительной")
        if self.balance >= amount:
            self.balance -= amount
            return True
        return False

    def get_balance(self) -> float:
        return self.balance

    def get_info(self) -> dict:
        info = super().get_info()
        info.update({"owner_id": self.owner_id, "balance": self.balance})
        return info

    def __repr__(self) -> str:
        return f"<Wallet id={self.id} owner_id={self.owner_id} balance={self.balance}>"
