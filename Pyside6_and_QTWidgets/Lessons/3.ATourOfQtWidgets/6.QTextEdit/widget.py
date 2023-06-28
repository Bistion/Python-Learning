from PySide6.QtWidgets import QWidget, QTextEdit, QPushButton, QVBoxLayout, QHBoxLayout

class Widget(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QTextEdit")

        self.text_edit = QTextEdit()

        current_text_button = QPushButton("Current Text")
        current_text_button.clicked.connect(self.current_text_button_clicked)

        copy_button = QPushButton("Copy")
        copy_button.clicked.connect(self.text_edit.copy) # This uses a built in slot for QTextEdit

        cut_button = QPushButton("Cut")
        cut_button.clicked.connect(self.text_edit.cut) # This uses a built in slot for QTextEdit

        paste_button = QPushButton("Paste")
        paste_button.clicked.connect(self.paste) # Instead of the built in slot for QTextEdit being used her we define it below

        undo_button = QPushButton("Undo")
        undo_button.clicked.connect(self.text_edit.undo) # This uses a built in slot for QTextEdit

        redo_button = QPushButton("Redo")
        redo_button.clicked.connect(self.text_edit.redo) # This uses a built in slot for QTextEdit

        set_plain_text_button = QPushButton("Set Plain Text")
        set_plain_text_button.clicked.connect(self.set_plain_text)

        set_html_button = QPushButton("Set HTML")
        set_html_button.clicked.connect(self.set_html)

        clear_button = QPushButton("Clear")
        clear_button.clicked.connect(self.text_edit.clear)

        h_layout = QHBoxLayout()
        h_layout.addWidget(current_text_button)
        h_layout.addWidget(copy_button)
        h_layout.addWidget(cut_button)
        h_layout.addWidget(paste_button)
        h_layout.addWidget(undo_button)
        h_layout.addWidget(redo_button)
        h_layout.addWidget(set_plain_text_button)
        h_layout.addWidget(set_html_button)
        h_layout.addWidget(clear_button)

        v_layout = QVBoxLayout()
        v_layout.addLayout(h_layout)
        v_layout.addWidget(self.text_edit)

        self.setLayout(v_layout)

    def paste(self): # Instead of using the built in slot up with the Signal we declare it down here.  This is just extra lines since it can be done easier above.
        self.text_edit.paste()
    
    def set_plain_text(self):
        self.text_edit.setPlainText("string of information")

    def set_html(self):
        self.text_edit.setHtml("<h1>My title</h1><p>entered paragraph</p>")

    def current_text_button_clicked(self):
        print(self.text_edit.toPlainText())


       