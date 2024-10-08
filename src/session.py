import os
import src.measurement

class Session:
    def __init__(self, sessionName, path):
        self.name = sessionName
        self.earsInputDevice = ""
        self.roomInputDeviceLeft = ""
        self.roomInputDeviceForce1ChannelLeft = False
        self.roomInputDeviceRight = ""
        self.roomInputDeviceForce1ChannelRight = False
        self.roomInputDeviceCenter = ""
        self.roomInputDeviceForce1ChannelCenter = False
        self.measurements = src.measurement.Measurement.load(path+'/'+self.name, self)
    def load(path):
        if os.path.isdir(path):
            return [Session(f.name, path) for f in os.scandir(path) if f.is_dir()]
        else:
            return []
    def __str__(self):
        ret =  "Session name: "+self.name
        for m in self.measurements:
            ret += '\n\t'+m.__str__()
        return ret

