# -*- coding: UTF-8 -*-
import RPi.GPIO as GPIO
import websocket
import json
import time
import traceback
class Gpio:

    def setup(self,args):
        pin=int(args['pin'])
        val=int(args['val'])

        GPIO.setup(pin,val)
        return {'pin':pin,'val':val},None

    def get(self,args):
        pin=int(args['pin'])
        val=GPIO.gpio_function(pin)
        return {'pin':pin,'val':val},None

    def output(self,args):
        pin=int(args['pin'])
        val=int(args['val'])

        GPIO.output(pin,val)
        return {'pin':pin,'val':val},None
    
    def setmode(self,args):
        mode=int(args['mode'])
        GPIO.setmode(mode)
        return {'mode':mode},None

    def getmode(self,args):
        mode = GPIO.getmode()
        if mode == None:
            mode="undefined"
        return {'mode':mode},None

    def input(self,args):
        pins=args['pins']
        vals={}
        for pin in pins:
        	pin=int(pin)
        	vals[pin]=GPIO.input(pin)
        return vals,None
        
    def cleanup(self,args):
        pin = int(args['pin'])
        GPIO.cleanup(pin)
        return {'pin':pin},None