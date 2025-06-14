from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QListWidget, QListWidgetItem, QApplication

from vk_girl_dater.gui.girl_item_widget import GirlItemWidget
from vk_girl_dater.gui.girl_detail_window import GirlDetailWindow


class GirlListWidget(QListWidget):
    def __init__(self):
        super().__init__()
        self.detail_window = None
        self.itemClicked.connect(self.on_item_clicked)
        self.add_girl('Анна')
        self.add_girl('Мария')

    def add_girl(self, name):
        item = QListWidgetItem(self)
        widget = GirlItemWidget(name)
        item.setSizeHint(widget.sizeHint())
        self.setItemWidget(item, widget)
        item.setData(Qt.ItemDataRole.UserRole, name)

    def on_item_clicked(self, item):
        main_window = self.parent()
        self.detail_window = GirlDetailWindow()
        main_window.hide()
        self.detail_window.exec()
        main_window.show()