from PyQt6.QtWidgets import QScrollArea, QWidget, QVBoxLayout

from vk_girl_dater.gui.message_widget import MessageWidget


class MessageListWidget(QScrollArea):
    def __init__(self, messages):
        super().__init__()
        self.setWidgetResizable(True)
        layout = QVBoxLayout()
        widgets = []
        for message in messages:
            widgets.append(MessageWidget(message))

        for widget in widgets:
            layout.addLayout(widget.message_layout)

        layout.addStretch()
        self.setLayout(layout)
