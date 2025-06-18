import sys
from PyQt6.QtWidgets import QApplication

from vk_girl_dater.gui.event_controller import EventController
from vk_girl_dater.gui.main_widnow import MainWindow
import vk_girl_dater.gui as gui
import vk_girl_dater.utils as utils
import vk_girl_dater.usecases as usecases
from vk_girl_dater.gui.stub_event_controller import StubEventController
from vk_girl_dater.main.usecase_factory import UsecaseFactory
from vk_girl_dater.utils.console_logger import ConsoleLogger


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

if __name__ == "__main__":
    setup_utils()
    setup_usecases()
    app = QApplication(sys.argv)
    chats_info = usecases.get_chats_info_command.execute()
    window = MainWindow(chats_info)
    window.show()
    sys.exit(app.exec())