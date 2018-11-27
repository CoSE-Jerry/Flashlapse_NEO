from datetime import datetime
from threading import Timer

x=datetime.today()
print(x)
y=x.replace(day=x.day+1, hour=1, minute=0, second=0, microsecond=0)
print(y)
delta_t=y-x
print(delta_t)

secs=delta_t.seconds+1
print(secs)

def hello_world():
    print ("hello world")

t = Timer(secs, hello_world)
t.start()
