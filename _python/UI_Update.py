import Settings
import Commands
import PyQt5
from PyQt5 import QtCore, QtGui, QtWidgets

def LED_validate(self):
    if(self.Start_spinBox.value()>=self.End_spinBox.value()):
        self.lightConfirm_pushButton.setEnabled(False)
    else:
        self.lightConfirm_pushButton.setEnabled(True)

def desync(self):
    error_img = PyQt5.QtGui.QImage("../_image/Error.png")
    self.Image_Frame.setPixmap(QtGui.QPixmap(error_img))
    self.Control_Tab.setEnabled(False)
    self.Misc_Frame.setEnabled(False)

def cycle_start(self):
    self.confirmCycle_pushButton.setText("TERMINATE CYCLE")

def cycle_end(self):
    self.confirmCycle_pushButton.setText("CONFIRM")
    Commands.deploy_lights()

def test_start(self):
    self.schedulerTest_pushButton.setText("TERMINATE TEST")

def test_end(self):
    self.schedulerTest_pushButton.setText("Test Run")
    Settings.test_running = False

def schedule_start(self):
    self.schedulerSet_pushButton.setText("TERMINATE")

def schedule_end(self):
    self.schedulerSet_pushButton.setText("Set Schedule")

def imaging_disable(self):
    self.Misc_Frame.setEnabled(False)

def imaging_enable(self):
    self.Misc_Frame.setEnabled(True)

def timelapse_disable(self):
    if(Settings.storage_mode):
        self.startRoutines_pushButton.setText("End CLOUD Image Sequence")
    else:
        self.startRoutines_pushButton.setText("End LOCAL Image Sequence")
    self.snapshot_pushButton.setEnabled(False)
    self.liveFeed_pushButton.setEnabled(False)
    self.preview_pushButton.setEnabled(False)
    self.rotate_pushButton.setEnabled(False)

def timelapse_enable(self):
    if(Settings.storage_mode):
        self.startRoutines_pushButton.setText("Start CLOUD Image Sequence")
    else:
        self.startRoutines_pushButton.setText("Start LOCAL Image Sequence")
    self.snapshot_pushButton.setEnabled(True)
    self.liveFeed_pushButton.setEnabled(True)
    self.preview_pushButton.setEnabled(True)
    self.rotate_pushButton.setEnabled(True)

def update_frame(self,file):
    self.Misc_Frame.setEnabled(True)
    temp_img = PyQt5.QtGui.QImage(file)
    self.Image_Frame.setPixmap(QtGui.QPixmap(temp_img))

def validate_input(self):
    Settings.total = int((Settings.duration*60)/Settings.interval)
    if(Settings.total>0 and len(Settings.sequence_name)!=0):
        self.startRoutines_pushButton.setEnabled(True)
    else:
        self.startRoutines_pushButton.setEnabled(False)
    self.Progress_Label.setText("Progress: "+str(Settings.current) + "/" + str(Settings.total))
    if(self.storage_tabWidget.currentIndex() ==0):
        Settings.storage_mode=0
        self.startRoutines_pushButton.setText("Start LOCAL Image Sequence")
    else:
        if(len(Settings.email)!=0):
            Settings.storage_mode=1
            self.startRoutines_pushButton.setText("Start CLOUD Image Sequence")
        
