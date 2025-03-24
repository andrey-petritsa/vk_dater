from vk_girl_dater.group_usecases.send_message_to_group_command import SendMessageToGroupCommand

class SpyChatGroup:
    def send_message(self, text, group_id):
        self.last_sended_message = f"{text} to {group_id}"

class TestSendMessageToGroup:
    def test_send_message(self):
        chat_group = SpyChatGroup()
        cmd = SendMessageToGroupCommand(chat_group)
        text = 'тест'
        group_id = 1
        cmd.execute(text, group_id)

        assert chat_group.last_sended_message == f"тест to 1"