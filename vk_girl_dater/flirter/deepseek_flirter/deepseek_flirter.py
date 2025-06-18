import json
from test.tests.vk_date_platform.settings import guess_message_constant, auto_mode_promt, hand_mode_promt
import vk_girl_dater.utils as utils


class DeepseekFlirter:
    def __init__(self, deepseek_api):
        self.__deepseek_api = deepseek_api
        self.promts = {
            'auto': auto_mode_promt, 'hand': hand_mode_promt
        }

    def guess_next_message(self, chat):
        deepseek_messages = self.__get_deepseek_messages(chat, self.promts['auto'])
        response = self.__deepseek_api.get_chat_response(deepseek_messages)
        return self._get_text_from(response)

    def guess_next_message_options(self, chat, try_count=0):
        if try_count >= 3:
            raise Exception(f"Флиртер Возвращает ответ не в json формате")

        deepseek_messages = self.__get_deepseek_messages(chat, self.promts['hand'])
        response = self.__deepseek_api.get_chat_response(deepseek_messages)
        text = self._get_text_from(response)

        try:
            return json.loads(text)
        except json.JSONDecodeError:
            utils.logger.send_info(f'Deepseek вернул не json. Повторная попытка... Полученный текст\n{text}')
            return self.guess_next_message_options(chat, try_count + 1)

    def __get_deepseek_messages(self, chat, promt):
        promt_message = {"role":"system", "content":promt}
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
        if message['name'] == 'bot':
            return 'assistant'
        else:
            return 'user'

    def __get_tag_by(self, message):
        if message['name'] == 'bot':
            return 'парень(бот)'
        else:
            return 'девушка'