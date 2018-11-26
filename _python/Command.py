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
            Settings.ASD.write(bytes('~0'+"\n", 'UTF-8'))
            sleep(Settings.delay_1*5)
            Settings.ASD.write(bytes('~'+str(Settings.angle_2)+"\n", 'UTF-8'))
            Settings.ASD.write(bytes('~0'+"\n", 'UTF-8'))
            sleep(Settings.delay_2*5)

class Test(QThread):
    
    def __init__(self):
        QThread.__init__(self)
        Settings.test_running = True

    def __del__(self):
        self._running = False
        
    def run(self):
        while True:
            Settings.ASD.write(bytes('~'+str(Settings.angle_1)+"\n", 'UTF-8'))
            Settings.ASD.write(bytes("~0\n", "UTF-8"))
            sleep(5)
            Settings.ASD.write(bytes('~'+str(Settings.angle_2)+"\n", 'UTF-8'))
            Settings.ASD.write(bytes("~0\n", "UTF-8"))
            sleep(5)

def full_color_change(self):
    temp = self.Full_Color_Select.currentIndex()
    if temp == 1:
        Settings.ASD.write(bytes('1', 'UTF-8'))
    elif temp == 2:
        Settings.ASD.write(bytes('2', 'UTF-8'))
    elif temp == 3:
        Settings.ASD.write(bytes('3', 'UTF-8'))
    elif temp == 4:
        Settings.ASD.write(bytes('4', 'UTF-8'))
    else:
        Settings.ASD.write(bytes('0', 'UTF-8'))

def half_color_change_left(self):
    temp = self.Left_Select.currentIndex()
    if temp == 1:
        Settings.ASD.write(bytes('a', 'UTF-8'))
    elif temp == 2:
        Settings.ASD.write(bytes('b', 'UTF-8'))
    elif temp == 3:
        Settings.ASD.write(bytes('c', 'UTF-8'))
    elif temp == 4:
        Settings.ASD.write(bytes('d', 'UTF-8'))
    else:
        Settings.ASD.write(bytes('e', 'UTF-8'))

def half_color_change_right(self):
    temp = self.Right_Select.currentIndex()
    if temp == 1:
        Settings.ASD.write(bytes('A', 'UTF-8'))
    elif temp == 2:
        Settings.ASD.write(bytes('B', 'UTF-8'))
    elif temp == 3:
        Settings.ASD.write(bytes('C', 'UTF-8'))
    elif temp == 4:
        Settings.ASD.write(bytes('D', 'UTF-8'))
    elif temp == 0:
        Settings.ASD.write(bytes('E', 'UTF-8'))
