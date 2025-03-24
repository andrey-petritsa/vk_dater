import vk_girl_dater.gui as gui
from vk_girl_dater.gui.event_controller import EventController
from vk_girl_dater.main.usecase_factory import UsecaseFactory
import vk_girl_dater.usecases as usecases
import vk_girl_dater.utils as utils
from vk_girl_dater.utils import ConsoleLogger


def setup_usecases():
    factory = UsecaseFactory()
    usecases.get_message_options_command = factory.create_get_message_options_command()
    usecases.send_message_command = factory.create_send_message_command()
    usecases.get_chats_command = factory.create_get_main_screen_command()
    usecases.get_chat_command = factory.create_get_chat_command()
    usecases.get_chats_info_command = factory.create_get_chats_info_command()

def setup_utils():
    gui.event_controller = EventController()
    utils.logger = ConsoleLogger()