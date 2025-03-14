from test.mock_datas.get_history_response import response as get_history_response
from test.mock_datas.get_chats_response import response as get_chats_response


class StubVkDateApi:
    def get_history(self, chat_id):
        return get_history_response

    def get_chats(self):
        return get_chats_response


class SpyVkDateApi:
    def __init__(self):
        self.last_sended_message = ""

    def send_message(self, message):
        self.last_sended_message = message
