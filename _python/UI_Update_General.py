def check_stat(self):
    return self.Start_Imaging.isEnabled(),self.Start_Schedule.isEnabled()

def start_image_disable(self):
    self.Start_Imaging.setEnabled(False)

def schedule_disable(self):
    self.Start_Schedule.setEnabled(False)

def start_image_enable(self):
    self.Start_Imaging.setEnabled(True)

def start_image_enable(self):
    self.Start_Schedule.setEnabled(True)
