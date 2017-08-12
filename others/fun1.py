#coding=utf-8
import datetime

class Deco(object):
    def __init__(self,obj):
        self.func = obj
    def __call__(self,*args,**kwarg):
        print "现在时间："
        self.func(*args,**kwarg)

@Deco   #装饰器，带闭包的函数，与getTime()一起使用,效果与单独使用begin(getTime)()相同

def getTime(a,b,c,d):
    print a,b,c,d
    print datetime.datetime.now()


getTime(666,888,3,4)
