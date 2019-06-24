import serial
import UI_Update

def init(self):

    global base_Connected
    base_Connected = True

    try:
        global ASD
        ASD = serial.Serial('/dev/ttyACM0', 9600)
    
    except:
        UI_Update.desync(self)
    

    global commands_list
    commands_list = []

    global current_CMD
    current_CMD = ""

    global cycle_running
    cycle_running = False

    global cycle_time
    cycle_time =60

    global sch_running
    sch_running = False

    global test_running
    test_running = False
    
    global angle_1
    angle_1 = 0
    global angle_2
    angle_2 = 0
    global delay_1
    delay_1 = 0
    global delay_2
    delay_2 = 0
    
    global rpm
    RPM = 5

    
    '''global dropbox_running
    dropbox_running = False
    
    global ASD
    ASD = serial.Serial('/dev/ttyACM0', 9600)
    

    global sch_confirmed
    sch_confirmed = False
    global cycle
    cycle = 0

    global sequence_name
    sequence_name = ""
    global email
    email = ""
    global file_list
    file_list = []
    global link
    link = ""
    global file
    file = ""
    global full_dir
    full_dir = ""
    global current_image
    current_image = ""
    global command_list
    command_list = []'''
