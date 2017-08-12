#coding=utf-8

#lambda：简单函数/匿名函数。 是内置函数,使用时，变量a = lambda + 变量b ：计算表达式
L = [lambda x : x ** 2,
     lambda x : x ** 3,
     lambda x : x ** 4
]
#在赋值时，通过lambda所定义的对象来赋值
for f in L:
    print(f(3))

print "==========="
x = (lambda b : b * 2)
print x(b = 5)

print "==========="
g = lambda x,y=2,z=3 : x+y+z
print g(45,z=4,y=5)


print "==========="

L = [(lambda x: x**2),
    (lambda y: y**3),
    (lambda x: x**4)]
print L[0](4),L[1](3),L[2](2)   #赋值

print "==========="
D = {'f1':(lambda: 2+3),
    'f2':(lambda: 2*3),
    'f3':(lambda: 2**3)}
print D['f1'](),D['f2'](),D['f3']()
