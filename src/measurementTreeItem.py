from PyQt5.QtWidgets import *
from src.measurement import Measurement

class measurementTreeItemMeasurement(QTreeWidgetItem):
    def __init__(self, measurement):
        QTreeWidgetItem.__init__(self)
        self.setText(0, measurement.name)
        self.measurement = measurement

class measurementTreeItemSession(QTreeWidgetItem):
    def __init__(self, tree, session):
        QTreeWidgetItem.__init__(self, tree)
        self.setText(0, session.name)
        for m in session.measurements:
            measurementItem = measurementTreeItemMeasurement(m)
            self.addChild(measurementItem)
        self.session = session
        #self.showDetailsSignalTarget = showDetailsSignalTarget
        #self.clicked.connect(self.showDetailsSignalTarget.showSessionDetails)

    def addMeasurement(self):
        newMeasurementName = "newMeasurements" 
        newNameFree = False
        while newNameFree == False:
            newNameFree = True
            for m in self.session.measurements:
                if m.name == newMeasurementName:
                    newMeasurementName += "_bis"
                    newNameFree = False;
                    break
        print("newNameFree = "+str(newNameFree)+" newMeasurementName = "+newMeasurementName)
        newMeasurement = Measurement(newMeasurementName, self.session)
        newItem = measurementTreeItemMeasurement(newMeasurement)
        self.session.measurements.append(newMeasurement)
        self.addChild(newItem)


