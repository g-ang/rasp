# -*- coding: UTF-8 -*-
import RPi.GPIO as GPIO
import time 
import dis
#led 灯，每隔一秒亮一次
def led(pin,flag):
	GPIO.setup(pin,GPIO.OUT)

	GPIO.output(pin,flag)
		

def callback(d):
	if d<20:
	    led(13,GPIO.LOW)
	else:
		led(13,GPIO.HIGH)

if __name__ == "__main__":
	print("hello led")
	try:
		GPIO.setmode(GPIO.BOARD)
		dis.distance(11,7,callback)
		GPIO.cleanup()
	except Exception as err:
		GPIO.cleanup()
		print("exit")
