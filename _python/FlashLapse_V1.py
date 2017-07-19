# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FlashLapse_CP.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import PyQt5
from threading import Timer
from picamera import PiCamera
from time import sleep
from PyQt5.QtWidgets import QApplication
import os
import serial
name =None
directory = None
global stop
ASD = serial.Serial('/dev/ttyACM0', 9600)
interval = None
duration = None
total = None

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 480)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("/home/pi/Desktop/Flashlapse/_image/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Image_Frame = QtWidgets.QLabel(self.centralwidget)
        self.Image_Frame.setGeometry(QtCore.QRect(480, 20, 300, 300))
        self.Image_Frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Image_Frame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.Image_Frame.setLineWidth(5)
        self.Image_Frame.setText("")
        self.Image_Frame.setPixmap(QtGui.QPixmap("/home/pi/Desktop/Flashlapse/_image/background1.png"))
        self.Image_Frame.setScaledContents(True)
        self.Image_Frame.setObjectName("Image_Frame")
        self.Snapshot = QtWidgets.QPushButton(self.centralwidget)
        self.Snapshot.setEnabled(True)
        self.Snapshot.setGeometry(QtCore.QRect(679, 330, 101, 25))
        self.Snapshot.setObjectName("Snapshot")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(480, 330, 160, 51))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.JPG = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.JPG.setObjectName("JPG")
        self.JPG.setChecked(True)
        self.verticalLayout_4.addWidget(self.JPG)
        self.PNG = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.PNG.setObjectName("PNG")
        self.verticalLayout_4.addWidget(self.PNG)
        self.Control_Tab = QtWidgets.QTabWidget(self.centralwidget)
        self.Control_Tab.setGeometry(QtCore.QRect(30, 20, 441, 411))
        self.Control_Tab.setObjectName("Control_Tab")
        self.Lighting = QtWidgets.QWidget()
        self.Lighting.setObjectName("Lighting")
        self.Lights = QtWidgets.QTabWidget(self.Lighting)
        self.Lights.setGeometry(QtCore.QRect(10, 10, 381, 361))
        self.Lights.setObjectName("Lights")
        self.Constant = QtWidgets.QWidget()
        self.Constant.setObjectName("Constant")
        self.Constant_Mode = QtWidgets.QTabWidget(self.Constant)
        self.Constant_Mode.setGeometry(QtCore.QRect(10, 10, 321, 311))
        self.Constant_Mode.setObjectName("Constant_Mode")
        self.FullColor = QtWidgets.QWidget()
        self.FullColor.setObjectName("FullColor")
        self.Color_Frame = QtWidgets.QLabel(self.FullColor)
        self.Color_Frame.setGeometry(QtCore.QRect(30, 10, 250, 250))
        self.Color_Frame.setText("")
        self.Color_Frame.setPixmap(QtGui.QPixmap("/home/pi/Desktop/Flashlapse/_image/Color_None.png"))
        self.Color_Frame.setScaledContents(True)
        self.Color_Frame.setObjectName("Color_Frame")
        self.Full_Color_Select = QtWidgets.QComboBox(self.FullColor)
        self.Full_Color_Select.setGeometry(QtCore.QRect(120, 100, 69, 22))
        self.Full_Color_Select.setObjectName("Full_Color_Select")
        self.Full_Color_Select.addItem("")
        self.Full_Color_Select.addItem("")
        self.Full_Color_Select.addItem("")
        self.Full_Color_Select.addItem("")
        self.Constant_Mode.addTab(self.FullColor, "")
        self.HalfColor = QtWidgets.QWidget()
        self.HalfColor.setObjectName("HalfColor")
        self.Half_Left = QtWidgets.QLabel(self.HalfColor)
        self.Half_Left.setGeometry(QtCore.QRect(11, 10, 125, 250))
        self.Half_Left.setText("")
        self.Half_Left.setPixmap(QtGui.QPixmap("/home/pi/Desktop/Flashlapse/_image/Color_None_Left.png"))
        self.Half_Left.setScaledContents(True)
        self.Half_Left.setObjectName("Half_Left")
        self.Half_Right = QtWidgets.QLabel(self.HalfColor)
        self.Half_Right.setGeometry(QtCore.QRect(165, 10, 125, 250))
        self.Half_Right.setText("")
        self.Half_Right.setPixmap(QtGui.QPixmap("/home/pi/Desktop/Flashlapse/_image/Color_None_Right.png"))
        self.Half_Right.setScaledContents(True)
        self.Half_Right.setObjectName("Half_Right")
        self.layoutWidget = QtWidgets.QWidget(self.HalfColor)
        self.layoutWidget.setGeometry(QtCore.QRect(50, 130, 191, 22))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Left_Select = QtWidgets.QComboBox(self.layoutWidget)
        self.Left_Select.setObjectName("Left_Select")
        self.Left_Select.addItem("")
        self.Left_Select.addItem("")
        self.Left_Select.addItem("")
        self.Left_Select.addItem("")
        self.horizontalLayout.addWidget(self.Left_Select)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.Right_Select = QtWidgets.QComboBox(self.layoutWidget)
        self.Right_Select.setObjectName("Right_Select")
        self.Right_Select.addItem("")
        self.Right_Select.addItem("")
        self.Right_Select.addItem("")
        self.Right_Select.addItem("")
        self.horizontalLayout.addWidget(self.Right_Select)
        self.Constant_Mode.addTab(self.HalfColor, "")
        self.Lights.addTab(self.Constant, "")
        self.Presets = QtWidgets.QWidget()
        self.Presets.setObjectName("Presets")
        self.Presets1 = QtWidgets.QTabWidget(self.Presets)
        self.Presets1.setGeometry(QtCore.QRect(10, 10, 321, 311))
        self.Presets1.setObjectName("Presets1")
        self.Gravitropic = QtWidgets.QWidget()
        self.Gravitropic.setObjectName("Gravitropic")
        self.Gravi_Text = QtWidgets.QTextBrowser(self.Gravitropic)
        self.Gravi_Text.setGeometry(QtCore.QRect(10, 20, 290, 110))
        self.Gravi_Text.setObjectName("Gravi_Text")
        self.Gravi_Confirm = QtWidgets.QPushButton(self.Gravitropic)
        self.Gravi_Confirm.setGeometry(QtCore.QRect(220, 195, 81, 23))
        self.Gravi_Confirm.setObjectName("Gravi_Confirm")
        self.layoutWidget1 = QtWidgets.QWidget(self.Gravitropic)
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 160, 189, 90))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.Color_Gravi = QtWidgets.QLabel(self.layoutWidget1)
        self.Color_Gravi.setAlignment(QtCore.Qt.AlignCenter)
        self.Color_Gravi.setObjectName("Color_Gravi")
        self.horizontalLayout_2.addWidget(self.Color_Gravi)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.Gravi_Red = QtWidgets.QRadioButton(self.layoutWidget1)
        self.Gravi_Red.setObjectName("Gravi_Red")
        self.verticalLayout_5.addWidget(self.Gravi_Red)
        self.Gravi_Green = QtWidgets.QRadioButton(self.layoutWidget1)
        self.Gravi_Green.setObjectName("Gravi_Green")
        self.verticalLayout_5.addWidget(self.Gravi_Green)
        self.Gravi_Blue = QtWidgets.QRadioButton(self.layoutWidget1)
        self.Gravi_Blue.setObjectName("Gravi_Blue")
        self.verticalLayout_5.addWidget(self.Gravi_Blue)
        self.Gravi_White = QtWidgets.QRadioButton(self.layoutWidget1)
        self.Gravi_White.setObjectName("Gravi_White")
        self.verticalLayout_5.addWidget(self.Gravi_White)
        self.horizontalLayout_2.addLayout(self.verticalLayout_5)
        self.Presets1.addTab(self.Gravitropic, "")
        self.Germination = QtWidgets.QWidget()
        self.Germination.setObjectName("Germination")
        self.Germi_Text = QtWidgets.QTextBrowser(self.Germination)
        self.Germi_Text.setGeometry(QtCore.QRect(10, 20, 290, 110))
        self.Germi_Text.setObjectName("Germi_Text")
        self.Germi_Confirm = QtWidgets.QPushButton(self.Germination)
        self.Germi_Confirm.setGeometry(QtCore.QRect(220, 195, 81, 23))
        self.Germi_Confirm.setObjectName("Germi_Confirm")
        self.layoutWidget_2 = QtWidgets.QWidget(self.Germination)
        self.layoutWidget_2.setGeometry(QtCore.QRect(10, 160, 189, 90))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.Color_Germi = QtWidgets.QLabel(self.layoutWidget_2)
        self.Color_Germi.setAlignment(QtCore.Qt.AlignCenter)
        self.Color_Germi.setObjectName("Color_Germi")
        self.horizontalLayout_3.addWidget(self.Color_Germi)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.Germi_Red = QtWidgets.QRadioButton(self.layoutWidget_2)
        self.Germi_Red.setObjectName("Germi_Red")
        self.verticalLayout_7.addWidget(self.Germi_Red)
        self.Germi_Green = QtWidgets.QRadioButton(self.layoutWidget_2)
        self.Germi_Green.setObjectName("Germi_Green")
        self.verticalLayout_7.addWidget(self.Germi_Green)
        self.Germi_Blue = QtWidgets.QRadioButton(self.layoutWidget_2)
        self.Germi_Blue.setObjectName("Germi_Blue")
        self.verticalLayout_7.addWidget(self.Germi_Blue)
        self.Germi_White = QtWidgets.QRadioButton(self.layoutWidget_2)
        self.Germi_White.setObjectName("Germi_White")
        self.verticalLayout_7.addWidget(self.Germi_White)
        self.horizontalLayout_3.addLayout(self.verticalLayout_7)
        self.Presets1.addTab(self.Germination, "")
        self.Barrier = QtWidgets.QWidget()
        self.Barrier.setObjectName("Barrier")
        self.Barrier_Text = QtWidgets.QTextBrowser(self.Barrier)
        self.Barrier_Text.setGeometry(QtCore.QRect(10, 20, 290, 110))
        self.Barrier_Text.setObjectName("Barrier_Text")
        self.Barrier_Confirm = QtWidgets.QPushButton(self.Barrier)
        self.Barrier_Confirm.setGeometry(QtCore.QRect(220, 195, 81, 23))
        self.Barrier_Confirm.setObjectName("Barrier_Confirm")
        self.layoutWidget_3 = QtWidgets.QWidget(self.Barrier)
        self.layoutWidget_3.setGeometry(QtCore.QRect(10, 160, 189, 90))
        self.layoutWidget_3.setObjectName("layoutWidget_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.layoutWidget_3)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.Color_Barri = QtWidgets.QLabel(self.layoutWidget_3)
        self.Color_Barri.setAlignment(QtCore.Qt.AlignCenter)
        self.Color_Barri.setObjectName("Color_Barri")
        self.horizontalLayout_4.addWidget(self.Color_Barri)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.Barri_Red = QtWidgets.QRadioButton(self.layoutWidget_3)
        self.Barri_Red.setObjectName("Barri_Red")
        self.verticalLayout_8.addWidget(self.Barri_Red)
        self.Barri_Green = QtWidgets.QRadioButton(self.layoutWidget_3)
        self.Barri_Green.setObjectName("Barri_Green")
        self.verticalLayout_8.addWidget(self.Barri_Green)
        self.Barri_Blue = QtWidgets.QRadioButton(self.layoutWidget_3)
        self.Barri_Blue.setObjectName("Barri_Blue")
        self.verticalLayout_8.addWidget(self.Barri_Blue)
        self.Barri_White = QtWidgets.QRadioButton(self.layoutWidget_3)
        self.Barri_White.setObjectName("Barri_White")
        self.verticalLayout_8.addWidget(self.Barri_White)
        self.horizontalLayout_4.addLayout(self.verticalLayout_8)
        self.Presets1.addTab(self.Barrier, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.disco = QtWidgets.QPushButton(self.tab)
        self.disco.setGeometry(QtCore.QRect(40, 70, 231, 141))
        self.disco.setObjectName("disco")
        self.Presets1.addTab(self.tab, "")
        self.Lights.addTab(self.Presets, "")
        self.Control_Tab.addTab(self.Lighting, "")
        self.Imaging = QtWidgets.QWidget()
        self.Imaging.setObjectName("Imaging")
        self.layoutWidget2 = QtWidgets.QWidget(self.Imaging)
        self.layoutWidget2.setGeometry(QtCore.QRect(10, 10, 381, 301))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.Image_Title = QtWidgets.QLabel(self.layoutWidget2)
        self.Image_Title.setObjectName("Image_Title")
        self.verticalLayout.addWidget(self.Image_Title)
        self.IST_Editor = QtWidgets.QLineEdit(self.layoutWidget2)
        self.IST_Editor.setObjectName("IST_Editor")
        self.verticalLayout.addWidget(self.IST_Editor)
        self.Image_Interval = QtWidgets.QLabel(self.layoutWidget2)
        self.Image_Interval.setObjectName("Image_Interval")
        self.verticalLayout.addWidget(self.Image_Interval)
        self.ICI_spinBox = QtWidgets.QSpinBox(self.layoutWidget2)
        self.ICI_spinBox.setMaximum(100000)
        self.ICI_spinBox.setObjectName("ICI_spinBox")
        self.verticalLayout.addWidget(self.ICI_spinBox)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.Image_Duration = QtWidgets.QLabel(self.layoutWidget2)
        self.Image_Duration.setObjectName("Image_Duration")
        self.verticalLayout_2.addWidget(self.Image_Duration)
        self.ISD_spinBox = QtWidgets.QSpinBox(self.layoutWidget2)
        self.ISD_spinBox.setMaximum(100000)
        self.ISD_spinBox.setObjectName("ISD_spinBox")
        self.verticalLayout_2.addWidget(self.ISD_spinBox)
        self.line = QtWidgets.QFrame(self.layoutWidget2)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_2.addWidget(self.line)
        spacerItem1 = QtWidgets.QSpacerItem(20, 120, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.Directory = QtWidgets.QLabel(self.layoutWidget2)
        self.Directory.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Directory.setAlignment(QtCore.Qt.AlignCenter)
        self.Directory.setObjectName("Directory")
        self.verticalLayout_2.addWidget(self.Directory)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.live_feed = QtWidgets.QPushButton(self.layoutWidget2)
        self.live_feed.setObjectName("live_feed")
        self.verticalLayout_3.addWidget(self.live_feed)
        self.layoutWidget3 = QtWidgets.QWidget(self.Imaging)
        self.layoutWidget3.setGeometry(QtCore.QRect(14, 330, 411, 42))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.layoutWidget3)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.Console = QtWidgets.QLabel(self.layoutWidget3)
        self.Console.setText("")
        self.Console.setObjectName("Console")
        self.verticalLayout_6.addWidget(self.Console)
        self.Progress_Bar = QtWidgets.QProgressBar(self.layoutWidget3)
        self.Progress_Bar.setProperty("value", 0)
        self.Progress_Bar.setObjectName("Progress_Bar")
        self.verticalLayout_6.addWidget(self.Progress_Bar)
        self.layoutWidget.raise_()
        self.layoutWidget.raise_()
        self.Control_Tab.addTab(self.Imaging, "")
        self.Start_Imaging = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.Start_Imaging.setGeometry(QtCore.QRect(470, 380, 291, 51))
        self.Start_Imaging.setAutoFillBackground(False)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("/home/pi/Desktop/Flashlapse/_image/Start-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Start_Imaging.setIcon(icon1)
        self.Start_Imaging.setIconSize(QtCore.QSize(35, 35))
        self.Start_Imaging.setObjectName("Start_Imaging")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.actionOpen_Directory = QtWidgets.QAction(MainWindow)
        self.actionOpen_Directory.setObjectName("actionOpen_Directory")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionCreate_Timelapse = QtWidgets.QAction(MainWindow)
        self.actionCreate_Timelapse.setObjectName("actionCreate_Timelapse")
        self.menuFile.addAction(self.actionOpen_Directory)
        self.menuFile.addAction(self.actionCreate_Timelapse)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        self.Control_Tab.setCurrentIndex(0)
        self.Lights.setCurrentIndex(0)
        self.Constant_Mode.setCurrentIndex(0)
        self.Presets1.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "FlashLapse Commad Point"))
        self.Snapshot.setText(_translate("MainWindow", "Snapshot"))
        self.JPG.setText(_translate("MainWindow", "JPG"))
        self.PNG.setText(_translate("MainWindow", "PNG"))
        self.Full_Color_Select.setCurrentText(_translate("MainWindow", "None"))
        self.Full_Color_Select.setItemText(0, _translate("MainWindow", "none"))
        self.Full_Color_Select.setItemText(1, _translate("MainWindow", "Red"))
        self.Full_Color_Select.setItemText(2, _translate("MainWindow", "Green"))
        self.Full_Color_Select.setItemText(3, _translate("MainWindow", "Blue"))
        self.Constant_Mode.setTabText(self.Constant_Mode.indexOf(self.FullColor), _translate("MainWindow", "Full"))
        self.Left_Select.setItemText(0, _translate("MainWindow", "None"))
        self.Left_Select.setItemText(1, _translate("MainWindow", "Red"))
        self.Left_Select.setItemText(2, _translate("MainWindow", "Green"))
        self.Left_Select.setItemText(3, _translate("MainWindow", "Blue"))
        self.Right_Select.setItemText(0, _translate("MainWindow", "None"))
        self.Right_Select.setItemText(1, _translate("MainWindow", "Red"))
        self.Right_Select.setItemText(2, _translate("MainWindow", "Green"))
        self.Right_Select.setItemText(3, _translate("MainWindow", "Blue"))
        self.Constant_Mode.setTabText(self.Constant_Mode.indexOf(self.HalfColor), _translate("MainWindow", "Half"))
        self.Lights.setTabText(self.Lights.indexOf(self.Constant), _translate("MainWindow", "Constant"))
        self.Gravi_Text.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">12 hours full spectrum light from above, 90 degree rotation &amp; all lights become a certain color.</p></body></html>"))
        self.Gravi_Confirm.setText(_translate("MainWindow", "Confirm "))
        self.Color_Gravi.setText(_translate("MainWindow", "Color:"))
        self.Gravi_Red.setText(_translate("MainWindow", "Red"))
        self.Gravi_Green.setText(_translate("MainWindow", "Green"))
        self.Gravi_Blue.setText(_translate("MainWindow", "Blue"))
        self.Gravi_White.setText(_translate("MainWindow", "White"))
        self.Presets1.setTabText(self.Presets1.indexOf(self.Gravitropic), _translate("MainWindow", "Gravitropic"))
        self.Germi_Text.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">7 days of a certain colored light from all sides.</p></body></html>"))
        self.Germi_Confirm.setText(_translate("MainWindow", "Confirm "))
        self.Color_Germi.setText(_translate("MainWindow", "Color:"))
        self.Germi_Red.setText(_translate("MainWindow", "Red"))
        self.Germi_Green.setText(_translate("MainWindow", "Green"))
        self.Germi_Blue.setText(_translate("MainWindow", "Blue"))
        self.Germi_White.setText(_translate("MainWindow", "White"))
        self.Presets1.setTabText(self.Presets1.indexOf(self.Germination), _translate("MainWindow", "Germination"))
        self.Barrier_Text.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">24 hour of a certain colored light from above.</p></body></html>"))
        self.Barrier_Confirm.setText(_translate("MainWindow", "Confirm "))
        self.Color_Barri.setText(_translate("MainWindow", "Color:"))
        self.Barri_Red.setText(_translate("MainWindow", "Red"))
        self.Barri_Green.setText(_translate("MainWindow", "Green"))
        self.Barri_Blue.setText(_translate("MainWindow", "Blue"))
        self.Barri_White.setText(_translate("MainWindow", "White"))
        self.Presets1.setTabText(self.Presets1.indexOf(self.Barrier), _translate("MainWindow", "Barrier"))
        self.disco.setText(_translate("MainWindow", "Start!"))
        self.Presets1.setTabText(self.Presets1.indexOf(self.tab), _translate("MainWindow", "Disco"))
        self.Lights.setTabText(self.Lights.indexOf(self.Presets), _translate("MainWindow", "Presets"))
        self.Control_Tab.setTabText(self.Control_Tab.indexOf(self.Lighting), _translate("MainWindow", "Lighting"))
        self.Image_Title.setText(_translate("MainWindow", "Image Sequence Title"))
        self.Image_Interval.setText(_translate("MainWindow", "Image Capture Interval"))
        self.ICI_spinBox.setSuffix(_translate("MainWindow", " s"))
        self.Image_Duration.setText(_translate("MainWindow", "Image Sequence Duration"))
        self.ISD_spinBox.setSuffix(_translate("MainWindow", " min"))
        self.Directory.setText(_translate("MainWindow", "Storage Directory"))
        self.live_feed.setText(_translate("MainWindow", "Start Live Feed (30s)"))
        self.Control_Tab.setTabText(self.Control_Tab.indexOf(self.Imaging), _translate("MainWindow", "Imaging"))
        self.Start_Imaging.setText(_translate("MainWindow", "Start Image Sequence"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionOpen_Directory.setText(_translate("MainWindow", "Open Directory"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionCreate_Timelapse.setText(_translate("MainWindow", "Create Timelapse"))
        self.run()

    def run(self):
        self.IST_Editor.editingFinished.connect(self.IST_Edit)
        self.ICI_spinBox.valueChanged.connect(self.ICI_Change)
        self.ISD_spinBox.valueChanged.connect(self.ISD_Change)
        self.Snapshot.clicked.connect(self.take_snapshot)
        self.live_feed.clicked.connect(self.start_live_feed)
        self.Start_Imaging.clicked.connect(self.start_imaging)
        self.Full_Color_Select.currentIndexChanged.connect(self.full_color_change)
        self.Left_Select.currentIndexChanged.connect(self.half_color_change_left)
        self.Right_Select.currentIndexChanged.connect(self.half_color_change_right)
        self.Gravi_Confirm.clicked.connect(self.gravi_confirm)
        self.Germi_Confirm.clicked.connect(self.germi_confirm)
        self.Barrier_Confirm.clicked.connect(self.barri_confirm)
        self.disco.clicked.connect(self.disco_confirm)

    def IST_Edit(self):
        global directory, name
        name = self.IST_Editor.text()
        print("name: " + name)
        directory = "/home/pi/Desktop/" + name
        self.Directory.setText(directory)

    def ICI_Change(self):
        global interval
        interval = self.ICI_spinBox.value()

    def ISD_Change(self):
        global duration
        duration = self.ISD_spinBox.value()
        
    def take_snapshot(self):
        with PiCamera() as camera:
            camera.resolution = (2464,2464)
            camera.capture("/home/pi/Desktop/Flashlapse/temp/snap.jpg")
        user_img = PyQt5.QtGui.QImage("/home/pi/Desktop/Flashlapse/temp/snap.jpg")
        self.Image_Frame.setPixmap(QtGui.QPixmap(user_img))

    def start_live_feed(self):
        with PiCamera() as camera:
            camera.start_preview()
            sleep(30)
            camera.stop_preview()
            

    def start_imaging(self):
        global directory, name
        global duration, interval, total
        total = int((duration*60)/interval)
        self.Progress_Bar.setMaximum(total)
        self.Start_Imaging.setText("Imaging...")
        if self.JPG.isChecked():
            finaldir = directory+"/"+ name +"_%04d.jpg"
        elif self.PNG.isChecked():
            finaldir = directory+"/"+ name +"_%04d.png"
        if(not os.path.isdir(directory)):
            os.mkdir(directory)
        for i in range(total):
            with PiCamera() as camera:
                camera.resolution = (2464,2464)
                sleep(1)
                temp = finaldir % i
                camera.capture(temp)
            current_img = PyQt5.QtGui.QImage(temp)
            self.Image_Frame.setPixmap(QtGui.QPixmap(current_img))
            self.Progress_Bar.setValue(i+1)
            QApplication.processEvents()

            sleep(interval-1)

    def stop_imaging(self):
        global stop
        stop = 2
        self.Start_Imaging.setText("Start Image Sequence")


    def full_color_change(self):
        temp = self.Full_Color_Select.currentIndex()
        if temp == 1:
            ASD.write(bytes('1', 'UTF-8'))
            self.Color_Frame.setPixmap(QtGui.QPixmap("/home/pi/Desktop/Flashlapse/_image/Color_Red.png"))
        elif temp == 2:
            ASD.write(bytes('2', 'UTF-8'))
            self.Color_Frame.setPixmap(QtGui.QPixmap("/home/pi/Desktop/Flashlapse/_image/Color_Green.png"))
        elif temp == 3:
            ASD.write(bytes('3', 'UTF-8'))
            self.Color_Frame.setPixmap(QtGui.QPixmap("/home/pi/Desktop/Flashlapse/_image/Color_Blue.png"))
        elif temp == 4:
            ASD.write(bytes('4', 'UTF-8'))
            self.Color_Frame.setPixmap(QtGui.QPixmap("/home/pi/Desktop/Flashlapse/_image/Color_Rainbow.png"))
        else:
            ASD.write(bytes('0', 'UTF-8'))
            self.Color_Frame.setPixmap(QtGui.QPixmap("/home/pi/Desktop/Flashlapse/_image/Color_None.png"))

        self.Half_Left.setPixmap(QtGui.QPixmap("/home/pi/Desktop/Flashlapse/_image/Color_None_Left.png"))
        self.Half_Right.setPixmap(QtGui.QPixmap("/home/pi/Desktop/Flashlapse/_image/Color_None_Right.png"))

    
    def half_color_change_left(self):
        temp = self.Left_Select.currentIndex()
        if temp == 1:
            ASD.write(bytes('a', 'UTF-8'))
            self.Half_Left.setPixmap(QtGui.QPixmap("/home/pi/Desktop/Flashlapse/_image/Color_Red_Left.png"))
        elif temp == 2:
            ASD.write(bytes('b', 'UTF-8'))
            self.Half_Left.setPixmap(QtGui.QPixmap("/home/pi/Desktop/Flashlapse/_image/Color_Green_Left.png"))
        elif temp == 3:
            ASD.write(bytes('c', 'UTF-8'))
            self.Half_Left.setPixmap(QtGui.QPixmap("/home/pi/Desktop/Flashlapse/_image/Color_Blue_Left.png"))
        elif temp == 0:
            ASD.write(bytes('A', 'UTF-8'))
            self.Half_Left.setPixmap(QtGui.QPixmap("/home/pi/Desktop/Flashlapse/_image/Color_None_Left.png"))

            self.Color_Frame.setPixmap(QtGui.QPixmap("/home/pi/Desktop/Flashlapse/_image/Color_None.png"))

    def half_color_change_right(self):
        temp = self.Right_Select.currentIndex()
        if temp == 1:
            ASD.write(bytes('d', 'UTF-8'))
            self.Half_Right.setPixmap(QtGui.QPixmap("/home/pi/Desktop/Flashlapse/_image/Color_Red_Right.png"))
        elif temp == 2:
            ASD.write(bytes('e', 'UTF-8'))
            self.Half_Right.setPixmap(QtGui.QPixmap("/home/pi/Desktop/Flashlapse/_image/Color_Green_Right.png"))
        elif temp == 3:
            ASD.write(bytes('f', 'UTF-8'))
            self.Half_Right.setPixmap(QtGui.QPixmap("/home/pi/Desktop/Flashlapse/_image/Color_Blue_Right.png"))
        elif temp == 0:
            ASD.write(bytes('B', 'UTF-8'))
            self.Half_Right.setPixmap(QtGui.QPixmap("/home/pi/Desktop/Flashlapse/_image/Color_None_Right.png"))

        self.Color_Frame.setPixmap(QtGui.QPixmap("/home/pi/Desktop/Flashlapse/_image/Color_None.png"))

    def gravi_confirm(self):
        if self.Gravi_Red.isChecked():
            ASD.write(bytes('g', 'UTF-8'))
        elif self.Gravi_Green.isChecked():
            ASD.write(bytes('h', 'UTF-8'))
        elif self.Gravi_Blue.isChecked():
            ASD.write(bytes('i', 'UTF-8'))
        elif self.Gravi_White.isChecked():
            ASD.write(bytes('j', 'UTF-8'))


    def germi_confirm(self):
        if self.Germi_Red.isChecked():
            ASD.write(bytes('k', 'UTF-8'))
        elif self.Germi_Green.isChecked():
            ASD.write(bytes('l', 'UTF-8'))
        elif self.Germi_Blue.isChecked():
            ASD.write(bytes('m', 'UTF-8'))
        elif self.Germi_White.isChecked():
            ASD.write(bytes('n', 'UTF-8'))

    def barri_confirm(self):
        if self.Barri_Red.isChecked():
            ASD.write(bytes('o', 'UTF-8'))
        elif self.Barri_Green.isChecked():
            ASD.write(bytes('p', 'UTF-8'))
        elif self.Barri_Blue.isChecked():
            ASD.write(bytes('q', 'UTF-8'))
        elif self.Barri_White.isChecked():
            ASD.write(bytes('r', 'UTF-8'))
            
    def disco_confirm(self):
        ASD.write(bytes('s', 'UTF-8'))
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

