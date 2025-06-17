import sys
from PyQt6.QtWidgets import QApplication

from vk_girl_dater.gui.main_widnow import MainWindow
import vk_girl_dater.gui as gui
import vk_girl_dater.utils as utils
from vk_girl_dater.gui.stub_event_controller import StubEventController
from vk_girl_dater.utils.console_logger import ConsoleLogger




def setup_utils():
    gui.event_controller = StubEventController()
    utils.logger = ConsoleLogger()

if __name__ == "__main__":
    setup_utils()
    app = QApplication(sys.argv)
    chats_view_model = gui.chats_view_model
    window = MainWindow(chats_view_model)
    window.show()
    sys.exit(app.exec())