import src.session
from src.mainWindow import mainWindow
from PyQt5.QtWidgets import *
import sys

sessions = src.session.Session.load("data/measurements")
for s in sessions:
    print(s)

app = QApplication.instance()
if not app:
    app = QApplication(sys.argv)

win = mainWindow()
win.show()
app.exec_()
