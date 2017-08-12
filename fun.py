#coding=utf-8
#非局部变量

# def fun_out():
#     a = 4
#     def fun_in():
#         nonlocal a
#         a += 1
#     fun_in()
#     print a
# fun_out()

a = 1

def out():
    b = 2
    def inner():
        nonlocal b
        b += 1
        print (b)
    inner()

out()
#闭包
# def out():
#     a = 1
#     print a
#     def inner():
#         print a+1
#         print "I'm inner"
#     return inner
#
# f = out()
# f()
#
# def func(name):
#     def inner_func(age):
#         print 'name:', name, 'age:', age
#     return inner_func
#
# b = func('the 5 fire')
# b(26)
#
# #装饰器
# def makebold(fn):
#     def wrapped():
#         return "<b>" + fn() + "</b>"
#     return wrapped
#
# def makeitalic(fn):
#     def wrapped():
#         return "<i>" + fn() + "</i>"
#     return wrapped
#
# @makebold
# @makeitalic
#
# def hello():
#     return "hello world"
#
# print hello()
#
# #匿名函数  lambda是一个表达式而不是一个语句，它返回一个函数对象
# L = [lambda x: x ** 2,
#      lambda x: x + 3,
#      lambda x: x * 4]
#
# for f in L:
#     print(f(2))
#==================================
#coding=utf-8

# class TestStaticMethod(object):
#     @staticmethod
#     def foo():
#         print "calling static method foo()"
#
#     #foo = staticmethod(foo)
#
# class Child(TestStaticMethod):
#     pass
#
# static = TestStaticMethod()
#
# static.foo()
# TestStaticMethod.foo()
#
#
# child = Child()
#
# child.foo()
#
# print "==============================================="
# class TestClassMethod(object):
#     @classmethod
#     def foo(cls):
#         print "calling class method foo()"
#         print cls.__name__
#
# class Child1(TestClassMethod):
#     pass
#
# cls = TestClassMethod()
#
# cls.foo()
# TestClassMethod.foo()
#
#
# child = Child1()
#
# child.foo()
