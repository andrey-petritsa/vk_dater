class MessagePresenter:
    def to_view_messages(self, chat):
        self.__chat = chat
        view_messages = []
        for message in chat['messages']:
            view_messages.append(self.__to_view_messages(message))
        return view_messages

    def __to_view_messages(self, message):
        if message['name'] == 'bot':
            name = 'bot'
            position = 'left'
        else:
            name = self.__chat['name']
            position = 'right'
        msg = {'name':name, 'text':message['text'], 'position':position}
        return msg