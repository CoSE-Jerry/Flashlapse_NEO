#disable all ui elements that utilizes the cameraduring the snapshot is taken
def snap_enable(self):
    snap_img = PyQt5.QtGui.QImage("../_temp/snapshot.jpg")
    self.Image_Frame.setPixmap(QtGui.QPixmap(snap_img))
    self.Snapshot.setText("Snapshot")
    self.Snapshot.setEnabled(True)
    self.Live_Feed.setEnabled(True)
    if not self.Start_Imaging.isEnabled():
        self.Start_Imaging.setEnabled(True)
