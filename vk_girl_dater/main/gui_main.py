import sys
from PyQt6.QtWidgets import QApplication

from vk_girl_dater.gui.event_controller import EventController
from vk_girl_dater.gui.main_widnow import MainWindow
import vk_girl_dater.gui as gui
import vk_girl_dater.utils as utils
import vk_girl_dater.usecases as usecases
from vk_girl_dater.gui.stub_event_controller import StubEventController
from vk_girl_dater.main.usecase_factory import UsecaseFactory
from vk_girl_dater.presenters.chat_presenter import ChatPresenter
from vk_girl_dater.utils.console_logger import ConsoleLogger


def setup_usecases():
    factory = UsecaseFactory()
    usecases.get_message_options_command = factory.create_get_message_options_command()
    usecases.send_message_command = factory.create_send_message_command()
    usecases.get_chats_command = factory.create_get_main_screen_command()
    usecases.get_chat_command = factory.create_get_chat_command()
    usecases.get_chats_info_command = factory.create_get_chats_info_command()

def get_chat_info_views():
    presenter = ChatPresenter()
    chat_infos = usecases.get_chats_info_command.execute()

    chat_info_views = []
    for chat_info in chat_infos:
        chat_info_view = presenter.to_view_chat_info(chat_info)
        chat_info_views.append(chat_info_view)
    return chat_info_views

def setup_utils():
    gui.event_controller = EventController()
    utils.logger = ConsoleLogger()

if __name__ == "__main__":
    setup_utils()
    setup_usecases()
    app = QApplication(sys.argv)
    chats_info_views = get_chat_info_views()
    window = MainWindow(chats_info_views)
    window.show()
    sys.exit(app.exec())