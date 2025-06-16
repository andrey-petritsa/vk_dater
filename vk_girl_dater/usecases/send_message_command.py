class SendMessageCommand:
    def __init__(self, flirt_platform):
        self.flirt_platform = flirt_platform

    def execute(self, message):
        self.flirt_platform.send_message(message)