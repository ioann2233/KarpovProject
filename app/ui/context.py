from functools import lru_cache

from main import create_app


@lru_cache
def get_flask_app():
    return create_app()


def run_with_context(func, *args, **kwargs):
    app = get_flask_app()
    with app.app_context():
        return func(*args, **kwargs)
