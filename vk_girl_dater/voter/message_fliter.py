class MessageFilter:
    def __init__(self, messages):
        self.messages = messages

    def since_date(self, date):
        return [msg for msg in self.messages if msg['date'] >= date]
