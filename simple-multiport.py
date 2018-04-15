#!/usr/bin/env python
# -*- coding: utf-8 -*-
import SocketServer
import socket

class SimpleTCPHandler(SocketServer.BaseRequestHandler):
    # Must implement this function
    def handle(self):
        resp = """HTTP/1.1 200 OK\r\nDate: Tue, 17 Oct 2017 19:47:29 GMT\r\nExpires: -1\r\nContent-Type: text/html; charset=ISO-8859-1\r\n\r\n"""
        self.data = self.request.recv(1024).strip()
        print "{} wrote:".format(self.client_address[0])
        print self.data
        # just send back the same data, but upper-cased
        self.request.sendall(resp)

class SimpleServer(object):
    def __init__(self, port):
        self.host = socket.gethostname()
        self.port = port
        try:
            print "Starting @ port: %s" % self.port
            self.server = SocketServer.TCPServer((self.host, self.port), SimpleTCPHandler)
            self.server.serve_forever()
        except Exception, e:
            print "Error creating server. Exception: %s" % str(e)
 

if __name__ == '__main__':

    servers = []
    ports = range(81,120)
    for port in ports:
        s = SimpleServer(port)
        servers.append( s )
        
