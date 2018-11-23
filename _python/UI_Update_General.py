def check_stat(self):
    return self.Start_Schedule.isEnabled()

def schedule_disable(self):
    self.Start_Schedule.setEnabled(False)

def schedule_enable(self):
    self.Start_Schedule.setEnabled(True)
