from PyQt6.QtWidgets import QDialog, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QScrollArea, QWidget, QTextEdit
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap, QColor

from vk_girl_dater.gui.message_widget import MessageWidget
from vk_girl_dater.gui.qt_utils import QtUtils


class GirlChatWindow(QDialog):
    def __init__(self, girl_name="Екатерина"):
        super().__init__()
        self.setLayout(self.__get_main_layout(girl_name))

        self.setWindowTitle(f"Чат с {girl_name}")
        self.setGeometry(100, 100, 500, 600)
        QtUtils.center(self)

    def __get_main_layout(self, girl_name):
        main_layout = QVBoxLayout()
        main_layout.addLayout(self.__get_header(girl_name))
        main_layout.addWidget(self.__get_chat_area())
        main_layout.addLayout(self.__get_input_layout())
        main_layout.addWidget(self.__get_back_button())
        return main_layout

    def __get_input_layout(self):
        input_layout = QHBoxLayout()
        input_layout.addWidget(self.__get_message_input())
        input_layout.addWidget(self.__get_send_button())
        return input_layout

    def __get_back_button(self):
        back_button = QPushButton("Назад")
        back_button.clicked.connect(self.on_back_clicked)
        return back_button

    def __get_send_button(self):
        send_button = QPushButton("Отправить")
        send_button.setFixedWidth(100)
        send_button.clicked.connect(self.on_send_clicked)
        return send_button

    def __get_message_input(self):
        message_input = QTextEdit()
        message_input.setFixedHeight(60)
        message_input.setPlaceholderText("Введите сообщение...")
        return message_input

    def __get_chat_area(self):
        chat_area = QScrollArea()
        chat_area.setWidgetResizable(True)
        chat_widget = QWidget()
        chat_layout = QVBoxLayout(chat_widget)
        self.__add_message(chat_layout, "Андрей", "Привет как дела")
        self.__add_message(chat_layout, "Екатерина", "Неплохо, как сам?")
        self.__add_message(chat_layout, "Андрей", "Хорошо")
        chat_layout.addStretch()
        chat_widget.setLayout(chat_layout)
        chat_area.setWidget(chat_widget)
        return chat_area

    def __get_header(self, girl_name):
        header_layout = QHBoxLayout()
        avatar_label = self.__get_avatar_label()
        header_layout.addWidget(avatar_label)
        name_label = QLabel(girl_name)
        name_label.setStyleSheet("font-size: 18px; font-weight: bold;")
        header_layout.addWidget(name_label)
        header_layout.addStretch()
        return header_layout

    def __get_avatar_label(self):
        size = 70
        avatar_label = QLabel()
        avatar_label.setFixedSize(size, size)

        pixmap = QPixmap(size, size)
        pixmap.fill(QColor(0, 100, 0))  # Зеленый цвет как заглушка

        avatar_label.setPixmap(pixmap)
        return avatar_label

    def __add_message(self, layout, sender, text):
        message = {'sender_name': sender,'text': text}
        message_widget = MessageWidget(message)
        layout.addLayout(message_widget.message_container)

    def on_send_clicked(self):
        pass

    def on_back_clicked(self):
        self.accept()
