from extensions import db


def init_db(app, drop_all: bool = False) -> None:
    with app.app_context():
        import models  # noqa: F401

        if drop_all:
            db.drop_all()
        db.create_all()
