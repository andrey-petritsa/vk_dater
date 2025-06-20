class Voter:
    def __init__(self, chat_api):
        self.chat_api = chat_api

    def send_message(self, text):
        self.chat_api.send_message(text)


class SpyTelegram:
    def send_message(self, text):
        self.last_sended_message = text

    def get_updates(self):
        return {
            "ok": True,
            "result": [
                {
                    "update_id": 899977158,
                    "message": {
                        "message_id": 17,
                        "from": {
                            "id": 1065236568,
                            "is_bot": False,
                            "first_name": "Андрей",
                            "last_name": "Петрица",
                            "username": "Acrosspaper",
                            "language_code": "ru",
                            "is_premium": True
                        },
                        "chat": {
                            "id": -4868817417,
                            "title": "Конор",
                            "type": "group",
                            "all_members_are_administrators": True,
                            "accepted_gift_types": {
                                "unlimited_gifts": False,
                                "limited_gifts": False,
                                "unique_gifts": False,
                                "premium_subscription": False
                            }
                        },
                        "date": 1750348648,
                        "text": "тест"
                    }
                }
            ]
        }

class TestVoter:
    def test_send_message(self):
        chat_api = SpyTelegram()
        voter = Voter(chat_api)
        voter.send_message('abracadabra')

    def test_get_messages(self):
        chat_api = SpyTelegram()
        voter = Voter(chat_api)
        messages = voter.get_messages(s)