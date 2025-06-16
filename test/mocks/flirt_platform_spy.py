class FlirtPlatformSpy:
    def send_message(self, message):
        self.last_sended_message = message

    def get_chats(self):
        return [
            {
                'id':39277097,
                'messages':[
                    {'date':'2025-01-27T16:14:21.211Z', 'text':'Тест1', 'user':'bot'},
                    {'date':'2025-01-27T16:14:21.211Z', 'text':'Тест2', 'user':'girl'}
                ],
                'name':'Анна'
            }
        ]
