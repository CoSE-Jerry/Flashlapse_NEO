# import basic libraries
import sys
import datetime

#import UI functions
import UI_Update_Disable
import UI_Update_Enable
import UI_Update_General

#import custom functions
import Camera
 
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
sequence_name = None
default_dir = "/home/pi/Desktop"
full_dir = ""
 
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
        sequence_name = self.IST_Editor.text()
        full_dir = default_dir + "/" + sequence_name
        self.Directory_Label.setText(full_dir)

    def Add_Date(self):
        full_dir=full_dir + "_" + str(datetime.date.today()).replace("-","_")
        self.Directory_Label.setText(full_dir)

    def Start_Rotate(self):
        try:
            UI_Update_Enable.snap_enable(self)
        except Exception as e:
            print(e)
            
 # access variables inside of the UI's file
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self) # gets defined in the UI file
        self.Snapshot.clicked.connect(lambda: self.Start_Snapshot())
        self.IST_Editor.editingFinished.connect(lambda: self.IST_Edit())
        self.Rotate.clicked.connect(lambda: self.Start_Rotate())
        self.add_Date.clicked.connect(lambda: self.Add_Date())

        
        
 
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
