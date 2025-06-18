from vk_girl_dater.presenters.chat_presenter import ChatPresenter


class GetChatCommand:
    def __init__(self, flirt_platform):
        self.flirt_platform = flirt_platform
        self.chat_presenter = ChatPresenter()

    def execute(self, user_id):
        chat = self.flirt_platform.get_chat(user_id)
        chat['messages'] = self.chat_presenter.to_view_messages(chat)
        return chat
