#!/usr/bin/python
import multiprocessing
from time import sleep
import os

def worker(msg):
    print "parent pid: ",os.getpid()
    while True:
        sleep(2)
        print msg
    return



if __name__ == "__main__":
    p = multiprocessing.Pool(processes=4)   #创建进程池，创建4个进程，存放在内存中，使用时直接取
    result = []
    for i in xrange(10):
        msg = "hello %d"%(i)
        result.append(p.apply_async(worker,(msg,)))
        #获取线程池-----p.apply_async(worker,(msg,)
    p.close()
    p.join()
    for res in result:
        print res.get()
    # print os.getpid()
