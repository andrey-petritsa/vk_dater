import pytest

from vk_girl_dater.vk_date_platform.vk_date_api import VkDateApi
from .settings import user_id
from test.utils.vk_date_token_extractor import VkDateTokenExtractor

class TestVkDateApi:
    def setup_method(self):
        self.api = VkDateApi()
        self.api.token = VkDateTokenExtractor.extract()

    @pytest.mark.integration
    def test_get_history(self):
        response = self.api.get_history(user_id)
        assert response.ok is True

    @pytest.mark.integration
    def test_send_message(self):
        message_text = 'тест'
        message = {'user_id': user_id, 'text': message_text}
        response = self.api.send_message(message)
        assert response.ok is True

    @pytest.mark.integration
    def test_get_chats(self):
        response = self.api.get_chats()
        assert response.ok is True
