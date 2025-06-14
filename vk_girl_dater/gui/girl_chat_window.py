from PyQt6.QtWidgets import QDialog, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QScrollArea, QWidget, QTextEdit
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap, QColor

from vk_girl_dater.gui.qt_utils import QtUtils


class GirlChatWindow(QDialog):
    def __init__(self, girl_name="Екатерина"):
        super().__init__()
        self.girl_name = girl_name

        self.setWindowTitle(f"Чат с {girl_name}")
        self.setGeometry(100, 100, 500, 600)
        QtUtils.center(self)

        main_layout = QVBoxLayout()

        # Верхняя секция с именем и аватаркой
        header_layout = QHBoxLayout()

        # Аватарка
        avatar_label = self._create_avatar_label()
        header_layout.addWidget(avatar_label)

        # Имя девушки
        name_label = QLabel(girl_name)
        name_label.setStyleSheet("font-size: 18px; font-weight: bold;")
        header_layout.addWidget(name_label)
        header_layout.addStretch()

        main_layout.addLayout(header_layout)

        # Чат с историей сообщений
        chat_area = QScrollArea()
        chat_area.setWidgetResizable(True)
        chat_widget = QWidget()
        chat_layout = QVBoxLayout(chat_widget)

        # Примеры сообщений в чате
        self._add_message(chat_layout, "Андрей", "Привет как дела")
        self._add_message(chat_layout, self.girl_name, "Неплохо, как сам?")
        self._add_message(chat_layout, "Андрей", "Хорошо")

        chat_layout.addStretch()
        chat_widget.setLayout(chat_layout)
        chat_area.setWidget(chat_widget)

        main_layout.addWidget(chat_area, 1)  # Растягиваем по вертикали

        # Поле для ввода нового сообщения
        input_layout = QHBoxLayout()
        self.message_input = QTextEdit()
        self.message_input.setFixedHeight(60)
        self.message_input.setPlaceholderText("Введите сообщение...")
        input_layout.addWidget(self.message_input)

        send_button = QPushButton("Отправить")
        send_button.setFixedWidth(100)
        send_button.clicked.connect(self.on_send_clicked)
        input_layout.addWidget(send_button)

        main_layout.addLayout(input_layout)

        # Кнопка назад
        back_button = QPushButton("Назад")
        back_button.clicked.connect(self.on_back_clicked)
        main_layout.addWidget(back_button)

        self.setLayout(main_layout)

    def _create_avatar_label(self):
        size = 70
        avatar_label = QLabel()
        avatar_label.setFixedSize(size, size)

        pixmap = QPixmap(size, size)
        pixmap.fill(QColor(0, 100, 0))  # Зеленый цвет как заглушка

        avatar_label.setPixmap(pixmap)
        return avatar_label

    def _add_message(self, layout, sender, text):
        message_widget = QWidget()
        message_layout = QVBoxLayout(message_widget)
        message_layout.setSpacing(2)  # Уменьшаем отступы между элементами

        # Имя отправителя
        sender_label = QLabel(sender)
        sender_label.setStyleSheet("font-weight: bold;")

        # Текст сообщения
        text_label = QLabel(text)
        text_label.setWordWrap(True)  # Включаем перенос слов
        text_label.setTextInteractionFlags(Qt.TextInteractionFlag.TextSelectableByMouse)  # Делаем текст выделяемым

        # Делаем текст более видимым
        text_label.setStyleSheet("color: black; font-size: 12px;")

        message_layout.addWidget(sender_label)
        message_layout.addWidget(text_label)
        message_layout.setContentsMargins(10, 10, 10, 10)  # Увеличиваем внутренние отступы

        message_widget.setLayout(message_layout)

        # Добавляем выравнивание в зависимости от отправителя
        message_container = QHBoxLayout()
        if sender == "Андрей":
            message_widget.setStyleSheet("background-color: #DCF8C6; border-radius: 10px; margin: 2px;")
            message_container.addStretch()
            message_container.addWidget(message_widget)
        else:
            message_widget.setStyleSheet("background-color: #ECECEC; border-radius: 10px; margin: 2px;")
            message_container.addWidget(message_widget)
            message_container.addStretch()

        # Устанавливаем минимальную ширину для сообщений
        message_widget.setMinimumWidth(200)
        message_widget.setMaximumWidth(300)  # Ограничиваем максимальную ширину

        layout.addLayout(message_container)

    def on_send_clicked(self):
        message = self.message_input.toPlainText().strip()
        if message:
            chat_layout = self.findChild(QScrollArea).widget().layout()
            self._add_message(chat_layout, "Андрей", message)
            self.message_input.clear()

            # Автоматический ответ от девушки (для демонстрации)
            # В реальном приложении здесь может быть логика генерации ответа
            if self.girl_name:
                self._add_message(chat_layout, self.girl_name, "Хорошо, понятно")

    def on_back_clicked(self):
        self.accept()
