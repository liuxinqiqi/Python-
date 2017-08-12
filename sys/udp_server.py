#!/usr/bin/python
#coding=utf-8

from socket import *
from time import ctime

HOST = "192.168.0.204"
PORT = 8888
BUFSIZE = 1024
ADDR = (HOST,PORT)
sockfd = socket(AF_INET, SOCK_DGRAM)
sockfd.bind(ADDR)

while True:
    print "waiting for massage..."
    data, addr = sockfd.recvfrom(BUFSIZE)
    print "client addr :",addr
    print data
    sockfd.sendto('[%s] : %s' % (ctime(), data ),addr)
    data = raw_input(">")

sockfd.close()
