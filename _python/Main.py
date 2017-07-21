# always seem to need this
from threading import Thread
import sys
import os
import time
 
# This gets the Qt stuff
import PyQt5
import functions
import Email
from PyQt5.QtWidgets import *
directory = None
# This is our window from QtCreator
import FlashLapse_UI
import functions

from picamera import PiCamera
from time import sleep

class CaptureImage:  
    def __init__(self):
        self._running = True

    def terminate(self):  
        self._running = False  

    def run(self):
        while self._running:
            with PiCamera() as camera:
                camera.capture("test.jpg")
            os.system("/home/pi/Dropbox-Uploader/dropbox_uploader.sh upload test.jpg /test")
            os.system("rm test.jpg")
            
            Email.sendtest() 

# create class for our Raspberry Pi GUI
class MainWindow(QMainWindow, FlashLapse_UI.Ui_MainWindow):
 # access variables inside of the UI's file

    def IST_Edit(self):
        file = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
        #Create Class
      #  Capture = CaptureImage()
        #Create Thread
      #  CaptureThread = Thread(target=Capture.run) 
      #  #Start Thread 
      #  CaptureThread.start()
      #  Capture.terminate()
     

    
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self) # gets defined in the UI file
        self.IST_Editor.editingFinished.connect(lambda: self.IST_Edit())

# I feel better having one of these
def main():
 # a new app instance
 app = QApplication(sys.argv)
 form = MainWindow()
 
 form.show()
 # without this, the script exits immediately.
 sys.exit(app.exec_())
 
# python bit to figure how who started This
if __name__ == "__main__":
 main()
