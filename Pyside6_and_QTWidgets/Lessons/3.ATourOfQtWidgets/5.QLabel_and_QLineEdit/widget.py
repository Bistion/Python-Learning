from PySide6.QtWidgets import QLabel, QLineEdit, QWidget, QPushButton, QVBoxLayout, QHBoxLayout

class Widget(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QLabel and QLineEdit")

        label = QLabel("Fullname: ") # Create the label
        self.line_edit = QLineEdit() # Create the edit text block
        # These are are signals linked to slots below
        #self.line_edit.textChanged.connect(self.text_changed)
        #self.line_edit.cursorPositionChanged.connect(self.cursor_position_changed)
        #self.line_edit.editingFinished.connect(self.editting_finished)
        #self.line_edit.returnPressed.connect(self.return_pressed)
        #self.line_edit.selectionChanged.connect(self.selection_changed)
        self.line_edit.textEdited.connect(self.text_edited)

        button = QPushButton("Grab Data") # Button that can be pushed
        button.clicked.connect(self.button_clicked) # Adding a slot and signal to pull entered data
        self.text_holder_label = QLabel("I am here") # Another label

        # Horizontal layout with our label and edit block
        h_layout = QHBoxLayout()
        h_layout.addWidget(label)
        h_layout.addWidget(self.line_edit)

        # Vertical layout where we add the horizontal layout at the top
        # and then add our button and other label
        v_layout = QVBoxLayout()
        v_layout.addLayout(h_layout)
        v_layout.addWidget(button)
        v_layout.addWidget(self.text_holder_label)

        self.setLayout(v_layout) # Sets v_layout as the overall layout we want.  This already includes pulling h_layout into it

    # Slots
    def button_clicked(self):
        print("Fullname: ", self.line_edit.text()) # This will pull the typed info from our line edit field as TEXT when button is clicked
        self.text_holder_label.setText(self.line_edit.text()) # This updates the text_holder_label at the bottom of the widget with our entered value from line_edit

    def text_changed(self): #this slot will update the bottom label as we type into the line_edit box
        self.text_holder_label.setText(self.line_edit.text())

    def cursor_position_changed(self, old, new): #This will print the location of the cursor as you type or move it in our line_edit box
        print("Cursor old position: ",old," and new position: ",new)

    def editting_finished(self): # This will do something when you are done editting the line_edit box.  This triggers on hitting enter
        print("Editting finished")

    def return_pressed(self): # This will trigger when you hit return when inside the line_edit box.
        print("You pressed return")

    def selection_changed(self): # Triggers when you select text in line_edit with your mouse
        print("Your selection changed: ",self.line_edit.selectedText())

    def text_edited(self, new_text): # Can be used to show what changed when edited.
        print("Text edited. New text: ", new_text)