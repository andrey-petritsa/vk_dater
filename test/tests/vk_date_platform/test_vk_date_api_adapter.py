
from test.mocks.mock_datas.mocks import StubVkDateApi, SpyVkDateApi
from test.utils.chat_utils import to_str_one
from vk_girl_dater.vk_date_platform.vk_date_api_adapter import VkDateApiAdapter


def test_adapt_send_message():
    spy = SpyVkDateApi()
    adapter = VkDateApiAdapter(spy)

    adapter.send_message('привет как дела?')

    assert 'привет как дела?' == spy.last_sended_message

def test_adapt_get_chats():
    adapter = VkDateApiAdapter(StubVkDateApi())
    chats = adapter.get_chats()

    assert to_str_one(chats[0]) == 39277097
