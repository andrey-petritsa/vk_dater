from test.mock_datas.get_history_response import response


class StubVkDateApi:
    def get_history(self, chat_id):
        return response

class SpyVkDateApi:
    def send_message(self, message):
        self.last_sended_message = message