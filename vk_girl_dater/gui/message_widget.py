from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QHBoxLayout


class MessageWidget(QWidget):
    def __init__(self, message):
        super().__init__()
        self.content_widget = QWidget()
        self.content_widget.setLayout(self.__get_content_layout(message))
        self.setLayout(self.__get_message_layout(message) )
        self.__set_size()

    def __get_message_layout(self, message):
        layout = QHBoxLayout()
        if message['position'] == "left":
            self.content_widget.setStyleSheet("background-color: #DCF8C6; border-radius: 10px; margin: 2px;")
            layout.addStretch()
            layout.addWidget(self.content_widget)
        else:
            self.content_widget.setStyleSheet("background-color: #ECECEC; border-radius: 10px; margin: 2px;")
            layout.addWidget(self.content_widget)
            layout.addStretch()
        return layout

    def __set_size(self):
        self.setMinimumWidth(200)
        self.setMinimumHeight(100)

    def __get_content_layout(self, message):
        layout = QVBoxLayout(self.content_widget)
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