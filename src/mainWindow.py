from PyQt5.QtWidgets import *
from src.measurementsTab import measurementsTab
from src.processingsTab import processingsTab


class mainWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("GUImpulcifer")

        self.menuBar = QMenuBar(self)
        fileMenu = self.menuBar.addMenu('File')
        editMenu = self.menuBar.addMenu('Edit')
        optionsMenu = self.menuBar.addMenu('Options')
        helpMenu = self.menuBar.addMenu('Help')

        self.tabs = QTabWidget()
        self.measurementsTab = measurementsTab()
        self.processingsTab = processingsTab()
        self.tabs.addTab(self.measurementsTab, "Measurements")
        self.tabs.addTab(self.processingsTab, "Processings")

        layout = QVBoxLayout()
        layout.addWidget(self.menuBar)
        layout.addWidget(self.tabs)
        self.setLayout(layout)
