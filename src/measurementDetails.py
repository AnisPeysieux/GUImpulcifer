from PyQt5.QtWidgets import *
from src.session import Session
from src.measurementTreeItem import measurementTreeItemSession
from src.multiCamViewWindow import *
from src.camView import *

class measurementDetails(QWidget):
    def __init__(self, parent):
        QWidget.__init__(self, parent)

class measurementDetailsSession(measurementDetails):
    def __init__(self, item, parent):
        measurementDetails.__init__(self, parent)

        self.treeItem = item

        self.nameLabel = QLabel(self.treeItem.session.name, self)
        print("Showing "+self.treeItem.session.name+" details")

        self.camViewButton = QPushButton("Cam", self)
        self.camViewButton.clicked.connect(self.launchCamView)

        self.addMeasurementButton = QPushButton("Add measurement", self)
        self.addMeasurementButton.clicked.connect(self.addMeasurement)

        layout = QVBoxLayout()
        layout.addWidget(self.nameLabel)
        layout.addWidget(self.addMeasurementButton)
        self.setLayout(layout)

    def addMeasurement(self):
        self.treeItem.addMeasurement()

    def launchCamView(self):

        c0 = tilingTreeItemCamView("c0")
        c2 = tilingTreeItemCamView("c2")
        c1 = tilingTreeItemCamView("c1")
        c1_c0 = tilingTreeItemCamView("c1_c0")
        c1_c1 = tilingTreeItemCamView("c1_c1")
        c1_c2 = tilingTreeItemCamView("c1_c2")
        c1_c0_c0 = tilingTreeItemCamView("c1_c0_c0")

        self.tTree = tilingTree()
        c0_t = self.tTree.addChild(c0, "Before", None, "H")
        c2_t = c0_t.addChild(c2, "After", c0, "H")
        c1_t = c2_t.addChild(c1, "Before", c2, "H")
        c1_c0_t = c1_t.addChild(c1_c0, "Before", c1, "V")
        c1_c1_t = c1_c0_t.addChild(c1_c1, "Before", c1_c0, "V")
        c1_c2_t = c1_c1_t.addChild(c1_c2, "After", c1_c1, "V")
        c1_c0_c0_t = c1_c0_t.addChild(c1_c0_c0, "Before", c1_c0, "H")

        print(self.tTree.printTree(0))
        self.tTree.show()
        print("tTree showed")

        #self.camView = camViewWindow()
        #self.camView.show()


class measurementDetailsMeasurement(measurementDetails):
    def __init__(self, item, parent):
        measurementDetails.__init__(self, parent)

        self.treeItem = item

        self.nameLabel = QLabel(self.treeItem.measurement.name)

        layout = QVBoxLayout()
        layout.addWidget(self.nameLabel)
        self.setLayout(layout)
