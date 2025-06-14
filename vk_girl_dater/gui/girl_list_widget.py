from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QListWidget, QListWidgetItem, QApplication

from vk_girl_dater.gui.girl_item_widget import GirlItemWidget
from vk_girl_dater.gui.girl_chat_window import GirlChatWindow


class GirlListWidget(QListWidget):
    def __init__(self):
        super().__init__()
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
        self.chat_window = GirlChatWindow()
        main_window.hide()
        self.chat_window.exec()
        main_window.show()