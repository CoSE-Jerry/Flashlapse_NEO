import Settings
from time import sleep
from PyQt5.QtCore import QThread

def full_color_change(self):
    temp = self.Full_Color_Select.currentIndex()
    
    self.Left_Select.setCurrentIndex(0)
    self.Right_Select.setCurrentIndex(0)
    self.Top_Color_Select.setCurrentIndex(0)
    self.LL_Color_Select.setCurrentIndex(0)
    self.LR_Color_Select.setCurrentIndex(0)

    if temp == 1:
        Settings.ASD.write(bytes("1~0~58~255~0~0~1", 'UTF-8'))
    elif temp == 2:
        Settings.ASD.write(bytes("1~0~58~0~255~0~1", 'UTF-8'))
    elif temp == 3:
        Settings.ASD.write(bytes("1~0~58~0~0~255~1", 'UTF-8'))
    elif temp == 4:
        Settings.ASD.write(bytes("1~0~58~85~85~85~1", 'UTF-8'))
    elif temp == 5:
        Settings.ASD.write(bytes("1~0~58~" + str(Settings.custom_R) + "~" + str(Settings.custom_G) + "~" + str(Settings.custom_B) + "~1", 'UTF-8'))
    else:
        Settings.ASD.write(bytes("1~0~58~0~0~0~1", 'UTF-8'))

def half_color_change_left(self):

    temp = self.Left_Select.currentIndex()
    self.Full_Color_Select.setCurrentIndex(0)
    self.Top_Color_Select.setCurrentIndex(0)
    self.LL_Color_Select.setCurrentIndex(0)
    self.LR_Color_Select.setCurrentIndex(0)

    if temp == 1:
        Settings.ASD.write(bytes('A', 'UTF-8'))
    elif temp == 2:
        Settings.ASD.write(bytes('B', 'UTF-8'))
    elif temp == 3:
        Settings.ASD.write(bytes('C', 'UTF-8'))
    elif temp == 4:
        Settings.ASD.write(bytes('D', 'UTF-8'))
    else:
        Settings.ASD.write(bytes('E', 'UTF-8'))

def half_color_change_right(self):

    self.Full_Color_Select.setCurrentIndex(0)
    self.Top_Color_Select.setCurrentIndex(0)
    self.LL_Color_Select.setCurrentIndex(0)
    self.LR_Color_Select.setCurrentIndex(0)
    
    temp = self.Right_Select.currentIndex()
    if temp == 1:
        Settings.ASD.write(bytes('a', 'UTF-8'))
    elif temp == 2:
        Settings.ASD.write(bytes('b', 'UTF-8'))
    elif temp == 3:
        Settings.ASD.write(bytes('c', 'UTF-8'))
    elif temp == 4:
        Settings.ASD.write(bytes('d', 'UTF-8'))
    elif temp == 0:
        Settings.ASD.write(bytes('e', 'UTF-8'))

def third_color_change_top(self):

    self.Full_Color_Select.setCurrentIndex(0)
    self.Left_Select.setCurrentIndex(0)
    self.Right_Select.setCurrentIndex(0)
    
    temp = self.Top_Color_Select.currentIndex()
    if temp == 1:
        Settings.ASD.write(bytes('f', 'UTF-8'))
    elif temp == 2:
        Settings.ASD.write(bytes('g', 'UTF-8'))
    elif temp == 3:
        Settings.ASD.write(bytes('h', 'UTF-8'))
    elif temp == 4:
        Settings.ASD.write(bytes('i', 'UTF-8'))
    else:
        Settings.ASD.write(bytes('j', 'UTF-8'))

def third_color_change_lower_left(self):

    self.Full_Color_Select.setCurrentIndex(0)
    self.Left_Select.setCurrentIndex(0)
    self.Right_Select.setCurrentIndex(0)
    
    temp = self.LL_Color_Select.currentIndex()
    if temp == 1:
        Settings.ASD.write(bytes('k', 'UTF-8'))
    elif temp == 2:
        Settings.ASD.write(bytes('l', 'UTF-8'))
    elif temp == 3:
        Settings.ASD.write(bytes('m', 'UTF-8'))
    elif temp == 4:
        Settings.ASD.write(bytes('n', 'UTF-8'))
    else:
        Settings.ASD.write(bytes('o', 'UTF-8'))

def third_color_change_lower_right(self):

    self.Full_Color_Select.setCurrentIndex(0)
    self.Left_Select.setCurrentIndex(0)
    self.Right_Select.setCurrentIndex(0)
    
    temp = self.LR_Color_Select.currentIndex()
    if temp == 1:
        Settings.ASD.write(bytes('p', 'UTF-8'))
    elif temp == 2:
        Settings.ASD.write(bytes('q', 'UTF-8'))
    elif temp == 3:
        Settings.ASD.write(bytes('r', 'UTF-8'))
    elif temp == 4:
        Settings.ASD.write(bytes('s', 'UTF-8'))
    else:
        Settings.ASD.write(bytes('t', 'UTF-8'))
