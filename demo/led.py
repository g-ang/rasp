# -*- coding: UTF-8 -*-
import RPi.GPIO as GPIO
import time 

#led 灯，每隔一秒亮一次
def led(pin):
    print(GPIO.IN, GPIO.OUT, GPIO.SPI, GPIO.I2C, GPIO.HARD_PWM, GPIO.SERIAL, GPIO.UNKNOWN)
    1, 0, 41, 42, 43, 40, -1
    GPIO.setmode(GPIO.BOARD)
    func=GPIO.gpio_function(pin)
    print(func)
  
    GPIO.setup(pin,GPIO.OUT)
    print(GPIO.input(pin))
    for x in xrange(10):
        
        GPIO.output(pin,GPIO.HIGH)
        time.sleep(1)		
        
        GPIO.output(pin,GPIO.LOW)
        time.sleep(1)

    GPIO.cleanup()

if __name__ == "__main__":
    print("hello led")
    led(7)