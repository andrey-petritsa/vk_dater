from test.mocks.mocks import SpyFlirtPlatform
from vk_girl_dater.usecases.get_chats_info_command import GetChatsInfoCommand

class TestGetChatsInfoCommand:
    def test_execute(self):
        flirt_platform = SpyFlirtPlatform()
        cmd = GetChatsInfoCommand(flirt_platform)
        chats_info = cmd.execute()

        e_chats_info = [
            {
                'id': 1,
                'name': 'Анна',
                'avatar_url':'avatar_url',
                'last_message_timedelta': {'days': 137, 'hours': 23, 'minutes': 43},
                'is_answered': True,
            }
        ]

        assert chats_info == e_chats_info