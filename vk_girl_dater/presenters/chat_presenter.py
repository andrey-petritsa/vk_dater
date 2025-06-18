class ChatPresenter:
    def to_view_chat(self, chat):
        self.__chat = chat
        view_messages = []
        for message in chat['messages']:
            view_messages.append(self.__to_view_messages(message))
        chat['messages'] = view_messages
        return chat

    def __to_view_messages(self, message):
        if message['name'] == 'bot':
            name = 'bot'
            position = 'left'
        else:
            name = self.__chat['name']
            position = 'right'
        msg = {'name':name, 'text':message['text'], 'position':position}
        return msg

    def to_view_chat_info(self, chat_info):
        return {
            'id': chat_info['id'],
            'name': chat_info['name'],
            'avatar_url':chat_info['avatar_url'],
            'last_message_hint': '137 дней',
            'is_answered_status_icon': '👀',
        }