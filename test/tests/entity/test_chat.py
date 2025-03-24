from test.utils.stub_time_provider import StubTimeProvider
from vk_girl_dater.entity.chat import Chat
import vk_girl_dater.utils as utils


class TestChat:

    def test_timedelta_one_message(self):
        chat = Chat()
        last_message = {'date': '2025-01-01T12:00:00.000Z'}
        utils.time_provider = StubTimeProvider()

        time_delta = chat.get_last_message_timedelta(last_message)

        e_time_delta = {'days': 1,'hours': 6,'minutes': 5}
        assert time_delta == e_time_delta

    def test_is_chat_answered(self):
        chat = Chat()
        last_message = {'name': 'girl'}

        assert chat.is_answered(last_message) == False