from test.settings import token, chat_id
from vk_girl_dater.vk_date_api import VkDateApi

api = VkDateApi()
api.token = token

def test_get_history():
    get_history_response = api.get_history(chat_id)
    assert 'messages' in get_history_response.keys()