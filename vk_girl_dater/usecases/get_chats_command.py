from vk_girl_dater.presenters.chat_presenter import ChatPresenter


class GetChatsCommand:
    def __init__(self, flirt_platform):
        self.chat_presenter = ChatPresenter()
        self.flirt_platform = flirt_platform

    def execute(self):
        chats = self.flirt_platform.get_chats()
        return self.__convert_chats(chats)

    def __convert_chats(self, chats):
        con_chats = []
        for chat in chats:
            chat = self.chat_presenter.to_view_chat(chat)
            con_chats.append(chat)
        return con_chats


