from test.mocks.flirt_platform_spy import FlirtPlatformSpy
from vk_girl_dater.usecases.get_chats_command import GetChatsCommand


class TestGetChatsCommand:
    def test_get_chats_command(self):
        flirt_platform = FlirtPlatformSpy()
        cmd = GetChatsCommand(flirt_platform)
        screen = cmd.execute()

        e_screen = [
            {
                'name': 'Анна',
                'id': 39277097,
                'messages': [
                    {'name': 'bot', 'text': 'Тест1', 'position': 'left'},
                    {'name': 'Анна', 'text': 'Тест2', 'position': 'right'}
                ],
            },
        ]
        assert e_screen == screen