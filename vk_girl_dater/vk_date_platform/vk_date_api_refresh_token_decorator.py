import vk_girl_dater.utils as utils

from test.utils.vk_date_token_extractor import VkDateTokenExtractor
from vk_girl_dater.vk_date_platform.exception import InvalidTokenException


class VkDateApiRefreshTokenDecorator:
    def __init__(self, vk_date_api):
        self.vk_date_api = vk_date_api
        self.max_tries = 3

    def get_history(self, user_id, try_count=0):
        if try_count >= self.max_tries:
            raise Exception('Too many tries for refreshing token')

        try:
            return self.vk_date_api.get_history(user_id)
        except InvalidTokenException:
            utils.logger.send_info("Invalid token. Refreshing...")
            try_count = try_count + 1
            token = VkDateTokenExtractor.extract()
            self.vk_date_api.token = token
            return self.get_history(user_id, try_count)

    def send_message(self, message, try_count=0):
        if try_count >= self.max_tries:
            raise Exception('Too many tries for refreshing token')

        try:
            return self.vk_date_api.send_message(message)
        except InvalidTokenException:
            utils.logger.send_info("Invalid token. Refreshing...")
            try_count = try_count + 1
            token = VkDateTokenExtractor.extract()
            self.vk_date_api.token = token
            return self.send_message(message, try_count)

    def get_chats(self, try_count=0):
        if try_count >= self.max_tries:
            raise Exception('Too many tries for refreshing token')

        try:
            return self.vk_date_api.get_chats()
        except InvalidTokenException:
            utils.logger.send_info("Invalid token. Refreshing...")
            try_count = try_count + 1
            token = VkDateTokenExtractor.extract()
            self.vk_date_api.token = token
            return self.get_chats(try_count)