#coding=utf-8

import datetime

def begin(func):
    def wrapper(*args,**kwargs):
        print "现在时间："
        func(*args,**kwargs)
        # wrapper
    return wrapper     #return返回的只能是一个变量，不能是函数，而函数名也可以是一个变量


@begin   #装饰器，带闭包的函数，与getTime()一起使用,效果与单独使用begin(getTime)()相同
def f(a,b,c,d):
    print a,b,c,d
    print datetime.datetime.now()


# f = getTime
# f()

# begin(getTime)()
f(666,888,3,4)





#函数内嵌套函数
# import datetime
#
# def deco(arg):
#     def begin(func):
#         def wrapper(*args,**kwargs):
#             print arg
#             print "现在时间："
#             func(*args,**kwargs)
#             # wrapper
#         return wrapper     #return返回的只能是一个变量，不能是函数，而函数名也可以是一个变量
#     return begin
#
# @deco('deco')   #装饰器，带闭包的函数，与getTime()一起使用,效果与单独使用begin(getTime)()相同
#
# def getTime(a,b,c,d):
#     print a,b,c,d
#     print datetime.datetime.now()
#
# begin(getTime)()
# getTime(666,888,3,4)
