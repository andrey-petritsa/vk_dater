from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap, QPainter, QColor
from PyQt6.QtWidgets import QWidget, QLabel, QHBoxLayout, QListWidgetItem


class GirlItemWidget(QListWidgetItem):
    def __init__(self, parent_list, name):
        super().__init__(parent_list)
        
        self.widget = self._create_widget(name)
        self.setSizeHint(self.widget.sizeHint())
        parent_list.setItemWidget(self, self.widget)

    def _create_widget(self, name):
        widget = QWidget()
        name_label = QLabel(name)
        avatar_label = self._create_avatar_label()

        layout = QHBoxLayout()
        layout.addWidget(avatar_label)
        layout.addWidget(name_label)
        layout.addStretch()
        
        widget.setLayout(layout)
        return widget

    def _create_avatar_label(self):
        size = 50
        avatar_label = QLabel()
        avatar_label.setFixedSize(size, size)
        
        pixmap = QPixmap(size, size)
        pixmap.fill(QColor(0, 100, 0))
        
        avatar_label.setPixmap(pixmap)
        return avatar_label