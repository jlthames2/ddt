#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import random

server = None
resp = "HTTP/1.1 200 OK\r\nConnection: close\r\n\r\n"

while True:
    if server:
        server.shutdown(socket.SHUT_RDWR)
        server.close()
    else:
        server = socket.socket()
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        host = socket.gethostname()

    port = random.randrange(80,90)
    server.bind((host, port))
    server.listen(1)
    print "Listen on port: %s" % port

    while True:
       client, address = server.accept()
       print 'RECVD FROM: %s' % str(address)
       client.send(resp)
       client.close()
       server.shutdown(socket.SHUT_RDWR)
       server.close()
       server = None
       break