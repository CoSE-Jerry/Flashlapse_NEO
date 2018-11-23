#disable all ui elements that utilizes the cameraduring the snapshot is taken
def snap_disable(self,pre_flip,sch_flip):
    self.Snapshot.setEnabled(False)
    self.Snapshot.setText("Processing...")
    self.Live_Feed.setEnabled(False)
    if pre_flip:
        self.Start_Imaging.setEnabled(False)
    if sch_flip:
        self.Start_Schedule.setEnabled(False)
        
    
    
