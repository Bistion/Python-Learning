from PySide6.QtWidgets import QApplication
from mainwindow import MainWindow
import sys

app = QApplication(sys.argv) # creates the application

window = MainWindow(app) # specifies we want a window in our application
window.show() # we want to show this window

app.exec() # execute the application 

