from PySide6.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QLineEdit, QSizePolicy

class Widget(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Size Policies and Stretches")

        label = QLabel("My test: ")
        line_edit =QLineEdit()

        # Setting expanding horizontally and fixed vertically for line_edit
        line_edit.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Fixed)
        label.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Fixed)

        h_layout_1 = QHBoxLayout()

        # Adding an integer after naming the variable gives it a stretch value
        # By hovering over addWidget you can see this option plus the abiltiy to set alignment
        h_layout_1.addWidget(label, 1)
        h_layout_1.addWidget(line_edit, 2)

        button_1 = QPushButton("One")
        button_2 = QPushButton("Two")
        button_3 = QPushButton("Three")

        h_layout_2 = QHBoxLayout()
        h_layout_2.addWidget(button_1, 2)
        h_layout_2.addWidget(button_2, 1)
        h_layout_2.addWidget(button_3, 1)

        v_layout = QVBoxLayout()
        v_layout.addLayout(h_layout_1)
        v_layout.addLayout(h_layout_2)

        self.setLayout(v_layout)






        