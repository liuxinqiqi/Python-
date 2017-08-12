#!usr/bin/python
#coding=utf-8
import SocketServer
import time
class WebSocketServer(SocketServer.StreamRequestHandler):
    def handle(self):
        print "run"
        print self.client_address
        while True:
            data = self.rfile.readline()
            self.wfile.write('%s %s'%(time.ctime(),data))
            print data
            # data = raw_input('> ')
            if not data:
                break

if __name__ == "__main__" :
    wsServer = SocketServer.ThreadingTCPServer(( 'localhost',9600),WebSocketServer)
    print "run"
    wsServer.serve_forever()
