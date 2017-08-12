#!/usr/bin/python
#coding=utf-8
import time
import sys

def produce(l):
    i = 0
    while True:
        if i < 5:
            l.append(i)
            yield i   #yield函数在 Python 中被称之为 generator（生成器）
            #yield 的作用就是把一个函数变成一个 generator，带有 yield 的函数
            #不再是一个普通函数，Python 解释器会将其视为一个 generator，调用 fab(5)
            #不会执行 fab 函数，而是返回一个 iterable 对象！在 for 循环执行时，
            #每次循环都会执行 fab 函数内部的代码，执行到 yield b 时，fab 函数
            #就返回一个迭代值，下次迭代时，代码从 yield b 的下一条语句继续执行，
            #而函数的本地变量看起来和上次中断执行前是完全一样的，于是函数继续执行，
            #直到再次遇到 yield。
            i += 1
            time.sleep(1)
        else:
            return

def consum(l):
    p = produce(l)
    while True:
        try:
            p.next()
            while len(l) > 0:
                print l.pop()
        except StopIteration:
            sys.exit(0)

l = []
consum(l)
