import time
import vk_girl_dater.utils as utils
from vk_girl_dater.main.flirt_command_factory import FlirtCommandFactory
from vk_girl_dater.utils.console_logger import ConsoleLogger

utils.logger = ConsoleLogger()
command = FlirtCommandFactory.create()

while(True):
    command.execute()
    time.sleep(60 * 5)