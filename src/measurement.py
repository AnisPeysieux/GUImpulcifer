import os

class Measurement:
    def __init__(self, measurementName, parentSession):
        self.name = measurementName
        self.output_device = ""
        self.sweep = ""
        self.earsInputDevice = ""
        self.roomInputDeviceLeft = ""
        self.roomInputDeviceForce1ChannelLeft = False
        self.roomInputDeviceRight = ""
        self.roomInputDeviceForce1ChannelRight = False
        self.roomInputDeviceCenter = ""
        self.roomInputDeviceForce1ChannelCenter = False
        self.session = parentSession
    def load(path, parent):
        if os.path.isdir(path):
            return [Measurement(f.name, parent) for f in os.scandir(path) if f.is_dir()]
        else:
            return []
    def __str__(self):
        return "Measurement name: "+self.name+" session: "+self.session.name

