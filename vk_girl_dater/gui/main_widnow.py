from PyQt6.QtWidgets import (QWidget, QListWidget, QHBoxLayout, QListWidgetItem)
from PyQt6.QtCore import QRect, QPoint

from vk_girl_dater.gui.girl_item_widget import GirlItemWidget
from vk_girl_dater.gui.girl_list_widget import GirlListWidget


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 400, 500)
        self.center_window()

        girls_list = self.__create_girls_list()
        main_layout = QHBoxLayout()
        main_layout.addWidget(girls_list)
        self.setLayout(main_layout)

    def __create_girls_list(self):
        girls_list = GirlListWidget()
        girls_list.add_girl('Анна')
        girls_list.add_girl('Мария')

        return girls_list

    def center_window(self):
        screen = self.screen().geometry()
        window_size = self.geometry()
        center_point = screen.center()
        new_rect = QRect(QPoint(0, 0), window_size.size())
        new_rect.moveCenter(center_point)
        self.setGeometry(new_rect)

    def on_item_clicked(self, item):
        print("Привет")