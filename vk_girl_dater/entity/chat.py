from datetime import datetime
import vk_girl_dater.utils as utils


class Chat:
    def get_last_message_timedelta(self, last_message):
        now_date = utils.time_provider.get_now_date()
        return self.__get_time_delta(last_message['date'], now_date)

    def __get_time_delta(self, time1, time2):
        dt1 = datetime.strptime(time1, '%Y-%m-%dT%H:%M:%S.%fZ')
        dt2 = datetime.strptime(time2, '%Y-%m-%dT%H:%M:%S.%fZ')
        delta = dt2 - dt1
        return {
            'days': delta.days,
            'hours': delta.seconds // 3600,
            'minutes': (delta.seconds % 3600) // 60
        }

    def is_answered(self, last_message):
        if last_message['name'] == 'bot':
            return True
        else:
            return False