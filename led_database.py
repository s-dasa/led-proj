from gpiozero import *
import RPi.GPIO as GPIO
from time import sleep
#from tester import *
class led_class(object):
    #pin = {"red": 6, "green": 22, "blue": 18, "white": 10}
    #values = {"white":[255, 255, 255], "red": [255, 0, 0], "orange":[255, 127, 0], "yellow":[255, 255, 0], "green":[0, 255, 0], "blue":[0, 0, 255], "indigo":[39, 9, 5], "violet":[139, 0, 255]}
    #rev_values = {"[255, 255, 255]":"white", "[255, 0, 0]":"red", "[255, 127, 0]":"orange", "[255, 255, 0]":"yellow", "[0, 255, 0]":"green", "[0, 0, 255]":"blue", "[39, 9, 5]":"indigo", "[139, 0, 255]":"violet"}
    def __init__(self):
        self.pin_dict = {"red": 12, "green": 22, "blue": 18, "white": 10}
        self.values = {"white":list([255, 255, 255]), "red": list([255, 0, 0]), "orange":list([255, 127, 0]), "yellow":list([255, 255, 0]), "green":list([0, 255, 0]), "blue":list([0, 0, 255]), "indigo":list([39, 9, 5]), "violet":list([139, 0, 255])}
        self.rev_values = {"[255, 255, 255]":"white", "[255, 0, 0]":"red", "[255, 127, 0]":"orange", "[255, 255, 0]":"yellow", "[0, 255, 0]":"green", "[0, 0, 255]":"blue", "[39, 9, 5]":"indigo", "[139, 0, 255]":"violet"}

    def getValue(color):
        return self.values[color]
    def getValues(self):
        return self.values
    def getPin(self, color):
        #print(color)
        return self.pin_dict[color]
    def getColor(self, color):
        return self.rev_values[color]
    def checkList(self, color):
        #print(color)
        if color in self.values: return True
        if color in self.rev_values:
            return True
        else: return False
    def setUp(self):
        #if color == "all":
        GPIO.setup(self.pin_dict["red"], GPIO.OUT)
        GPIO.setup(self.pin_dict["green"], GPIO.OUT)
        GPIO.setup(self.pin_dict["blue"], GPIO.OUT)
        #else: GPIO.setup(self.pin_dict[color], GPIO.OUT)
        print("I'm set up")
    def lightUp(self, color):
        print("I'm lighting up ", color)
        pwmr = GPIO.PWM(self.pin_dict["red"],50)
        pwmb = GPIO.PWM(self.pin_dict["blue"], 50)
        pwmg = GPIO.PWM(self.pin_dict["green"], 50)
        #pwmr.start((self.values[color][0]/255)*100)
        #pwmg.sta rt((self.values[color][1]/255)*100)
        #pwmb.start(100)
    def test(self):
        pwmr = GPIO.PWM(12, 50)
        pwmr.start(100)
        """
        for x in range (0, 3):
            rgbs = ("red", "green", "blue")
            power = (((self.values[color])[x])/255)*100
            print("My power is ", power)
            #print(type(self.values[color]))
            #print("the color is", str(self.values[color]), "and the current rgb value is ", str(list(self.values[color])[x]))
            pwm = GPIO.PWM(self.pin_dict[rgbs[x]],50)
            print("the pin I'm using rn is", self.pin_dict[rgbs[x]])
            pwm.  power)
          """
my_leds = led_class()
#print(my_leds.values)
#my_leds.getValue("red")

