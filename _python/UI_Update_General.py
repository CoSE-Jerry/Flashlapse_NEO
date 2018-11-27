import Settings
def check_stat(self):
    return self.Start_Schedule.isEnabled()

def schedule_disable(self):
    self.Start_Schedule.setEnabled(False)

def schedule_enable(self):
    self.Start_Schedule.setEnabled(True)

def schedule_update(self):
    sn = len(Settings.sequence_name)
    em = len(Settings.email)
    if(sn != 0 and em != 0 and Settings.sch_confirmed):
        schedule_enable(self)
    else:
        schedule_disable(self)
