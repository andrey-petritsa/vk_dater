import requests

from test.vk_date_platform.settings import promt


class DeepseekApi:
    def __init__(self, token):
        self.__token = token
        self.promt = promt

    def set_promt(self, promt):
        self.promt = promt

    def get_chat_response(self, messages):
        url = "https://api.deepseek.com/chat/completions"
        headers = {"Content-Type": "application/json","Authorization": f"Bearer {self.__token}"}
        promt_message = {"role":"system", "content":f"{self.promt}"}
        messages = [promt_message, *messages]

        data = {
            "model": "deepseek-chat",
            "messages":messages,
            "stream": False
        }

        response = requests.post(url, json=data, headers=headers)
        if not response.ok:
            raise Exception(response.text)

        return response