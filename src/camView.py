from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtMultimedia import *
from PyQt5.QtMultimediaWidgets import *
import time

class camView(QCameraViewfinder):
    def __init__(self):
        QWidget.__init__(self)

        self.online_webcams = QCameraInfo.availableCameras()
        if not self.online_webcams:
            print("No online webcams")
            pass

        self.cam = QCamera(self.online_webcams[0])
        self.cam.setViewfinder(self)
        self.cam.setCaptureMode(QCamera.CaptureStillImage)
        #self.cam.start()

    def start(self):
        self.cam.start()
