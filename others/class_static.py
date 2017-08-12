#coding=utf-8
class Color(object):
    _color = (0,0,0)    #双下划线才是私有变量

    @classmethod        #  装饰器
    def value(cls):       # cls 是类自带的表示类的参数
        if cls.__name__ == 'Red':     #用 cls. 调用
            cls._color = (255,0,0)
        elif cls.__name__ == 'Green':
            cls._color = (0,255,0)
        return cls._color

class Red(Color):
    pass

class Green(Color):
    pass
class UnknowColor(Color):
    pass

red = Red()
green = Green()
xcolor = UnknowColor()

print 'red = ',red.value()
print 'green = ',green.value()
print 'xcolor = ',xcolor.value()

"""=========================================================="""

class Color(object):
    _color = (0,0,0)

    def value(self):    #self是方法自带的对象，可以用self直接调用内建函数
        if self.__name__ == 'Red':
            self._color = (255,0,0)
        elif self.__name__ == 'Green':
            self._color = (0,255,0)
        return self._color


class Red(Color):
    pass

class Green(Color):
    pass
class UnknowColor(Color):
    pass

red = Red()
green = Green()
xcolor = UnknowColor()

print 'red = ',red.value()
print 'green = ',green.value()
print 'xcolor = ',xcolor.value()
