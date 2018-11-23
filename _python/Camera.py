from time import sleep
from PyQt5.QtCore import QThread
from picamera import PiCamera
from Main import *

#QThread for snapshot function
class Snap(QThread):

    def __init__(self):
         QThread.__init__(self)

    def __del__(self):
         self._running = False

    def run(self):
        with PiCamera() as camera:
            sleep(1)
            camera.resolution = (2464,2464)
            camera._set_rotation(180)
            camera.capture("../_temp/snapshot.jpg")
            
class Live(QThread):

    def __init__(self):
         QThread.__init__(self)

    def __del__(self):
         self._running = False

    def run(self):
        with PiCamera() as camera:
            camera._set_rotation(180)
            camera.start_preview()
            sleep(30)
