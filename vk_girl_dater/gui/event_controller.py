import vk_girl_dater.usecases as usecases
import vk_girl_dater.utils as utils

class EventController:
    def handle_event(self, event):
        utils.logger.send_info(event)

        if event['name'] == 'show_options':
            chat = event['context']['chat']
            return usecases.get_message_options_command.execute(chat)

        if event['name'] == 'send_message':
            message = {'text': event['context']['text'], 'user_id': event['context']['user_id']}
            return usecases.send_message_command.execute(message)

        if event['name'] == 'get_chat':
            user_id = event['context']['user_id']
            return usecases.get_chat_command.execute(user_id)