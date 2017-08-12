#coding=utf-8
#自省机制函数
#hasattr  getattr  setattr delattr
#isinstance(判断某个对象是否是该类的对象)
#issubclass(判断一个类是否继承另一个类)


class Parent(object):
    name = 'liu'

class Child(Parent):
    pass


p = Child()
print issubclass(Child,Parent)    #判断第一个类是否由第二个类创建
print isinstance(p,Parent)        #判断对象p是否属于Parent类


print "======================="

print hasattr(p,'name')      #获取name的值

l = []
print hasattr(l,'append')    #append为内建函数，hasattr是判断是否存在
print getattr(p,'name')      #getattr是获取类内的属性变量

setattr(p,'age',23)
print p.age


delattr(p,'age')      #可以删除age，以为age是由变量p自定义的变量

# delattr(p,'name')     #不可删除name，因为name是属于类里的属性变量
