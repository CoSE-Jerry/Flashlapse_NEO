from time import sleep
import PyQt5
from PyQt5.QtCore import QThread, QTimer, QEventLoop
from pylibseek_ext import *
from Main import *
import cv2
import numpy as np

class SeekCamera():
    def __init__(self, scale=1.0, colormap=9, rotate=90):
        self.scale      = scale
        self.colormap   = colormap
        self.rotate     = rotate
        self.st         = SeekThermal()
        self.st.open()

    def __del__(self):
        self.st.close()

    def read(self):
        return(self.st.read())

    def process_frame(self, inframe):
        scale     = self.scale
        colormap  = self.colormap
        rotate    = self.rotate

        frame_g16 = cv2.normalize(inframe, alpha=0, beta=65535, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_16UC1)
        frame_g8  = cv2.convertScaleAbs(src=frame_g16, alpha=1.0/256.0, beta=0.0)

        #Rotate the image, if desired
        if( rotate == 90 ):
            frame_g8 = cv2.transpose(src=frame_g8)
            frame_g8 = cv2.flip(src=frame_g8, flipCode=1)
        elif( rotate == 180 ):
            frame_g8 = cv2.flip(src=frame_g8, flipCode=-1)
        elif( rotate == 270 ):
            frame_g8 = cv2.transpose(src=frame_g8)
            frame_g8 = cv2.flip(src=frame_g8, flipCode=0)

        #Scale the image up/down
        if ( scale != 1.0 ):
            frame_g8 = cv2.resize(src=frame_g8, dsize=(0,0), dst=frame_g8, fx=scale, fy=scale, interpolation=cv2.INTER_LINEAR)

        #Apply adaptive histogram equalization
        #clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(4,4))
        #frame_g8 = clahe.apply(frame_g8)
        #frame_g8 = cv2.equalizeHist(frame_g8)

        #Change the colormap
        if( colormap != -1 ):
            frame_g8_color  = cv2.applyColorMap(frame_g8, colormap=colormap)
        else:
            frame_g8_color  = cv2.cvtColor(src=frame_g8, code=cv2.COLOR_GRAY2BGR)

        return(frame_g8_color)

    def capture(self, dst):
        frame = self.process_frame(self.st.read())
        cv2.imwrite(dst, frame)


class Snap(QThread):
    def __init__(self, scale=1.0, colormap=9, rotate=90):
        self.sc  = SeekCamera(scale=scale, colormap=colormap, rotate=rotate)
        QThread.__init__(self)

    def __del__(self):
        self._running = False

    def run(self):
        sc     = self.sc
        sc.capture("../_temp/snapshot.jpg")
        del sc
        self.sc = None

            
class Live(QThread):

    def __init__(self, Image_Frame, fps=4, scale=1.0, colormap=9, rotate=90, runtime=86400):
        self.Image_Frame      = Image_Frame
        self.fps              = fps
        self.nsteps           = long(runtime * fps)
        self.currstep         = 0
        self.sc               = SeekCamera(scale=scale, colormap=colormap, rotate=rotate)
        self.timer            = QTimer()
        self.timer_finished   = False
        self.timeout_running  = False
        QThread.__init__(self)

    def __del__(self):
        self._running = False


    def timeout(self):
        self.timeout_running = True
        sc              = self.sc
        dst             = "../_temp/snapshot.jpg"
        sc.capture(dst)
        user_img        = PyQt5.QtGui.QImage(dst)
        self.Image_Frame.setPixmap(QtGui.QPixmap(user_img))
        self.currstep = self.currstep + 1
        if( self.currstep >= self.nsteps ):
            self.timer_finished = True
        self.timeout_running = False

    def stop(self):
        self.timer.stop()
        #If the timer timeout is already running, give it time to complete so as to prevent any weird deallocation errors.
        while(self.timeout_running):
            sleep(.1)
        self.timer_finished=True

    def run(self):
        sc        = self.sc
        nsteps    = self.nsteps
        interval  = 1000.0/self.fps #Convert to milliseconds
        self.timer.timeout.connect(self.timeout)
        self.timer.start(interval)
        while( self.timer_finished == False ):
            sleep(0.15)
        #Wait for the timer to finish
        self.timer.stop()
        del self.timer
        del sc
        self.sc = None
