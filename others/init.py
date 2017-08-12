#coding=utf-8
class Magic1(object):
    def __init__(self):  #执行完__new__的时候执行__init__，初始化对象/构造对象
        print "__init__............."

    def __new__(cls):  #首先执行__new__，若本类中没有，则调用父类，最终执行object中的__new__函数
        print "__new__............"
        return super(Magic1,cls).__new__(cls)

    def __call__(self,a):    #传递参数,调用时执行
        print "=============================================="
        print a

    def __del__(self):      # 释放时自动执行
        print "__del__...."

m = Magic1()
m("this is call")
m(1)
del m
print "over"
