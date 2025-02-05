from vk_girl_dater.vk_date_api import VkDateApi


def test_get_history():
    api = VkDateApi()
    get_history_response = api.get_history()

    assert 'messages' in get_history_response.keys()