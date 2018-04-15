#!/usr/bin/env python
# -*- coding: utf-8 -*-
import SocketServer
import socket
import threading
import time
import random

class SimpleTCPHandler(SocketServer.BaseRequestHandler):
    # Must implement this function
    def handle(self):
        resp = """HTTP/1.1 200 OK\r\nDate: Tue, 17 Oct 2017 19:47:29 GMT\r\nExpires: -1\r\nContent-Type: text/html; charset=ISO-8859-1\r\n\r\n"""
        t = threading.current_thread()
        print "Server @ {} handling client {} request".format(t.name, self.client_address)
        self.request.sendall(resp)

class SimpleThreadedServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
    pass

class SimpleServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
    def __init__(self, port):
        self.host = socket.gethostname()
        self.port = port
        self.allow_reuse_address=True
        try:
            print "Starting @ port: %s" % self.port
            self.server = SimpleThreadedServer((self.host, self.port), SimpleTCPHandler)
            self.server_thread = threading.Thread(target=self.server.serve_forever)
            self.server_thread.daemon = True
            self.server_thread.start()
        except Exception, e:
            self.server=None
            print "Error creating server. Exception: %s" % str(e)


def spin_up():
    population = range(8000, 8900)
    num_ports = 10
    ports = random.sample(population,num_ports)
    servers = list()
    for port in ports:
        s = SimpleServer(port)
        servers.append( s )
    return servers

def spin_down(servers):
    for s in servers:
        if s.server:
            s.server.shutdown()
            s.server.server_close()


if __name__ == '__main__':

    while True:
        servers = spin_up()
        time.sleep(15)
        spin_down(servers)

