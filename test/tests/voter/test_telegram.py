import requests

from vk_girl_dater.voter.telegram import Telegram


class TestTelegram:
    def test_get_updates(self):
        telegram = Telegram()
        response = telegram.get_updates()
        
        assert response.ok == True

    def test_send_message(self):
        telegram = Telegram()
        response = telegram.send_message("test", -4868817417)

        assert response.ok == True