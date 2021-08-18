import sys

from PySide6.QtGui import QFont
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout


class BasicApp(QWidget):

    def __init__(self):
        super().__init__()

        self.text_label = QLabel()
        self.text_label.setText("Hello World!")
        self.text_label.setFont(QFont('Arial', 20))

        self.button = QPushButton("Click to Change")
        self.button.setFont(QFont('PT Mono', 14))
        self.button.clicked.connect(lambda: self.text_label.setText("Changed!"))

        self.setGeometry(50, 50, 300, 200)
        self.setWindowTitle("PySide6 Example")

        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.text_label)
        self.layout.addWidget(self.button)
        self.setLayout(self.layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    basic_app = BasicApp()
    basic_app.show()
    sys.exit(app.exec())
