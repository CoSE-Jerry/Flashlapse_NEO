import Settings
import PyQt5

from PyQt5 import QtCore, QtGui, QtWidgets
def check_stat(self):
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
        self.Start_Schedule.setEnabled(True)
