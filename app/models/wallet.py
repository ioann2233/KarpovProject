from typing import Any, Dict

from models.base import BaseClass


class Wallet(BaseClass):
    def __init__(self, wallet_id: int, owner_id: int, initial_balance: float = 0.0):
        super().__init__(wallet_id)
        self._owner_id = owner_id
        self._balance = initial_balance

    def add_balance(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Введенная сумма должна быть положительной")
        self._balance += amount

    def subtract_balance(self, amount: float) -> bool:
        if amount <= 0:
            raise ValueError("Введенная сумма должна быть положительной")
        if self._balance >= amount:
            self._balance -= amount
            return True
        return False

    def get_balance(self) -> float:
        return self._balance

    def get_info(self) -> Dict[str, Any]:
        info = super().get_info()
        info.update({"owner_id": self._owner_id, "balance": self._balance})
        return info
