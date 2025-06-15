from PyQt6.QtWidgets import QScrollArea, QWidget, QVBoxLayout

from vk_girl_dater.gui.message_widget import MessageWidget


class MessageListWidget(QScrollArea):
    def __init__(self, messages):
        super().__init__()
        wdg = QWidget()
        self.setWidgetResizable(True)
        chat_layout = QVBoxLayout(wdg)
        for message in messages:
            widget = MessageWidget(message)
            chat_layout.addLayout(widget.message_layout)
        chat_layout.addStretch()
        self.setLayout(chat_layout)
        self.setWidget(wdg)