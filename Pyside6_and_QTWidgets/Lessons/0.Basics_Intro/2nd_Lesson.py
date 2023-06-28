from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

# sys allow me to run command line arguments
import sys

app = QApplication(sys.argv)

window = QMainWindow()
window.setWindowTitle("Our first MainWindow APP!")

button = QPushButton()
button.setText("Press Me")

window.setCentralWidget(button)

window.show()
app.exec()