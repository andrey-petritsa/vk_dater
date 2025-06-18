class StubTimeProvider:
    def __init__(self):
        self.now_date = '2025-01-02T18:05:25'

    def get_now_date(self):
        return self.now_date
