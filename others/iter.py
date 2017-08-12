#coding=utf-8
# class TestIter(object):
#     def __init__(self,a):
#         self.a = a
#         print a
#         print "--------------------"
#
#     def __iter__(self):   #迭代器，生成一个个
#         return self
#
#     def next(self):
#         self.a += 1
#         if self.a > 10:
#             print "++++++++++++"
#             raise
#         return self.a ** 2
#
# n = TestIter(2)
# print n.a
# print " ============="
# print n.next()
# print n.next()
# print n.next()
# print n.next()
# print n.next()
# print n.next()
# print n.next()
# print n.next()


class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1 # 初始化两个计数器a，b

    def __iter__(self):
        return self # 实例本身就是迭代对象，故返回自己

    def next(self):
        self.a, self.b = self.b, self.a + self.b # 计算下一个值
        if self.a > 1000: # 退出循环的条件
            raise StopIteration();
        return self.a # 返回下一个值
for n in Fib():
    print n





i = iter('abcd')
print i.next()
print i.next()
print i.next()





s = {'one':1,'two':2,'three':3}
print s
m = iter(s)
print m.next()
print m.next()
print m.next()
