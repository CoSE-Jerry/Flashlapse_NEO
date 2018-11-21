# always seem to need this
import sys
 
# This gets the Qt stuff
import PyQt5
from PyQt5.QtWidgets import *
 
# This is our window from QtCreator
import FlashLapse_UI
 
# create class for our Raspberry Pi GUI
class MainWindow(QMainWindow, FlashLapse_UI.Ui_MainWindow):
 # access variables inside of the UI's file
 def __init__(self):
     super(self.__class__, self).__init__()
     self.setupUi(self) # gets defined in the UI file
 
# I feel better having one of these
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
