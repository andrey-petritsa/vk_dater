from vk_girl_dater.vk_girl_dater import VkGirlDater


def test_get_girls():
    dater = VkGirlDater()
    girls = dater.get_girls()

    assert 'Настя' in girls

def test_get_chat():
    dater = VkGirlDater()
    chat = dater.get_chats()
    first_message = chat[0]

    assert 'Приветствуем в VK Знакомствах!' in first_message['text']
    assert 'павел' in first_message['person']
