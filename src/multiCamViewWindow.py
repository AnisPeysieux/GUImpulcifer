from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from src.camView import camView
from PyQt5.QtCore import Qt, QMimeData
from PyQt5.QtGui import *

class tilingTreeMovement(QWidget):
    def __init__(self, item, label):
        QWidget.__init__(self)
        self.setAcceptDrops(True)
        self.item = item
        self.h = 50
        self.w = 50
        self.resize(50, 50)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.label = QLabel(label)
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.label)
        self.setLayout(self.layout)

    def dragEnterEvent(self, e):
        print("dragEnterEvent")
        #self.show()
        e.accept()

    def dragLeaveEvent(self, e):
        print("dragLeaveEvent")
        if not self.item.rect().contains(self.item.mapFromGlobal(QCursor.pos())):
            self.swapMovement.setVisible(False)
        e.accept()

        e.accept()

class tilingTreeMovementSwap(tilingTreeMovement):
    def __init__(self, item):
        tilingTreeMovement.__init__(self, item, "S")

    def showEvent(self, e):
        xItem = self.item.mapToGlobal(self.item.rect().center()).x()
        yItem = self.item.mapToGlobal(self.item.rect().center()).y()
        print("xItem = ", xItem)
        self.move(xItem-self.h, yItem-self.w/2)

    def dropEvent(self, e):
        print("dropEvent swap")
        print("source = ", e.source())

class tilingTreeMovementCopy(tilingTreeMovement):
    def __init__(self, item):
        tilingTreeMovement.__init__(self, item, "C")

    def showEvent(self, e):
        xItem = self.item.mapToGlobal(self.item.rect().center()).x()
        yItem = self.item.mapToGlobal(self.item.rect().center()).y()
        print("xItem = ", xItem)
        self.move(xItem, yItem-self.w/2)

    def dropEvent(self, e):
        print("dropEvent copy")



class tilingTreeItem(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setAcceptDrops(True)
        self.swapMovement = tilingTreeMovementSwap(self)
        self.copyMovement = tilingTreeMovementCopy(self)
        
    def __str__(self):
        return ""

    def mouseMoveEvent(self, e):
        if e.buttons() == Qt.LeftButton:
            drag = QDrag(self)
            mime = QMimeData()
            drag.setMimeData(mime)
            drag.exec_(Qt.MoveAction)

    def dragEnterEvent(self, e):
        print("dragEnterEvent")
        self.swapMovement.show()
        self.copyMovement.show()
        e.accept()

    def dragLeaveEvent(self, e):
        print("dragLeaveEvent")
        if not self.swapMovement.rect().contains(self.swapMovement.mapFromGlobal(QCursor.pos())):
            if not self.copyMovement.rect().contains(self.copyMovement.mapFromGlobal(QCursor.pos())):
                self.swapMovement.setVisible(False)
                self.copyMovement.setVisible(False)
        e.accept()

    def dragMoveEvent(self, e):
        #print("dragMoveEvent")
        answerRect = e.answerRect()
        coords = answerRect.getCoords()
        rect = answerRect.getRect()
        #print("coords = ", coords)
        #print("rect = ", rect)
        #print("w = ", self.width(), " h = ", self.height())
        e.accept()

    def dropEvent(self, e):
        #print("dropEvent")
        self.swapMovement.setVisible(False)
        self.copyMovement.setVisible(False)
        e.accept()

class tilingTreeItemCamView(tilingTreeItem):
    def __init__(self, name):
        tilingTreeItem.__init__(self)
        self.name = name
        self.camView = camView()
        if name == "c0":
            self.camView.start()
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.camView)
        self.setLayout(self.layout)

    def __str__(self):
        return self.name



class tilingTree(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.orientation = None
        self.tree_childs = []
        self.layout = QVBoxLayout()
        self.splitter = QSplitter(Qt.Horizontal)

    def addChild(self, newChild, pos, child, orientation):
        childPos = 0
        for c in self.tree_childs:
            if c == child:
                break;
            childPos += 1
        print("addChild: newChild=", newChild ,"tree_childs=", self.tree_childs, " childPos=", childPos)

        if len(self.tree_childs) < 2:
            self.orientation = orientation

        if orientation == self.orientation:
            if pos == "Before":
                self.tree_childs.insert(childPos, newChild)
            else:
                self.tree_childs.insert(childPos+1, newChild)
            self.initView()
            return self
        else:
            subTree = tilingTree()
            subTree.orientation = orientation
            subTree.addChild(self.tree_childs[childPos], "Before", None, orientation)
            subTree.addChild(newChild, pos, self.tree_childs[childPos], orientation)
            self.tree_childs[childPos] = subTree
            self.initView()
            return subTree

    def initView(self):
        self.splitter.deleteLater()
        if self.orientation == "H":
            self.splitter = QSplitter(Qt.Horizontal)
        else:
            self.splitter = QSplitter(Qt.Vertical)
        for c in self.tree_childs:
            if isinstance(c, tilingTree):
                c.initView()
                self.splitter.addWidget(c)
            else:
                self.splitter.addWidget(c)
        self.layout.addWidget(self.splitter)
        self.setLayout(self.layout)

    def printTree(self, level):
        thisstr = self.orientation
        for c in self.tree_childs:
            if isinstance(c, tilingTree):
                thisstr += "\n"+("|"+" "*5)*level+"|-----"+c.printTree(level+1)
            else:
                thisstr += "\n"+("|"+" "*5)*level+"|-----"+str(c)
        #thisstr += "\n|\n|\n|"
        return thisstr


class camViewWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self)


        layout = QVBoxLayout()

        group0 = QGroupBox("0")
        group1 = QGroupBox("1")
        group2 = QGroupBox("2")
        group3 = QGroupBox("3")

        group4 = QGroupBox("4")
        group5 = QGroupBox("5")
        group6 = QGroupBox("6")
        group7 = QGroupBox("7")

        group8 = QGroupBox("8")
        group9 = QGroupBox("9")
        group10 = QGroupBox("10")
        group11 = QGroupBox("11")


        splitterH0 = QSplitter(Qt.Horizontal)
        splitterH0.addWidget(group0)
        splitterH0.addWidget(group1)
        splitterH0.addWidget(group2)
        splitterH0.addWidget(group3)

        splitterH1 = QSplitter(Qt.Horizontal)
        splitterH1.addWidget(group4)
        splitterH1.addWidget(group5)
        splitterH1.addWidget(group6)
        splitterH1.addWidget(group7)

        splitterH2 = QSplitter(Qt.Horizontal)
        splitterH2.addWidget(group8)
        splitterH2.addWidget(group9)
        splitterH2.addWidget(group10)
        splitterH2.addWidget(group11)

        splitterV = QSplitter(Qt.Vertical)
        splitterV.addWidget(splitterH0)
        splitterV.addWidget(splitterH1)
        splitterV.addWidget(splitterH2)


        layout.addWidget(splitterV)
        self.setLayout(layout)
        print("Init camViewWindow")

    def addCam(row, col):
        if nRows <= row:
            for i in range(row-nRows+1):
                newHSplitter = QSplitter
                hSplitter.append()
                vSplitter.addWidget()

