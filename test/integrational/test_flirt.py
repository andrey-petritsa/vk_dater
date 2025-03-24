from vk_girl_dater.main.flirt_command_factory import FlirtCommandFactory


class TestFlirt:
    def test_flirt(self):
        command = FlirtCommandFactory.create()
        command.execute()

        chats = command.chat_repository.find_all_chats()
        assert len(chats) > 0
