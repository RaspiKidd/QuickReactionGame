from gpiozero import *
from time import sleep

led = LED(18)

while True:
    led.on ()
    sleep (2)
    led.off ()
    sleep (1)