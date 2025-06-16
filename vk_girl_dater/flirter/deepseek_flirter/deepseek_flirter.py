import json
from test.tests.vk_date_platform.settings import guess_message_constant


class DeepseekFlirter:
    def __init__(self, deepseek_api):
        self.__deepseek_api = deepseek_api

    def guess_next_message(self, chat):
        deepseek_messages = self.__get_deepseek_messages(chat)
        response = self.__deepseek_api.get_chat_response(deepseek_messages)
        return self._get_text_from(response)

    def guess_next_message_options(self, chat):
        deepseek_messages = self.__get_deepseek_messages(chat)
        response = self.__deepseek_api.get_chat_response(deepseek_messages)
        text = self._get_text_from(response)
        return json.loads(text)

    def __get_deepseek_messages(self, chat):
        promt_message = {"role":"system", "content":f"{chat['promt']}"}
        if len(chat['messages']) == 0:
            deepseek_messages = self.__get_deepseek_message_for_empty_chat()
        else:
            deepseek_messages = self.__get_deepseek_messages_for_non_empty_chat(chat)
        return [promt_message] + deepseek_messages

    def __get_deepseek_message_for_empty_chat(self):
        return [{'content':guess_message_constant, 'role':'user'}]

    def __get_deepseek_messages_for_non_empty_chat(self, chat):
        return [{'role':self.__get_role_by(msg), 'content':self.__get_message_text(msg)} for msg in chat['messages']]

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