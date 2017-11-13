import RPi.GPIO as GPIO
import time 



def led(pin):	
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(pin,GPIO.OUT)
	for x in xrange(10):
		GPIO.output(pin,GPIO.HIGH)
		time.sleep(1)		
		GPIO.output(pin,GPIO.LOW)
		time.sleep(1)
	GPIO.cleanup()

if __name__ == "__main__":
	print("hello world")
	led(7)
