#!/usr/bin/python
#coding=utf-8

from socket import *

HOST = "192.168.0.204"
PORT = 8888
BUFSIZE = 1024
ADDR = (HOST, PORT)

sockfd = socket(AF_INET, SOCK_STREAM, 0)
sockfd.connect(ADDR)

while True:
    data = raw_input('>')
    if not data:
        break
    sockfd.send(data.encode())
    data = sockfd.recv(BUFSIZE).decode()
    if not data:
        break
    print (data)
sockfd.close()
