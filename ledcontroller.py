from gpiozero import *
import RPi.GPIO as GPIO
from time import sleep
import led_database
class controller:
    color = input("Enter your desired color (from ROYGBIV and White) or its RGB value in the format: [R, G, B].")
    led_database.database.retrievePin(color)
    if (color.isdigit()):
        print("it's a number") 
    elif (isinstance(color, str)):
        if color in led_database.database.values.keys():
                currentrgb = led_database.database.getValues(color)
        else:
                print("That's not one of the colors I know! Try again!") 
    else:
        print("That's not a valid input!")
        #continue
    times = int(input("How many times do you want it to blink?"))
    speed = int(input("And how fast do you want it to blink"))
#color = input("Which color LED do you want to light? (Red/Green)")
    rate = 1/speed
    led = LED(led_database.database.retrievePin(color))
    for x in range (times):
        sleep(rate)
        led.on()
        sleep(rate)
        led.off()
