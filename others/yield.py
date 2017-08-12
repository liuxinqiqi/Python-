def fib(max):     #斐波那契数列
    a,b = 0,1
    while a < max:
        yield a
        # yield a,b    #yield 相当于一个生成器，yield后的内容返回到调用生成器的位置，并将其返回，用来记录执行位置
        a,b = b,a + b

for i in fib(100):
    print (i)
