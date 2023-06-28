from PySide6.QtWidgets import QApplication, QWidget

# sys allow me to run command line arguments
import sys

app = QApplication(sys.argv)

window = QWidget()
window.show()

app.exec()
