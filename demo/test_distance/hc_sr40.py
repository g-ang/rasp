#!/bin/env python
# -*- coding:utf-8 -*-
# -------------------------------
import time
import RPi.GPIO as GPIO
import datetime as dt
# 初始化
# 需要注意输出与输入的接口
# 17为发射，18为接收
def distance(pin_out,pin_in):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(pin_out, GPIO.OUT)
    GPIO.setup(pin_in, GPIO.IN)
    GPIO.output(pin_out, False)
    while 1:
        time.sleep(1)
        # IO 触发，给10us的高电平
        # 模块自动发送8个40khz的方波
        GPIO.output(pin_out, GPIO.HIGH)
        time.sleep(0.001)
        GPIO.output(pin_out, GPIO.LOW)
        # 获取发射完毕时间
        t1 = time.time()
        # 未接收为False，循环检查开始接受点
        # 转为True为开始接受
        while GPIO.input(pin_in) == False:
            pass
        # 循环检查开始接收，转为False。则为接受完毕
        while GPIO.input(pin_in):
            pass
        # 获取接受完毕时间
        t2 = time.time()
        # 计算发送与接收时间差
        t3 = t2-t1
        print t3
        # 空气中1个标准大气压在温度15度时速度为340m/s
        # 所以按照一秒钟34000厘米计算
        # 根据硬件文档，该模块探测距离在2-400cm之间
        # 测试范围的时间间隔应该为0.000117到0.023529
        # 为了方便取值自行变化一点
        if t3 > 0.00015:
            distance = t3*34000/2
            #if distance>100
            #   distance=distance / 100 

            print 'Distance: %f cm' % distance
        else:
            print 'Null'
if __name__ == "__main__":
	print("hello led")
	distance(11,7)
