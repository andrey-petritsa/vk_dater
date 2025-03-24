from test.chat_utils import to_str
from test.vk_date_platform.mock_datas.mocks import StubVkDateApi, SpyVkDateApi
from vk_girl_dater.vk_date_platform.vk_date_api_adapter import VkDateApiAdapter


def test_adapt_send_message():
    spy = SpyVkDateApi()
    adapter = VkDateApiAdapter(spy)

    adapter.send_message('привет альтушка')

    assert 'привет альтушка' == spy.last_sended_message

def test_adapt_get_chats():
    adapter = VkDateApiAdapter(StubVkDateApi())
    chats = adapter.get_chats()

    assert to_str(chats[0]) == '46344340 bot:Наш мед раньше тюрьмой был'
    assert to_str(chats[1]) == '39277097 bot:Наш мед раньше тюрьмой был'
