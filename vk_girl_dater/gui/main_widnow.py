from PyQt6.QtWidgets import (QWidget, QListWidget, QHBoxLayout)
from PyQt6.QtCore import QRect, QPoint

from vk_girl_dater.gui.girl_item_widget import GirlItemWidget


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.girls_list = QListWidget()
        self.girls_list.itemClicked.connect(self.on_item_clicked)
        main_layout = QHBoxLayout()
        main_layout.addWidget(self.girls_list)
        self.setLayout(main_layout)
        GirlItemWidget(self.girls_list, 'Анна')
        GirlItemWidget(self.girls_list, 'Мария')

        self.setGeometry(100, 100, 400, 500)
        self.center_window()

    def center_window(self):
        screen = self.screen().geometry()
        window_size = self.geometry()
        center_point = screen.center()
        new_rect = QRect(QPoint(0, 0), window_size.size())
        new_rect.moveCenter(center_point)
        self.setGeometry(new_rect)

    def on_item_clicked(self, item):
        print("Привет")