#!/usr/bin/python
import os
from time import sleep
pid = os.fork()  #执行此句时，内核会自动复制生成一个文件，则此文件位父文件，复制的文件为子文件，
#在父文件中，pid的值为大于0的值，而在子文件中，pid的值为0.
#两个进程相互独立，互不影响，在父文件中设置的变量，子进程依然可以调用。
#但子进程的程序在fork后才开始执行。

if pid < 0:
    print "create process faile"
elif pid == 0:
    print pid
    print "this is a child process : ", os.getpid()
else:
    sleep(0.1)
    print pid
    print "this is a parent process : ", os.getpid()

print "==================="

#父进程先于子进程结束后，子进程会变为孤儿进程，由系统进行收养
#若由于某些原因，子进程先于父进程结束且父进程未处理，则会产生僵尸进程。
#解决方法：
# 1.wait()函数：（os.wait()阻塞等待）
# 2.创建三级子进程，将二级子进程注销掉
# 3.用信号进行处理，在父进程中挂在子进程推出处理信号，因为信号是异步方式，不会阻塞父进程运行
