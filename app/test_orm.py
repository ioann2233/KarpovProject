from main import create_app
from seed import seed_database
from service.testing.ml_model import get_active_models
from service.testing.transaction import get_user_transactions
from service.testing.user import create_user, get_all_users, get_user_by_username
from service.testing.wallet import get_balance, spend_credits, top_up_balance


def run_tests() -> None:
    app = create_app()
    seed_database(drop_all=True)

    with app.app_context():
        print("\n" + "=" * 60)
        print("ТЕСТ 1. Создание нового пользователя")
        print("=" * 60)
        user = create_user(
            username="test_user",
            password="testpass",
            role="user",
            initial_balance=0.0,
        )
        print(f"Создан: {user.get_info()}")

        print("\n" + "=" * 60)
        print("ТЕСТ 2. Пополнение баланса")
        print("=" * 60)
        tx_top_up = top_up_balance(user.id, 200.0)
        print(f"Транзакция: {tx_top_up.get_info()}")
        print(f"Баланс после пополнения: {get_balance(user.id)}")

        print("\n" + "=" * 60)
        print("ТЕСТ 3. Списание кредитов")
        print("=" * 60)
        models = get_active_models()
        assert models, "Нет активных моделей после seed"
        model = models[0]
        print(f"Модель для списания: {model.get_info()}")

        tx_spend = spend_credits(user.id, model.price)
        print(f"Транзакция: {tx_spend.get_info()}")
        print(f"Баланс после списания: {get_balance(user.id)}")

        print("\n" + "=" * 60)
        print("ТЕСТ 4. История транзакций")
        print("=" * 60)
        history = get_user_transactions(user.id)
        for item in history:
            print(f"  - {item.get_info()}")

        print("\n" + "=" * 60)
        print("ТЕСТ 5. Недостаточно средств")
        print("=" * 60)
        try:
            spend_credits(user.id, 1_000_000)
            print("ОШИБКА: исключение не было выброшено")
        except ValueError as exc:
            print(f"Ожидаемая ошибка: {exc}")

        print("\n" + "=" * 60)
        print("ТЕСТ 6. Демо-пользователи и модели из seed")
        print("=" * 60)
        for u in get_all_users():
            print(f"  user: {u.get_info()}")
        for m in get_active_models():
            print(f"  model: {m.get_info()}")

        demo = get_user_by_username("demo_user")
        admin = get_user_by_username("demo_admin")
        assert demo is not None and demo.role == "user"
        assert admin is not None and admin.role == "admin"
        assert get_balance(demo.id) == 150.0
        assert get_balance(user.id) == 200.0 - model.price

        print("\nВсе тесты пройдены успешно.")


if __name__ == "__main__":
    run_tests()
