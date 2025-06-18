import requests

class TelegramBot:
    def __init__(self, token, user_id):
        self.token = token
        self.user_id = user_id

    def send_message(self, message):
        url = f"https://api.telegram.org/bot{self.token}/sendMessage"
        payload = {
            "chat_id": self.user_id,
            "text": message
        }
        response = requests.post(url, data=payload)
        print("Telegram Antwort:", response.status_code, response.text)
