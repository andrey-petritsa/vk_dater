class GetChatsInfoCommand:
    def __init__(self, flirt_platform):
        self.flirt_platform = flirt_platform

    def execute(self):
        chats_info = self.flirt_platform.get_chats_info()
        return chats_info