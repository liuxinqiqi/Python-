import socket

HOST = 'localhost'
PORT = 9600
BUFSIZ = 1024
ADDR = (HOST, PORT)

udpCliSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udpCliSock.connect(ADDR)

while True:
    data = raw_input('> ')
    if not data:
        break
    udpCliSock.send("%s\r\n"%data)
    data = udpCliSock.recv(BUFSIZ)
    if not data:
        break
    print data.strip()
