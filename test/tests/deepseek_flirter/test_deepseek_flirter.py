from test.tests.deepseek_flirter.mocks import SpyDeepseekApi
from vk_girl_dater.flirter.deepseek_flirter.deepseek_flirter import DeepseekFlirter

class DeepseekFlirterTestable(DeepseekFlirter):
    def __init__(self, deepseek_api):
        super().__init__(deepseek_api)
        self.promts = {
            'auto': 'промт для авто режима',
            'hand': 'промт для ручного режима'
        }
        self.return_mode = "plain_text"

    def _get_text_from(self, response):
        if self.return_mode == "plain_text":
            return "текст deepseek"

        if self.return_mode == 'json':
            return "{}"

class TestDeepseekFlirter:
    def test_guess_next_message(self):
        deepseek_api = SpyDeepseekApi()
        flirter = DeepseekFlirterTestable(deepseek_api)

        chat = {
            'messages': [
                {'text': 'привет как дела?', 'name': 'bot'},
                {'text': 'все хорошо', 'name': 'анна'},
            ],
        }
        flirter.guess_next_message(chat)

        assert deepseek_api.last_messages == [
            {'content': 'промт для авто режима', 'role': 'system'},
            {'content': 'парень(бот): привет как дела?', 'role': 'assistant'},
            {'content': 'девушка: все хорошо', 'role': 'user'},
        ]

    def test_guess_next_message__when_chat_has_no_messages(self):
        deepseek_api = SpyDeepseekApi()
        flirter = DeepseekFlirterTestable(deepseek_api)
        chat = {'messages': []}
        flirter.guess_next_message(chat)

        assert deepseek_api.last_messages == [
            {'content': 'промт для авто режима', 'role': 'system'},
            {'content': '*GUESS_MESSAGE', 'role': 'user'}
        ]

    def test_guess_next_message_options(self):
        deepseek_api = SpyDeepseekApi()
        flirter = DeepseekFlirterTestable(deepseek_api)
        flirter.return_mode = 'json'
        chat = {
            'messages': [
                {'text': 'привет как дела?', 'name': 'bot'},
                {'text': 'все хорошо', 'name': 'анна'},
            ],
        }

        flirter.guess_next_message_options(chat)

        assert deepseek_api.last_messages == [
            {'content': 'промт для ручного режима', 'role': 'system'},
            {'content': 'парень(бот): привет как дела?', 'role': 'assistant'},
            {'content': 'девушка: все хорошо', 'role': 'user'},
        ]

