from typing import Any, Dict, Optional

from models.base import BaseClass
from models.user import User


class Transaction(BaseClass):
    def __init__(
        self,
        transaction_id: int,
        user: User,
        amount: float,
        transaction_type: str,
        task_id: Optional[int] = None,
    ):
        super().__init__(transaction_id)
        self.user = user
        self.task_id = task_id
        self.amount = amount
        self.transaction_type = transaction_type

    def get_info(self) -> Dict[str, Any]:
        info = super().get_info()
        info.update({
            "user": self.user.username,
            "type": self.transaction_type,
            "amount": self.amount,
            "task_id": self.task_id,
        })
        return info
