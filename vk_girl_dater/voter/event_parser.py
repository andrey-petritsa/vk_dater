from test.tests.vk_date_platform.settings import max_options


class EventParser:
    def __init__(self):
        self.command_mappings = {
            '*добавить_чат': 'add_chat_for_vote'
        }

    def to_events(self, msgs):
        events = []
        for msg in msgs:
            if self.__is_vote_command(msg) and self.__is_in_option_range(msg):
                events.append(self.__to_vote_command(msg))

            if self.__is_admin_command(msg):
                events.append(self.__to_admin_command(msg))

        return events

    def __is_vote_command(self, msg):
        return msg['text'].isnumeric()

    def __is_in_option_range(self, msg):
        return 1 <= int(msg['text']) <= max_options

    def __to_vote_command(self, msg):
        context = {
            'option_number':int(msg['text']),
            'user_id':msg['id'],
            'first_name': msg['first_name'],
            'last_name': msg['last_name']
        }
        command = {'name':'vote_option', 'context':context}
        return command

    def __to_admin_command(self, msg):
        name = msg['text'].split(' ')[0]
        name = self.command_mappings[name]
        if name == 'add_chat_for_vote':
            chat_id = msg['text'].split(' ')[1]
            context = {'chat_id':chat_id, 'user_id':msg['id']}
            command = {'name':name, 'context':context}
            return command

    def __is_admin_command(self, msg):
        left_part = msg['text'].split(' ')[0]
        return left_part in self.command_mappings.keys()