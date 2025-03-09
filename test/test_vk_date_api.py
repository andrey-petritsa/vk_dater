from test.settings import token, chat_id
from vk_girl_dater.vk_date_api import VkDateApi

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
