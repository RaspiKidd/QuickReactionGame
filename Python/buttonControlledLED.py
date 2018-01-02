from gpiozero import *

led = LED (18)
button = Button (14)

button.when_pressed = led.on
button.when_released = led.off