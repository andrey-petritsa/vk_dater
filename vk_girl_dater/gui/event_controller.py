import vk_girl_dater.usecases as usecases

class EventController:
    def handle_event(self, event):
        if event['name'] == 'show_options':
            chat = event['context']['chat']
            return usecases.get_message_options_command.execute(chat)

        if event['name'] == 'send_message':
            message = {'text': event['context']['text'], 'chat_id': event['context']['chat_id']}
            return usecases.send_message_command.execute(message)