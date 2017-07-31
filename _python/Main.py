# always seem to need this
import sys
import os
import time
import subprocess
import serial
 
# This gets the Qt stuff
import PyQt5
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QThread
from PyQt5.QtWidgets import *

directory = None
# This is our window from QtCreator
import FlashLapse_UI

#import custom functions
import Camera

#camera libraries
from picamera import PiCamera
from time import sleep

#email libraries
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

#global variables
file_list = []
directory = ""
link =""
email=""
m_directory=""
interval = 0
duration = 0
total = 0
current = 0
noti_count = 0
current_image = None
file = None
name = None
on_flag = False
off = False
low = False
done = False
average = False
high = False
cloud =False
run_timelapse = True
ASD = serial.Serial('/dev/ttyACM0', 9600)

class Image(QThread):
    capture = QtCore.pyqtSignal()
    check_point = QtCore.pyqtSignal()
    imaging_running = QtCore.pyqtSignal()
    imaging_running_done = QtCore.pyqtSignal()
    def __init__(self):
        QThread.__init__(self)

    def __del__(self):
        self._running = False

    def run(self):
        global current, current_image, file_list, file
        for i in range(total):
            current = i
            sleep(0.2)
            current_image = file % i
            self.imaging_running.emit()
            with PiCamera() as camera:
                sleep(0.8)
                camera.resolution = (2464,2464)
                camera._set_rotation(180)
                camera.capture(current_image)
            self.imaging_running_done.emit()
            self.capture.emit()
            sleep(interval-1)
            file_list.append(current_image)
            if(current%(0.1*total)==0):
                self.check_point.emit()
            
    def stop(self):
        self.running = False

class Dropbox(QThread):
    upload_complete = QtCore.pyqtSignal()
    
    def __init__(self):
        QThread.__init__(self)

    def __del__(self):
        self._running = False

    def run(self):  
        global file_list, name, link

        os.system("/home/pi/Dropbox-Uploader/dropbox_uploader.sh mkdir /" + name)
        link = str(subprocess.check_output("/home/pi/Dropbox-Uploader/dropbox_uploader.sh share /" + name, shell=True))
        link = link.replace("b' > ", "")
        link = link.split("\\")[0]
        while True:
            if (len(file_list) > 0):
                os.system("/home/pi/Dropbox-Uploader/dropbox_uploader.sh upload " + file_list[0] + " /"+name)
                del file_list[0]
            if(current == total - 1 and len(file_list) == 0):
                self.upload_complete.emit()
                
class Timelapse(QThread):
    begin = QtCore.pyqtSignal()
    done = QtCore.pyqtSignal()
    
    def __init__(self):
        QThread.__init__(self)

    def __del__(self):
        self._running = False

    def run(self):
        global file, directory, cloud, file_list
        os.system("avconv -r 10 -i " + file + " -r 5 -vcodec libx264 -crf 20 -g 15 -vf scale=400:400 " + directory + "/timelapse.mp4")
        os.system("omxplayer -p -o hdmi " + directory + "/timelapse.mp4")
        os.system("rm " + directory + "/timelapse.mp4")
    def stop(self):
        self.running = False

