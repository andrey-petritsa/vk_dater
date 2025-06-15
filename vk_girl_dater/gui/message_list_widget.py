from PyQt6.QtWidgets import QScrollArea, QWidget, QVBoxLayout

from vk_girl_dater.gui.message_widget import MessageWidget


class MessageListWidget(QScrollArea):
    def __init__(self):
        super().__init__()
        message_widget = QWidget()
        self.setWidgetResizable(True)
        chat_layout = QVBoxLayout(message_widget)
        self.__add_message(chat_layout, "Андрей", "Привет как дела")
        self.__add_message(chat_layout, "Екатерина", "Неплохо, как сам?")
        self.__add_message(chat_layout, "Андрей", "Хорошо")
        chat_layout.addStretch()
        self.setLayout(chat_layout)
        self.setWidget(message_widget)

    def __add_message(self, layout, sender, text):
        message = {'sender_name': sender,'text': text}
        message_widget = MessageWidget(message)
        layout.addLayout(message_widget.message_container)