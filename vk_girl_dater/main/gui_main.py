import sys
from PyQt6.QtWidgets import QApplication

from vk_girl_dater.gui.main_widnow import MainWindow
import vk_girl_dater.gui as gui
import vk_girl_dater.usecases as usecases
from vk_girl_dater.main.usecase_factory import UsecaseFactory

def setup_usecases():
    usecases.get_message_options_command = UsecaseFactory.create_get_message_options_command()
    usecases.send_message_command = UsecaseFactory.create_send_message_command()


if __name__ == "__main__":
    setup_usecases()
    app = QApplication(sys.argv)
    window = MainWindow(gui.girls_view_model)
    window.show()
    sys.exit(app.exec())