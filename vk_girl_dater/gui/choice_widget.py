from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QButtonGroup, QHBoxLayout, QRadioButton, QTextEdit


class ChoiceWidget(QWidget):
    def __init__(self, options):
        super().__init__()

        layout = QVBoxLayout()
        self.button_group = QButtonGroup()

        for i, text in enumerate(options):
            option_widget = QWidget()
            option_layout = QHBoxLayout()
            option_widget.setLayout(option_layout)

            radio = QRadioButton()
            self.button_group.addButton(radio, i)
            option_layout.addWidget(radio, alignment=Qt.AlignmentFlag.AlignTop)

            text_edit = QTextEdit()
            text_edit.setPlainText(text)
            text_edit.setReadOnly(True)
            text_edit.setMaximumHeight(100)  # Ограничиваем высоту
            text_edit.setStyleSheet("""
                QTextEdit {
                    border: none;
                    background-color: transparent;
                }
            """)
            option_layout.addWidget(text_edit)

            layout.addWidget(option_widget)

        self.button_group.buttonClicked.connect(self.on_button_clicked)
        self.setLayout(layout)

    def on_button_clicked(self, button):
        index = self.button_group.id(button)
        print(f"Выбран вариант {index + 1}")
