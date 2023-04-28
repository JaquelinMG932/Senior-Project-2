import os
import sys
from PySide6.QtWidgets import QApplication
from mainwindow import *

# Displays screen
myApp = QApplication(sys.argv)
window = MainWindow(myApp)
window.show()
myApp.exec()
