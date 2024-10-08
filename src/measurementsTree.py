from PyQt5.QtWidgets import *
from src.session import Session
from src.measurementTreeItem import measurementTreeItemSession, measurementTreeItemMeasurement

class measurementsTree(QWidget):
    def __init__(self, showDetailsSignalTarget):
        QWidget.__init__(self)

        self.showDetailsSignalTarget = showDetailsSignalTarget

        self.addButton = QPushButton("Add session", self)
        self.addButton.clicked.connect(self.addSession)

        self.scrollAreaLayout = QVBoxLayout()
        self.tree = QTreeWidget()
        self.tree.setColumnCount(1)
        self.tree.itemClicked.connect(self.showSessionDetails)

        self.sessions = Session.load("data/measurements")
        #self.sessionsTreeItems = [measurementTreeItemSession(self.tree, s, parent) for s in self.sessions]
        self.sessionsTreeItems = [measurementTreeItemSession(self.tree, s) for s in self.sessions]
        

        layout = QVBoxLayout()
        layout.addWidget(self.addButton)
        layout.addWidget(self.tree)
        self.setLayout(layout)

    def showSessionDetails(self, sender):
        if isinstance(sender, measurementTreeItemSession):
            self.showDetailsSignalTarget.showSessionDetails(sender)
        elif isinstance(sender, measurementTreeItemMeasurement): 
            self.showDetailsSignalTarget.showMeasurementDetails(sender)
        else:
            print("Unknown instance of item")

    def addSession(self):
        newSessionName = "newSession" 
        newNameFree = False
        while newNameFree == False:
            newNameFree = True
            for s in self.sessions:
                if s.name == newSessionName:
                    newSessionName += "_bis"
                    newNameFree = False;
                    break
        print("newNameFree = "+str(newNameFree)+" newSessionName = "+newSessionName)
        newSession = Session(newSessionName, "data/measurements")
        newItem = measurementTreeItemSession(self.tree, newSession)
        self.sessions.append(newSession)
        self.sessionsTreeItems.append(newItem)




