
from test.utils.vk_date_token_extractor import VkDateTokenExtractor
from test.tests.vk_date_platform.settings import deepseek_token
from vk_girl_dater.chat_repository.in_file_chat_repository.in_file_chat_repository import InFileChatRepository
from vk_girl_dater.flirter.deepseek_flirter.deepseek_api import DeepseekApi
from vk_girl_dater.flirter.deepseek_flirter.deepseek_flirter import DeepseekFlirter
from vk_girl_dater.usecases.flirt_with_girl_command import FlirtWithGirlCommand
from vk_girl_dater.vk_date_platform.vk_date_api import VkDateApi
from vk_girl_dater.vk_date_platform.vk_date_platform import VkDatePlatform

class FlirtCommandFactory:
    @staticmethod
    def create():
        command = FlirtWithGirlCommand()
        vk_date_api = VkDateApi()
        vk_api_token = VkDateTokenExtractor.extract()
        vk_date_api.token = vk_api_token
        command.flirt_platform = VkDatePlatform(vk_date_api)
        deepseek_api = DeepseekApi(deepseek_token)
        command.flirter = DeepseekFlirter(deepseek_api)
        command.chat_repository = InFileChatRepository()

        return command
