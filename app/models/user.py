from typing import Any, Dict, Optional

from models.base import BaseClass
from models.wallet import Wallet


class User(BaseClass):
    def __init__(
        self,
        user_id: int,
        username: str,
        password: str,
        role: str = "user",
        wallet: Optional[Wallet] = None,
    ):
        super().__init__(user_id)
        self.username = username
        self._password = password
        self.role = role
        self.wallet = wallet if wallet else Wallet(wallet_id=user_id, owner_id=user_id)

    def get_balance(self) -> float:
        return self.wallet.get_balance()

    def add_balance(self, amount: float) -> None:
        self.wallet.add_balance(amount)

    def subtract_balance(self, amount: float) -> bool:
        return self.wallet.subtract_balance(amount)

    def get_info(self) -> Dict[str, Any]:
        info = super().get_info()
        info.update({
            "username": self.username,
            "role": self.role,
            "balance": self.get_balance(),
        })
        return info
