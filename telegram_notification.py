import os
import time
import requests

telegram_token = os.environ['TELEGRAM_TOKEN']
chat_id = os.environ['TELEGRAM_CHAT_ID']

def send_telegram_message(text):
    url = f'https://api.telegram.org/bot{telegram_token}/sendMessage'
    data = {
        'chat_id': chat_id,
        'text': text
    }
    response = requests.post(url, data=data)
    if response.status_code != 200:
        print(f'Failed to send Telegram message. Error: {response.text}')

while True:
    send_telegram_message("안녕")
    time.sleep(60)  # 1분마다 실행
