class GetMessageOptionsCommand:
    def __init__(self, flirter):
        self.__flirter = flirter

    def execute(self, chat):
        options = self.__flirter.guess_next_message_options(chat)
        return options