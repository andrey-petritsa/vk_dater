from vk_girl_dater.vk_date_platform.vk_date_api import VkDateApi
from .settings import chat_id, token

api = VkDateApi()
api.token = token

def test_get_history():
    response = api.get_history(chat_id)
    assert response.ok is True

def test_send_message():
    message_text = 'тест'
    message = {'user_id': chat_id,'text': message_text}
    response = api.send_message(message)
    assert response.ok is True

def test_get_chats():
    response = api.get_chats()
    assert response.ok is True
