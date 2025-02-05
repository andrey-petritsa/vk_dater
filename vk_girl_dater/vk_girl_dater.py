from vk_girl_dater.vk_date_api import VkDateApi


class VkGirlDater:
    def __init__(self):
        self.vk_date_api = VkDateApi()

    def get_girls(self):
        return ['Настя']

    def get_chats(self):
        chat = []
        get_history_response = self.vk_date_api.get_history()

        for message in get_history_response['messages']:
            message = {
                'text': message['content'],
                'person': message['']
            }
            chat.append(message)

        return chat