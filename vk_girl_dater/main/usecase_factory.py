from test.tests.vk_date_platform.settings import deepseek_token
from vk_girl_dater.flirter.deepseek_flirter.deepseek_api import DeepseekApi
from vk_girl_dater.flirter.deepseek_flirter.deepseek_flirter import DeepseekFlirter
from vk_girl_dater.usecases.get_message_options_command import GetMessageOptionsCommand


class UsecaseFactory:
    @classmethod
    def create_get_message_options_command(cls):
        deepseek_api = DeepseekApi(deepseek_token)
        flirter = DeepseekFlirter(deepseek_api)
        cmd = GetMessageOptionsCommand(flirter)
        return cmd