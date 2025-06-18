from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QListWidget, QListWidgetItem, QApplication

from vk_girl_dater import gui
from vk_girl_dater.gui.girl_item_widget import GirlItemWidget
from vk_girl_dater.gui.girl_chat_window import GirlChatWindow


class GirlListWidget(QListWidget):
    def __init__(self, chats_info):
        super().__init__()
        self.chats_info = chats_info
        self.itemClicked.connect(self.on_item_clicked)
        for chat_info in chats_info:
            self.add_girl(chat_info)

    def add_girl(self, chat_info):
        item = QListWidgetItem(self)
        widget = GirlItemWidget(chat_info)
        item.setSizeHint(widget.sizeHint())
        self.setItemWidget(item, widget)
        item.setData(Qt.ItemDataRole.UserRole, chat_info['name'])

    def on_item_clicked(self, item):
        main_window = self.parent()
        index = self.row(item)
        chat_info = self.chats_info[index]
        event = {
            'name': 'get_chat',
            'context': {
                'user_id': chat_info['id']
            }
        }
        chat = gui.event_controller.handle_event(event)
        self.chat_window = GirlChatWindow(chat)
        main_window.hide()
        self.chat_window.exec()
        main_window.show()