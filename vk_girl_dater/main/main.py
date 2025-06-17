import time
import vk_girl_dater.utils as utils
import vk_girl_dater.usecases as usecases
from vk_girl_dater.main.flirt_command_factory import FlirtCommandFactory
from vk_girl_dater.main.usecase_factory import UsecaseFactory
from vk_girl_dater.utils.console_logger import ConsoleLogger

utils.logger = ConsoleLogger()
command = FlirtCommandFactory.create()



while(True):
    command.execute()
    time.sleep(60 * 5)