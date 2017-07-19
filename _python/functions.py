import Main
import FlashLapse_UI

import PyQt5
import functions
from PyQt5.QtWidgets import *

directory = None
name =None

def IST_Edit():

    print("test")
   # global directory, name
    name = FlashLapse_UI.IST_Editor.text()
    print("name: " + name)
   #directory = "/home/pi/Desktop/" + name
  #  Main.Directory.setText(directory)
