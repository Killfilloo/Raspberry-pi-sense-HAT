#Imports
import random
from sense_hat import SenseHat
from time import sleep

#Instance af sensehat for using the joystick events and displaying on the senseHat display
sense = SenseHat()

#Global variables
x, y = 4, 4

curDir = [1,0]

score = 0

fruit = 0

tick = 1

Snake = [[2,4],
         [3,4],
         [4,4]]

Fruit = [0,0]

#Function for calculating and changing the global variable "score"
def calcScore():
    global score, tick
    tick = round(tick,2)
    score = int(score)
    score += (fruit * 5)
    
    
#Function for declaring death then displaying the score and speed credits on the senseHat display and allowing closing the game by hitting the middle joyStick
def declareDeath():
    global score, tick
    while True:
        for event in sense.stick.get_events():
            if event.direction == 'middle':
                print("GAME CLOSED")
                quit()
        sense.clear()
        #FYI scroll_speed is amount of pixels it moves per second
        sense.show_message("SCORE: "+str(score), text_colour=(255,0,0), scroll_speed=0.1)
        sense.show_message("SPEED: "+str(tick),text_colour=(255,0,255), scroll_speed=0.1)
        
#Function for speeding up the global variable time by 25% of current speed per function-call
def speedUp():
    global tick
    tick *= 0.75

#Function for drawing in the snake on the display by looping through the entire Snake array
#And then getting the coordinates for each bodypart and then drawing in a pixel at set coordinate
def drawSnake():
    for bodyPart in Snake:
        sense.set_pixel(bodyPart[0], bodyPart[1],255,0,255)

#Function for drawing in fruits
#Also ensures that the fruit does not spawn ontop of the snake by checking against every possible snake bodypart
#In case that it would spawn ontop of the snake then it returns another drawFruit call which esssentially breaks out of itself and runs itself again
def drawFruit():
    global Fruit
    r1 = random.randint(0,7)
    r2 = random.randint(0,7)
    for bodyPart in Snake:
        if r1 == bodyPart[0] and r2 == bodyPart[1]:
            print("Fruit spawn - Failed - at",r1,",",r2)
            return drawFruit()
    Fruit = [r1,r2]
    sense.set_pixel(Fruit[0], Fruit[1],255,0,0)
    print("Fruit spawn - Success - at",r1,",",r2)

#Function for moving the x,y by adding the numbers given in the direction array
def move(direction):
    global y, x, curDir
    curDir = direction
    x += direction[0]
    y += direction[1]

#Function for checking the current position of the snake and then calling the drawFruit(), calcScore(), declareDeath() and speedUp() functions depending on position
#Checks if the snake head eats the fruit position
#Also removes end of the snake unless a fruit was eaten
def checkPosition():
    global score,fruit
    if y == 8 or x == 8 or y == -1 or x == -1:
        calcScore()
        print("Snake hit the edge")
        declareDeath()
    for sn in Snake:
        if sn == [x,y]:
            calcScore()
            print("Snake ate itself")
            declareDeath()
    if x == Fruit[0] and y == Fruit[1]:
        print('Fruit eaten - at',Fruit[0],",",Fruit[1])
        drawFruit()
        fruit += 1
        if fruit % 3 == 0:
            speedUp()
    else:
        sense.set_pixel(Snake[0][0], Snake[0][1],0,0,0) #fjerner røv-pixelen på slangen
        Snake.remove(Snake[0]) #fjerner røven.
    Snake.append([x,y]) #tilføjer hoved
    score += 0.1
    

#Initial clears and draws of the snake
sense.clear()
drawSnake()
drawFruit()

#Running Code
while True:
    print("Snake head at",x,",",y,"going",curDir,"at",tick,"speed")
    drawSnake()
    sleep(tick)
    for event in sense.stick.get_events():
        print(event.direction,"was", event.action)
        if event.direction == 'up' and (event.action == 'pressed' or event.action == 'held'):
            move([0,-1])
            break
        elif event.direction == 'down' and (event.action == 'pressed' or event.action == 'held'):
            move([0,1])
            break
        elif event.direction == 'left' and (event.action == 'pressed' or event.action == 'held'):
            move([-1,0])
            break
        elif event.direction == 'right' and (event.action == 'pressed' or event.action == 'held'):
            move([1,0])
            break
    else:
        move(curDir)
        
    checkPosition()