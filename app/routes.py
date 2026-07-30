from flask import Blueprint, jsonify

bp = Blueprint("main", __name__)


@bp.get("/")
def index():
    return jsonify({"message": "Hello, World!"})


@bp.post("/register")
def register():
    return jsonify({"message": "Тут будет регистрация пользователя"})


@bp.get("/balance/<int:user_id>")
def balance(user_id):
    return jsonify({"message": f"Тут будет баланс пользователя {user_id}"})


@bp.post("/balance/top-up")
def top_up():
    return jsonify({"message": "Тут будет пополнение баланса"})


@bp.post("/tasks")
def create_task():
    return jsonify({"message": "Тут будет создание ML-задачи"})


@bp.get("/history/<int:user_id>")
def history(user_id):
    return jsonify({"message": f"Тут будет история операций пользователя {user_id}"})
