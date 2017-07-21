# always seem to need this
from threading import Thread
import sys
import os
import time
 
# This gets the Qt stuff
import PyQt5
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication

import functions
import Email
from PyQt5.QtWidgets import *
directory = None
# This is our window from QtCreator
import FlashLapse_UI
import functions

#camera libraries
from picamera import PiCamera
from time import sleep

#global variables 
name = None
directory = None
interval = None
duration = None
snapping = True

class Snapshot:

    def __init__(self):
        self._running = True

    def terminate(self):  
        self._running = False  

    def run(self):
        global snapping
        while self._running:
            
            with PiCamera() as camera:
                camera.resolution = (2464,2464)
                camera._set_rotation(180)
                camera.capture("../_temp/snapshot.jpg")

            #os.system("/home/pi/Dropbox-Uploader/dropbox_uploader.sh upload test.jpg /test")
            #os.system("rm test.jpg")
            
           # Email.sendtest() 

# create class for our Raspberry Pi GUI
class MainWindow(QMainWindow, FlashLapse_UI.Ui_MainWindow):
 # access variables inside of the UI's file

    def IST_Edit(self):
        global directory, name
        name = self.IST_Editor.text()
        print("name: " + name)
        
    def ICI_Change(self):
        global interval
        interval = self.ICI_spinBox.value()
        print(interval)
        
    def ISD_Change(self):
        global duration
        duration = self.ISD_spinBox.value()
        print(duration)
        
    def Take_Snapshot(self):
        #self.Snapshot.setEnabled(False)
        #directory = "/home/pi/Desktop/" + name
        #self.Directory.setText(directory)
        
        #file = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
        #Create Class
        
        self.Snapshot.setEnabled(False)
        self.Snapshot.setText("Processing...")
        QApplication.processEvents()
        
        #Snap = Snapshot()
        #Create Thread
        #SnapThread = Thread(target=Snap.run) 
        #Start Thread
        
        #SnapThread.start()
        #Snap.terminate()
        

    
       

        
        with PiCamera() as camera:
            camera.resolution = (2464,2464)
            camera._set_rotation(180)
            camera.capture("../_temp/snapshot.jpg")
        user_img = PyQt5.QtGui.QImage("../_temp/snapshot.jpg")
        self.Image_Frame.setPixmap(QtGui.QPixmap(user_img))
        self.Snapshot.setText("Snapshot")
        self.Snapshot.setEnabled(True)
    
    def Start_Live_Feed(self):
        
        with PiCamera() as camera:
            camera.start_preview()
            sleep(10)
            camera.stop_preview()

    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self) # gets defined in the UI file
        self.IST_Editor.editingFinished.connect(lambda: self.IST_Edit())
        self.ICI_spinBox.valueChanged.connect(lambda: self.ICI_Change())
        self.ISD_spinBox.valueChanged.connect(lambda: self.ISD_Change())
        self.Snapshot.clicked.connect(lambda: self.Take_Snapshot())
        self.Live_Feed.clicked.connect(lambda: self.Start_Live_Feed)

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
