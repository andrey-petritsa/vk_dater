from PyQt6.QtWidgets import QScrollArea, QWidget, QVBoxLayout

from vk_girl_dater.gui.message_widget import MessageWidget


class MessageListWidget(QScrollArea):
    def __init__(self, messages):
        super().__init__()
        wdg = QWidget()
        self.setWidgetResizable(True)
        layout = QVBoxLayout(wdg)
        for message in messages:
            widget = MessageWidget(message)
            layout.addLayout(widget.message_layout)
        layout.addStretch()
        self.setLayout(layout)
        self.setWidget(wdg)