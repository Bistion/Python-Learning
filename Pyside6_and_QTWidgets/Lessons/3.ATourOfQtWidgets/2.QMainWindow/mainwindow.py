from PySide6.QtWidgets import QApplication, QMainWindow, QToolBar, QPushButton, QStatusBar
from PySide6.QtCore import QSize
from PySide6.QtGui import QAction, QIcon

class MainWindow(QMainWindow):
    def __init__(self, app):
        super().__init__()
        self.app = app # Declaring an app member
        self.setWindowTitle("Custom MainWindow")

        # Menubar and Menus
        menu_bar = self.menuBar() #creates menubar
        file_menu = menu_bar.addMenu("&File") #creates the first menu on menu_bar
        quit_action = file_menu.addAction("Quit") #adds an action to our specified menu
        quit_action.triggered.connect(self.quit_app) #connects to the defined action quit_app

        edit_menu = menu_bar.addMenu("&Edit")
        edit_menu.addAction("Copy")
        edit_menu.addAction("Cut")
        edit_menu.addAction("Paste")
        edit_menu.addAction("Undo")
        edit_menu.addAction("Redo")

        window_menu = menu_bar.addMenu("&Window")
        settings_menu = menu_bar.addMenu("&Settings")
        help_menu = menu_bar.addMenu("&Help")

        # Working with toolbars
        toolbar = QToolBar("My main toolbar") #creates the toolbar
        toolbar.setIconSize(QSize(16,16)) #sets size of toolbar
        self.addToolBar(toolbar) #adds toolbar to our class

        # Add the quit action to the toolbar
        toolbar.addAction(quit_action) #adds quit action to toolbar

        action1 = QAction("Some Action", self)
        action1.setToolTip("Status message for some action") #sets hovered over text
        action1.triggered.connect(self.toolbar_button_click) #connects to the defined action toolbar_button_click
        toolbar.addAction(action1) #adds action1 to toolbar

        action2 = QAction(QIcon("start.png"), "Some other action", self) # Adding an icon instead of words
        action2.setStatusTip("Status message for action2") # Sets the status bar message when you hover over action
        action2.triggered.connect(self.toolbar_button_click)
        action2.setCheckable(True)
        toolbar.addAction(action2)

        toolbar.setIconSize(QSize(30, 30)) #setting icon size

        toolbar.addSeparator() # adds a seperator to the toolbar
        toolbar.addWidget(QPushButton("Click Here")) # Add a widget to the toolbar on the other side of our seperator

        # Working with status bars
        self.setStatusBar(QStatusBar(self)) #add the status bar at the bottom of the window

        button1 = QPushButton("Button 1")
        button1.clicked.connect(self.button1_clicked)
        self.setCentralWidget(button1)


    def quit_app(self): 
        self.app.quit() #connects to our quit_action to close the program
    
    def toolbar_button_click(self):
        self.statusBar().showMessage("Message from my app", 3000)  #will show this message when toolbar_button_click gets called by either action 1 or action 2
                                                                    #the 3000 is set for timeout for when message will disappear
    def button1_clicked(self):
        print("Clicked on the button")

    