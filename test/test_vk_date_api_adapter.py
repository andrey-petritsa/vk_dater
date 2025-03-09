
from test.mock_datas.mocks import SpyVkDateApi, StubVkDateApi
from vk_girl_dater.vk_date_api_adapter import VkDateApiAdapter


def test_adapt_get_history():
    adapter = VkDateApiAdapter(StubVkDateApi())
    chat_id = 1
    messages = adapter.get_messages(chat_id)

    e_message = {
        'text': 'Наш мед раньше тюрьмой был',
        'date': '2025-01-27T16:14:21.211Z',
        'user': 'bot'
    }

    assert messages[0] == e_message

def test_adapt_send_message():
    spy = SpyVkDateApi()
    adapter = VkDateApiAdapter(spy)

    adapter.send_message('привет альтушка')

    assert 'привет альтушка' == spy.last_sended_message

def test_adapt_get_chats():
    pass
