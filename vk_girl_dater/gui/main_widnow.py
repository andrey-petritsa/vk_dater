from PyQt6.QtWidgets import QWidget, QHBoxLayout

from vk_girl_dater.gui.girl_list_widget import GirlListWidget
from vk_girl_dater.gui.qt_utils import QtUtils


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 400, 500)
        QtUtils.center(self)

        girls_list = GirlListWidget()
        main_layout = QHBoxLayout()
        main_layout.addWidget(girls_list)
        self.setLayout(main_layout)

    def on_item_clicked(self, item):
        print("Привет")