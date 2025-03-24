from vk_girl_dater.voter.event_parser import EventParser


class TestEventParser:
    def setup_method(self):
        self.parser = EventParser()

    def test_parse(self):
        msgs = [
            {
                'text':'*добавить_чат 123', 'first_name': 'Андрей', 'last_name': 'Петрица', 'id': 1
            },
            {
                'text':'1', 'first_name': 'Андрей', 'last_name': 'Петрица', 'id': 1
            },
            {
                'text':'привет', 'first_name': 'Андрей', 'last_name': 'Петрица', 'id': 1
            }
        ]
        events = self.parser.to_events(msgs)

        assert events == [
            {'name': 'add_chat_for_vote', 'context': {'chat_id': '123', 'user_id': 1}},
            {'name': 'vote_option', 'context': {'option_number': 1, 'user_id': 1, 'first_name': 'Андрей', 'last_name': 'Петрица'}}
        ]