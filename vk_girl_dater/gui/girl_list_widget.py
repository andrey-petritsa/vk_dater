from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QListWidget, QListWidgetItem, QApplication

from vk_girl_dater.gui.girl_item_widget import GirlItemWidget
from vk_girl_dater.gui.girl_chat_window import GirlChatWindow
import vk_girl_dater.gui as gui


class GirlListWidget(QListWidget):
    def __init__(self):
        super().__init__()
        self.itemClicked.connect(self.on_item_clicked)
        for girl in gui.girls_view_model:
            self.add_girl(girl['name'])

    def add_girl(self, name):
        item = QListWidgetItem(self)
        widget = GirlItemWidget(name)
        item.setSizeHint(widget.sizeHint())
        self.setItemWidget(item, widget)
        item.setData(Qt.ItemDataRole.UserRole, name)

    def on_item_clicked(self, item):
        main_window = self.parent()
        index = self.row(item)
        self.chat_window = GirlChatWindow(gui.girls_view_model[index])
        main_window.hide()
        self.chat_window.exec()
        main_window.show()