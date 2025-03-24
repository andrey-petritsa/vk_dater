from test.tests.vk_date_platform.settings import user_id


class FlirtPlatformSpy:
    def send_message(self, message):
        self.last_sended_message = message
        self.last_called_method = ""

    def get_chats(self):
        return [
            {
                'id':39277097,
                'messages':[
                    {'date':'2025-01-27T16:14:21.211Z', 'text':'Тест1', 'name':'bot'},
                    {'date':'2025-01-27T16:14:21.211Z', 'text':'Тест2', 'name':'girl'}
                ],
                'name':'Анна'
            }
        ]

    def get_chat(self, user_id):
        self.last_called_method = f"get_chat {user_id}"
        return {
            'id':user_id,
            'messages':[
                {'date':'2025-01-27T16:14:21.211Z', 'text':'Тест1', 'name':'bot'},
                {'date':'2025-01-27T16:14:21.211Z', 'text':'Тест2', 'name':'girl'}
            ],
            'name':'Анна'
        }
