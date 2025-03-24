import time

from vk_girl_dater.main.flirt_command_factory import FlirtCommandFactory

command = FlirtCommandFactory.create()

while(True):
    command.execute()
    time.sleep(60 * 5)