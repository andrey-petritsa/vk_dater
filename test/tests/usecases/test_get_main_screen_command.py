from test.mocks.flirt_platform_spy import FlirtPlatformSpy


class GetMainScreenCommand:
    def __init__(self, flirt_platform):
        self.flirt_platform = flirt_platform

    def execute(self):
        chats = self.flirt_platform.get_chats()

        return self.__convert_chats(chats)

    def __convert_chats(self, chats):
        con_chats = []
        for chat in chats:
            self.__chat = chat
            chat['messages'] = self.__convert_to_messages(chat)
            con_chats.append(chat)
        return con_chats

    def __convert_to_messages(self, chat):
        messages = []
        for message in chat['messages']:
            messages.append(self.__convert_to_message(message))
        return messages

    def __convert_to_message(self, message):
        if message['user'] == 'bot':
            name = 'Бот'
            position = 'left'
        else:
            name = self.__chat['name']
            position = 'right'
        msg = {'name':name, 'text':message['text'], 'position':position}
        return msg


class TestGetMainScreenCommand:
    def test_get_main_screen_command(self):
        flirt_platform = FlirtPlatformSpy()
        cmd = GetMainScreenCommand(flirt_platform)
        screen = cmd.execute()

        e_screen = [
            {
                'name': 'Анна',
                'id': 39277097,
                'messages': [
                    {'name': 'Бот', 'text': 'Тест1', 'position': 'left'},
                    {'name': 'Анна', 'text': 'Тест2', 'position': 'right'}
                ],
            },
        ]
        assert e_screen == screen