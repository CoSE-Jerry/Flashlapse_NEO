# always seem to need this
import sys
import os
import time
 
# This gets the Qt stuff
import PyQt5
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QThread

import functions
import Camera
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
directory = '/home/pi/Desktop'
interval = None
duration = None
total = None
jpg = True
total = 0



#class Image(QThread):

  #  def __init__(self):
  #       QThread.__init__(self)

  #  def __del__(self):
  #       self.wait()

  #  def run(self):
       # global jpg, directory, name, duration, interval, total
  #      total = int((duration*60)/interval)
   #     print(total)
   #     if jpg:
   #         tempdir = directory+"/"+ name +"_%04d.jpg"
    #    else:
    #        tempdir = directory+"/"+ name +"_%04d.png"

    #    if(not os.path.isdir(directory)):
     #       os.mkdir(directory)
            
    #    with PiCamera() as camera:
     #       camera.resolution = (2464,2464)
      #      camera._set_rotation(180)
                
             #   camera.capture("../_temp/snapshot.jpg")
      #  print("Testing Threads")
                
                

            #os.system("/home/pi/Dropbox-Uploader/dropbox_uploader.sh upload test.jpg /test")
            #os.system("rm test.jpg")
            
           # Email.sendtest()
           


# create class for our Raspberry Pi GUI
class MainWindow(QMainWindow, FlashLapse_UI.Ui_MainWindow):
 # access variables inside of the UI's file

    def IST_Edit(self):
        global directory, name
        name = self.IST_Editor.text()
        
    def ICI_Change(self):
        global interval
        interval = self.ICI_spinBox.value()
        print(interval)
        
    def ISD_Change(self):
        global duration
        duration = self.ISD_spinBox.value()
        print(duration)
        
    def Start_Snapshot(self):
        
        self.Snap_Thread = Camera.Snap()
       
        self.Snap_Thread.started.connect(lambda: self.Processing_Snapshot())
        self.Snap_Thread.finished.connect(lambda: self.Processing_Complete())
        self.Snap_Thread.start()
        #directory = "/home/pi/Desktop/" + name
        #self.Directory.setsasdText(directory)
        
        #self.Snapshot.setEnabled(False)
        #self.Snapshot.setText("Processing...")
        #QApplication.processEvents()
   
        
        #user_img = PyQt5.QtGui.QImage("../_temp/snapshot.jpg")
        #self.Image_Frame.setPixmap(QtGui.QPixmap(user_img))
        #self.Snapshot.setText("Snapshot")
        #self.Snapshot.setEnabled(True)
        
    def Processing_Snapshot(self):
        self.Snapshot.setEnabled(False)
        self.Snapshot.setText("Processing...")
        
    def Processing_Complete(self):
        user_img = PyQt5.QtGui.QImage("../_temp/snapshot.jpg")
        self.Image_Frame.setPixmap(QtGui.QPixmap(user_img))
        self.Snapshot.setEnabled(True)
        self.Snapshot.setText("Snapshot")
        
    def Start_Live_Feed(self):
        with PiCamera() as camera:
            camera.start_preview()
            sleep(10)
            camera.stop_preview()

    def Select_Storage_Directory(self):
        directory = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
        self.Directory_Label.setText(directory)
        
    def Begin_Imaging(self):
        self.Image_Thread = Snapshot.Image()
        self.Image_Thread.started.connect(lambda: self.Threading_GUI())
        self.Image_Thread.start()
        
    def Threading_GUI(self):
        self.Start_Imaging.setEnabled(False)
        
                

    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self) # gets defined in the UI file
        self.IST_Editor.editingFinished.connect(lambda: self.IST_Edit())
        self.ICI_spinBox.valueChanged.connect(lambda: self.ICI_Change())
        self.ISD_spinBox.valueChanged.connect(lambda: self.ISD_Change())
        self.Snapshot.clicked.connect(lambda: self.Start_Snapshot())
        self.Live_Feed.clicked.connect(lambda: self.Start_Live_Feed())
        self.Storage_Directory.clicked.connect(lambda: self.Select_Storage_Directory())
        self.Start_Imaging.clicked.connect(lambda: self.Begin_Imaging())

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
