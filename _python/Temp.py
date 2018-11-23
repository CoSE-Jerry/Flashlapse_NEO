# import vital libraries
import sys

#import UI functions
import UI_Update_Disable
import UI_Update_Enable

#import custom functions
import Camera
 
# import Qt content
import PyQt5.*
from PyQt5.QtWidgets import *
 
# import generated UI

import FlashLapse_UI
 
# create class for Raspberry Pi GUI
class MainWindow(QMainWindow, FlashLapse_UI.Ui_MainWindow):

    def Start_Snapshot(self):
        try:
            self.Snap_Thread = Camera.Snap()
            self.Snap_Thread.started.connect(lambda: UI_Update_Disable.snap_disable(self))
            self.Snap_Thread.finished.connect(lambda: UI_Update_Enable.snap_enable(self))
            self.Snap_Thread.start()
            
        except Exception as e:
            print(e)

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
        self.Rotate.clicked.connect(lambda: self.Start_Rotate())
        
 
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
