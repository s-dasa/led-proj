from gpiozero import *
import RPi.GPIO as GPIO
from time import sleep
from led_database import *
#from tester import *
class controller():
    def __init__(self):
        self.led_obj = led_class()
        #self.my_tester = testing()
        self.color = ""
        self.times = 0
        self.rate = 1
        self.led_obj.setUp()
        self= self
        self.speed = 0

    def userInput(self):
        self.color = input("Enter your desired color (from ROYGBIV and White) or its RGB value in the format: [R, G, B].")
        self.times
        int(input("How many times do you want it to blink?"))
        self.speed = int(input("And how fast do you want it to blink"))
        if (isinstance(self.color, list) and self.led_obj.checkList(self.color)):
            #print("it's a list")
            self.color = self.led_obj.getColor(self.color)
            print(self.color)
        elif (isinstance(self.color, str) and self.led_obj.checkList(self.color)):
            self.color=self.color.lower()
            #print("It's a string")
        else:
            print("That's not a valid input!")
            userInput()
    def lightUp(self):
        self.led_obj.setUp()
        self.led_obj.lightUp(self.color)
        #self.my_tester.powerOn(self.color)
    def execution(self):
        rate = 1/self.speed
        #print(self.led_obj.getPin(self.color))
        led = LED(self.led_obj.getPin(self.color))
        for x in range (self.times):
            sleep(rate)
            led.on()
            sleep(rate)
            led.off()
        again = input("Again? Y or N")
        if (again == "Y"):
            userInput(self)
        else: print("Thank you for using the LedController. Have a nice day")
    """
    def main(self):
        userInput(self)
        execution(self)
    main(self)
    """
#ontrol = controller()
c = controller()
