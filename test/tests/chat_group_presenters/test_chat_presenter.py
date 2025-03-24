from vk_girl_dater.chat_group_presenters.chat_presenter import ChatPresenter


class TestChatPresenter:
    def test_present(self):
        presenter = ChatPresenter()

        chat = [
            {'name': 'Андрей', 'text': 'Тест1', 'position': 'left'},
            {'name': 'Анна', 'text': 'Тест2', 'position': 'right'},
            {'name': 'Андрей', 'text': 'Тест3', 'position': 'left'}
        ]

        e_chat_view = "🤖Андрей: Тест1\n\n❤️Анна: Тест2\n\n🤖Андрей: Тест3"
        assert presenter.present(chat) == e_chat_view


