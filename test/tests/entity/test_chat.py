from test.utils.stub_time_provider import StubTimeProvider
from vk_girl_dater.entity.chat import Chat


class TestChat:
    def test_timedelta_no_message(self):
        chat_data = {'messages': []}
        chat = Chat(chat_data)
        chat.time_provider = StubTimeProvider()

        time_delta = chat.get_last_message_timedelta()

        e_time_delta = {'days': 0,'hours': 0,'minutes': 0}
        assert time_delta == e_time_delta

    def test_timedelta_one_message(self):
        chat_data = {'messages': [{'date': '2025-01-01T12:00:00'}]}
        chat = Chat(chat_data)
        chat.time_provider = StubTimeProvider()

        time_delta = chat.get_last_message_timedelta()

        e_time_delta = {'days': 1,'hours': 6,'minutes': 5}
        assert time_delta == e_time_delta

    def test_is_chat_answered_no_messages(self):
        chat_data = {'messages': []}
        chat = Chat(chat_data)

        assert chat.is_answered() == False

    def test_is_chat_answered(self):
        chat_data = {'messages': [{'name': 'bot'}, {'name': 'girl'}]}
        chat = Chat(chat_data)

        assert chat.is_answered() == False