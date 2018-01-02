from gpiozero import *
from time import sleep
import random

led = LED(18)

led.on ()
sleep (random.uniform(5,10))
led.off ()