#coding=utf-8
'''
题目要求：编程读写一个文件test.txt，每隔1秒向文件中写入一行数据，类似这样：

1,  2007-7-30 15:16:42
2,  2007-7-30 15:16:43
该程序应该无限循环，直到按Ctrl-C中断程序。再次启动程序写文件时可以追加到原文件之后，并且序号能够接续上次的序号，比如：
1,  2007-7-30 15:16:42
2,  2007-7-30 15:16:43
3,  2007-7-30 15:19:02
4,  2007-7-30 15:19:03
5,  2007-7-30 15:19:04'''

import time

try:
    f = open(  'test.txt','a+')
except IOError as e:
    print e

time_t = time.localtime()
n = f.readline()

def writetime():
    f.writelines(n1)
    t = time.strftime(",%Y-%m-%d %H:%M:%S\n", time.localtime())
    f.writelines(t)
    f.flush()
    time.sleep(1)

if not n:
    n = 1
    while n:
        n1 = '%d'%n
        writetime()
        n += 1
else:
    line = f.readlines()
    l = line[-1]    #取最后一行
    n = int(l[0])       #取得最后一行第一个数并强转为整数
    while n:
        n += 1
        n1 = '%d'%n
        writetime()
