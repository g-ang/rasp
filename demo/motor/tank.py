# -*- coding: UTF-8 -*-
import RPi.GPIO as GPIO
import time

def left():
    pin1=7
    pin2=11
    en1=13
    en2=15
    GPIO.setmode(GPIO.BOARD)

    GPIO.setup(pin1,GPIO.OUT)
    GPIO.setup(pin2,GPIO.OUT)
    GPIO.setup(en1,GPIO.OUT)
    GPIO.setup(en2,GPIO.OUT)
    
    GPIO.output(pin1,True)
    GPIO.output(pin2,False)

    pwm2=GPIO.PWM(en2,500)
    pwm2.start(1)
    pwm2.ChangeDutyCycle(50)

    pwm=GPIO.PWM(en1,500)
    pwm.start(1)
    pwm.ChangeDutyCycle(50)
   
    time.sleep(5)

    pwm.stop()
    pwm2.stop()
    GPIO.cleanup()
if __name__ == "__main__":
    left()