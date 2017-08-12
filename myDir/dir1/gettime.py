import time
try:
    f = open('time.txt','a+')
except IOError as e:
    print e

line = 0
for i in f:
    line += 1
while True:
    tm = time.localtime()
    line += 1
    print >> f,"%d,%4d-%02d-%02d %02d:%02d:%02d"%(line,tm.tm_year,tm.tm_mon,tm.tm_mday,tm.tm_hour,tm.tm_min,tm.tm_sec)
    f.flush()
    time.sleep(1)
