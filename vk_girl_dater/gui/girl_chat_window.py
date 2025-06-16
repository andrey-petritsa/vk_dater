from PyQt6.QtWidgets import QDialog, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QScrollArea, QWidget, QTextEdit
from PyQt6.QtGui import QPixmap, QColor

from vk_girl_dater.gui.choice_widget import ChoiceWidget
from vk_girl_dater.gui.event_controller import EventController
from vk_girl_dater.gui.message_list_widget import MessageListWidget
from vk_girl_dater.gui.qt_utils import QtUtils


class GirlChatWindow(QDialog):
    def __init__(self, chat):
        super().__init__()
        self.chat = chat
        self.message_input = None
        self.options = []

        self.setLayout(self.__get_main_layout())

        self.setWindowTitle(f"Чат с {self.chat['name']}")
        self.setGeometry(100, 100, 500, 600)
        QtUtils.center(self)

    def __get_main_layout(self):
        main_layout = QVBoxLayout()
        main_layout.addLayout(self.__get_header())
        main_layout.addWidget(MessageListWidget(self.chat['messages']))
        main_layout.addLayout(self.__get_input_layout())
        main_layout.addWidget(ChoiceWidget(self.options))
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
        self.message_input = QTextEdit()
        self.message_input.setFixedHeight(60)
        self.message_input.setPlaceholderText("Введите сообщение...")
        return self.message_input

    def __get_header(self):
        header_layout = QHBoxLayout()
        avatar_label = self.__get_avatar_label()
        header_layout.addWidget(avatar_label)
        name_label = QLabel(self.chat['name'])
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

    def on_send_clicked(self):
        message_text = self.message_input.toPlainText().strip()
        event = {
            'name': 'send_message',
            'context': {
                'text': message_text, 'chat_id': self.chat['id']
            }
        }
        EventController.handle_event(event)
        self.message_input.clear()

    def on_back_clicked(self):
        self.accept()

    def showEvent(self, event):
        super().showEvent(event)
        event = {
            'name': 'show_options',
            'context': {
                'chat': self.chat
            },
        }
        self.options = EventController.handle_event(event)