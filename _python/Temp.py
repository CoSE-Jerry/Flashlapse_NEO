# import basic libraries
import sys
import time
import re

#import UI functions
import UI_Update_Disable
import UI_Update_Enable
import UI_Update_General

#import settings
import Settings

#import custom functions
import Camera
import Command
 
# import Qt content
import PyQt5
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
 
# import generated UI
import FlashLapse_UI

#UI variables
sch_ready = False
sch_flip = False

#global variables
sequence_name = ""
email = ""
full_dir = ""
default_dir = "/home/pi/Desktop"
date = time.strftime('%m_%d_%Y')
 
# create class for Raspberry Pi GUI
class MainWindow(QMainWindow, FlashLapse_UI.Ui_MainWindow):

    def Start_Snapshot(self):
        try:
            sch_ready= UI_Update_General.check_stat(self)
            sch_flip = sch_ready
            self.Snap_Thread = Camera.Snap()
            self.Snap_Thread.started.connect(lambda: UI_Update_Disable.snap_disable(self,sch_flip))
            self.Snap_Thread.finished.connect(lambda: UI_Update_Enable.snap_enable(self,sch_flip))
            self.Snap_Thread.start()
            
        except Exception as e:
            print(e)

    def IST_Edit(self):
        global sequence_name
        sequence_name = self.IST_Editor.text()
        full_dir = default_dir + "/" + sequence_name
        self.Directory_Label.setText(full_dir)
        if date not in sequence_name: 
            self.add_Date.setEnabled(True)
        if(len(sequence_name) == 0):
            self.add_Date.setEnabled(False)

    def Add_Date(self):
        global sequence_name
        sequence_name = sequence_name + "_" + date
        self.IST_Editor.setText(sequence_name)
        full_dir = default_dir + "/" + sequence_name
        self.Directory_Label.setText(full_dir)
        self.add_Date.setEnabled(False)

    def Start_Rotate(self):
        try:
            UI_Update_Enable.snap_enable(self)
        except Exception as e:
            print(e)

    def Email_Change(self):
        valid = None
        if (len(self.Dropbox_Email.text())) > 7:
            valid = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', self.Dropbox_Email.text())
        if (valid != None):
            self.Dropbox_Confirm.setEnabled(True)
        else:
            self.Dropbox_Confirm.setEnabled(False)
            self.Cloud_Sync.setEnabled(False)
            self.Local_Storage.setChecked(True)
            self.Save_Default.setEnabled(False)

    def Email_Entered(self):
        global email
        email = self.Dropbox_Email.text()
        self.Cloud_Sync.setEnabled(True)
        self.Cloud_Sync.setChecked(True)
        self.Save_Default.setEnabled(True)
        

    def Save_Email(self):
        global email
        open("../_temp/save_data.txt", "w").close()

        file = open("../_temp/save_data.txt","w") 
        file.write(email)  
        file.close()

    def Select_Storage_Directory(self):
        global full_dir, default_dir
        default_dir = str(QFileDialog.getExistingDirectory(self, "Select Directory",'/home/pi/Desktop'))
        if(len(default_dir)!=0):
            full_dir = default_dir + "/" + sequence_name
            self.Directory_Label.setText(full_dir)

    def start_scheduler(self):
        Settings.angle_1 = self.rotate_to_spinbox_1.value()
        Settings.angle_2 = self.rotate_to_spinbox_2.value()
        Settings.delay_1 = self.wait_spinbox_1.value()
        Settings.delay_2 = self.wait_spinbox_2.value()

        if(Settings.sch_running):
            self.Schedule_Thread.terminate()
            Settings.sch_running = False;
        if(Settings.test_running):
            self.Test_Thread.terminate()
            test_running = False;
            
        self.Schedule_Thread = Command.Schedule()
        self.Schedule_Thread.start()

    def test_run(self):

        try:
            Settings.angle_1 = self.rotate_to_spinbox_1.value()
            Settings.angle_2 = self.rotate_to_spinbox_2.value()

            if(Settings.sch_running):
                self.Schedule_Thread.terminate()
                Settings.sch_running = False;
            if(Settings.test_running):
                print("testrunning")
                self.Test_Thread.terminate()
                Settings.test_running = False;
                print("testrunning")
                
            self.Test_Thread = Command.Test()
            self.Test_Thread.start()
        except Exception as e:
            print(e)

    def reset_position(self):
        if(Settings.sch_running):
            self.Schedule_Thread.terminate()
            Settings.sch_running = False;
        if(Settings.test_running):
            self.Test_Thread.terminate()
            Settings.test_running = False;
        Settings.ASD.write(bytes("~0\n", 'UTF-8'))

    def value_changed(self):
        self.Motor_Speed.setText("Motor Speed: "+str(self.Speed_Select.value()))

    def slider_released(self):
        Settings.ASD.write(bytes('+'+str(self.Speed_Select.value())+"\n", 'UTF-8'))

    def brightness_change(self):
        Settings.ASD.write(bytes('.'+str(self.brightness_spinBox.value())+"\n", 'UTF-8'))
        
            
 # access variables inside of the UI's file
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self) # gets defined in the UI file

        Settings.init()

        #load default email
        fh = open("../_temp/save_data.txt", "r") 
        self.Dropbox_Email.setText(fh.readline())
        fh.close
        self.Email_Change()
        
        self.Snapshot.clicked.connect(lambda: self.Start_Snapshot())
        self.IST_Editor.textChanged.connect(lambda: self.IST_Edit())
        self.Rotate.clicked.connect(lambda: self.Start_Rotate())
        self.add_Date.clicked.connect(lambda: self.Add_Date())
        self.Dropbox_Email.textChanged.connect(lambda: self.Email_Change())
        self.Dropbox_Confirm.clicked.connect(lambda: self.Email_Entered())
        self.Save_Default.clicked.connect(lambda: self.Save_Email())
        self.Storage_Directory.clicked.connect(lambda: self.Select_Storage_Directory())
        self.Start_Schedule.clicked.connect(lambda: self.start_scheduler())
        self.Test_Run.clicked.connect(lambda: self.test_run())
        self.Reset_Position.clicked.connect(lambda: self.reset_position())
        self.Speed_Select.valueChanged.connect(lambda: self.value_changed())
        self.Speed_Select.sliderReleased.connect(lambda: self.slider_released())
        self.Full_Color_Select.currentIndexChanged.connect(lambda: Command.full_color_change(self))
        self.brightness_spinBox.valueChanged.connect(lambda: self.brightness_change())
        self.Left_Select.currentIndexChanged.connect(lambda: Command.half_color_change_left(self))
        self.Right_Select.currentIndexChanged.connect(lambda: Command.half_color_change_right(self))

        
        
        
        

        

        
# main function
def main():
    # a new app instance
    app = QApplication(sys.argv)
    form = MainWindow()
    form.show()
    
    # without this, the script exits immediately.
    sys.exit(app.exec_())
 
# python bit to figure how who started This
if __name__ == "__main__":
    main()