class Email(QThread):
    
    def __init__(self):
        QThread.__init__(self)

    def __del__(self):
        self._running = False

    def run(self):

        sys.path.insert(0,'../../HP')
        import Email
        global link, current, total, noti_count, off, low, average, high, done
        body = None
        fromaddr = "notification_noreply@flashlapseinnovations.com"
        toaddr = email
        msg = MIMEMultipart()
        msg['From'] = fromaddr
        msg['To'] = toaddr
        msg['Subject'] = "FLASHLAPSE NOTIFICATION"

        if (current == 0):
            sleep(1)     
        else:
            if(noti_count == 0):
                body = "Hi " + email.split("@")[0] + "! \n\n" "Your Flashlapse image sequence "+name+" has been initiated, check it out here.\n\n" + link + "\n\nTeam Flashlapse"
            elif(noti_count == 1 and high):
                body = "Hi " + email.split("@")[0] + "! \n\n" "Your Flashlapse image sequence "+name+" is 10% complete, check it out here.\n\n" + link + "\n\nTeam Flashlapse"
            elif(noti_count == 2 and (high or average)):
                body = "Hi " + email.split("@")[0] + "! \n\n" "Your Flashlapse image sequence "+name+" is 20% complete, check it out here.\n\n" + link + "\n\nTeam Flashlapse"
            elif(noti_count == 3 and high):
                body = "Hi " + email.split("@")[0] + "! \n\n" "Your Flashlapse image sequence "+name+" is 30% complete, check it out here.\n\n" + link + "\n\nTeam Flashlapse"
            elif(noti_count == 4 and (high or average)):
                body = "Hi " + email.split("@")[0] + "! \n\n" "Your Flashlapse image sequence "+name+" is 40% complete, check it out here.\n\n" + link + "\n\nTeam Flashlapse"
            elif(noti_count == 5 and ((off == False) and average == False)):
                body = "Hi " + email.split("@")[0] + "! \n\n" "Your Flashlapse image sequence "+name+" is 50% complete, check it out here.\n\n" + link + "\n\nTeam Flashlapse"
            elif(noti_count == 6 and (high or average)):
                body = "Hi " + email.split("@")[0] + "! \n\n" "Your Flashlapse image sequence "+name+" is 60% complete, check it out here.\n\n" + link + "\n\nTeam Flashlapse"
            elif(noti_count == 7 and high):
                body = "Hi " + email.split("@")[0] + "! \n\n" "Your Flashlapse image sequence "+name+" is 70% complete, check it out here.\n\n" + link + "\n\nTeam Flashlapse"
            elif(noti_count == 8 and (high or average)):
                body = "Hi " + email.split("@")[0] + "! \n\n" "Your Flashlapse image sequence "+name+" is 80% complete, check it out here.\n\n" + link + "\n\nTeam Flashlapse"
            elif(noti_count == 9 and high):
                body = "Hi " + email.split("@")[0] + "! \n\n" "Your Flashlapse image sequence "+name+" is 90% complete, check it out here.\n\n" + link + "\n\nTeam Flashlapse"
                
            noti_count += 1
            
        if(done):
            body = "Hi " + email.split("@")[0] + "! \n\n" "Your Flashlapse image sequence "+name+" is complete, check it out here.\n" + link + "\n\nTeam Flashlapse"
            done = False
            
        if(body != None):
            msg.attach(MIMEText(body, 'plain'))
            server = smtplib.SMTP('email-smtp.us-east-1.amazonaws.com', 587)
            server.ehlo()
            server.starttls()
            server.ehlo()
            server.login(Email.user, Email.password)
            text = msg.as_string()
            server.sendmail(fromaddr, toaddr, text)
           
