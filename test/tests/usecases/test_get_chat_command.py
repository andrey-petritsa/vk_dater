from test.mocks.flirt_platform_spy import FlirtPlatformSpy


class GetChatCommand:
    def __init__(self, flirt_platform):
        self.flirt_platform = flirt_platform

    def execute(self, user_id):
        return self.flirt_platform.get_chat(user_id)

class TestGetChatCommand:
    def test_get_chat_command(self):
        flirt_platform = FlirtPlatformSpy()
        cmd = GetChatCommand(flirt_platform)
        user_id = 1
        chat = cmd.execute(user_id)

        assert flirt_platform.last_called_method == 'get_chat 1'