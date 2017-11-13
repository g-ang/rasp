# -*- coding: UTF-8 -*-
import RPi.GPIO as GPIO
import time 

#led 灯，每隔一秒亮一次
def led(pin):	
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(pin,GPIO.OUT)
	
	pwm=GPIO.PWM(pin,50)
	pwm.start(0)
	for x in xrange(30):
            
		for dc in range (0,101,5):
			pwm.ChangeDutyCycle(dc)
			time.sleep(0.1)
		for dc in range(100,-1,-5):
			pwm.ChangeDutyCycle(dc)
			time.sleep(0.1)

	pwm.stop()
	GPIO.cleanup()

if __name__ == "__main__":
	print("hello led")
	led(7)
