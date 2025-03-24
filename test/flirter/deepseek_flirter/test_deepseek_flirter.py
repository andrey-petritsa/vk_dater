from test.flirter.deepseek_flirter.mocks import SpyDeepseekApi
from test.vk_date_platform.settings import podcat_promt
from vk_girl_dater.flirter.deepseek_flirter.deepseek_flirter import DeepseekFlirter

class TestableDeepseekFlirter(DeepseekFlirter):
    def _get_text_from(self, response):
        return "текст deepseek"

class TestDeepseekFlirter:
    def test_guess_next_message(self):
        spy = SpyDeepseekApi()
        flirter = TestableDeepseekFlirter(spy)
        chat = {
            'messages': [
                {'text': 'привет как дела?', 'user': 'bot'},
                {'text': 'все хорошо', 'user': 'girl'},
            ]
        }
        flirter.guess_next_message(chat)

        assert spy.last_messages == [
            {'content': 'парень(бот): привет как дела?', 'role': 'assistant'},
            {'content': 'девушка: все хорошо', 'role': 'user'},
        ]

    def test_guess_next_message__when_chat_has_no_messages(self):
        spy = SpyDeepseekApi()
        flirter = TestableDeepseekFlirter(spy)
        chat = {
            'messages': []
        }
        flirter.guess_next_message(chat)

        assert spy.last_messages == [{'content':podcat_promt, 'role':'user'}]
