import sys
from PyQt6.QtWidgets import QApplication

from vk_girl_dater.gui.main_widnow import MainWindow
import vk_girl_dater.gui as gui
import vk_girl_dater.usecases as usecases
from vk_girl_dater.main.usecase_factory import UsecaseFactory

def setup_usecases():
    usecases.get_message_options_command = UsecaseFactory.create_get_message_options_command()
    usecases.send_message_command = UsecaseFactory.create_send_message_command()
    usecases.get_chats_command = UsecaseFactory.create_get_main_screen_command()


if __name__ == "__main__":
    setup_usecases()
    app = QApplication(sys.argv)
    chats_view_model = usecases.get_chats_command.execute()
    window = MainWindow(chats_view_model)
    window.show()
    sys.exit(app.exec())