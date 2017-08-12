#!/usr/bin/python
#coding=utf-8
import socket, traceback, os, sys
host = "192.168.0.204"
port = 8888

s = socket.socket()
s.bind((host,port))
s.listen(5)
while True:
    c, addr = s.accept()
    pid = os.fork()
    if pid:
        c.close()
        continue
    else:
        s.close()
        while True:
            data = c.recv(1024).decode()
            if not len(data):
                break
            print "addr:",(addr)
            print ( data)
            # data = raw_input(">")

            c.send("recv your message")
        c.close()
        sys.exit(0)
