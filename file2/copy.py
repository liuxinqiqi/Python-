#coding=utf-8
# f = open('07.jpg','r')
# f1 = open('/home/linux/python/07.jpg','w')
#
# for i in f:
#     f1.write(i)


try:
    f = open('07.jpg','r')
    f1 = open('/home/linux/python/07.jpg','w')
except:
    print "open failed"


#判断 行
n = 0
while True:
    n += 1
    s = f.readline()
    if not s:      #如果s为空，结束循环
        break
    f1.write(s)
