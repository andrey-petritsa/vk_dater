from datetime import datetime
from test.utils.stub_time_provider import StubTimeProvider
from vk_girl_dater.utils.time_provider import TimeProvider


class Chat:
    def __init__(self, chat):
        self.time_provider = TimeProvider()
        self.chat = chat

    def get_last_message_timedelta(self):
        last_message = self.chat['messages'][-1]
        now_date = self.time_provider.get_now_date()
        return self.__get_time_delta(last_message['date'], now_date)

    def __get_time_delta(self, time1, time2):
        dt1 = datetime.strptime(time1, '%Y-%m-%dT%H:%M:%S')
        dt2 = datetime.strptime(time2, '%Y-%m-%dT%H:%M:%S')
        delta = dt2 - dt1
        return {
            'days':delta.days,
            'hours':delta.seconds // 3600,
            'minutes':(delta.seconds % 3600) // 60
        }


class TestChat:
    def test_nth(self):
        chat_data = {'messages': [{'date': '2025-01-01T12:00:00'}]}
        chat = Chat(chat_data)
        chat.time_provider = StubTimeProvider()

        time_delta = chat.get_last_message_timedelta()

        e_time_delta = {'days': 1,'hours': 6,'minutes': 5}
        assert time_delta == e_time_delta