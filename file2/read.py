#coding=utf-8
import sys


# with open('file','r+') as f:
#     print dir(f)
#     print f.__sizeof__()




with open('file','r+') as f:
    s = f.read(7)
    s1 = f.readline(12)
    s2 = f.readline(34)
    s3 = f.readlines()
print s
print s1
print s2
print"=============="
print s3


# s = sys.stdin.read(12)       #字节到12则结束
# # s = sys.stdin.read()          #缓冲区满才结束
# print s
