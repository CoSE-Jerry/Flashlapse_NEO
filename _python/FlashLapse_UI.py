# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FlashLapse_CP.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 510)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../_image/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Image_Frame = QtWidgets.QLabel(self.centralwidget)
        self.Image_Frame.setGeometry(QtCore.QRect(480, 20, 300, 300))
        self.Image_Frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Image_Frame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.Image_Frame.setLineWidth(5)
        self.Image_Frame.setText("")
        self.Image_Frame.setPixmap(QtGui.QPixmap("../_image/background1.png"))
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
        self.JPG.setChecked(True)
        self.JPG.setObjectName("JPG")
        self.verticalLayout_4.addWidget(self.JPG)
        self.PNG = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.PNG.setObjectName("PNG")
        self.verticalLayout_4.addWidget(self.PNG)
        self.Control_Tab = QtWidgets.QTabWidget(self.centralwidget)
        self.Control_Tab.setGeometry(QtCore.QRect(30, 20, 441, 431))
        self.Control_Tab.setObjectName("Control_Tab")
        self.Lighting = QtWidgets.QWidget()
        self.Lighting.setObjectName("Lighting")
        self.Lights = QtWidgets.QTabWidget(self.Lighting)
        self.Lights.setGeometry(QtCore.QRect(10, 10, 381, 371))
        self.Lights.setObjectName("Lights")
        self.Constant = QtWidgets.QWidget()
        self.Constant.setObjectName("Constant")
        self.Constant_Mode = QtWidgets.QTabWidget(self.Constant)
        self.Constant_Mode.setGeometry(QtCore.QRect(10, 10, 321, 321))
        self.Constant_Mode.setObjectName("Constant_Mode")
        self.FullColor = QtWidgets.QWidget()
        self.FullColor.setObjectName("FullColor")
        self.Color_Frame = QtWidgets.QLabel(self.FullColor)
        self.Color_Frame.setGeometry(QtCore.QRect(30, 10, 250, 250))
        self.Color_Frame.setText("")
        self.Color_Frame.setPixmap(QtGui.QPixmap("../_image/Color_None.png"))
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
        self.Half_Left.setPixmap(QtGui.QPixmap("../_image/Color_None_Left.png"))
        self.Half_Left.setScaledContents(True)
        self.Half_Left.setObjectName("Half_Left")
        self.Half_Right = QtWidgets.QLabel(self.HalfColor)
        self.Half_Right.setGeometry(QtCore.QRect(165, 10, 125, 250))
        self.Half_Right.setText("")
        self.Half_Right.setPixmap(QtGui.QPixmap("../_image/Color_None_Right.png"))
        self.Half_Right.setScaledContents(True)
        self.Half_Right.setObjectName("Half_Right")
        self.layoutWidget = QtWidgets.QWidget(self.HalfColor)
        self.layoutWidget.setGeometry(QtCore.QRect(50, 130, 191, 24))
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
        self.Presets1.setGeometry(QtCore.QRect(10, 10, 321, 321))
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
        self.pushButton_4 = QtWidgets.QPushButton(self.tab)
        self.pushButton_4.setGeometry(QtCore.QRect(40, 70, 231, 141))
        self.pushButton_4.setObjectName("pushButton_4")
        self.Presets1.addTab(self.tab, "")
        self.Lights.addTab(self.Presets, "")
        self.Control_Tab.addTab(self.Lighting, "")
        self.Imaging = QtWidgets.QWidget()
        self.Imaging.setObjectName("Imaging")
        self.layoutWidget2 = QtWidgets.QWidget(self.Imaging)
        self.layoutWidget2.setGeometry(QtCore.QRect(10, 10, 381, 311))
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
        self.IST_Editor.setEnabled(True)
        self.IST_Editor.setObjectName("IST_Editor")
        self.verticalLayout.addWidget(self.IST_Editor)
        self.Image_Interval = QtWidgets.QLabel(self.layoutWidget2)
        self.Image_Interval.setObjectName("Image_Interval")
        self.verticalLayout.addWidget(self.Image_Interval)
        self.ICI_spinBox = QtWidgets.QSpinBox(self.layoutWidget2)
        self.ICI_spinBox.setEnabled(False)
        self.ICI_spinBox.setMaximum(9999999)
        self.ICI_spinBox.setObjectName("ICI_spinBox")
        self.verticalLayout.addWidget(self.ICI_spinBox)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.Image_Duration = QtWidgets.QLabel(self.layoutWidget2)
        self.Image_Duration.setObjectName("Image_Duration")
        self.verticalLayout_2.addWidget(self.Image_Duration)
        self.ISD_spinBox = QtWidgets.QSpinBox(self.layoutWidget2)
        self.ISD_spinBox.setEnabled(False)
        self.ISD_spinBox.setMaximum(9999999)
        self.ISD_spinBox.setObjectName("ISD_spinBox")
        self.verticalLayout_2.addWidget(self.ISD_spinBox)
        self.line = QtWidgets.QFrame(self.layoutWidget2)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_2.addWidget(self.line)
        spacerItem1 = QtWidgets.QSpacerItem(20, 120, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.Directory_Label = QtWidgets.QLabel(self.layoutWidget2)
        self.Directory_Label.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Directory_Label.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Directory_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.Directory_Label.setObjectName("Directory_Label")
        self.verticalLayout_2.addWidget(self.Directory_Label)
        self.Storage_Directory = QtWidgets.QPushButton(self.layoutWidget2)
        self.Storage_Directory.setEnabled(False)
        self.Storage_Directory.setCheckable(False)
        self.Storage_Directory.setObjectName("Storage_Directory")
        self.verticalLayout_2.addWidget(self.Storage_Directory)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.Live_Feed = QtWidgets.QPushButton(self.layoutWidget2)
        self.Live_Feed.setObjectName("Live_Feed")
        self.verticalLayout_3.addWidget(self.Live_Feed)
        self.layoutWidget3 = QtWidgets.QWidget(self.Imaging)
        self.layoutWidget3.setGeometry(QtCore.QRect(14, 330, 411, 51))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.layoutWidget3)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.Progress_Label = QtWidgets.QLabel(self.layoutWidget3)
        self.Progress_Label.setObjectName("Progress_Label")
        self.verticalLayout_6.addWidget(self.Progress_Label)
        self.Progress_Bar = QtWidgets.QProgressBar(self.layoutWidget3)
        self.Progress_Bar.setEnabled(False)
        self.Progress_Bar.setProperty("value", 0)
        self.Progress_Bar.setObjectName("Progress_Bar")
        self.verticalLayout_6.addWidget(self.Progress_Bar)
        self.Control_Tab.addTab(self.Imaging, "")
        self.Cloud = QtWidgets.QWidget()
        self.Cloud.setObjectName("Cloud")
        self.Service_Select = QtWidgets.QTabWidget(self.Cloud)
        self.Service_Select.setGeometry(QtCore.QRect(10, 10, 401, 271))
        self.Service_Select.setObjectName("Service_Select")
        self.Dropbox = QtWidgets.QWidget()
        self.Dropbox.setObjectName("Dropbox")
        self.label = QtWidgets.QLabel(self.Dropbox)
        self.label.setGeometry(QtCore.QRect(60, 10, 271, 140))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../_image/dropbox_logo.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.Dropbox)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(50, 130, 291, 80))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_9.addItem(spacerItem2)
        self.Dropbox_Email_Prompt = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.Dropbox_Email_Prompt.setObjectName("Dropbox_Email_Prompt")
        self.verticalLayout_9.addWidget(self.Dropbox_Email_Prompt)
        self.Drop_Box_Email = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.Drop_Box_Email.setObjectName("Drop_Box_Email")
        self.verticalLayout_9.addWidget(self.Drop_Box_Email)
        self.Dropbox_Confirm = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.Dropbox_Confirm.setEnabled(False)
        self.Dropbox_Confirm.setObjectName("Dropbox_Confirm")
        self.verticalLayout_9.addWidget(self.Dropbox_Confirm)
        self.Service_Select.addTab(self.Dropbox, "")
        self.CyVerse = QtWidgets.QWidget()
        self.CyVerse.setObjectName("CyVerse")
        self.label_2 = QtWidgets.QLabel(self.CyVerse)
        self.label_2.setGeometry(QtCore.QRect(60, 50, 281, 61))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("../_image/cyverse_logo.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.CyVerse)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(50, 130, 291, 80))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_10.addItem(spacerItem3)
        self.CyVerse_Email_Prompt = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.CyVerse_Email_Prompt.setObjectName("CyVerse_Email_Prompt")
        self.verticalLayout_10.addWidget(self.CyVerse_Email_Prompt)
        self.CyVerse_Email = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        self.CyVerse_Email.setObjectName("CyVerse_Email")
        self.verticalLayout_10.addWidget(self.CyVerse_Email)
        self.CyVerse_Confirm = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.CyVerse_Confirm.setEnabled(False)
        self.CyVerse_Confirm.setObjectName("CyVerse_Confirm")
        self.verticalLayout_10.addWidget(self.CyVerse_Confirm)
        self.Service_Select.addTab(self.CyVerse, "")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.Cloud)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(40, 330, 361, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.Frequency_off = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.Frequency_off.setCheckable(True)
        self.Frequency_off.setChecked(False)
        self.Frequency_off.setObjectName("Frequency_off")
        self.horizontalLayout_6.addWidget(self.Frequency_off)
        self.Frequency_Rare = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.Frequency_Rare.setObjectName("Frequency_Rare")
        self.horizontalLayout_6.addWidget(self.Frequency_Rare)
        self.Frequency_Average = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.Frequency_Average.setChecked(True)
        self.Frequency_Average.setObjectName("Frequency_Average")
        self.horizontalLayout_6.addWidget(self.Frequency_Average)
        self.Frequency_Frequent = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.Frequency_Frequent.setObjectName("Frequency_Frequent")
        self.horizontalLayout_6.addWidget(self.Frequency_Frequent)
        self.Email_Update_Prompt = QtWidgets.QLabel(self.Cloud)
        self.Email_Update_Prompt.setGeometry(QtCore.QRect(40, 310, 171, 20))
        self.Email_Update_Prompt.setObjectName("Email_Update_Prompt")
        self.Control_Tab.addTab(self.Cloud, "")
        self.Start_Imaging = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.Start_Imaging.setEnabled(False)
        self.Start_Imaging.setGeometry(QtCore.QRect(480, 380, 291, 51))
        self.Start_Imaging.setAutoFillBackground(False)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../_image/Start-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
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
        self.Service_Select.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "FlashLapse Commad Point"))
        self.Snapshot.setText(_translate("MainWindow", "Snapshot"))
        self.JPG.setText(_translate("MainWindow", "JPG"))
        self.PNG.setText(_translate("MainWindow", "PNG"))
        self.Full_Color_Select.setCurrentText(_translate("MainWindow", "None"))
        self.Full_Color_Select.setItemText(0, _translate("MainWindow", "None"))
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
        self.Color_Gravi.setText(_translate("MainWindow", "Rotation Color:"))
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
        self.Color_Germi.setText(_translate("MainWindow", "Color Setting:"))
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
        self.Color_Barri.setText(_translate("MainWindow", "Color Setting:"))
        self.Barri_Red.setText(_translate("MainWindow", "Red"))
        self.Barri_Green.setText(_translate("MainWindow", "Green"))
        self.Barri_Blue.setText(_translate("MainWindow", "Blue"))
        self.Barri_White.setText(_translate("MainWindow", "White"))
        self.Presets1.setTabText(self.Presets1.indexOf(self.Barrier), _translate("MainWindow", "Barrier"))
        self.pushButton_4.setText(_translate("MainWindow", "Start!"))
        self.Presets1.setTabText(self.Presets1.indexOf(self.tab), _translate("MainWindow", "Disco"))
        self.Lights.setTabText(self.Lights.indexOf(self.Presets), _translate("MainWindow", "Presets"))
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
        self.Dropbox_Email_Prompt.setText(_translate("MainWindow", "Please Enter Your Email Adress: "))
        self.Dropbox_Confirm.setText(_translate("MainWindow", "Confirm Email"))
        self.Service_Select.setTabText(self.Service_Select.indexOf(self.Dropbox), _translate("MainWindow", "Dropbox"))
        self.CyVerse_Email_Prompt.setText(_translate("MainWindow", "Please Enter Your Email Adress:"))
        self.CyVerse_Confirm.setText(_translate("MainWindow", "Confirm Email"))
        self.Service_Select.setTabText(self.Service_Select.indexOf(self.CyVerse), _translate("MainWindow", "CyVerse "))
        self.Frequency_off.setText(_translate("MainWindow", "OFF"))
        self.Frequency_Rare.setText(_translate("MainWindow", "RARE"))
        self.Frequency_Average.setText(_translate("MainWindow", "AVERAGE"))
        self.Frequency_Frequent.setText(_translate("MainWindow", "FREQUENT"))
        self.Email_Update_Prompt.setText(_translate("MainWindow", "Email Status Update Frequency:"))
        self.Control_Tab.setTabText(self.Control_Tab.indexOf(self.Cloud), _translate("MainWindow", "Cloud"))
        self.Start_Imaging.setText(_translate("MainWindow", "Start Image Sequence"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionOpen_Directory.setText(_translate("MainWindow", "Open Directory"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionCreate_Timelapse.setText(_translate("MainWindow", "Create Timelapse"))

