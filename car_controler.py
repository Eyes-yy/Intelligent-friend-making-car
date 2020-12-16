import RPi.GPIO as GPIO
import time
import configparser

class CarMv():
    def __init__(self):
        config=configparser.ConfigParser()
        config.read("config.ini")
        self.IN1=config.getint("car","IN1")
        self.IN2=config.getint("car","IN2")
        self.IN3=config.getint("car","IN3")
        self.IN4=config.getint("car","IN4")
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.IN1,GPIO.OUT)
        GPIO.setup(self.IN2,GPIO.OUT)
        GPIO.setup(self.IN3,GPIO.OUT)
        GPIO.setup(self.IN4,GPIO.OUT)
    def reset(self):
        GPIO.output(self.IN1,GPIO.LOW)
        GPIO.output(self.IN2,GPIO.LOW)
        GPIO.output(self.IN3,GPIO.LOW)
        GPIO.output(self.IN4,GPIO.LOW)
    def __up(self):
        self.reset()
        GPIO.output(self.IN1,GPIO.HIGH)
        GPIO.output(self.IN2,GPIO.LOW)
        GPIO.output(self.IN3,GPIO.LOW)
        GPIO.output(self.IN4,GPIO.HIGH)
    def __down(self):
        self.reset()
        GPIO.output(self.IN1,GPIO.LOW)
        GPIO.output(self.IN2,GPIO.HIGH)
        GPIO.output(self.IN3,GPIO.HIGH)
        GPIO.output(self.IN4,GPIO.LOW)
    def __turnRight(self):
        self.reset()
        GPIO.output(self.IN1,GPIO.LOW)
        GPIO.output(self.IN2,GPIO.HIGH)
        GPIO.output(self.IN3,GPIO.LOW)
        GPIO.output(self.IN4,GPIO.HIGH)
    def __turnLeft(self):
        self.reset()
        GPIO.output(self.IN1,GPIO.HIGH)
        GPIO.output(self.IN2,GPIO.LOW)
        GPIO.output(self.IN3,GPIO.HIGH)
        GPIO.output(self.IN4,GPIO.LOW)
    def __stop(self):
        self.reset()
    def carMove(self, direction):
        print(direction)
        if direction=='1':
            self.__up()
        if direction=='2':
            self.__down()
        if direction=='3':
           self.__turnLeft()
        if direction=='4':
           self.__turnRight()
        if direction=='5':
           self.__stop()
if __name__ == "__main__":
    raspCar=CarMv()
    while True:
        direction=input()
        raspCar.carMove(direction)

   # time.sleep(1)