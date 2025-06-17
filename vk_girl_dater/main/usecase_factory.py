from test.tests.vk_date_platform.settings import deepseek_token
from test.utils.vk_date_token_extractor import VkDateTokenExtractor
from vk_girl_dater.flirter.deepseek_flirter.deepseek_api import DeepseekApi
from vk_girl_dater.flirter.deepseek_flirter.deepseek_flirter import DeepseekFlirter
from vk_girl_dater.usecases.get_chats_command import GetChatsCommand
from vk_girl_dater.usecases.get_message_options_command import GetMessageOptionsCommand
from vk_girl_dater.usecases.send_message_command import SendMessageCommand
from vk_girl_dater.vk_date_platform.vk_date_api import VkDateApi
from vk_girl_dater.vk_date_platform.vk_date_api_adapter import VkDateApiAdapter


class UsecaseFactory:
    vk_date_api = VkDateApi()
    vk_date_api.token = VkDateTokenExtractor.extract()
    platform = VkDateApiAdapter(vk_date_api)
    deepseek_api = DeepseekApi(deepseek_token)
    flirter = DeepseekFlirter(deepseek_api)

    @classmethod
    def create_get_message_options_command(cls):
        cmd = GetMessageOptionsCommand(cls.flirter)
        return cmd

    @classmethod
    def create_send_message_command(cls):
        cmd = SendMessageCommand(cls.platform)
        return cmd

    @classmethod
    def create_get_main_screen_command(cls):
        cmd = GetChatsCommand(cls.platform)
        return cmd