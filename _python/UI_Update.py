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

def update_frame(self,file):
    self.Misc_Frame.setEnabled(True)
    temp_img = PyQt5.QtGui.QImage(file)
    self.Image_Frame.setPixmap(QtGui.QPixmap(temp_img))

def validate_input(self):
    Settings.total = int(Settings.duration/Settings.interval)
    if(Settings.total>0 and len(Settings.sequence_name)!=0):
        self.startRoutines_pushButton.setEnabled(True)
    else:
        self.startRoutines_pushButton.setEnabled(False)
    self.Progress_Label.setText("Progress: "+str(Settings.current) + "/" + str(Settings.total))
    

'''def check_stat(self):
    return self.Start_Schedule.isEnabled()

def schedule_disable(self):
    self.Start_Schedule.setEnabled(False)

def schedule_enable(self):
    self.Start_Schedule.setEnabled(True)

def schedule_update(self):
    sn = len(Settings.sequence_name)
    if(sn != 0 and Settings.sch_confirmed):
        schedule_enable(self)
    else:
        schedule_disable(self)

def snap_disable(self,sch_flip):
    self.Snapshot.setEnabled(False)
    self.Snapshot.setText("Processing...")
    self.Live_Feed.setEnabled(False)
    if sch_flip:
        self.Start_Schedule.setEnabled(False)

def snap_enable(self,sch_flip):
    snap_img = PyQt5.QtGui.QImage("../_temp/snapshot.jpg")
    self.Image_Frame.setPixmap(QtGui.QPixmap(snap_img))
    self.Snapshot.setText("Snapshot")
    self.Snapshot.setEnabled(True)
    self.Live_Feed.setEnabled(True)
    if sch_flip:
        self.Start_Schedule.setEnabled(True)'''
