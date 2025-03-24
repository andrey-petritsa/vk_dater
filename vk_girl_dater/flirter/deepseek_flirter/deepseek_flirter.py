from test.vk_date_platform.settings import podcat_promt


class DeepseekFlirter:
    def __init__(self, deepseek_api):
        self.__deepseek_api = deepseek_api

    def guess_next_message(self, chat):
        if len(chat['messages']) == 0:
            deepseek_messages = [{'content': podcat_promt, 'role': 'user'}]
        else:
            deepseek_messages = [{'role': self.__get_role_by(msg), 'content': self.__get_message_text(msg)} for msg in chat['messages']]

        response = self.__deepseek_api.get_chat_response(deepseek_messages)
        return self._get_text_from(response)

    def __get_message_text(self, message):
        return f"{self.__get_tag_by(message)}: {message['text']}"

    def _get_text_from(self, response):
        response = response.json()
        text = response['choices'][0]['message']['content']
        return text

    def __get_role_by(self, message):
        if message['user'] == 'girl':
            return 'user'
        if message['user'] == 'bot':
            return 'assistant'

    def __get_tag_by(self, message):
        if message['user'] == 'girl':
            return 'девушка'
        if message['user'] == 'bot':
            return 'парень(бот)'