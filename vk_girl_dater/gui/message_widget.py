from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QHBoxLayout


class MessageWidget(QWidget):
    def __init__(self, message):
        super().__init__()
        message_layout = self.__get_message_layout(message)
        self.setLayout(message_layout)

        self.message_container = self.__get_message_container(message)
        self.__set_size()
        

    def __set_size(self):
        self.setMinimumWidth(200)
        self.setMaximumWidth(300)

    def __get_message_container(self, message):
        message_container = QHBoxLayout()
        if message['sender_name'] == "Андрей":
            self.setStyleSheet("background-color: #DCF8C6; border-radius: 10px; margin: 2px;")
            message_container.addStretch()
            message_container.addWidget(self)
        else:
            self.setStyleSheet("background-color: #ECECEC; border-radius: 10px; margin: 2px;")
            message_container.addWidget(self)
            message_container.addStretch()
        return message_container

    def __get_message_layout(self, message):
        message_layout = QVBoxLayout(self)
        message_layout.setSpacing(2)
        message_layout.addWidget(self.__get_sender_label(message))
        message_layout.addWidget(self.__get_text_label(message))
        message_layout.setContentsMargins(10, 10, 10, 10)
        return message_layout

    def __get_text_label(self, message):
        text_label = QLabel(message['text'])
        text_label.setWordWrap(True)
        text_label.setTextInteractionFlags(Qt.TextInteractionFlag.TextSelectableByMouse)
        text_label.setStyleSheet("color: black; font-size: 12px;")
        return text_label

    def __get_sender_label(self, message):
        sender_label = QLabel(message['sender_name'])
        sender_label.setStyleSheet("font-weight: bold;")
        return sender_label
