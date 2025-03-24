from test.mocks.flirt_platform_spy import FlirtPlatformSpy
from vk_girl_dater.usecases.get_chat_command import GetChatCommand


class TestGetChatCommand:
    def test_get_chat_command(self):
        flirt_platform = FlirtPlatformSpy()
        cmd = GetChatCommand(flirt_platform)
        user_id = 1
        chat = cmd.execute(user_id)

        assert flirt_platform.last_called_method == 'get_chat 1'