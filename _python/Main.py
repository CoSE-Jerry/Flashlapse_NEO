# import basic libraries
import sys
import time
import os

#import settings
import Settings

#import custom functions
import Commands
import Threads

#import UI functions
import UI_Update


'''

#import custom functions
import Camera'''
 
# import Qt content
import PyQt5
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
 
# import generated UI
import FlashLapse_UI

#global variables
default_dir = "/home/pi/Desktop"
date = time.strftime('%m_%d_%Y')
 
# create class for Raspberry Pi GUI
class MainWindow(QMainWindow, FlashLapse_UI.Ui_MainWindow):

    def start_cycle(self):
        if not Settings.cycle_running:
            try:
                Settings.cycle_time = self.powerCycle_spinBox.value()
                self.Cycle_Thread = Threads.Cycle()

                self.Cycle_Thread.started.connect(lambda: UI_Update.cycle_start(self))
                self.Cycle_Thread.finished.connect(lambda: UI_Update.cycle_end(self))
                
                self.Cycle_Thread.start()
                
            except Exception as e:
                print(e)
        else:
            UI_Update.cycle_end(self)
            Settings.cycle_running=False


    def schedule_test(self):
        if not Settings.test_running:
            try:
                Settings.angle_1 = self.rotate1_spinbox.value()
                Settings.angle_2 = self.rotate2_spinbox.value()
                
                self.Test_Thread = Threads.Test()
                self.Test_Thread.started.connect(lambda: UI_Update.test_start(self))
                self.Test_Thread.finished.connect(lambda: UI_Update.test_end(self))
                self.Test_Thread.start()
            except Exception as e:
                print(e)
        else:
            UI_Update.test_end(self)
            Settings.test_running=False

    def schedule_run(self):
        if not Settings.sch_running:
            try:
                Settings.angle_1 = self.rotate1_spinbox.value()
                Settings.angle_2 = self.rotate2_spinbox.value()
                Settings.delay_1 = self.wait1_spinbox.value()
                Settings.delay_2 = self.wait2_spinbox.value()
                
                self.Schedule_Thread = Threads.Schedule()
                self.Schedule_Thread.started.connect(lambda: UI_Update.schedule_start(self))
                self.Schedule_Thread.start()
            except Exception as e:
                print(e)
        else:
            UI_Update.schedule_end(self)
            Settings.sch_running=False       

    def start_snapshot(self):
        try:
            self.Camera_update()
            self.Snap_Thread = Threads.Snap()
            self.Snap_Thread.started.connect(lambda: UI_Update.imaging_disable(self))
            self.Snap_Thread.finished.connect(lambda: UI_Update.update_frame(self,"../_temp/snapshot.jpg"))
            self.Snap_Thread.start()
            
            
        except Exception as e:
            print(e)

    def start_livefeed(self):
        try:
            Settings.livetime = self.liveFeed_spinBox.value()
            self.livefeed_Thread = Threads.Live()
            self.livefeed_Thread.started.connect(lambda: UI_Update.imaging_disable(self))
            self.livefeed_Thread.finished.connect(lambda: UI_Update.imaging_enable(self))
            self.livefeed_Thread.start()
            
            
        except Exception as e:
            print(e)

    def start_preview(self):
        try:
            self.Camera_update()
            self.Preview_Thread = Threads.Preview()
            self.Preview_Thread.started.connect(lambda: UI_Update.imaging_disable(self))
            if(Settings.image_format):
                self.Preview_Thread.finished.connect(lambda: UI_Update.update_frame(self,"../_temp/preview.jpg"))
            else:
                self.Preview_Thread.finished.connect(lambda: UI_Update.update_frame(self,"../_temp/preview.png"))
            self.Preview_Thread.start()
            
        except Exception as e:
            print(e)
            
    def Camera_update(self):
        Settings.AOI_X = self.AOIX_doubleSpinBox.value()
        Settings.AOI_Y = self.AOIY_doubleSpinBox.value()
        Settings.AOI_W = self.AOIW_doubleSpinBox.value()
        Settings.AOI_H = self.AOIH_doubleSpinBox.value()
        
        Settings.x_resolution=self.x_resolution_spinBox.value()
        Settings.y_resolution=self.y_resolution_spinBox.value()

        if(self.JPG_radioButton.isChecked()):
            Settings.image_format = 1
        else:
            Settings.image_format = 0

    def rotate_image(self):
        try:
            self.Camera_update()
            Settings.rotation += 1
            self.Snap_Thread = Threads.Snap()
            self.Snap_Thread.started.connect(lambda: UI_Update.imaging_disable(self))
            self.Snap_Thread.finished.connect(lambda: UI_Update.update_frame(self,"../_temp/snapshot.jpg"))
            self.Snap_Thread.start()
            
            
        except Exception as e:
            print(e)

    def IST_Edit(self):
        Settings.sequence_name = self.imageTitle_lineEdit.text().replace(" ", "_")
        self.imageTitle_lineEdit.setText(Settings.sequence_name)
        Settings.full_dir = Settings.default_dir + "/" + Settings.sequence_name
        self.directory_label.setText(Settings.full_dir)
        
        if Settings.date not in Settings.sequence_name: 
            self.addDate_pushButton.setEnabled(True)
        if(len(Settings.sequence_name) == 0):
            self.addDate_pushButton.setEnabled(False)
        UI_Update.validate_input(self)

    def add_date(self):
        Settings.sequence_name = Settings.sequence_name + "_" + Settings.date
        self.imageTitle_lineEdit.setText(Settings.sequence_name)
        Settings.full_dir = Settings.default_dir + "/" + Settings.sequence_name
        self.directory_label.setText(Settings.full_dir)
        self.addDate_pushButton.setEnabled(False)
        
                
 # access variables inside of the UI's file
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self) # gets defined in the UI file
        Settings.init(self)
        
        
        self.Start_spinBox.valueChanged.connect(lambda: UI_Update.LED_validate(self))
        self.End_spinBox.valueChanged.connect(lambda: UI_Update.LED_validate(self))

        self.lightConfirm_pushButton.clicked.connect(lambda: Commands.light_confirm(self))
        self.lightReset_pushButton.clicked.connect(lambda: Commands.light_reset(self))
        
        self.disco_pushButton.clicked.connect(lambda: Commands.disco_run(self))
        self.rainbow_pushButton.clicked.connect(lambda: Commands.rainbow_run(self))
        self.sundial_pushButton.clicked.connect(lambda: Commands.sundial_run(self))
        self.pulse_pushButton.clicked.connect(lambda: Commands.pulse_run(self))

        self.confirmCycle_pushButton.clicked.connect(lambda: self.start_cycle())
        
        self.schedulerTest_pushButton.clicked.connect(lambda: self.schedule_test())
        self.schedulerSet_pushButton.clicked.connect(lambda: self.schedule_run())
        self.motorSpeed_slider.valueChanged.connect(lambda: Commands.motorSliderChange(self))
        self.motorSpeed_slider.sliderReleased.connect(lambda: Commands.motorSliderRelease(self))

        self.clinostatSet_pushButton.clicked.connect(lambda: Commands.clinoStart(self))
        self.snapshot_pushButton.clicked.connect(lambda: self.start_snapshot())
        self.liveFeed_pushButton.clicked.connect(lambda: self.start_livefeed())
        self.preview_pushButton.clicked.connect(lambda: self.start_preview())
        self.x_resolution_spinBox.valueChanged.connect(lambda: self.update_resolution())
        self.y_resolution_spinBox.valueChanged.connect(lambda: self.update_resolution())
        self.rotate_pushButton.clicked.connect(lambda: self.rotate_image())

        self.motorConfirm_pushButton.clicked.connect(lambda: Commands.motor_rotate(self))

        self.imageTitle_lineEdit.textChanged.connect(lambda: self.IST_Edit())
        self.addDate_pushButton.clicked.connect(lambda: self.add_date())
        

        

        
        
        '''

        #load default email
        fh = open("../_temp/save_data.txt", "r") 
        self.Dropbox_Email.setText(fh.readline())
        fh.close
        self.Email_Change()
        
        
        self.IST_Editor.textChanged.connect(lambda: self.IST_Edit())
        self.add_Date.clicked.connect(lambda: self.Add_Date())
        self.Dropbox_Email.textChanged.connect(lambda: self.Email_Change())
        self.Dropbox_Confirm.clicked.connect(lambda: self.Email_Entered())
        self.Save_Default.clicked.connect(lambda: self.Save_Email())
        self.Storage_Directory.clicked.connect(lambda: self.Select_Storage_Directory())
        self.Start_Schedule.clicked.connect(lambda: self.start_scheduler())
        self.Set_Schedule.clicked.connect(lambda: self.Confirm_Schedule())
        self.Test_Run.clicked.connect(lambda: self.test_run())
        
        self.Reset_Position.clicked.connect(lambda: self.reset_position())
        self.Speed_Select.valueChanged.connect(lambda: self.value_changed())
        self.Speed_Select.sliderReleased.connect(lambda: self.slider_released())
        self.Full_Color_Select.activated.connect(lambda: Command.full_color_change(self))
        self.brightness_spinBox.valueChanged.connect(lambda: self.brightness_change())
        self.Left_Select.activated.connect(lambda: Command.half_color_change_left(self))
        self.Right_Select.activated.connect(lambda: Command.half_color_change_right(self))
        self.Top_Color_Select.activated.connect(lambda: Command.third_color_change_top(self))
        self.LL_Color_Select.activated.connect(lambda: Command.third_color_change_lower_left(self))
        self.LR_Color_Select.activated.connect(lambda: Command.third_color_change_lower_right(self))

        self.R_spinBox.valueChanged.connect(lambda: self.custom_update())
        self.G_spinBox.valueChanged.connect(lambda: self.custom_update())
        self.B_spinBox.valueChanged.connect(lambda: self.custom_update())

        self.Live_Feed.clicked.connect(lambda: self.Start_Live_Feed())
        self.Inject_Code.clicked.connect(lambda: Command.inject_code(self))'''


        

        
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
