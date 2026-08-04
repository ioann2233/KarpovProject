from typing import Optional

from extensions import db
from models.transaction import Transaction
from service.testing.user import get_user_by_id


def get_balance(user_id: int) -> float:
    user = get_user_by_id(user_id)
    if not user:
        raise ValueError(f"Пользователь id={user_id} не найден")
    return user.get_balance()


def top_up_balance(user_id: int, amount: float) -> Transaction:
    user = get_user_by_id(user_id)
    if not user:
        raise ValueError(f"Пользователь id={user_id} не найден")

    user.add_balance(amount)
    transaction = Transaction(
        user_id=user.id,
        amount=amount,
        transaction_type="top_up",
    )
    db.session.add(transaction)
    db.session.commit()
    db.session.refresh(transaction)
    return transaction


def spend_credits(
    user_id: int,
    amount: float,
    task_id: Optional[int] = None,
) -> Transaction:
    user = get_user_by_id(user_id)
    if not user:
        raise ValueError(f"Пользователь id={user_id} не найден")

    if not user.subtract_balance(amount):
        raise ValueError("Недостаточно средств на балансе")

    transaction = Transaction(
        user_id=user.id,
        amount=amount,
        transaction_type="spend",
        task_id=task_id,
    )
    db.session.add(transaction)
    db.session.commit()
    db.session.refresh(transaction)
    return transaction
