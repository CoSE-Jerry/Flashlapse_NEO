#disable all ui elements that utilizes the cameraduring the snapshot is taken
def snap_enable(self):
    self.Snapshot.setEnabled(True)
    self.Live_Feed.setEnabled(True)
    if not self.Start_Imaging.isEnabled():
        self.Start_Imaging.setEnabled(True)
