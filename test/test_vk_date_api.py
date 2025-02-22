from test.settings import token, chat_id
from vk_girl_dater.vk_date_api import VkDateApi
import random
import string

api = VkDateApi()
api.token = token

def test_get_history():
    get_history_response = api.get_history(chat_id)
    assert 'messages' in get_history_response.keys()

def test_send_message():
    message_text = f'привет {get_random_test_marker()}'
    message = {'user_id': chat_id,'text': message_text}
    api.send_message(message)

    history = api.get_history(chat_id)
    last_message = history['messages'][-1]
    assert message_text == last_message['content']


def get_random_test_marker():
    return ''.join(random.choices(string.ascii_lowercase, k=3))


def test_get_chats():
    get_chats_response = api.get_chats()
    assert "chats" in get_chats_response
