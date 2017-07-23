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
file_list = []
directory = ""
interval = 0
duration = 0
total = 0
current = 0
current_image = None
file = None
jpg = True
name = None
on_flag = False

class Image(QThread):
    
    capture = QtCore.pyqtSignal()
    
    
    def __init__(self):
        QThread.__init__(self)

    def __del__(self):
        self._running = False

    def run(self):
        global current, current_image, file_list
        for i in range(total):
            sleep(1)  
            current = i
            current_image = file % i
            with PiCamera() as camera:
                camera.resolution = (2464,2464)
                camera._set_rotation(180)
                camera.capture(current_image)
            file_list.append(current_image)
            self.capture.emit()
            sleep(interval-1)
                
            #os.system("/home/pi/Dropbox-Uploader/dropbox_uploader.sh upload test.jpg /test")
            #os.system("rm test.jpg")
            
           # Email.sendtest()
    def stop(self):
        self.running = False

class Dropbox(QThread):
    
    def __init__(self):
        QThread.__init__(self)

    def __del__(self):
        self._running = False

    def run(self):  
        global file_list, name

        os.system("/home/pi/Dropbox-Uploader/dropbox_uploader.sh mkdir /" + name)
        print(os.system("/home/pi/Dropbox-Uploader/dropbox_uploader.sh share /" + name))
        while True:
            if (len(file_list) > 0):
                os.system("/home/pi/Dropbox-Uploader/dropbox_uploader.sh upload " + file_list[0] + " /"+name)
                print("test")
                del file_list[0]
                
            #os.system("rm test.jpg")
            
           # Email.sendtest()

           


