# main.py

import var
import subfile

var.init()          # Call only once
subfile.stuff()         # Do stuff with global var
print(var.myList[0]) # Check the result
var.myList.append('test')
print(var.myList[1])
