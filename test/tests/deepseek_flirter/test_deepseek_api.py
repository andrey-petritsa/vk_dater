import json
from test.tests.vk_date_platform.settings import deepseek_token, hand_mode_promt
from vk_girl_dater.flirter.deepseek_flirter.deepseek_api import DeepseekApi


def is_json(text):
    try:
        json.loads(text)
        return True
    except json.JSONDecodeError:
        return False


class TestDeepseekApi:
    def test_get_chat_response(self):
        api = DeepseekApi(deepseek_token)
        api.set_promt("Ты полезный помошник")
        messages = [
            {"role": "user", "content": "Привет!"},
            {"role": "assistant", "content": "Привет! Как дела?"},
            {"role": "user", "content": "Все хорошо, а у тебя?"}
        ]
        response = api.get_chat_response(messages)

        assert response.status_code == 200

    def test_get_chat_response_as_json(self):
        api = DeepseekApi(deepseek_token)
        api.set_promt(hand_mode_promt)
        messages = [
            {"role": "user", "content": "Привет!"},
            {"role": "assistant", "content": "Привет! Как дела?"},
            {"role": "user", "content": "Все хорошо, а у тебя?"}
        ]
        response = api.get_chat_response(messages)

        assert response.status_code == 200
        assert is_json(response.text) == True
