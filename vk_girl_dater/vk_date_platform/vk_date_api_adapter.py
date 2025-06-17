class VkDatePlatform:
    service_chat = {
        "id":1,
        "name":"service",
        "messages":[]
    }

    def __init__(self, vk_date_api):
        self.__vk_date_api = vk_date_api

    def send_message(self, message):
        self.__vk_date_api.send_message(message)

    def get_chats(self):
        get_chats_response = self.__vk_date_api.get_chats()
        get_chats_response = get_chats_response.json()
        chats = []
        for vk_chat in get_chats_response["chats"]:
            if not self.__is_service_chat(vk_chat) and not self.__is_invalid_chat(vk_chat):
                chats.append(self.__convert_to_chat(vk_chat))

        return chats

    def __convert_to_chat(self, vk_api_chat):
        user_id = vk_api_chat['user_id']

        if self.__is_service_chat(vk_api_chat):
            return self.service_chat

        user_name = vk_api_chat["user"]["name"]
        return {
            "id" : user_id,
            "name" : user_name,
            "messages": self.__get_messages(user_id)
        }

    def __get_messages(self, user_id):
        messages = []
        get_history_response = self.__vk_date_api.get_history(user_id)
        get_history_response = get_history_response.json()
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

    def __is_service_chat(self, chat):
        return chat['user_id'] == 1

    def __is_invalid_chat(self, chat):
        return chat['type'] == 'invalid'