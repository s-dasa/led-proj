from gpiozero import *
import RPi.GPIO as GPIO
from time import sleep
from led_database import *
class controller:
    
    color = input("Enter your desired color (from ROYGBIV and White) or its RGB value in the format: [R, G, B].")
    if (color.isdigit()):
        print("it's a number")
        color = led_database.getColor(color)
    elif (isinstance(color, str)):
        color=color.lower()
    else:
        print("That's not a valid input!")
        #continue
    times = int(input("How many times do you want it to blink?"))
    speed = int(input("And how fast do you want it to blink"))
#color = input("Which color LED do you want to light? (Red/Green)")
    rate = 1/speed
    led = LED(led_database.getPin(color))
    for x in range (times):
        sleep(rate)
        led.on()
        sleep(rate)
        led.off()
