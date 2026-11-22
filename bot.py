# akkord-kz-bot.
Telegram-бот для поиска популярных казахстанских песен и аккордов с автоматической публикацией в канале @anderakkord.

import os
import requests

TOKEN = os.environ["BOT_TOKEN"]
CHANNEL = "@anderakkord"

def publish(text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

    response = requests.post(
        url,
        data={
            "chat_id": CHANNEL,
            "text": text
        },
        timeout=20
    )

    response.raise_for_status()
    print("Публикация успешна!")

if __name__ == "__main__":
    publish(
        "🎸 Akkord KZ\n\n"
        "Бот подключён к каналу!\n"
        "Скоро здесь появятся аккорды казахстанских песен."
    )
  
