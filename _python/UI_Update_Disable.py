#disable all ui elements that utilizes the cameraduring the snapshot is taken
def snap_disable(self):
    self.Snapshot.setEnabled(False)
    self.Snapshot.setText("Processing...")
    self.Live_Feed.setEnabled(False)
    if self.pre_flip:
        self.Start_Imaging.setEnabled(False)
        
    
    
