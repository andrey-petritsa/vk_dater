import sys
from PyQt6.QtWidgets import QApplication

from vk_girl_dater.gui.main_widnow import MainWindow
import vk_girl_dater.usecases as usecases
from vk_girl_dater.main import setup_usecases, setup_utils
from vk_girl_dater.presenters.chat_presenter import ChatPresenter

def get_chat_info_views():
    presenter = ChatPresenter()
    chat_infos = usecases.get_chats_info_command.execute()

    chat_info_views = []
    for chat_info in chat_infos:
        chat_info_view = presenter.to_view_chat_info(chat_info)
        chat_info_views.append(chat_info_view)
    return chat_info_views

if __name__ == "__main__":
    setup_utils()
    setup_usecases()
    app = QApplication(sys.argv)
    chats_info_views = get_chat_info_views()
    window = MainWindow(chats_info_views)
    window.show()
    sys.exit(app.exec())