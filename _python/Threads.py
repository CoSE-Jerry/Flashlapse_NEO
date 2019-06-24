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

'''class Schedule(QThread):
    
    def __init__(self):
        QThread.__init__(self)
        Settings.sch_running = True

    def __del__(self):
        
        self._running = False
        
    def run(self):
        count = 1
        while (count/2)<Settings.cycle:
            Settings.current_image = Settings.file % count
            with PiCamera() as camera:
                sleep(0.8)
                camera.resolution = (2464,2464)
                camera._set_rotation(90*Settings.rotation)
                camera.capture(Settings.current_image)
                self.captured.emit()
            Settings.file_list.append(Settings.current_image)
            
            count+=1
            Settings.ASD.write(bytes("2~"+str(Settings.angle_1), 'UTF-8'))
            sleep(Settings.delay_1*60)

            Settings.current_image = Settings.file % count
            with PiCamera() as camera:
                sleep(0.8)
                camera.resolution = (2464,2464)
                camera._set_rotation(90*Settings.rotation)
                camera.capture(Settings.current_image)
                self.captured.emit()
            Settings.file_list.append(Settings.current_image)

            count+=1
            Settings.ASD.write(bytes("2~"+str(Settings.angle_2), 'UTF-8'))
            sleep(Settings.delay_2*60)
        Settings.dropbox_running = False'''


class Test(QThread):
    
    def __init__(self):
        QThread.__init__(self)
        Settings.test_running = True

    def __del__(self): 
        self._running = False
       
    def run(self):
        while True:
            Commands.reflex_to(Settings.angle_1)
            sleep(5)
            Commands.reflex_to(Settings.angle_2)
            sleep(5)

'''class Dropbox(QThread):
    def __init__(self):
        QThread.__init__(self)
        os.system("/home/pi/Dropbox-Uploader/dropbox_uploader.sh mkdir /MECHSTIM/" + Settings.sequence_name)
        Settings.dropbox_running = True
        Settings.file_list.clear
        
    def __del__(self):
        self._running = False

    def run(self):  
        Settings.link = str(subprocess.check_output("/home/pi/Dropbox-Uploader/dropbox_uploader.sh share /MECHSTIM/" + Settings.sequence_name, shell=True))
        Settings.link = Settings.link.replace("b' > ", "")
        Settings.link = Settings.link.split("\\")[0]
        while Settings.dropbox_running:
            if (len(Settings.file_list) > 0):
                os.system("/home/pi/Dropbox-Uploader/dropbox_uploader.sh upload " + Settings.file_list[0] + " /MECHSTIM/"+Settings.sequence_name)
                os.system("rm " + Settings.file_list[0])
                del Settings.file_list[0]

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
        fromaddr = "notification_noreply@flashlapseinnovations.com"
        toaddr = Settings.email
        msg = MIMEMultipart()
        msg['From'] = fromaddr
        msg['To'] = toaddr
        msg['Subject'] = "MECHSTIM NOTIFICATION"

        body = "Hi " + Settings.email.split("@")[0] + "! \n\n" "Your MECHSTIM image sequence " + Settings.sequence_name + " has been initiated, check it out here.\n\n" + Settings.link + "\n\nTeam Flashlapse"       
        
        msg.attach(MIMEText(body, 'plain'))
        server = smtplib.SMTP('email-smtp.us-east-1.amazonaws.com', 587)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(Email.user, Email.password)
        text = msg.as_string()
        server.sendmail(fromaddr, toaddr, text)
        Settings.email_running = False'''
