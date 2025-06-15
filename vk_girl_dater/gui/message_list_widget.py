from PyQt6.QtWidgets import QScrollArea, QWidget, QVBoxLayout

from vk_girl_dater.gui.message_widget import MessageWidget


class MessageListWidget(QScrollArea):
    def __init__(self, messages):
        super().__init__()
        message_widget = QWidget()
        self.setWidgetResizable(True)
        chat_layout = QVBoxLayout(message_widget)
        for message in messages:
            widget = MessageWidget(message)
            chat_layout.addLayout(widget.message_container)
        chat_layout.addStretch()
        self.setLayout(chat_layout)
        self.setWidget(message_widget)