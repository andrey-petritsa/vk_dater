from test.mocks.flirt_platform_spy import FlirtPlatformSpy
from vk_girl_dater.usecases.get_main_screen_command import GetMainScreenCommand


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