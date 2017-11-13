import json
import time
import tank
import thread
import RPi.GPIO as GPIO
import cli
import gpio

c=cli.Ws()
c.register("tank",tank.Tank("G"))
c.register("gpio",gpio.Gpio())
c.run()