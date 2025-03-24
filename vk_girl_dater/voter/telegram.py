import requests

from test.tests.vk_date_platform.settings import tg_bot_token


class Telegram:
    def __init__(self):
        self.last_response = None

    def get_updates(self, last_update_id=None):
        url = f"https://api.telegram.org/bot{tg_bot_token}/getUpdates"
        if last_update_id:
            url += f"?offset={last_update_id}"
        response = requests.get(url)
        self.last_response = response
        return response.json()

    def send_message(self, text, group_id):
        url = f"https://api.telegram.org/bot{tg_bot_token}/sendMessage"
        params = {
            "chat_id":group_id,
            "text":text
        }
        response = requests.post(url, params=params)
        self.last_response = response
        return response.json()