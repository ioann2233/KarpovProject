import os

import requests

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "")
API_URL = f"https://api.telegram.org/bot{BOT_TOKEN}"


def send_message(chat_id: int, text: str) -> None:
    requests.post(f"{API_URL}/sendMessage", json={"chat_id": chat_id, "text": text})


def handle_update(update: dict):
    message = update.get("message", {})
    chat_id = message.get("chat", {}).get("id")
    text = message.get("text", "")

    if text == "/start":
        send_message(chat_id, "Добро пожаловать в ML-сервис.")
    else:
        send_message(chat_id, f"Получено: {text}")
