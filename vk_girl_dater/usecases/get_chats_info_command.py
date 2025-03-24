

class GetChatsInfoCommand:
    def __init__(self, flirt_platform):
        self.flirt_platform = flirt_platform

    def execute(self):
        chats_info = self.flirt_platform.get_chats_info()
        return chats_info

def to_str(chat_info):
    return f"{chat_info['id']}: {chat_info['name']}"

if __name__ == "__main__":
    from vk_girl_dater.main import UsecaseFactory
    factory = UsecaseFactory()
    cmd = factory.create_get_chats_info_command()
    chat_infos = cmd.execute()
    for chat_info in chat_infos:
        print(to_str(chat_info))