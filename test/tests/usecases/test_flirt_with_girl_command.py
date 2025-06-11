from datetime import datetime, timezone

from test.mocks.mocks import SpyFlirtPlatform, SpyFlirter, SpyChatRepository
from test.utils.chat_utils import to_str_many
from vk_girl_dater.usecases.flirt_with_girl_command import FlirtWithGirlCommand

young_date = '2025-01-01T12:00:00.000Z'
old_date = '2025-01-01T11:30:00.000Z'

class TestalbeFlirtWithGirlCommand(FlirtWithGirlCommand):
    def _get_chats_for_flirt(self):
        chats = super()._get_chats_for_flirt()
        self.chats_for_flirt = to_str_many(chats)
        return chats

    def _get_current_date(self):
        return datetime.strptime(young_date, "%Y-%m-%dT%H:%M:%S.%fZ").replace(tzinfo=timezone.utc)


class TestFlirtWithGirlCommand:
    def setup_method(self):
        self.command = TestalbeFlirtWithGirlCommand()
        self.command.flirt_platform = SpyFlirtPlatform()
        self.command.flirter = SpyFlirter()
        self.command.chat_repository = SpyChatRepository()

        self.plt = self.command.flirt_platform
        self.flirter = self.command.flirter
        self.chat_repository = self.command.chat_repository

    def test_get_chats_for_flirt__when_no_messages_in_chat(self):
        self.command.flirt_platform.chats = [
            {'id':1, 'messages':[], 'name': 'test'},
        ]
        self.command.execute()

        assert self.command.chats_for_flirt == [1]
        assert self.command.flirt_platform.sended_messages == ["1 привет как дела?"]

    def test_get_chats_for_flirt__when_last_message_is_old_enough(self):
        self.command.flirt_platform.chats = [
            {'id':1, 'messages':[{'text':'привет, я вика', 'date': young_date}]},
            {'id':2, 'messages':[{'text':'привет, я катя', 'date': old_date}]},
        ]
        self.command.execute()

        assert self.command.chats_for_flirt == [2]
        assert self.command.flirt_platform.sended_messages == ["2 привет как дела?"]


    def test_save_chats_in_repository(self):
        self.command.flirt_platform.chats = [
            {'id':1, 'messages':[{'text':'привет, я вика', 'date': young_date}]},
        ]

        self.command.execute()
        assert self.chat_repository.is_save_called == True