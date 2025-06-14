from PyQt6.QtWidgets import (QWidget, QListWidget, QHBoxLayout, QListWidgetItem)

from vk_girl_dater.gui.girl_item_widget import GirlItemWidget


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 400, 500)

        self.girls_list = QListWidget()
        self.girls_list.itemClicked.connect(self.on_item_clicked)

        main_layout = QHBoxLayout()
        main_layout.addWidget(self.girls_list)
        self.setLayout(main_layout)

        self.add_girl("Анна", "path/to/anna.jpg")
        self.add_girl("Мария", "path/to/maria.jpg")
        self.add_girl("Елена", "path/to/elena.jpg")

    def add_girl(self, name, image_path):
        item = QListWidgetItem()
        self.girls_list.addItem(item)
        widget = GirlItemWidget(name, image_path)
        item.setSizeHint(widget.sizeHint())
        self.girls_list.setItemWidget(item, widget)

    def on_item_clicked(self, item):
        print("Привет")