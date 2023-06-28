from PySide6.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout
from PySide6.QtGui import QPixmap

class Widget(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QLabel and Images")

        image_label = QLabel()
        image_label.setPixmap(QPixmap("images/Learning.png"))

        layout = QVBoxLayout()
        layout.addWidget(image_label)

        self.setLayout(layout)

        