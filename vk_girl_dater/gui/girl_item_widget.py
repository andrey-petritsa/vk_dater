import requests
from PyQt6.QtCore import Qt, QByteArray
from PyQt6.QtGui import QPixmap, QColor
from PyQt6.QtWidgets import QWidget, QLabel, QHBoxLayout


class GirlItemWidget(QWidget):
    def __init__(self, chat_info):
        super().__init__()
        
        name_label = QLabel(chat_info['name'])
        avatar_label = self._create_avatar_label(chat_info)

        layout = QHBoxLayout()
        layout.addWidget(avatar_label)
        layout.addWidget(name_label)
        layout.addStretch()
        
        self.setLayout(layout)

    def _create_avatar_label(self, chat_info):
        size = 200
        avatar_label = QLabel()
        avatar_label.setFixedSize(size, size)

        if 'avatar_url' in chat_info and chat_info['avatar_url']:
            response = requests.get(chat_info['avatar_url'])
            image_data = QByteArray(response.content)
            pixmap = QPixmap()
            pixmap.loadFromData(image_data)
            pixmap = pixmap.scaled(size, size, Qt.AspectRatioMode.KeepAspectRatio)
        else:
            pixmap = QPixmap(size, size)
            pixmap.fill(QColor(0, 100, 0))

        avatar_label.setPixmap(pixmap)
        return avatar_label