# create class for our Raspberry Pi GUI
class MainWindow(QMainWindow, FlashLapse_UI.Ui_MainWindow):
 # access variables inside of the UI's file

    def IST_Edit(self):
        global directory, name
        name = self.IST_Editor.text()
        
    def IST_Change(self):
        self.ICI_spinBox.setEnabled(True)
        if(len(self.IST_Editor.text())==0):
            self.ICI_spinBox.setEnabled(False)
            self.ISD_spinBox.setEnabled(False)
            self.Start_Imaging.setEnabled(False)
            
            
        
    def ICI_Change(self):
        global interval, duration, total, directory
        interval = self.ICI_spinBox.value()
        self.ISD_spinBox.setEnabled(True)
        if(interval == 0):
            self.ISD_spinBox.setEnabled(False)
        if(interval!= 0):
            total = int((duration*60)/interval)
            if(total>0 and len(directory)!=0):
                self.Start_Imaging.setEnabled(True)
            else:
                self.Start_Imaging.setEnabled(False)
                
    def ISD_Change(self):
        global interval, duration, total, directory
        duration = self.ISD_spinBox.value()
        self.Storage_Directory.setEnabled(True)
        if(interval!= 0):
            total = int((duration*60)/interval)
            if(total>0 and len(directory)!=0):
                self.Start_Imaging.setEnabled(True)
            else:
                self.Start_Imaging.setEnabled(False)
            
        
        
    def Select_Storage_Directory(self):
        global interval, duration, total, directory
        directory = str(QFileDialog.getExistingDirectory(self, "Select Directory",'/home/pi/Desktop'))
        if(len(directory)!=0):
            directory = directory +"/"+name
            self.Directory_Label.setText(directory)
            if(interval!= 0):
                total = int((duration*60)/interval)
                if(total>0 and len(directory)!=0):
                    self.Start_Imaging.setEnabled(True)
                else:
                    self.Start_Imaging.setEnabled(False)
        
    def Start_Snapshot(self):
        self.Snap_Thread = Camera.Snap()
        self.Snap_Thread.started.connect(lambda: self.Processing_Snapshot())
        self.Snap_Thread.finished.connect(lambda: self.Processing_Complete())
        self.Snap_Thread.start()
        
    def Processing_Snapshot(self):
        self.Snapshot.setEnabled(False)
        self.Snapshot.setText("Processing...")
        
    def Processing_Complete(self):
        user_img = PyQt5.QtGui.QImage("../_temp/snapshot.jpg")
        self.Image_Frame.setPixmap(QtGui.QPixmap(user_img))
        self.Snapshot.setEnabled(True)
        self.Snapshot.setText("Snapshot")
        
    def Start_Live_Feed(self):
        self.Live_Thread = Camera.Live()
        self.Live_Thread.started.connect(lambda: self.Processing_Live())
        self.Live_Thread.finished.connect(lambda: self.Live_Complete())
        self.Live_Thread.start()
        
    def Processing_Live(self):
        self.Snapshot.setEnabled(False)
        self.Live_Feed.setEnabled(False)
        self.Start_Imaging.setEnabled(False)
        self.Live_Feed.setText("Processing...")
        
    def Live_Complete(self):
        self.Snapshot.setEnabled(True)
        self.Live_Feed.setEnabled(True)
        self.Start_Imaging.setEnabled(True)
        self.Live_Feed.setText("Start Live Feed (30s)")
        
    def Begin_Imaging(self):
        global jpg, directory, name, duration, interval, total, file, on_flag, file_list
        
        if (on_flag == False): 
            global jpg, directory, name, duration, interval, total, file       
            self.Image_Thread = Image()
            self.Dropbox_Thread = Dropbox()
            total = int((duration*60)/interval)
            self.Progress_Bar.setMaximum(total)
            
            if(not os.path.isdir(directory)):
                os.mkdir(directory)
            
            if jpg:
                file = directory + "/" +name + "_%04d.jpg"
            else:
                file = directory + "/" +name + "_%04d.png"
            self.Image_Thread.started.connect(lambda: self.Start_Image())
            #self.Image_Thread.finished.connect(lambda: self.Image_Complete())
            self.Image_Thread.start()
            self.Dropbox_Thread.start()
            self.Image_Thread.capture.connect(lambda: self.Progress())
            on_flag = True
        
        else:
            self.Image_Thread.terminate()
            self.IST_Editor.setEnabled(True)
            self.ICI_spinBox.setEnabled(True)
            self.ISD_spinBox.setEnabled(True)
            self.Live_Feed.setEnabled(True)
            self.Storage_Directory.setEnabled(True)
            self.Snapshot.setEnabled(True)
            self.JPG.setEnabled(True)
            self.PNG.setEnabled(True)
            self.Dropbox_Email.setEnabled(True)
            self.Dropbox_Confirm.setEnabled(True)
            self.CyVerse_Email.setEnabled(True)
            self.CyVerse_Confirm.setEnabled(True)
            self.Frequency_Off.setEnabled(True)
            self.Frequency_Low.setEnabled(True)
            self.Frequency_Average.setEnabled(True)
            self.Frequency_High.setEnabled(True)
            self.Image_Frame.setPixmap(QtGui.QPixmap("../_image/background1.png"))
            icon3 = QtGui.QIcon()
            icon3.addPixmap(QtGui.QPixmap("../_image/Start-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.Start_Imaging.setIcon(icon3)
            self.Start_Imaging.setText("Start Image Sequence")
            self.Progress_Bar.setValue(0)
            del file_list[:]
            
            on_flag = False

        

        
    def Progress(self):
        global current, current_image
        self.Progress_Bar.setValue(current+1)
        self.Image_Frame.setPixmap(QtGui.QPixmap(current_image))
        #print(current)    
            
    def Start_Image(self):
                
        self.IST_Editor.setEnabled(False)
        self.ICI_spinBox.setEnabled(False)
        self.ISD_spinBox.setEnabled(False)
        self.Live_Feed.setEnabled(False)
        self.Storage_Directory.setEnabled(False)
        self.Snapshot.setEnabled(False)
        self.JPG.setEnabled(False)
        self.PNG.setEnabled(False)
        self.Dropbox_Email.setEnabled(False)
        self.Dropbox_Confirm.setEnabled(False)
        self.CyVerse_Email.setEnabled(False)
        self.CyVerse_Confirm.setEnabled(False)
        self.Frequency_Off.setEnabled(False)
        self.Frequency_Low.setEnabled(False)
        self.Frequency_Average.setEnabled(False)
        self.Frequency_High.setEnabled(False)
        
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../_image/Stop-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Start_Imaging.setIcon(icon2)
        self.Start_Imaging.setText("Stop Image Sequence")

    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self) # gets defined in the UI file
        self.IST_Editor.editingFinished.connect(lambda: self.IST_Edit())
        self.IST_Editor.textChanged.connect(lambda: self.IST_Change())
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
