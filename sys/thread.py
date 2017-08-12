#!/usr/bin/python

from time import ctime, sleep
import threading

def music(name):
    print ("music %s.%s"%(name, ctime()))
    sleep(2)

def movie(name):
    print ('movie %s! %s'%(name, ctime()))

threads = []
t1 = threading.Thread(target = music, args = ('baby',))
t2 = threading.Thread(target = movie, args = ('afanda',))

threads.append(t1)
threads.append(t2)

if __name__ == "__main__":
    for t in threads:
        t.setDaemon(True)
        t.start()
    t.join()

    print ("all over %s"%ctime())
