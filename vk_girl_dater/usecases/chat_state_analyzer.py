class ChatStateAnalyzer:
    def get_state(self, chat):
        last_message = chat['messages'][-1]
        if last_message['user'] == 'girl':
            return 'not_answered'
        else:
            return 'answered'

        raise Exception('wrong chat state')