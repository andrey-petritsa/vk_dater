import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QTextEdit, QPushButton


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt6: Вывод текста построчно")
        self.setGeometry(100, 100, 400, 300)

        self.text_edit = QTextEdit()
        self.text_edit.setReadOnly(True)

        self.button = QPushButton("Добавить строку")
        self.button.clicked.connect(self.add_line)

        layout = QVBoxLayout()
        layout.addWidget(self.text_edit)
        layout.addWidget(self.button)
        self.setLayout(layout)

        self.line_counter = 1

    def add_line(self):
        text = f"Это строка номер {self.line_counter}"
        self.text_edit.append(text)
        self.line_counter += 1


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())