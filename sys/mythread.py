from time import ctime, sleep
import threading

class MyThreat(threading.Thread):
    def __init__(self, func, args, name = ""):
        threading.Thread.__init__(self)
        self.name = name
        self.func = func
        self.args = args
    def run(self):
        self.func

def super_player(file, time):
    for i in range(2):
        print ("start playing:%s . %s"%(file, ctime()))
        sleep(1)

l = {"baby.mp3" : 3, "avatar.mp4" : 5, "you and me mp3" : 4}
threads = []
files = range(len(l))

for file, time in l.items():
    t = MyThreat(super_player(file, time),"lalala")
    threads.append(t)

if __name__ == '__main__':
    for i in files:
        threads[i].start()

    for i in files:
        threads[i].join()
