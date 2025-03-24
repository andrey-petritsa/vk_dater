from test.tests.usecases.test_get_chat_command import GetChatCommand
from test.tests.vk_date_platform.settings import deepseek_token
from test.utils.vk_date_token_extractor import VkDateTokenExtractor
from vk_girl_dater.flirter.deepseek_flirter.deepseek_api import DeepseekApi
from vk_girl_dater.flirter.deepseek_flirter.deepseek_flirter import DeepseekFlirter
from vk_girl_dater.usecases.get_chats_command import GetChatsCommand
from vk_girl_dater.usecases.get_chats_info_command import GetChatsInfoCommand
from vk_girl_dater.usecases.get_message_options_command import GetMessageOptionsCommand
from vk_girl_dater.usecases.send_message_command import SendMessageCommand
from vk_girl_dater.vk_date_platform.vk_date_api import VkDateApi
from vk_girl_dater.vk_date_platform.vk_date_api_refresh_token_decorator import VkDateApiRefreshTokenDecorator
from vk_girl_dater.vk_date_platform.vk_date_platform import VkDatePlatform


class UsecaseFactory:
    def __init__(self):
        self.vk_date_api = VkDateApi()
        self.vk_date_api.token = VkDateTokenExtractor.extract()
        self.vk_date_api = VkDateApiRefreshTokenDecorator(self.vk_date_api)
        self.platform = VkDatePlatform(self.vk_date_api)
        self.deepseek_api = DeepseekApi(deepseek_token)
        self.flirter = DeepseekFlirter(self.deepseek_api)

    def create_get_message_options_command(self):
        cmd = GetMessageOptionsCommand(self.flirter)
        return cmd

    def create_send_message_command(self):
        cmd = SendMessageCommand(self.platform)
        return cmd

    def create_get_main_screen_command(self):
        cmd = GetChatsCommand(self.platform)
        return cmd

    def create_get_chat_command(self):
        cmd = GetChatCommand(self.platform)
        return cmd

    def create_get_chats_info_command(self):
        cmd = GetChatsInfoCommand(self.platform)
        return cmd