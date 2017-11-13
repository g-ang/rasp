import RPi.GPIO as gpio
import time, sys

pin = 13

gpio.setmode(gpio.BOARD)
gpio.setup(pin, gpio.OUT)

p = gpio.PWM(pin, 400)

p.start(0)

p.ChangeDutyCycle(96)
time.sleep(2)
print("hight is finish")

p.ChangeDutyCycle(30)
time.sleep(2)
print("low is finish")

for dc in range(32,46,1):
    print 'dc:', dc
    p.ChangeDutyCycle(dc)
    time.sleep(1);

time.sleep(20)
p.stop()
gpio.cleanup()