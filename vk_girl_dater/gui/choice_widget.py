from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QButtonGroup, QHBoxLayout, QRadioButton, QTextEdit


class ChoiceWidget(QWidget):
    def __init__(self, options):
        super().__init__()

        main_layout = QVBoxLayout()
        self.button_group = QButtonGroup()

        for i, option in enumerate(options):
            option_widget = QWidget()
            option_layout = QHBoxLayout()
            option_widget.setLayout(option_layout)

            radio = QRadioButton()
            self.button_group.addButton(radio, i)
            option_layout.addWidget(radio, alignment=Qt.AlignmentFlag.AlignTop)

            text_edit = self.__get_text_edit(option)
            option_layout.addWidget(text_edit)

            main_layout.addWidget(option_widget)

        self.button_group.buttonClicked.connect(self.on_button_clicked)
        self.setLayout(main_layout)

    def __get_text_edit(self, option):
        text_edit = QTextEdit()
        text_edit.setPlainText(option)
        text_edit.setReadOnly(True)
        return text_edit

    def on_button_clicked(self, button):
        index = self.button_group.id(button)
        print(f"Выбран вариант {index + 1}")
