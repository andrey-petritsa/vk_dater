import requests

from test.tests.vk_date_platform.settings import tg_bot_token


class Telegram:
    def get_updates(self):
        url = f"https://api.telegram.org/bot{tg_bot_token}/getUpdates"
        response = requests.get(url)
        print(response.json())
        return response
    
    def send_message(self, text, group_id):
        url = f"https://api.telegram.org/bot{tg_bot_token}/sendMessage"
        params = {
            "chat_id":group_id,
            "text":text
        }
        response = requests.post(url, params=params)
        return response


class TestTelegram:
    def test_get_updates(self):
        telegram = Telegram()
        response = telegram.get_updates()
        
        assert response.ok == True

    def test_send_message(self):
        telegram = Telegram()
        response = telegram.send_message("test", -4868817417)

        assert response.ok == True