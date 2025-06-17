import vk_girl_dater.usecases as usecases

class EventController:
    @classmethod
    def handle_event(cls, event):
        print(event)

        if event['name'] == 'show_options':
            chat = event['context']['chat']
            return usecases.get_message_options_command.execute(chat)