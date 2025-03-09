class VkDateApiAdapter:
    def __init__(self, vk_date_api):
        self.__vk_date_api = vk_date_api

    def get_messages(self, chat_id):
        messages = []
        get_history_response = self.__vk_date_api.get_history(chat_id)
        for vk_message in get_history_response['messages']:
            messages.append(self.__convert_to_message(vk_message))

        return messages

    def __convert_to_message(self, vk_api_message):
        return {
            'text':vk_api_message['content'],
            'date':vk_api_message['created_at'],
            'user':self.__get_user_name(vk_api_message)
        }

    def __get_user_name(self, message):
        if message['is_my']:
            return 'bot'
        else:
            return 'girl'

    def send_message(self, message):
        self.__vk_date_api.send_message(message)