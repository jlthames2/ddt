from twisted.web.server import Site
from twisted.web.static import File
from twisted.internet import reactor
import random


class SimpleWeb(object):
    def __init__(self, port_low, port_high):
        self.port = random.randrange(port_low, port_high)
        self.factory = Site( File('web') )
        print "Listening @ %s" % self.port
        reactor.listenTCP(self.port, self.factory)


if __name__ == '__main__':
    s1 = SimpleWeb(80, 90)
    s2 = SimpleWeb(91, 100)
    s3 = SimpleWeb(8000, 8100)
    s4 = SimpleWeb(8101, 8200)

    reactor.run()
