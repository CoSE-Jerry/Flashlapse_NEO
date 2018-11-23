# import Qt content
import PyQt5

from PyQt5 import QtCore, QtGui, QtWidgets

#disable all ui elements that utilizes the cameraduring the snapshot is taken
def snap_enable(self,sch_flip):
    snap_img = PyQt5.QtGui.QImage("../_temp/snapshot.jpg")
    self.Image_Frame.setPixmap(QtGui.QPixmap(snap_img))
    self.Snapshot.setText("Snapshot")
    self.Snapshot.setEnabled(True)
    self.Live_Feed.setEnabled(True)
    if sch_flip:
        self.Start_Schedule.setEnabled(True)
