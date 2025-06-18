from vk_girl_dater.entity.chat_state_analyzer import ChatStateAnalyzer


class TestChatStateAnalyzer:
    def setup_method(self):
        self.analyzer = ChatStateAnalyzer()

    def test_get_not_answered_state(self):
        chat = {'messages': [{'user': 'girl'}]}
        state = self.analyzer.get_state(chat)

        assert state == 'not_answered'

    def test_get_answered_state(self):
        chat = {'messages': [{'user': 'girl'}, {'user': 'bot'}]}
        state = self.analyzer.get_state(chat)

        assert state == 'answered'

