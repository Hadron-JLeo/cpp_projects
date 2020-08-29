from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

def Window():
    app = QApplication(sys.argv)
    win = QMainWindow()

    screen_width = app.desktop().screenGeometry().width()
    screen_height = app.desktop().screenGeometry().height()
    
    win.setGeometry(0,0,500,550)
    win.setWindowTitle("Python Crafting System")

    win.show()
    sys.exit(app.exec_())

Window()