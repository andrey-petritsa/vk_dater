from datetime import datetime, timedelta, timezone

from test.tests.vk_date_platform import settings


class FlirtWithGirlCommand:
    def execute(self):
        chats = self._get_chats_for_flirt()
        for chat in chats:
            self.__send_flirt_message_to_girl(chat)

    def __send_flirt_message_to_girl(self, chat):
        msg = self.__get_flirt_message(chat)
        self.flirt_platform.send_message(msg)

    def __get_flirt_message(self, chat):
        chat['promt'] = settings.auto_mode_promt
        return {'user_id':chat['id'], 'text':self.flirter.guess_next_message(chat)}

    def _get_chats_for_flirt(self):
        chats = self.flirt_platform.get_chats()

        self.__save_chats(chats)

        chats_for_flirt = [chat for chat in chats if self.__is_chat_for_flirt(chat)]
        return chats_for_flirt

    def __is_chat_for_flirt(self, chat):
        return self.__is_chat_has_no_messages(chat) or self.__is_last_message_old_enough(chat)

    def __is_last_message_old_enough(self, chat):
        msg_date = self.__get_last_message_date(chat)
        cur_date = self._get_current_date()
        date_diff = (cur_date - msg_date)
        return date_diff >= timedelta(minutes=30)

    def __is_chat_has_no_messages(self, chat):
        return len(chat['messages']) == 0

    def __get_last_message_date(self, chat):
        msg = chat['messages'][-1]
        return datetime.strptime(msg['date'], "%Y-%m-%dT%H:%M:%S.%fZ").replace(tzinfo=timezone.utc)

    def __save_chats(self, chats):
        for chat in chats:
            self.chat_repository.save(chat)

    def _get_current_date(self):
        return datetime.now(timezone.utc)

