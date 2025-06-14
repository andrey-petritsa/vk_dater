from PyQt6.QtWidgets import QListWidget, QListWidgetItem

from vk_girl_dater.gui.girl_item_widget import GirlItemWidget


class GirlListWidget(QListWidget):
    def __init__(self):
        super().__init__()

        self.itemClicked.connect(self.on_item_clicked)

    def add_girl(self, name):
        item = QListWidgetItem(self)
        widget = GirlItemWidget(name)
        item.setSizeHint(widget.sizeHint())
        self.setItemWidget(item, widget)

    def on_item_clicked(self, item):
        print("Привет")