# -*- coding: UTF-8 -*-
import websocket
import json
import time
import tank
import types
import traceback
import StringIO
class Ws:
    ws=websocket
    callbacks={}
    def __init__(self):
        websocket.enableTrace(False)
        #192.168.1.85
        self.ws = websocket.WebSocketApp("ws://51helper.com:1811/rasp",
                              on_message = self.on_message,
                              on_error = self.on_error,
                              on_close = self.on_close)
        self.ws.on_open = self.on_open
        
    def run(self):
        self.ws.run_forever()

    def on_message(self,ws,message):
     
        data=json.loads(message)
        cmd=data['cmmand']

        r=cmd.split(".")
        class_name=r[0]  #类的名字
        method_name=r[1] #类方法的名字

        print("call:"+class_name+",method:"+method_name)

        #调用相应的类和方法，并返回，如果 err == Node 表示一切OK
        try:
            res,err=getattr(self.callbacks[class_name],method_name)(data['args'])
            if err == None:
                self.send(cmd,res)
            else:
                self.send(cmd,{"isFail":True,"error_msg":err})
        except:
            fp = StringIO.StringIO()    #创建内存文件对象
            traceback.print_exc(file=fp)
            err = fp.getvalue()
            self.send(cmd,{"isFail":True,"error_msg":err})


    def register(self,router,obj):
        print("regist :"+router)
        self.callbacks[router]=obj

    def send(self,cmmand,args):

        if type(args) is types.StringType:
            args={'text':args}

        data=json.dumps({'cmmand':cmmand,'args':args})
      
        self.ws.send(data)

    def on_error(self,ws,error):
        print("error:",error)
    
    def say(self,text):
        self.send('text',{'text':text})

    def on_close(self,ws):
        print("### -------------close----------- ###")

    def on_open(self,ws):
        print('connect ok')
        self.send('auth',{'name':'G'})
        self.say('hello ,i am rasp...')
