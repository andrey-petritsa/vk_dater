from test.mocks.flirt_platform_spy import FlirtPlatformSpy
from vk_girl_dater.presenters.message_presenter import MessagePresenter


class GetChatCommand:
    def __init__(self, flirt_platform):
        self.flirt_platform = flirt_platform
        self.message_presenter = MessagePresenter()

    def execute(self, user_id):
        chat = self.flirt_platform.get_chat(user_id)
        chat['messages'] = self.message_presenter.to_view_messages(chat)
        return chat

class TestGetChatCommand:
    def test_get_chat_command(self):
        flirt_platform = FlirtPlatformSpy()
        cmd = GetChatCommand(flirt_platform)
        user_id = 1
        chat = cmd.execute(user_id)

        assert flirt_platform.last_called_method == 'get_chat 1'