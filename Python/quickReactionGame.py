from gpiozero import *
from time import sleep
import random

player1_name = input('What is your name? ')
print ('Hello ' + player1_name +'!')

player2_name = input('What is your name? ')
print ('Hello ' + player2_name +'!')

led = LED(18)
player1 = Button (14)
player2 = Button (25)

led.on ()
sleep (random.uniform(5,10))
led.off ()

def pressed (button):
    if button.pin.number == 14:
        print (player1_name + ' Won the game')
    else:
        print (player2_name + ' Won the game')

player1.when_pressed = pressed
player2.when_pressed = pressed