#imports
from sense_hat import SenseHat
import random
from time import sleep
sense = SenseHat()

#variable declaration
off = (0,0,0)
run = True
c = ([off,off,off,off,off,off,off,off])

#clearing display upon starting
sense.clear

#function main, what generate the colors, and light the pixels.
def main():
    global run
    while run:
        for j in range(8):
            #random color getting added to the list, approx 16.6m outcomes 
            c.append((random.randint(0,255),random.randint(0,255),random.randint(0,255)))
            for i in range(8):
                sense.set_pixel(j,i,c[j])
            
            sleep(0.05)
            #option for turning off the loop
            for event in sense.stick.get_events():
                if event.direction == 'middle' and event.action == 'held':
                    run = False
                    
            c.remove(c[0])

while True:
    for event in sense.stick.get_events():
        if event.direction == 'middle' and event.action == 'pressed':
            run = True
            main()
