from PyQt5.QtWidgets import *

class processingsTab(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        layout = QHBoxLayout()
        self.label = QLabel("Processings tab widget")
        layout.addWidget(self.label)
        self.setLayout(layout)
