from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap, QColor
from PyQt6.QtWidgets import QWidget, QLabel, QHBoxLayout


class GirlItemWidget(QWidget):
    def __init__(self, name):
        super().__init__()
        
        name_label = QLabel(name)
        avatar_label = self._create_avatar_label()

        layout = QHBoxLayout()
        layout.addWidget(avatar_label)
        layout.addWidget(name_label)
        layout.addStretch()
        
        self.setLayout(layout)

    def _create_avatar_label(self):
        size = 50
        avatar_label = QLabel()
        avatar_label.setFixedSize(size, size)
        
        pixmap = QPixmap(size, size)
        pixmap.fill(QColor(0, 100, 0))
        
        avatar_label.setPixmap(pixmap)
        return avatar_label