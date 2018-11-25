def init():
    global sch_running
    sch_running = False
    
    global ASD
    ASD = serial.Serial('/dev/ttyACM0', 9600)
    
    global angle_1
    angle_1 = 0
    global angle_2
    angle_2 = 0
    global delay_1
    delay_1 = 0
    global delay_2
    delay_2 = 0
    
