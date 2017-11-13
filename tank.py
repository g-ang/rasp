# -*- coding: UTF-8 -*-
import RPi.GPIO as GPIO
import websocket
import json
import time
import traceback
import util
import os
import base64
class Tank:
    speed=0
    lspeed=0
    rspeed=0
    name=""
    gear="" 
    in1=""
    in2=""
    in3=""
    in4=""
    en1=""
    en2=""
    lpwm=""
    rpwm=""
    def __init__(self,name):
        self.name=name

    def test(self,args):
        print("hiHiHIHII tank test ")
        return "hello SB",None
  
    def setup(self,args):
        try:
            tank=args['tank']
            self.name=tank['name']
            self.in1=int(tank['in1'])
            self.in2=int(tank['in2'])
            self.in3=int(tank['in3'])
            self.in4=int(tank['in4'])
            self.en1=int(tank['en1'])
            self.en2=int(tank['en2'])
            
            self.setOut([self.in1,self.in2,self.en1,self.en2])
            self.setHigh([self.in1])
            self.setLow([self.in2])

            self.lpwm=GPIO.PWM(self.en1,100)
            self.lpwm.start(0)
            self.rpwm=GPIO.PWM(self.en2,100)
            self.rpwm.start(0)
            return "OK",None
        except:
            return None,util.error()
    
    def d(self,args):
        try:
            self.setHigh([self.in1])
            self.setLow([self.in2])
            self.speed(args)
            return "OK",None
        except:
            return None,util.error()
    
    def r(self,args):
        try:
            self.setHigh([self.in2])
            self.setLow([self.in1])
            self.speed(args)
            return "OK",None
        except:
            return None,util.error()

    def speed(self,args):
        try:
            left =int(args['left'])
            right=int(args['right'])
            self.lpwm.ChangeDutyCycle(left)
            self.rpwm.ChangeDutyCycle(right)

            return {'left':left,'right':right},None
        except:
            return None,util.error()

    def setOut(self,pins):
        for pin in pins:
            GPIO.setup(pin,GPIO.OUT)
    
    def cleanup(self,args):
        try:
            GPIO.cleanup()
            return "ok",None
        except:
            return None,util.error()

    def setHigh(self,pins):
        try:
            for pin in pins:
                GPIO.output(pin,GPIO.HIGH)
                return "ok",None
        except:
            return None,util.error()

    def setLow(self,pins):
        try:
            for pin in pins:
                GPIO.output(pin,GPIO.LOW)
                return "ok",None
        except:
            return None,util.error()

    def getSetup(self,args):
        try:
            setup={
                "in1":{"pin":self.in1,"value":GPIO.gpio_function(self.in1)},
                "in2":{"pin":self.in2,"value":GPIO.gpio_function(self.in2)},
                "in3":{"pin":self.in3,"value":GPIO.gpio_function(self.in3)},
                "in4":{"pin":self.in4,"value":GPIO.gpio_function(self.in4)},
                "en1":{"pin":self.en1,"value":GPIO.gpio_function(self.en1)},
                "en2":{"pin":self.en2,"value":GPIO.gpio_function(self.en2)},
            }
            return setup,None
        except:
            return None,util.error()
            
    def send(self,cmmand,args):
        self.ws.send(json.dumps({'cmmand':cmmand,'args':args}))

    def clap(self,args):
        body=os.popen('raspistill -w 120 -h 100 -q 100 -ss 50000 -br 85 -sa 30 -t 1 -o -').read()
        return {'body':base64.b64encode(body)},None