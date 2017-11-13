# -*- coding: UTF-8 -*-
import RPi.GPIO as GPIO
import time 
class Motor:
    pin1=""
    pin2=""
    pin3=""
    pin4=""
	
    def __init__(self,pin1,pin2,pin3,pin4):
        self.pin1=pin1
    	self.pin2=pin2
    	self.pin3=pin3
    	self.pin4=pin4
    	
    	GPIO.setmode(GPIO.BOARD)
    	GPIO.setwarnings(False)
        GPIO.setup(self.pin1,GPIO.OUT)
        GPIO.setup(self.pin2,GPIO.OUT)
        GPIO.setup(self.pin3,GPIO.OUT)
        GPIO.setup(self.pin4,GPIO.OUT)

    def run(self,steps,sec,v=1):
        for i in range(0,steps):
            self.output(f1=v)
            time.sleep(sec)
            self.output(f2=v)
            time.sleep(sec)
            self.output(f3=v)
            time.sleep(sec)
            self.output(f4=v)
            time.sleep(sec)
        GPIO.cleanup()

    def output(self,f1=0,f2=0,f3=0,f4=0):
    	print(f1)
        GPIO.output(self.pin1,f1)
        GPIO.output(self.pin2,f2)
        GPIO.output(self.pin3,f3)
        GPIO.output(self.pin4,f4)

if __name__ == "__main__":
    print("hello led")
    #里面那边真脚，第：4,6,7,8 对应 7,11,13,15
    m=Motor(pin1=7,pin2=11,pin3=13,pin4=15)
   
    #来1000次循环，间隔2毫秒
    m.run(1000,0.002,1)