class SendMessageToGroupCommand:
    def __init__(self, chat_group):
        self.chat = chat_group

    def execute(self, text, group_id):
        self.chat.send_message(text, group_id)