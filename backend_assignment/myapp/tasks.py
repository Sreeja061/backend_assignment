
from celery import shared_task
import time

@shared_task
def send_telegram_message(message):
    print(f"Sending Telegram message: {message}")
    time.sleep(3)  # simulate delay
    return f"Message '{message}' sent to Telegram!"

