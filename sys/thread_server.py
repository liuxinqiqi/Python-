#!/usr/bin/python
#coding=utf-8
import socket,os,sys,traceback
from threading import *
host = "192.168.0.204"
port = 8889
def handler(clientsock):
    print ("new child")
    print("Got connection from", clientsock.getpeername())
    while True:
        data = clientsock.recv(1024).decode()
        if not len(data):
            break
        clientsock.send("receive your message".encode())
        print host, data
        data = raw_input(">")

    clientsock.close()
s = socket.socket()
s.bind((host,port))
s.listen(5)
while True:
    try:
        clientsock, clientaddr = s.accept()
    except KeyboardInterrupt:
        raise
    except:
        traceback.print_exc()
        continue
    t = Thread(target = handler, args = (clientsock,))
    t.setDaemon(1)
    t.start()
s.close()
