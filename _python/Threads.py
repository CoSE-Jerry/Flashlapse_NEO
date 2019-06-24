import Settings
import Commands
import os
import sys
import subprocess
import smtplib

from PyQt5 import QtCore
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from time import sleep
from PyQt5.QtCore import QThread
from picamera import PiCamera



class Cycle(QThread):

    def __init__(self):
        QThread.__init__(self)
        Settings.cycle_running = True

    def __del__(self):
        self._running = False

    def run(self):
        
        Commands.clear_lights()
        sleep(1)
        Commands.deploy_lights()
        
        while True:
            for x in range(Settings.cycle_time*60):
                sleep(1)
                
                if not Settings.cycle_running:
                    break
                
            Commands.clear_lights()
            
            for x in range(Settings.cycle_time*60):
                sleep(1)
                
                if not Settings.cycle_running:
                    break
            Commands.deploy_lights()

            if not Settings.cycle_running:
                break

class Schedule(QThread):
    
    def __init__(self):
        QThread.__init__(self)
        Settings.sch_running = True

    def __del__(self):
        
        self._running = False
        
    def run(self):
        while Settings.sch_running:
            Commands.reflex_to(Settings.angle_1)
            for x in range (Settings.delay_1*60):
                sleep(1)
                if not Settings.sch_running:
                    break
            
            Commands.reflex_to(Settings.angle_2*60)
            for x in range (Settings.delay_2):
                sleep(1)
                if not Settings.sch_running:
                    break
        


class Test(QThread):
    
    def __init__(self):
        QThread.__init__(self)
        Settings.test_running = True

    def __del__(self): 
        self._running = False
       
    def run(self):
        for x in range (5):
            Commands.reflex_to(Settings.angle_1)
            for x in range (5):
                sleep(1)
                if not Settings.test_running:
                    break
            
            Commands.reflex_to(Settings.angle_2)
            for x in range (5):
                sleep(1)
                if not Settings.test_running:
                    break
            if not Settings.test_running:
                    break

class Snap(QThread):

    def __init__(self):
         QThread.__init__(self)

    def __del__(self):
         self._running = False

    def run(self):
        with PiCamera() as camera:
            camera.zoom = (Settings.AOI_X, Settings.AOI_Y, Settings.AOI_W, Settings.AOI_H)
            camera.resolution = (380,380)
            camera._set_rotation(90*Settings.rotation)
            camera.capture("../_temp/snapshot.jpg")

class Live(QThread):

    def __init__(self):
         QThread.__init__(self)

    def __del__(self):
         self._running = False

    def run(self):
        with PiCamera() as camera:
            camera._set_rotation(90*Settings.rotation)
            camera.start_preview()
            sleep(Settings.livetime)

class Preview(QThread):

    def __init__(self):
         QThread.__init__(self)

    def __del__(self):
         self._running = False

    def run(self):
        with PiCamera() as camera:
            camera.zoom = (Settings.AOI_X, Settings.AOI_Y, Settings.AOI_W, Settings.AOI_H)
            camera.resolution = (Settings.x_resolution,Settings.y_resolution)
            
            camera._set_rotation(90*Settings.rotation)

            if(Settings.image_format):
                camera.capture("../_temp/preview.jpg")
            else:
                camera.capture("../_temp/preview.png")

class Image(QThread):
    capturing = QtCore.pyqtSignal()
    complete = QtCore.pyqtSignal()
    def __init__(self):
        QThread.__init__(self)
        Settings.timelapse_running = True
        
    def __del__(self):
        self._running = False

    def run(self):
        if(not os.path.isdir(Settings.full_dir)):
            os.mkdir(Settings.full_dir)
        for i in range(Settings.total):
            Settings.current = i
            sleep(0.2)
            Settings.current_image = Settings.file % i
            self.capturing.emit()
            with PiCamera() as camera:
                sleep(0.8)
                camera.zoom = (Settings.AOI_X, Settings.AOI_Y, Settings.AOI_W, Settings.AOI_H)
                camera.resolution = (Settings.x_resolution,Settings.y_resolution)
                camera._set_rotation(90*Settings.rotation)
                camera.capture(Settings.current_image)
            self.complete.emit()

            if(Settings.storage_mode):
                Settings.file_list.append(Settings.current_image)

            for x in range(Settings.interval-1):
                sleep(1)
                if not Settings.timelapse_running:
                    break
            if not Settings.timelapse_running:
                break

class Dropbox(QThread):
    
    def __init__(self):
        QThread.__init__(self)
        Settings.dropbox_running = True

    def __del__(self):
        self._running = False

    def run(self):  
        os.system("/home/pi/Dropbox-Uploader/dropbox_uploader.sh mkdir /" + Settings.cpuserial)
        os.system("/home/pi/Dropbox-Uploader/dropbox_uploader.sh mkdir /" + Settings.cpuserial+"/"+Settings.sequence_name)
        Settings.link = str(subprocess.check_output("/home/pi/Dropbox-Uploader/dropbox_uploader.sh share /" + Settings.cpuserial, shell=True))
        Settings.link = Settings.link.replace("b' > ", "")
        Settings.link = Settings.link.split("\\")[0]
        count = 0
        while (count<Settings.total):
            if (len(Settings.file_list) > 0):
                os.system("/home/pi/Dropbox-Uploader/dropbox_uploader.sh upload " + Settings.file_list[0] + " /"+Settings.cpuserial+"/"+Settings.sequence_name)
                os.system("rm " + Settings.file_list[0])
                del Settings.file_list[0]
                count+=1
            if not Settings.dropbox_running:
                break
            
class Email(QThread):
    
    def __init__(self):
        QThread.__init__(self)
        Settings.email_running = True

    def __del__(self):
        self._running = False

    def run(self):
        while(len(Settings.link)==0):
            sleep(1)
        
        sys.path.insert(0,'../../HP')
        import Email
        body = None
        fromaddr = "notification_noreply@coseinstruments.com"
        toaddr = Settings.email
        msg = MIMEMultipart()
        msg['From'] = fromaddr
        msg['To'] = toaddr
        msg['Subject'] = "COSE FLASHLAPSE NOTIFICATION"

        body = "Hi " + Settings.email.split("@")[0] + "! \n\n" "Your Flashlapse image sequence " + Settings.sequence_name + " has been initiated, check it out here.\n\n" + Settings.link + "\n\nCOSE INSTRUMENTS"       
        
        msg.attach(MIMEText(body, 'plain'))
        server = smtplib.SMTP('email-smtp.us-east-1.amazonaws.com', 587)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(Email.user, Email.password)
        text = msg.as_string()
        server.sendmail(fromaddr, toaddr, text)
