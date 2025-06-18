from vk_girl_dater.presenters.message_presenter import MessagePresenter


class GetChatCommand:
    def __init__(self, flirt_platform):
        self.flirt_platform = flirt_platform
        self.message_presenter = MessagePresenter()

    def execute(self, user_id):
        chat = self.flirt_platform.get_chat(user_id)
        chat['messages'] = self.message_presenter.to_view_messages(chat)
        return chat
