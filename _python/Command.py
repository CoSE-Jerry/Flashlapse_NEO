import Settings
from time import sleep
from PyQt5.QtCore import QThread

#QThread for schedule function
class Schedule(QThread):
    
    def __init__(self):
        QThread.__init__(self)
        Settings.sch_running = True

    def __del__(self):
        self._running = False
        
    def run(self):  
        while True:
            Settings.ASD.write(bytes('~'+str(Settings.angle_1)+"\n", 'UTF-8'))
            sleep(Settings.delay_1*5)
            Settings.ASD.write(bytes('~'+str(Settings.angle_2)+"\n", 'UTF-8'))
            sleep(Settings.delay_2*5)
