from datetime import datetime

from vk_girl_dater.utils.time_provider import TimeProvider


class Chat:
    def __init__(self, chat):
        self.time_provider = TimeProvider()
        self.chat = chat

    def get_last_message_timedelta(self):
        if len(self.chat['messages']) == 0:
            return {'days': 0,'hours': 0,'minutes': 0}

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
