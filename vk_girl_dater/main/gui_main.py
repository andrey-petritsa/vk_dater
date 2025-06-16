import sys
from PyQt6.QtWidgets import QApplication

from vk_girl_dater.gui.main_widnow import MainWindow
import vk_girl_dater.gui as gui

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow(gui.girls_view_model)
    window.show()
    sys.exit(app.exec())