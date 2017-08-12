#coding=utf-8
class Magic(object):
    '''this is Magic doc'''
    pass

print dir(Magic)
print "===================="
m = Magic()
print dir(m)      #魔法方法：一些情况下可以自动化运行
print "----------------------------------"
print Magic.__module__
print Magic.__class__
print Magic.__doc__
