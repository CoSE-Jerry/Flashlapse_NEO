import Settings
from time import sleep
from PyQt5.QtCore import QThread

#QThread for schedule function
class Schedule(QThread):
    
    def __init__(self):
        QThread.__init__(self)
        Settings.sch_running = True

    def __del__(self):
        self._running = False
        
    def run(self):
        count = 1
        while True:
            capture(count)
            count++
            Settings.ASD.write(bytes('~'+str(Settings.angle_1)+"\n", 'UTF-8'))
            Settings.ASD.write(bytes('~0'+"\n", 'UTF-8'))
            sleep(Settings.delay_1*60)

            capture(count)
            count++
            Settings.ASD.write(bytes('~'+str(Settings.angle_2)+"\n", 'UTF-8'))
            Settings.ASD.write(bytes('~0'+"\n", 'UTF-8'))
            sleep(Settings.delay_2*60)

    def capture(num):
            current_image = Settings.file % num
            
            with PiCamera() as camera:
                sleep(0.8)
                camera.resolution = (2464,2464)
                camera._set_rotation(180)
                camera.capture(current_image)
            Settings.file_list.append(current_image)

class Test(QThread):
    
    def __init__(self):
        QThread.__init__(self)
        Settings.test_running = True

    def __del__(self):
        self._running = False
        
    def run(self):
        while True:
            Settings.ASD.write(bytes('~'+str(Settings.angle_1)+"\n", 'UTF-8'))
            Settings.ASD.write(bytes("~0\n", "UTF-8"))
            sleep(5)
            Settings.ASD.write(bytes('~'+str(Settings.angle_2)+"\n", 'UTF-8'))
            Settings.ASD.write(bytes("~0\n", "UTF-8"))
            sleep(5)

class Dropbox(QThread):
    def __init__(self):
        QThread.__init__(self)
        os.system("/home/pi/Dropbox-Uploader/dropbox_uploader.sh mkdir /MECHSTIM/" + Settings.sequence_name)

    def __del__(self):
        self._running = False

    def run(self):  
        Settings.link = str(subprocess.check_output("/home/pi/Dropbox-Uploader/dropbox_uploader.sh share /MECHSTIM/" + Settings.sequence_name, shell=True))
        Settings.link = Settings.link.replace("b' > ", "")
        Settings.link = Settings.link.split("\\")[0]
        while True:
            if (len(file_list) > 0):
                os.system("/home/pi/Dropbox-Uploader/dropbox_uploader.sh upload " + Settings.file_list[0] + " /"+Settings.sequence_name)
                os.system("rm " + Settings.file_list[0])
                del Settings.file_list[0]