# create class for our Raspberry Pi GUI
class MainWindow(QMainWindow, FlashLapse_UI.Ui_MainWindow):
 # access variables inside of the UI's file

    def IST_Edit(self):
        global name, directory, m_directory
        name = self.IST_Editor.text()
        if(len(m_directory)>0):
            directory = m_directory +"/"+name
            self.Directory_Label.setText(directory)
        
    def IST_Change(self):
        self.ICI_spinBox.setEnabled(True)
        if(len(self.IST_Editor.text())==0):
            self.ICI_spinBox.setEnabled(False)
            self.ISD_spinBox.setEnabled(False)
            self.Start_Imaging.setEnabled(False)
            
    def ICI_Change(self):
        global interval, duration, total, directory
        interval = self.ICI_spinBox.value()
        self.ISD_spinBox.setEnabled(True)
        if(interval == 0):
            self.ISD_spinBox.setEnabled(False)
        if(interval!= 0):
            total = int((duration*60)/interval)
            if(total>0 and len(directory)!=0):
                self.Start_Imaging.setEnabled(True)
            else:
                self.Start_Imaging.setEnabled(False)
                
    def ISD_Change(self):
        global interval, duration, total, directory
        duration = self.ISD_spinBox.value()
        self.Storage_Directory.setEnabled(True)
        if(interval!= 0):
            total = int((duration*60)/interval)
            if(total>0 and len(directory)!=0):
                self.Start_Imaging.setEnabled(True)
            else:
                self.Start_Imaging.setEnabled(False)
            
        
        
    def Select_Storage_Directory(self):
        global interval, duration, total, directory, m_directory
        m_directory = str(QFileDialog.getExistingDirectory(self, "Select Directory",'/home/pi/Desktop'))
        if(len(m_directory)!=0):
            directory = m_directory +"/"+name
            self.Directory_Label.setText(directory)
            if(interval!= 0):
                total = int((duration*60)/interval)
                if(total>0 and len(directory)!=0):
                    self.Start_Imaging.setEnabled(True)
                else:
                    self.Start_Imaging.setEnabled(False)
        
    def Start_Snapshot(self):
        self.Snap_Thread = Camera.Snap()
        self.Snap_Thread.started.connect(lambda: self.Processing_Snapshot())
        self.Snap_Thread.finished.connect(lambda: self.Processing_Complete())
        self.Snap_Thread.start()
        
    def Processing_Snapshot(self):
        self.Snapshot.setEnabled(False)
        self.Snapshot.setText("Processing...")
        
    def Processing_Complete(self):
        user_img = PyQt5.QtGui.QImage("../_temp/snapshot.jpg")
        self.Image_Frame.setPixmap(QtGui.QPixmap(user_img))
        self.Snapshot.setEnabled(True)
        self.Snapshot.setText("Snapshot")
        
    def Start_Live_Feed(self):
        self.Live_Thread = Camera.Live()
        self.Live_Thread.started.connect(lambda: self.Processing_Live())
        self.Live_Thread.finished.connect(lambda: self.Live_Complete())
        self.Live_Thread.start()
        
    def Processing_Live(self):
        self.Snapshot.setEnabled(False)
        self.Live_Feed.setEnabled(False)
        self.Start_Imaging.setEnabled(False)
        self.Live_Feed.setText("Processing...")
        
    def Live_Complete(self):
        self.Snapshot.setEnabled(True)
        self.Live_Feed.setEnabled(True)
        self.Start_Imaging.setEnabled(True)
        self.Live_Feed.setText("Start Live Feed (30s)")

    def Check_Point(self):
        if(self.Cloud_Sync.isChecked()):
            self.Email_Thread = Email()
            self.Email_Thread.start()
        
    def Begin_Imaging(self):
        global jpg, directory, name, duration, interval, total, file, on_flag, file_list
        
        if (on_flag == False): 
            self.Image_Thread = Image()
            self.Dropbox_Thread = Dropbox()
            self.Email_Thread = Email()
            total = int((duration*60)/interval)
            self.Progress_Bar.setMaximum(total)
            
            if(not os.path.isdir(directory)):
                os.mkdir(directory)
            
            if (self.JPG.isChecked()):
                file = directory + "/" +name + "_%04d.jpg"
            else:
                file = directory + "/" +name + "_%04d.png"
            self.Image_Thread.started.connect(lambda: self.Start_Image())
            self.Image_Thread.finished.connect(lambda: self.Done())
            self.Image_Thread.capture.connect(lambda: self.Progress())
            self.Image_Thread.check_point.connect(lambda: self.Check_Point())
            self.Image_Thread.imaging_running.connect(lambda: self.Imaging_Running())
            self.Image_Thread.imaging_running_done.connect(lambda: self.Imaging_Running_Complete())

            self.Image_Thread.start()

            if(self.Cloud_Sync.isChecked()):
                self.Dropbox_Thread.start()
                self.Email_Thread.start()

            on_flag = True
        
        else:
            self.Image_Thread.terminate()
            self.IST_Editor.setEnabled(True)
            self.ICI_spinBox.setEnabled(True)
            self.ISD_spinBox.setEnabled(True)
            self.Live_Feed.setEnabled(True)
            self.Storage_Directory.setEnabled(True)
            self.Snapshot.setEnabled(True)
            self.JPG.setEnabled(True)
            self.PNG.setEnabled(True)
            self.Dropbox_Email.setEnabled(True)
            self.Dropbox_Confirm.setEnabled(True)
            self.Frequency_Off.setEnabled(True)
            self.Frequency_Low.setEnabled(True)
            self.Frequency_Average.setEnabled(True)
            self.Frequency_High.setEnabled(True)
            self.Image_Frame.setPixmap(QtGui.QPixmap("../_image/background.png"))
            icon3 = QtGui.QIcon()
            icon3.addPixmap(QtGui.QPixmap("../_image/Start-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.Start_Imaging.setIcon(icon3)
            self.Start_Imaging.setText("Start Image Sequence")
            self.Progress_Bar.setValue(0)
            del file_list[:]
            self.Image_Thread.terminate()
            self.Dropbox_Thread.terminate()
            on_flag = False

    def Imaging_Running(self):
        self.Start_Imaging.setEnabled(False)
        self.Start_Imaging.setText("Imaging...")
        
    def Imaging_Running_Complete(self):
        self.Start_Imaging.setEnabled(True)
        self.Start_Imaging.setText("Stop Image Sequence")

    def Done(self):
        global done, on_flag, run_timelapse
        
        if(run_timelapse):
            self.Timelapse_Thread = Timelapse()
            self.Timelapse_Thread.start()

        done=True
        self.Check_Point()
        
        self.Start_Imaging.setText("Start Another Sequence")
        
        self.IST_Editor.setEnabled(True)
        self.ICI_spinBox.setEnabled(True)
        self.ISD_spinBox.setEnabled(True)
        self.Live_Feed.setEnabled(True)
        self.Storage_Directory.setEnabled(True)
        self.Snapshot.setEnabled(True)
        self.JPG.setEnabled(True)
        self.PNG.setEnabled(True)
        self.Dropbox_Email.setEnabled(True)
        self.Dropbox_Confirm.setEnabled(True)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("../_image/Start-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Start_Imaging.setIcon(icon3)
        on_flag = False
        
    def Progress(self):
        global current, current_image
        self.Progress_Bar.setValue(current+1)
        self.Image_Frame.setPixmap(QtGui.QPixmap(current_image))

    def Email_Change(self):
        match =None
        import re
        temp_email = self.Dropbox_Email.text()
        if (len(temp_email)) > 7:
            match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', temp_email)
        if (match != None):
            self.Dropbox_Confirm.setEnabled(True)
        else:
            self.Dropbox_Confirm.setEnabled(False)
            self.Cloud_Sync.setEnabled(False)
            self.Local_Storage.setChecked(True)

    def Email_Entered(self):
        global email
        email = self.Dropbox_Email.text()
        self.Cloud_Sync.setEnabled(True)
        self.Frequency_Off.setEnabled(True)
        self.Frequency_Low.setEnabled(True)
        self.Frequency_Average.setEnabled(True)
        self.Frequency_High.setEnabled(True)
            
    def Start_Image(self):
        global off, low, average, high, cloud
        
        self.IST_Editor.setEnabled(False)
        self.ICI_spinBox.setEnabled(False)
        self.ISD_spinBox.setEnabled(False)
        self.Live_Feed.setEnabled(False)
        self.Storage_Directory.setEnabled(False)
        self.Snapshot.setEnabled(False)
        self.JPG.setEnabled(False)
        self.PNG.setEnabled(False)
        self.Dropbox_Email.setEnabled(False)
        self.Dropbox_Confirm.setEnabled(False)
        self.CyVerse_Email.setEnabled(False)
        self.CyVerse_Confirm.setEnabled(False)
        self.Frequency_Off.setEnabled(False)
        self.Frequency_Low.setEnabled(False)
        self.Frequency_Average.setEnabled(False)
        self.Frequency_High.setEnabled(False)

        off= self.Frequency_Off.isChecked()
        low = self.Frequency_Low.isChecked()
        average = self.Frequency_Average.isChecked()
        high = self.Frequency_High.isChecked()
        cloud = self.Cloud_Sync.isChecked()
        
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../_image/Stop-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Start_Imaging.setIcon(icon2)
        self.Start_Imaging.setText("Stop Image Sequence")

    def Check_Network(self):
        import socket
        REMOTE_SERVER = "www.google.com"
        try:
            host = socket.gethostbyname(REMOTE_SERVER)
            s = socket.create_connection((host, 80), 2)
        except:
            pass
            self.Service_Select.setEnabled(False)
            self.Frequency_Off.setEnabled(False)
            self.Frequency_Low.setEnabled(False)
            self.Frequency_Average.setEnabled(False)
            self.Frequency_High.setEnabled(False)

    def full_color_change(self):
        temp = self.Full_Color_Select.currentIndex()
        if temp == 1:
            ASD.write(bytes('4', 'UTF-8'))
            self.Color_Frame.setPixmap(QtGui.QPixmap("../_image/Color_None.png"))
        elif temp == 2:
            ASD.write(bytes('1', 'UTF-8'))
            self.Color_Frame.setPixmap(QtGui.QPixmap("../_image/Color_Red.png"))
        elif temp == 3:
            ASD.write(bytes('2', 'UTF-8'))
            self.Color_Frame.setPixmap(QtGui.QPixmap("../_image/Color_Green.png"))
        elif temp == 4:
            ASD.write(bytes('3', 'UTF-8'))
            self.Color_Frame.setPixmap(QtGui.QPixmap("../_image/Color_Blue.png"))
        elif temp == 5:
            ASD.write(bytes('4', 'UTF-8'))
            self.Color_Frame.setPixmap(QtGui.QPixmap("../_image/Color_Rainbow.png"))
        else:
            ASD.write(bytes('0', 'UTF-8'))
            self.Color_Frame.setPixmap(QtGui.QPixmap("../_image/Color_None.png"))

        self.Half_Left.setPixmap(QtGui.QPixmap("../_image/Color_None_Left.png"))
        self.Half_Right.setPixmap(QtGui.QPixmap("../_image/Color_None_Right.png"))

    
    def half_color_change_left(self):
        temp = self.Left_Select.currentIndex()
        if temp == 1:
            ASD.write(bytes('y', 'UTF-8'))
            self.Half_Left.setPixmap(QtGui.QPixmap("../_image/Color_None_Left.png"))
        elif temp == 2:
            ASD.write(bytes('d', 'UTF-8'))
            self.Half_Left.setPixmap(QtGui.QPixmap("../_image/Color_Red_left.png"))
        elif temp == 3:
            ASD.write(bytes('e', 'UTF-8'))
            self.Half_Left.setPixmap(QtGui.QPixmap("../_image/Color_Red_left.png"))
        elif temp == 4:
            ASD.write(bytes('f', 'UTF-8'))
            self.Half_Left.setPixmap(QtGui.QPixmap("../_image/Color_Red_left.png"))
        elif temp == 0:
            ASD.write(bytes('B', 'UTF-8'))
            self.Half_Left.setPixmap(QtGui.QPixmap("../_image/Color_None_Left.png"))

            self.Color_Frame.setPixmap(QtGui.QPixmap("../_image/Color_None.png"))

    def half_color_change_right(self):
        temp = self.Right_Select.currentIndex()
        if temp == 1:
            ASD.write(bytes('x', 'UTF-8'))
            self.Half_Right.setPixmap(QtGui.QPixmap("../_image/Color_None_Right.png"))
        elif temp == 2:
            ASD.write(bytes('a', 'UTF-8'))
            self.Half_Right.setPixmap(QtGui.QPixmap("../_image/Color_Red_Right.png"))
        elif temp == 3:
            ASD.write(bytes('b', 'UTF-8'))
            self.Half_Right.setPixmap(QtGui.QPixmap("../_image/Color_Green_Right.png"))
        elif temp == 4:
            ASD.write(bytes('c', 'UTF-8'))
            self.Half_Right.setPixmap(QtGui.QPixmap("../_image/Color_Blue_Right.png"))
        elif temp == 0:
            ASD.write(bytes('A', 'UTF-8'))
            self.Half_Right.setPixmap(QtGui.QPixmap("../_image/Color_None_Right.png"))

        self.Color_Frame.setPixmap(QtGui.QPixmap("../_image/Color_None.png"))

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

    def rotate(self):
        ASD.write(bytes('z', 'UTF-8'))

    def timelapse_change(self):
        global run_timelapse
        if(run_timelapse):
            self.Timelapse.setText("Timelapse Generation: OFF")
            run_timelapse = False
        else:
            self.Timelapse.setText("Timelapse Generation: ON")
            run_timelapse = True
        

        
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self) # gets defined in the UI file
        self.Check_Network()
        self.IST_Editor.editingFinished.connect(lambda: self.IST_Edit())
        self.IST_Editor.textChanged.connect(lambda: self.IST_Change())
        self.ICI_spinBox.valueChanged.connect(lambda: self.ICI_Change())
        self.ISD_spinBox.valueChanged.connect(lambda: self.ISD_Change())
        self.Snapshot.clicked.connect(lambda: self.Start_Snapshot())
        self.Live_Feed.clicked.connect(lambda: self.Start_Live_Feed())
        self.Storage_Directory.clicked.connect(lambda: self.Select_Storage_Directory())
        self.Start_Imaging.clicked.connect(lambda: self.Begin_Imaging())
        self.Dropbox_Email.textChanged.connect(lambda: self.Email_Change())
        self.Dropbox_Confirm.clicked.connect(lambda: self.Email_Entered())
        self.Full_Color_Select.currentIndexChanged.connect(lambda: self.full_color_change())
        self.Left_Select.currentIndexChanged.connect(lambda: self.half_color_change_left())
        self.Right_Select.currentIndexChanged.connect(lambda: self.half_color_change_right())
        self.Gravi_Confirm.clicked.connect(lambda: self.gravi_confirm())
        self.Germi_Confirm.clicked.connect(lambda: self.germi_confirm())
        self.Barrier_Confirm.clicked.connect(lambda: self.barri_confirm())
        self.Disco.clicked.connect(lambda: self.disco_confirm())
        self.Rotate.clicked.connect(lambda: self.rotate())
        self.Timelapse.clicked.connect(lambda: self.timelapse_change())

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
