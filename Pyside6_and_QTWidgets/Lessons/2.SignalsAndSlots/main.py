# Using signals and slots

from PySide6.QtWidgets import QApplication, QPushButton, QSlider

#Version 1 : Just responding to the button click : Syntax
"""
#The slot : response when something happens
def button_clicked(data):
    print("You clicked the button, didn't you!)

app = QApplication()
button = QPushButton("Press Me")

#clicked is a signal of QPushButton.  It is emitted when you click on the button.
#You can wire a slot to the signal using the syntax below
button.clicked.connect(button_clicked)

button.show()
app.exec()
"""

#Version 2 : Signals sending values, capture values in slots
"""
#The slot : response when something happens
def button_clicked(data):
    print("You clicked the button, didn't you! checked : ", data)

app = QApplication()
button = QPushButton("Press Me")
button.setCheckable(True) # Makes the button checkage.  It is unchecked by default and clicking cycles it.

#clicked is a signal of QPushButton.  It is emitted when you click on the button.
#You can wire a slot to the signal using the syntax below
button.clicked.connect(button_clicked)

button.show()
app.exec()
"""

#Version 3 : Adding a slider and connecting to report back position
from PySide6.QtCore import Qt

def respond_to_slider(data):
    print("Slider moved to : ", data)

app = QApplication()
slider = QSlider(Qt.Horizontal)
slider.setMinimum(1)
slider.setMaximum(100)
slider.setValue(25)

#This makes the connection from slider to respond_to_slider
slider.valueChanged.connect(respond_to_slider)
slider.show()
app.exec()
