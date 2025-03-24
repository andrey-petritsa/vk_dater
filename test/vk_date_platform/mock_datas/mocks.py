import test.vk_date_platform.mock_datas.get_chats_response as get_chats_response
import test.vk_date_platform.mock_datas.get_history_response as get_history_response
from test.web_utils import get_json_response


class StubVkDateApi:
    def get_history(self, chat_id):
        return get_json_response(get_history_response.response)

    def get_chats(self):
        return get_json_response(get_chats_response.response)


class SpyVkDateApi:
    def __init__(self):
        self.last_sended_message = ""

    def send_message(self, message):
        self.last_sended_message = message
