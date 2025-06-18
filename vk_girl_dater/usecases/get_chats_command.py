from vk_girl_dater.presenters.message_presenter import MessagePresenter


class GetChatsCommand:
    def __init__(self, flirt_platform):
        self.message_presenter = MessagePresenter()
        self.flirt_platform = flirt_platform

    def execute(self):
        chats = self.flirt_platform.get_chats()
        return self.__convert_chats(chats)

    def __convert_chats(self, chats):
        con_chats = []
        for chat in chats:
            chat['messages'] = self.message_presenter.to_view_messages(chat)
            con_chats.append(chat)
        return con_chats


