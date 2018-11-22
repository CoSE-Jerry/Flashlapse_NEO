# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FlashLapse_CP.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 545)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../_image/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Image_Frame = QtWidgets.QLabel(self.centralwidget)
        self.Image_Frame.setGeometry(QtCore.QRect(480, 20, 300, 300))
        self.Image_Frame.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.Image_Frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Image_Frame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.Image_Frame.setLineWidth(5)
        self.Image_Frame.setText("")
        self.Image_Frame.setPixmap(QtGui.QPixmap("../_image/background.jpg"))
        self.Image_Frame.setScaledContents(True)
        self.Image_Frame.setObjectName("Image_Frame")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(490, 430, 91, 51))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.JPG = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.JPG.setChecked(True)
        self.JPG.setObjectName("JPG")
        self.verticalLayout_4.addWidget(self.JPG)
        self.PNG = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.PNG.setObjectName("PNG")
        self.verticalLayout_4.addWidget(self.PNG)
        self.Control_Tab = QtWidgets.QTabWidget(self.centralwidget)
        self.Control_Tab.setGeometry(QtCore.QRect(20, 20, 451, 481))
        self.Control_Tab.setTabPosition(QtWidgets.QTabWidget.North)
        self.Control_Tab.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.Control_Tab.setObjectName("Control_Tab")
        self.Lighting = QtWidgets.QWidget()
        self.Lighting.setObjectName("Lighting")
        self.Constant_Mode = QtWidgets.QTabWidget(self.Lighting)
        self.Constant_Mode.setGeometry(QtCore.QRect(20, 10, 401, 371))
        self.Constant_Mode.setObjectName("Constant_Mode")
        self.FullColor = QtWidgets.QWidget()
        self.FullColor.setObjectName("FullColor")
        self.Color_Frame = QtWidgets.QLabel(self.FullColor)
        self.Color_Frame.setGeometry(QtCore.QRect(50, 20, 300, 300))
        self.Color_Frame.setText("")
        self.Color_Frame.setPixmap(QtGui.QPixmap("../_image/Color_None.png"))
        self.Color_Frame.setScaledContents(True)
        self.Color_Frame.setObjectName("Color_Frame")
        self.Full_Color_Select = QtWidgets.QComboBox(self.FullColor)
        self.Full_Color_Select.setGeometry(QtCore.QRect(170, 160, 69, 22))
        self.Full_Color_Select.setObjectName("Full_Color_Select")
        self.Full_Color_Select.addItem("")
        self.Full_Color_Select.addItem("")
        self.Full_Color_Select.addItem("")
        self.Full_Color_Select.addItem("")
        self.Full_Color_Select.addItem("")
        self.Constant_Mode.addTab(self.FullColor, "")
        self.HalfColor = QtWidgets.QWidget()
        self.HalfColor.setObjectName("HalfColor")
        self.Half_Left = QtWidgets.QLabel(self.HalfColor)
        self.Half_Left.setGeometry(QtCore.QRect(20, 20, 150, 300))
        self.Half_Left.setText("")
        self.Half_Left.setPixmap(QtGui.QPixmap("../_image/Color_None_Left.png"))
        self.Half_Left.setScaledContents(True)
        self.Half_Left.setObjectName("Half_Left")
        self.Half_Right = QtWidgets.QLabel(self.HalfColor)
        self.Half_Right.setGeometry(QtCore.QRect(230, 20, 150, 300))
        self.Half_Right.setText("")
        self.Half_Right.setPixmap(QtGui.QPixmap("../_image/Color_None_Right.png"))
        self.Half_Right.setScaledContents(True)
        self.Half_Right.setObjectName("Half_Right")
        self.layoutWidget_2 = QtWidgets.QWidget(self.HalfColor)
        self.layoutWidget_2.setGeometry(QtCore.QRect(99, 150, 191, 24))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Left_Select = QtWidgets.QComboBox(self.layoutWidget_2)
        self.Left_Select.setObjectName("Left_Select")
        self.Left_Select.addItem("")
        self.Left_Select.addItem("")
        self.Left_Select.addItem("")
        self.Left_Select.addItem("")
        self.Left_Select.addItem("")
        self.horizontalLayout.addWidget(self.Left_Select)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.Right_Select = QtWidgets.QComboBox(self.layoutWidget_2)
        self.Right_Select.setObjectName("Right_Select")
        self.Right_Select.addItem("")
        self.Right_Select.addItem("")
        self.Right_Select.addItem("")
        self.Right_Select.addItem("")
        self.Right_Select.addItem("")
        self.horizontalLayout.addWidget(self.Right_Select)
        self.Constant_Mode.addTab(self.HalfColor, "")
        self.ThirdsColor = QtWidgets.QWidget()
        self.ThirdsColor.setObjectName("ThirdsColor")
        self.label_4 = QtWidgets.QLabel(self.ThirdsColor)
        self.label_4.setGeometry(QtCore.QRect(212, 140, 150, 190))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("../_image/Color_None_RB.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.label_3 = QtWidgets.QLabel(self.ThirdsColor)
        self.label_3.setGeometry(QtCore.QRect(50, 10, 301, 121))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("../_image/Color_None_Top.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(self.ThirdsColor)
        self.label_5.setGeometry(QtCore.QRect(40, 140, 150, 190))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("../_image/Color_None_LB.png"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.Full_Color_Select_2 = QtWidgets.QComboBox(self.ThirdsColor)
        self.Full_Color_Select_2.setGeometry(QtCore.QRect(170, 60, 69, 22))
        self.Full_Color_Select_2.setObjectName("Full_Color_Select_2")
        self.Full_Color_Select_2.addItem("")
        self.Full_Color_Select_2.addItem("")
        self.Full_Color_Select_2.addItem("")
        self.Full_Color_Select_2.addItem("")
        self.Full_Color_Select_2.addItem("")
        self.Full_Color_Select_3 = QtWidgets.QComboBox(self.ThirdsColor)
        self.Full_Color_Select_3.setGeometry(QtCore.QRect(100, 220, 69, 22))
        self.Full_Color_Select_3.setObjectName("Full_Color_Select_3")
        self.Full_Color_Select_3.addItem("")
        self.Full_Color_Select_3.addItem("")
        self.Full_Color_Select_3.addItem("")
        self.Full_Color_Select_3.addItem("")
        self.Full_Color_Select_3.addItem("")
        self.Full_Color_Select_4 = QtWidgets.QComboBox(self.ThirdsColor)
        self.Full_Color_Select_4.setGeometry(QtCore.QRect(235, 220, 69, 22))
        self.Full_Color_Select_4.setObjectName("Full_Color_Select_4")
        self.Full_Color_Select_4.addItem("")
        self.Full_Color_Select_4.addItem("")
        self.Full_Color_Select_4.addItem("")
        self.Full_Color_Select_4.addItem("")
        self.Full_Color_Select_4.addItem("")
        self.Constant_Mode.addTab(self.ThirdsColor, "")
        self.timeEdit_From = QtWidgets.QTimeEdit(self.Lighting)
        self.timeEdit_From.setEnabled(False)
        self.timeEdit_From.setGeometry(QtCore.QRect(290, 390, 91, 22))
        self.timeEdit_From.setObjectName("timeEdit_From")
        self.timeEdit_To = QtWidgets.QTimeEdit(self.Lighting)
        self.timeEdit_To.setEnabled(False)
        self.timeEdit_To.setGeometry(QtCore.QRect(290, 420, 91, 22))
        self.timeEdit_To.setObjectName("timeEdit_To")
        self.label_6 = QtWidgets.QLabel(self.Lighting)
        self.label_6.setGeometry(QtCore.QRect(260, 425, 47, 13))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.Lighting)
        self.label_7.setGeometry(QtCore.QRect(245, 395, 47, 13))
        self.label_7.setObjectName("label_7")
        self.lightScheduleButton = QtWidgets.QPushButton(self.Lighting)
        self.lightScheduleButton.setEnabled(False)
        self.lightScheduleButton.setGeometry(QtCore.QRect(390, 395, 40, 40))
        self.lightScheduleButton.setCheckable(False)
        self.lightScheduleButton.setAutoDefault(False)
        self.lightScheduleButton.setDefault(True)
        self.lightScheduleButton.setFlat(False)
        self.lightScheduleButton.setObjectName("lightScheduleButton")
        self.verticalLayoutWidget_11 = QtWidgets.QWidget(self.Lighting)
        self.verticalLayoutWidget_11.setGeometry(QtCore.QRect(130, 390, 101, 51))
        self.verticalLayoutWidget_11.setObjectName("verticalLayoutWidget_11")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_11)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.Constant_Lights = QtWidgets.QRadioButton(self.verticalLayoutWidget_11)
        self.Constant_Lights.setChecked(True)
        self.Constant_Lights.setObjectName("Constant_Lights")
        self.verticalLayout_5.addWidget(self.Constant_Lights)
        self.radioButton_2 = QtWidgets.QRadioButton(self.verticalLayoutWidget_11)
        self.radioButton_2.setObjectName("radioButton_2")
        self.verticalLayout_5.addWidget(self.radioButton_2)
        self.label_8 = QtWidgets.QLabel(self.Lighting)
        self.label_8.setGeometry(QtCore.QRect(50, 390, 81, 21))
        self.label_8.setObjectName("label_8")
        self.spinBox = QtWidgets.QSpinBox(self.Lighting)
        self.spinBox.setGeometry(QtCore.QRect(50, 410, 51, 22))
        self.spinBox.setMaximum(255)
        self.spinBox.setProperty("value", 50)
        self.spinBox.setObjectName("spinBox")
        self.dial = QtWidgets.QDial(self.Lighting)
        self.dial.setGeometry(QtCore.QRect(10, 390, 41, 51))
        self.dial.setNotchesVisible(True)
        self.dial.setObjectName("dial")
        self.Control_Tab.addTab(self.Lighting, "")
        self.Imaging = QtWidgets.QWidget()
        self.Imaging.setObjectName("Imaging")
        self.layoutWidget = QtWidgets.QWidget(self.Imaging)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 10, 391, 331))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.Image_Title = QtWidgets.QLabel(self.layoutWidget)
        self.Image_Title.setObjectName("Image_Title")
        self.verticalLayout.addWidget(self.Image_Title)
        self.IST_Editor = QtWidgets.QLineEdit(self.layoutWidget)
        self.IST_Editor.setEnabled(True)
        self.IST_Editor.setObjectName("IST_Editor")
        self.verticalLayout.addWidget(self.IST_Editor)
        self.Image_Interval = QtWidgets.QLabel(self.layoutWidget)
        self.Image_Interval.setObjectName("Image_Interval")
        self.verticalLayout.addWidget(self.Image_Interval)
        self.ICI_spinBox = QtWidgets.QSpinBox(self.layoutWidget)
        self.ICI_spinBox.setEnabled(False)
        self.ICI_spinBox.setMaximum(9999999)
        self.ICI_spinBox.setObjectName("ICI_spinBox")
        self.verticalLayout.addWidget(self.ICI_spinBox)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.Image_Duration = QtWidgets.QLabel(self.layoutWidget)
        self.Image_Duration.setObjectName("Image_Duration")
        self.verticalLayout_2.addWidget(self.Image_Duration)
        self.ISD_spinBox = QtWidgets.QSpinBox(self.layoutWidget)
        self.ISD_spinBox.setEnabled(False)
        self.ISD_spinBox.setMaximum(9999999)
        self.ISD_spinBox.setObjectName("ISD_spinBox")
        self.verticalLayout_2.addWidget(self.ISD_spinBox)
        self.line = QtWidgets.QFrame(self.layoutWidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_2.addWidget(self.line)
        spacerItem1 = QtWidgets.QSpacerItem(20, 120, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.Directory_Label = QtWidgets.QLabel(self.layoutWidget)
        self.Directory_Label.setEnabled(True)
        self.Directory_Label.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Directory_Label.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Directory_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.Directory_Label.setObjectName("Directory_Label")
        self.verticalLayout_2.addWidget(self.Directory_Label)
        self.Storage_Directory = QtWidgets.QPushButton(self.layoutWidget)
        self.Storage_Directory.setEnabled(False)
        self.Storage_Directory.setCheckable(False)
        self.Storage_Directory.setObjectName("Storage_Directory")
        self.verticalLayout_2.addWidget(self.Storage_Directory)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.Live_Feed = QtWidgets.QPushButton(self.layoutWidget)
        self.Live_Feed.setObjectName("Live_Feed")
        self.verticalLayout_3.addWidget(self.Live_Feed)
        self.layoutWidget1 = QtWidgets.QWidget(self.Imaging)
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 340, 411, 51))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.Progress_Label = QtWidgets.QLabel(self.layoutWidget1)
        self.Progress_Label.setObjectName("Progress_Label")
        self.verticalLayout_6.addWidget(self.Progress_Label)
        self.Progress_Bar = QtWidgets.QProgressBar(self.layoutWidget1)
        self.Progress_Bar.setEnabled(False)
        self.Progress_Bar.setProperty("value", 0)
        self.Progress_Bar.setObjectName("Progress_Bar")
        self.verticalLayout_6.addWidget(self.Progress_Bar)
        self.Control_Tab.addTab(self.Imaging, "")
        self.Scheduler = QtWidgets.QWidget()
        self.Scheduler.setObjectName("Scheduler")
        self.verticalLayoutWidget_6 = QtWidgets.QWidget(self.Scheduler)
        self.verticalLayoutWidget_6.setGeometry(QtCore.QRect(180, 5, 81, 51))
        self.verticalLayoutWidget_6.setObjectName("verticalLayoutWidget_6")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_6)
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.Rotate1 = QtWidgets.QLabel(self.verticalLayoutWidget_6)
        self.Rotate1.setAlignment(QtCore.Qt.AlignCenter)
        self.Rotate1.setObjectName("Rotate1")
        self.verticalLayout_11.addWidget(self.Rotate1)
        self.rotate_to_spinbox_1 = QtWidgets.QSpinBox(self.verticalLayoutWidget_6)
        self.rotate_to_spinbox_1.setMinimum(-180)
        self.rotate_to_spinbox_1.setMaximum(180)
        self.rotate_to_spinbox_1.setObjectName("rotate_to_spinbox_1")
        self.verticalLayout_11.addWidget(self.rotate_to_spinbox_1)
        self.verticalLayoutWidget_7 = QtWidgets.QWidget(self.Scheduler)
        self.verticalLayoutWidget_7.setGeometry(QtCore.QRect(300, 105, 81, 51))
        self.verticalLayoutWidget_7.setObjectName("verticalLayoutWidget_7")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_7)
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.Wait1 = QtWidgets.QLabel(self.verticalLayoutWidget_7)
        self.Wait1.setAlignment(QtCore.Qt.AlignCenter)
        self.Wait1.setObjectName("Wait1")
        self.verticalLayout_14.addWidget(self.Wait1)
        self.wait_spinbox_1 = QtWidgets.QSpinBox(self.verticalLayoutWidget_7)
        self.wait_spinbox_1.setMinimum(1)
        self.wait_spinbox_1.setMaximum(1440)
        self.wait_spinbox_1.setObjectName("wait_spinbox_1")
        self.verticalLayout_14.addWidget(self.wait_spinbox_1)
        self.R1 = QtWidgets.QLabel(self.Scheduler)
        self.R1.setGeometry(QtCore.QRect(290, 25, 71, 71))
        self.R1.setText("")
        self.R1.setPixmap(QtGui.QPixmap("../_image/R1.png"))
        self.R1.setScaledContents(True)
        self.R1.setObjectName("R1")
        self.verticalLayoutWidget_8 = QtWidgets.QWidget(self.Scheduler)
        self.verticalLayoutWidget_8.setGeometry(QtCore.QRect(180, 225, 81, 51))
        self.verticalLayoutWidget_8.setObjectName("verticalLayoutWidget_8")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_8)
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.Rotate2 = QtWidgets.QLabel(self.verticalLayoutWidget_8)
        self.Rotate2.setAlignment(QtCore.Qt.AlignCenter)
        self.Rotate2.setObjectName("Rotate2")
        self.verticalLayout_15.addWidget(self.Rotate2)
        self.rotate_to_spinbox_2 = QtWidgets.QSpinBox(self.verticalLayoutWidget_8)
        self.rotate_to_spinbox_2.setMinimum(-180)
        self.rotate_to_spinbox_2.setMaximum(180)
        self.rotate_to_spinbox_2.setObjectName("rotate_to_spinbox_2")
        self.verticalLayout_15.addWidget(self.rotate_to_spinbox_2)
        self.R2 = QtWidgets.QLabel(self.Scheduler)
        self.R2.setGeometry(QtCore.QRect(290, 165, 71, 71))
        self.R2.setText("")
        self.R2.setPixmap(QtGui.QPixmap("../_image/R2.png"))
        self.R2.setScaledContents(True)
        self.R2.setObjectName("R2")
        self.verticalLayoutWidget_9 = QtWidgets.QWidget(self.Scheduler)
        self.verticalLayoutWidget_9.setGeometry(QtCore.QRect(60, 105, 81, 51))
        self.verticalLayoutWidget_9.setObjectName("verticalLayoutWidget_9")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_9)
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.Wait2 = QtWidgets.QLabel(self.verticalLayoutWidget_9)
        self.Wait2.setAlignment(QtCore.Qt.AlignCenter)
        self.Wait2.setObjectName("Wait2")
        self.verticalLayout_16.addWidget(self.Wait2)
        self.wait_spinbox_2 = QtWidgets.QSpinBox(self.verticalLayoutWidget_9)
        self.wait_spinbox_2.setMinimum(1)
        self.wait_spinbox_2.setMaximum(1440)
        self.wait_spinbox_2.setObjectName("wait_spinbox_2")
        self.verticalLayout_16.addWidget(self.wait_spinbox_2)
        self.R2_2 = QtWidgets.QLabel(self.Scheduler)
        self.R2_2.setGeometry(QtCore.QRect(80, 165, 71, 71))
        self.R2_2.setText("")
        self.R2_2.setPixmap(QtGui.QPixmap("../_image/L2.png"))
        self.R2_2.setScaledContents(True)
        self.R2_2.setObjectName("R2_2")
        self.R2_3 = QtWidgets.QLabel(self.Scheduler)
        self.R2_3.setGeometry(QtCore.QRect(80, 25, 71, 71))
        self.R2_3.setText("")
        self.R2_3.setPixmap(QtGui.QPixmap("../_image/L1.png"))
        self.R2_3.setScaledContents(True)
        self.R2_3.setObjectName("R2_3")
        self.Color_Frame_2 = QtWidgets.QLabel(self.Scheduler)
        self.Color_Frame_2.setGeometry(QtCore.QRect(145, 60, 150, 150))
        self.Color_Frame_2.setText("")
        self.Color_Frame_2.setPixmap(QtGui.QPixmap("../_image/Scheduler.png"))
        self.Color_Frame_2.setScaledContents(True)
        self.Color_Frame_2.setObjectName("Color_Frame_2")
        self.line_2 = QtWidgets.QFrame(self.Scheduler)
        self.line_2.setGeometry(QtCore.QRect(-10, 280, 461, 21))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.Speed_Select = QtWidgets.QSlider(self.Scheduler)
        self.Speed_Select.setGeometry(QtCore.QRect(20, 320, 271, 21))
        self.Speed_Select.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.Speed_Select.setMinimum(100)
        self.Speed_Select.setMaximum(1000)
        self.Speed_Select.setSingleStep(20)
        self.Speed_Select.setPageStep(30)
        self.Speed_Select.setProperty("value", 600)
        self.Speed_Select.setSliderPosition(600)
        self.Speed_Select.setOrientation(QtCore.Qt.Horizontal)
        self.Speed_Select.setInvertedControls(True)
        self.Speed_Select.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.Speed_Select.setTickInterval(50)
        self.Speed_Select.setObjectName("Speed_Select")
        self.verticalLayoutWidget_10 = QtWidgets.QWidget(self.Scheduler)
        self.verticalLayoutWidget_10.setGeometry(QtCore.QRect(300, 300, 131, 91))
        self.verticalLayoutWidget_10.setObjectName("verticalLayoutWidget_10")
        self.verticalLayout_17 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_10)
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.Reset_Position = QtWidgets.QPushButton(self.verticalLayoutWidget_10)
        self.Reset_Position.setObjectName("Reset_Position")
        self.verticalLayout_17.addWidget(self.Reset_Position)
        self.Test_Run = QtWidgets.QPushButton(self.verticalLayoutWidget_10)
        self.Test_Run.setCheckable(False)
        self.Test_Run.setChecked(False)
        self.Test_Run.setObjectName("Test_Run")
        self.verticalLayout_17.addWidget(self.Test_Run)
        self.Start_Scheduler = QtWidgets.QPushButton(self.verticalLayoutWidget_10)
        self.Start_Scheduler.setObjectName("Start_Scheduler")
        self.verticalLayout_17.addWidget(self.Start_Scheduler)
        self.Motor_Speed = QtWidgets.QLabel(self.Scheduler)
        self.Motor_Speed.setGeometry(QtCore.QRect(20, 340, 139, 21))
        self.Motor_Speed.setObjectName("Motor_Speed")
        self.Start_Imaging_2 = QtWidgets.QCommandLinkButton(self.Scheduler)
        self.Start_Imaging_2.setEnabled(False)
        self.Start_Imaging_2.setGeometry(QtCore.QRect(100, 370, 191, 51))
        self.Start_Imaging_2.setAutoFillBackground(False)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../_image/time-left.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Start_Imaging_2.setIcon(icon1)
        self.Start_Imaging_2.setIconSize(QtCore.QSize(35, 35))
        self.Start_Imaging_2.setObjectName("Start_Imaging_2")
        self.Control_Tab.addTab(self.Scheduler, "")
        self.Cloud = QtWidgets.QWidget()
        self.Cloud.setObjectName("Cloud")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.Cloud)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(40, 300, 351, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.Frequency_Off = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.Frequency_Off.setEnabled(False)
        self.Frequency_Off.setCheckable(True)
        self.Frequency_Off.setChecked(False)
        self.Frequency_Off.setObjectName("Frequency_Off")
        self.horizontalLayout_6.addWidget(self.Frequency_Off)
        self.Frequency_Low = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.Frequency_Low.setEnabled(False)
        self.Frequency_Low.setObjectName("Frequency_Low")
        self.horizontalLayout_6.addWidget(self.Frequency_Low)
        self.Frequency_Average = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.Frequency_Average.setEnabled(False)
        self.Frequency_Average.setChecked(True)
        self.Frequency_Average.setObjectName("Frequency_Average")
        self.horizontalLayout_6.addWidget(self.Frequency_Average)
        self.Frequency_High = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.Frequency_High.setEnabled(False)
        self.Frequency_High.setObjectName("Frequency_High")
        self.horizontalLayout_6.addWidget(self.Frequency_High)
        self.Email_Update_Prompt = QtWidgets.QLabel(self.Cloud)
        self.Email_Update_Prompt.setGeometry(QtCore.QRect(40, 270, 221, 31))
        self.Email_Update_Prompt.setObjectName("Email_Update_Prompt")
        self.label = QtWidgets.QLabel(self.Cloud)
        self.label.setGeometry(QtCore.QRect(80, 50, 271, 140))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../_image/dropbox_logo.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.Cloud)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(70, 170, 291, 80))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_9.addItem(spacerItem2)
        self.Dropbox_Email_Prompt = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.Dropbox_Email_Prompt.setObjectName("Dropbox_Email_Prompt")
        self.verticalLayout_9.addWidget(self.Dropbox_Email_Prompt)
        self.Dropbox_Email = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.Dropbox_Email.setObjectName("Dropbox_Email")
        self.verticalLayout_9.addWidget(self.Dropbox_Email)
        self.Dropbox_Confirm = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.Dropbox_Confirm.setEnabled(False)
        self.Dropbox_Confirm.setObjectName("Dropbox_Confirm")
        self.verticalLayout_9.addWidget(self.Dropbox_Confirm)
        self.Control_Tab.addTab(self.Cloud, "")
        self.Start_Imaging = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.Start_Imaging.setEnabled(False)
        self.Start_Imaging.setGeometry(QtCore.QRect(600, 430, 191, 51))
        self.Start_Imaging.setAutoFillBackground(False)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../_image/Start-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Start_Imaging.setIcon(icon2)
        self.Start_Imaging.setIconSize(QtCore.QSize(35, 35))
        self.Start_Imaging.setObjectName("Start_Imaging")
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(490, 360, 121, 51))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.Local_Storage = QtWidgets.QRadioButton(self.verticalLayoutWidget_4)
        self.Local_Storage.setChecked(True)
        self.Local_Storage.setObjectName("Local_Storage")
        self.verticalLayout_12.addWidget(self.Local_Storage)
        self.Cloud_Sync = QtWidgets.QRadioButton(self.verticalLayoutWidget_4)
        self.Cloud_Sync.setEnabled(False)
        self.Cloud_Sync.setObjectName("Cloud_Sync")
        self.verticalLayout_12.addWidget(self.Cloud_Sync)
        self.verticalLayoutWidget_5 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_5.setGeometry(QtCore.QRect(680, 350, 101, 80))
        self.verticalLayoutWidget_5.setObjectName("verticalLayoutWidget_5")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_5)
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.Snapshot = QtWidgets.QPushButton(self.verticalLayoutWidget_5)
        self.Snapshot.setEnabled(True)
        self.Snapshot.setObjectName("Snapshot")
        self.verticalLayout_13.addWidget(self.Snapshot)
        self.Rotate = QtWidgets.QPushButton(self.verticalLayoutWidget_5)
        self.Rotate.setObjectName("Rotate")
        self.verticalLayout_13.addWidget(self.Rotate)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.actionOpen_Directory = QtWidgets.QAction(MainWindow)
        self.actionOpen_Directory.setEnabled(False)
        self.actionOpen_Directory.setObjectName("actionOpen_Directory")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionCreate_Timelapse = QtWidgets.QAction(MainWindow)
        self.actionCreate_Timelapse.setObjectName("actionCreate_Timelapse")

        self.retranslateUi(MainWindow)
        self.Control_Tab.setCurrentIndex(0)
        self.Constant_Mode.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "FlashLapse Commad Point"))
        self.JPG.setText(_translate("MainWindow", "JPG"))
        self.PNG.setText(_translate("MainWindow", "PNG"))
        self.Full_Color_Select.setCurrentText(_translate("MainWindow", "None"))
        self.Full_Color_Select.setItemText(0, _translate("MainWindow", "None"))
        self.Full_Color_Select.setItemText(1, _translate("MainWindow", "White"))
        self.Full_Color_Select.setItemText(2, _translate("MainWindow", "Red"))
        self.Full_Color_Select.setItemText(3, _translate("MainWindow", "Green"))
        self.Full_Color_Select.setItemText(4, _translate("MainWindow", "Blue"))
        self.Constant_Mode.setTabText(self.Constant_Mode.indexOf(self.FullColor), _translate("MainWindow", "Full"))
        self.Left_Select.setItemText(0, _translate("MainWindow", "None"))
        self.Left_Select.setItemText(1, _translate("MainWindow", "White"))
        self.Left_Select.setItemText(2, _translate("MainWindow", "Red"))
        self.Left_Select.setItemText(3, _translate("MainWindow", "Green"))
        self.Left_Select.setItemText(4, _translate("MainWindow", "Blue"))
        self.Right_Select.setItemText(0, _translate("MainWindow", "None"))
        self.Right_Select.setItemText(1, _translate("MainWindow", "White"))
        self.Right_Select.setItemText(2, _translate("MainWindow", "Red"))
        self.Right_Select.setItemText(3, _translate("MainWindow", "Green"))
        self.Right_Select.setItemText(4, _translate("MainWindow", "Blue"))
        self.Constant_Mode.setTabText(self.Constant_Mode.indexOf(self.HalfColor), _translate("MainWindow", "Half"))
        self.Full_Color_Select_2.setCurrentText(_translate("MainWindow", "None"))
        self.Full_Color_Select_2.setItemText(0, _translate("MainWindow", "None"))
        self.Full_Color_Select_2.setItemText(1, _translate("MainWindow", "White"))
        self.Full_Color_Select_2.setItemText(2, _translate("MainWindow", "Red"))
        self.Full_Color_Select_2.setItemText(3, _translate("MainWindow", "Green"))
        self.Full_Color_Select_2.setItemText(4, _translate("MainWindow", "Blue"))
        self.Full_Color_Select_3.setCurrentText(_translate("MainWindow", "None"))
        self.Full_Color_Select_3.setItemText(0, _translate("MainWindow", "None"))
        self.Full_Color_Select_3.setItemText(1, _translate("MainWindow", "White"))
        self.Full_Color_Select_3.setItemText(2, _translate("MainWindow", "Red"))
        self.Full_Color_Select_3.setItemText(3, _translate("MainWindow", "Green"))
        self.Full_Color_Select_3.setItemText(4, _translate("MainWindow", "Blue"))
        self.Full_Color_Select_4.setCurrentText(_translate("MainWindow", "None"))
        self.Full_Color_Select_4.setItemText(0, _translate("MainWindow", "None"))
        self.Full_Color_Select_4.setItemText(1, _translate("MainWindow", "White"))
        self.Full_Color_Select_4.setItemText(2, _translate("MainWindow", "Red"))
        self.Full_Color_Select_4.setItemText(3, _translate("MainWindow", "Green"))
        self.Full_Color_Select_4.setItemText(4, _translate("MainWindow", "Blue"))
        self.Constant_Mode.setTabText(self.Constant_Mode.indexOf(self.ThirdsColor), _translate("MainWindow", "Thirds"))
        self.label_6.setText(_translate("MainWindow", "TO:"))
        self.label_7.setText(_translate("MainWindow", "FROM:"))
        self.lightScheduleButton.setText(_translate("MainWindow", "OK"))
        self.Constant_Lights.setText(_translate("MainWindow", "Constant"))
        self.radioButton_2.setText(_translate("MainWindow", "Schedule"))
        self.label_8.setText(_translate("MainWindow", "Brightness:"))
        self.Control_Tab.setTabText(self.Control_Tab.indexOf(self.Lighting), _translate("MainWindow", "Lighting"))
        self.Image_Title.setText(_translate("MainWindow", "Image Sequence Title"))
        self.Image_Interval.setText(_translate("MainWindow", "Image Capture Interval"))
        self.ICI_spinBox.setSuffix(_translate("MainWindow", " s"))
        self.Image_Duration.setText(_translate("MainWindow", "Image Sequence Duration"))
        self.ISD_spinBox.setSuffix(_translate("MainWindow", " min"))
        self.Directory_Label.setText(_translate("MainWindow", "Storage Directory Not Selected"))
        self.Storage_Directory.setText(_translate("MainWindow", "Select Storage Directory"))
        self.Live_Feed.setText(_translate("MainWindow", "Start Live Feed (30s)"))
        self.Progress_Label.setText(_translate("MainWindow", "Progress:"))
        self.Control_Tab.setTabText(self.Control_Tab.indexOf(self.Imaging), _translate("MainWindow", "Imaging"))
        self.Rotate1.setText(_translate("MainWindow", "Reflex To"))
        self.rotate_to_spinbox_1.setSuffix(_translate("MainWindow", " °"))
        self.Wait1.setText(_translate("MainWindow", "Pause For"))
        self.wait_spinbox_1.setSuffix(_translate("MainWindow", " min"))
        self.Rotate2.setText(_translate("MainWindow", "Reflex To"))
        self.rotate_to_spinbox_2.setSuffix(_translate("MainWindow", " °"))
        self.Wait2.setText(_translate("MainWindow", "Pause For"))
        self.wait_spinbox_2.setSuffix(_translate("MainWindow", " min"))
        self.Reset_Position.setText(_translate("MainWindow", "Reset Position"))
        self.Test_Run.setText(_translate("MainWindow", "Test Run"))
        self.Start_Scheduler.setText(_translate("MainWindow", "Set Schedule"))
        self.Motor_Speed.setText(_translate("MainWindow", "Motor Speed: 600"))
        self.Start_Imaging_2.setText(_translate("MainWindow", "Start Scheduled Imaging"))
        self.Control_Tab.setTabText(self.Control_Tab.indexOf(self.Scheduler), _translate("MainWindow", "Scheduler"))
        self.Frequency_Off.setText(_translate("MainWindow", "OFF"))
        self.Frequency_Low.setText(_translate("MainWindow", "LOW"))
        self.Frequency_Average.setText(_translate("MainWindow", "AVERAGE"))
        self.Frequency_High.setText(_translate("MainWindow", "HIGH"))
        self.Email_Update_Prompt.setText(_translate("MainWindow", "Email Status Update Frequency:"))
        self.Dropbox_Email_Prompt.setText(_translate("MainWindow", "Please Enter Your Email Adress: "))
        self.Dropbox_Confirm.setText(_translate("MainWindow", "Confirm Email"))
        self.Control_Tab.setTabText(self.Control_Tab.indexOf(self.Cloud), _translate("MainWindow", "Cloud"))
        self.Start_Imaging.setText(_translate("MainWindow", "Start Image Sequence"))
        self.Local_Storage.setText(_translate("MainWindow", "Local Storage"))
        self.Cloud_Sync.setText(_translate("MainWindow", "Cloud Sync"))
        self.Snapshot.setText(_translate("MainWindow", "Snapshot"))
        self.Rotate.setText(_translate("MainWindow", "Rotate"))
        self.actionOpen_Directory.setText(_translate("MainWindow", "Open Directory"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionCreate_Timelapse.setText(_translate("MainWindow", "Create Timelapse"))

