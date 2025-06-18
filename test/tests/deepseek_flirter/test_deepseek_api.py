import json
from test.tests.vk_date_platform.settings import deepseek_token, hand_mode_promt
from vk_girl_dater.flirter.deepseek_flirter.deepseek_api import DeepseekApi


def is_json(text):
    try:
        json.loads(text)
        return True
    except json.JSONDecodeError:
        return False

def get_text_from(response):
    response = response.json()
    text = response['choices'][0]['message']['content']
    return text


class TestDeepseekApi:
    def test_get_chat_response(self):
        api = DeepseekApi(deepseek_token)
        messages = [
            {"role": "user", "content": "Привет!"},
            {"role": "assistant", "content": "Привет! Как дела?"},
            {"role": "user", "content": "Все хорошо, а у тебя?"}
        ]
        response = api.get_chat_response(messages)

        assert response.status_code == 200

    def test_get_chat_response_as_json(self):
        api = DeepseekApi(deepseek_token)
        messages = [
            {"role": "system", "content": hand_mode_promt},
            {"role": "user", "content": "Привет!"},
            {"role": "assistant", "content": "Привет! Как дела?"},
            {"role": "user", "content": "Все хорошо, а у тебя?"}
        ]
        response = api.get_chat_response(messages)
        text = get_text_from(response)

        assert response.status_code == 200
        assert is_json(text) == True
