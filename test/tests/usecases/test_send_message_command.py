from test.mocks.flirt_platform_spy import FlirtPlatformSpy
from vk_girl_dater.usecases.send_message_command import SendMessageCommand


class TestSendMessageCommand:
    def test_execute(self):
        spy = FlirtPlatformSpy()
        cmd = SendMessageCommand(spy)
        message = {'user_id': 1, 'text': 'привет'}

        cmd.execute(message)

        assert spy.last_sended_message == {'user_id': 1, 'text': 'привет'}