from test.mocks.flirt_platform_spy import FlirtPlatformSpy


class GetMainScreenCommand:
    def __init__(self, flirt_platform):
        self.flirt_platform = flirt_platform

    def execute(self):
        chats = self.flirt_platform.get_chats()
        messages = []

        chat = chats[0]
        msgs = chat['messages']
        self.__chat_name = chats[0]['name']
        for message in msgs:
            messages.append(self.__convert_to_message(message))

        return [
            {
                'name': chats[0]['name'],
                'messages': messages,
            },
        ]

    def __convert_to_message(self, message):
        if message['user'] == 'bot':
            name = 'Бот'
            position = 'left'
        else:
            name = self.__chat_name
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
                'messages': [
                    {'name': 'Бот', 'text': 'Тест1', 'position': 'left'},
                    {'name': 'Анна', 'text': 'Тест2', 'position': 'right'}
                ],
            },
        ]
        assert e_screen == screen