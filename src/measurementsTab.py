from PyQt5.QtWidgets import *
from src.measurementsTree import measurementsTree
from src.measurementDetails import measurementDetails, measurementDetailsSession, measurementDetailsMeasurement, QSplitter
from PyQt5.QtCore import Qt

class measurementsTab(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        self.measurementsTreeGroup = QGroupBox(self)
        self.measurementsTreeGroupLayout = QGridLayout()
        self.measurementsTree = measurementsTree(self)
        self.measurementsTreeGroupLayout.addWidget(self.measurementsTree)
        self.measurementsTreeGroup.setLayout(self.measurementsTreeGroupLayout)

        self.measurementDetailsGroup = QGroupBox(self)
        self.measurementDetailsGroupLayout = QGridLayout()
        self.measurementDetails = measurementDetails(self)
        self.measurementDetailsGroupLayout.addWidget(self.measurementDetails)
        self.measurementDetailsGroup.setLayout(self.measurementDetailsGroupLayout)

        self.splitter = QSplitter(Qt.Horizontal)
        self.splitter.addWidget(self.measurementsTreeGroup)
        self.splitter.addWidget(self.measurementDetailsGroup)

        #layout = QHBoxLayout()
        #layout.addWidget(self.measurementsTreeGroup)
        #layout.addWidget(self.measurementDetailsGroup)
        #self.setLayout(layout)

        layout = QHBoxLayout()
        layout.addWidget(self.splitter)
        self.setLayout(layout)





    def showSessionDetails(self, sender):
        self.measurementDetails.deleteLater()
        self.measurementDetails = measurementDetailsSession(sender, self)
        self.measurementDetailsGroupLayout.addWidget(self.measurementDetails)

    def showMeasurementDetails(self, sender):
        self.measurementDetails.deleteLater()
        self.measurementDetails = measurementDetailsMeasurement(sender, self)
        self.measurementDetailsGroupLayout.addWidget(self.measurementDetails)
