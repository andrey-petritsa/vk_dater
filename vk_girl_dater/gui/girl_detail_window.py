from PyQt6.QtWidgets import QDialog, QVBoxLayout, QPushButton, QLabel
from PyQt6.QtCore import QRect, QPoint


class GirlDetailWindow(QDialog):
    def __init__(self, name, parent=None):
        super().__init__(parent)
        self.setWindowTitle(f"Информация о {name}")
        self.parent_window = parent

        self.setGeometry(100, 100, 400, 500)
        self.center_window()

        layout = QVBoxLayout()

        info_label = QLabel(f"Профиль девушки: {name}")
        layout.addWidget(info_label)

        back_button = QPushButton("Назад")
        back_button.clicked.connect(self.on_back_clicked)
        layout.addWidget(back_button)

        self.setLayout(layout)

    def on_back_clicked(self):
        self.accept()

    def center_window(self):
        screen = self.screen().geometry()
        window_size = self.geometry()
        center_point = screen.center()
        new_rect = QRect(QPoint(0, 0), window_size.size())
        new_rect.moveCenter(center_point)
        self.setGeometry(new_rect)
