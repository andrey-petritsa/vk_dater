from PyQt6.QtWidgets import QDialog, QVBoxLayout, QPushButton, QLabel
from PyQt6.QtCore import QRect, QPoint

from vk_girl_dater.gui.qt_utils import QtUtils


class GirlDetailWindow(QDialog):
    def __init__(self):
        super().__init__()

        self.setGeometry(100, 100, 400, 500)
        QtUtils.center(self)

        layout = QVBoxLayout()
        info_label = QLabel(f"Профиль девушки: Тест")
        layout.addWidget(info_label)

        back_button = QPushButton("Назад")
        back_button.clicked.connect(self.on_back_clicked)
        layout.addWidget(back_button)

        self.setLayout(layout)

    def on_back_clicked(self):
        self.accept()
