from test.mocks.mocks import SpyFlirter
from vk_girl_dater.usecases.get_message_options_command import GetMessageOptionsCommand


class TestGetMessageOptionsCommand:
    def test_nth(self):
        flirter = SpyFlirter()
        cmd = GetMessageOptionsCommand(flirter)
        chat = {
            'name': 'Бот',
            'messages': [
                {'name': 'Бот', 'text': 'Тест1', 'position': 'left'},
                {'name': 'Анна', 'text': 'Тест2', 'position': 'right'}
            ]
        }
        options = cmd.execute(chat)

        assert ['опция1', 'опция2'] == options