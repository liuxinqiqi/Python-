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
        # 阻止handle退出 便于分析区别
        # while True:
        #     if not data:
        #         break
        #     pass

if __name__ == "__main__" :
    # 可以简单将下述ThreadingUDPServer替换为UDPServer
    wsServer = SocketServer.ThreadingUDPServer(( 'localhost',9600),WebSocketServer)
    print "run"
    wsServer.serve_forever()
