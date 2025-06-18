from datetime import datetime


class TimeProvider:
    def get_now_date(self):
        now = datetime.now()
        return now.strftime('%Y-%m-%dT%H:%M:%S')