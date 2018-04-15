#!/usr/bin/env python
# -*- coding: utf-8 -*-
import SocketServer
import socket
import threading
import time

class SimpleTCPHandler(SocketServer.BaseRequestHandler):
    # Must implement this function
    def handle(self):
        resp = """HTTP/1.1 200 OK\r\nDate: Tue, 17 Oct 2017 19:47:29 GMT\r\nExpires: -1\r\nContent-Type: text/html; charset=ISO-8859-1\r\n\r\n"""
        self.data = self.request.recv(1024).strip()
        t = threading.current_thread()
        print "{} wrote:".format(t.name)
        print self.data
        # just send back the same data, but upper-cased
        self.request.sendall(resp)

class SimpleThreadedServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
    pass

class SimpleServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
    def __init__(self, port):
        self.host = socket.gethostname()
        self.port = port
        try:
            print "Starting @ port: %s" % self.port
            self.server = SimpleThreadedServer((self.host, self.port), SimpleTCPHandler)
            self.server_thread = threading.Thread(target=self.server.serve_forever)
            self.server_thread.daemon = True
            self.server_thread.start()
        except Exception, e:
            print "Error creating server. Exception: %s" % str(e)


if __name__ == '__main__':

    servers = []
    ports = range(81,120)
    for port in ports:
        s = SimpleServer(port)
        servers.append( s )

    while True:
        time.sleep(5)
        for s in servers:
            print 'Port: %s' % s.port


