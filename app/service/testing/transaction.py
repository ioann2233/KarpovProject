from typing import List

from extensions import db
from models.transaction import Transaction


def get_user_transactions(user_id: int) -> List[Transaction]:
    return (
        db.session.query(Transaction)
        .filter_by(user_id=user_id)
        .order_by(Transaction.created_at.desc(), Transaction.id.desc())
        .all()
    )
