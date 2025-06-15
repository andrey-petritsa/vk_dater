from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QHBoxLayout


class MessageWidget(QWidget):
    def __init__(self, message):
        super().__init__()
        self.setLayout(self.__get_main_layout(message))
        self.message_container = self.__get_message_container(message)
        self.__set_size()


    def __set_size(self):
        self.setMinimumWidth(200)
        self.setMaximumWidth(300)

    def __get_message_container(self, message):
        layout = QHBoxLayout()
        if message['name'] == "Андрей":
            self.setStyleSheet("background-color: #DCF8C6; border-radius: 10px; margin: 2px;")
            layout.addStretch()
            layout.addWidget(self)
        else:
            self.setStyleSheet("background-color: #ECECEC; border-radius: 10px; margin: 2px;")
            layout.addWidget(self)
            layout.addStretch()
        return layout

    def __get_main_layout(self, message):
        layout = QVBoxLayout(self)
        layout.setSpacing(2)
        layout.addWidget(self.__get_sender_label(message))
        layout.addWidget(self.__get_text_label(message))
        layout.setContentsMargins(10, 10, 10, 10)
        return layout

    def __get_text_label(self, message):
        text_label = QLabel(message['text'])
        text_label.setWordWrap(True)
        text_label.setTextInteractionFlags(Qt.TextInteractionFlag.TextSelectableByMouse)
        text_label.setStyleSheet("color: black; font-size: 12px;")
        return text_label

    def __get_sender_label(self, message):
        sender_label = QLabel(message['name'])
        sender_label.setStyleSheet("font-weight: bold;")
        return sender_label
