from twisted.web.server import Site
from twisted.web.static import File
from twisted.internet import reactor
import random


class SimpleWeb(object):
    def __init__(self, port_low, port_high):
        self.port_low = port_low
        self.port_high = port_high
        self.factory = Site( File('web') )
        self.spinUp()

    def spinUp(self):
        self.port = random.randrange(self.port_low, self. port_high)
        print "Listening @ %s" % self.port
        reactor.listenTCP(self.port, self.factory)


def rrun(servers):
    print "\n\nRestaring listeners."
    reactor.removeAll()
    for server in servers:
        server.spinUp()
    reactor.callLater(20, rrun, servers)


if __name__ == '__main__':
    s1 = SimpleWeb(80, 90)
    s2 = SimpleWeb(91, 100)
    s3 = SimpleWeb(8000, 8100)
    s4 = SimpleWeb(8101, 8200)
    servers = [s1, s2, s3, s4]

    reactor.callLater(20, rrun, servers)
    reactor.run()
