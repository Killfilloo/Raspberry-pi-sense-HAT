#Imports
from sense_hat import SenseHat
import time
sense = senseHat()

#Running code
while True:
    hour = time.localtime()[3]
    minute = time.localtime()[4]
    second = time.localtime()[5]
    print(hour, minute, second)
    sense.show_message(str(hour)+’ : ‘+str(minute)+’ : ‘+str(second), text_colour=(255,0,0), scroll_speed=0.1)
