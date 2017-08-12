#!/usr/bin/Python
#coding=utf-8
from time import sleep
from greenlet import greenlet

def test1():
    while True:
        sleep(1)
        print 2
        gr2.switch()   #阻塞
        print 4

def test2():
    while True:
        sleep(1)
        print 1
        gr1.switch()  #阻塞
        print 3

gr1 = greenlet(test1)
#先执行test1，打印2，阻塞后执行test2，打印1，阻塞后回到test1，
#继续执行print 4，循环，打印2，阻塞回到test2继续打印3，循环打印1，阻塞后回到test1，继续执行打印4
gr2 = greenlet(test2)

gr1.switch()
gr2.switch()
