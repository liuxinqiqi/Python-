#coding=utf-8
class A(object):
    def __getattr__(self,name):
        print "you use getattr"
        return "NO"

    def __setattr__(self,name,value):
        print "you use setattr"
        self.__dict__[name] = value

a = A()

a.x    #当没有a.x时，自动调用__getattr__
print "--------------"
print a.x
print "================"
print a.k
print "=============="
a.y = "sex y"   #当赋值给一个不存在的a.y赋值时，自动调用__setattr__
print a.y
