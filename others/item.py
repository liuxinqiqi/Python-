#coding=utf-8
class DictDemo(object):
    def __init__(self,key,value):   # 实例化对象时即调用
        print "this is __init__."
        self.dict = {}
        self.dict[key] = value

    def __getitem__(self,key):      # 对象获取一个值的时候调用
        print "this is __getitem__."
        return self.dict[key]

    def __setitem__(self,key,value):    # 为对象赋值时调用
        print "this  is __setitem__."
        self.dict[key] = value

    def __len__(self):               # 计算对象的长度
        print "this is __len__"
        return len(self.dict)

d = DictDemo('key0',1)    # d 是类的一个对象,对象的初始化
d['key0']
print "============="
d['key1'] = 2
print d['key1']
print "---------------------"
d[3] = 5
print d[3]

print len(d)
