from twisted.web.server import Site
from twisted.web.static import File
from twisted.internet import reactor
import random


def rrun():
    reactor.removeAll()
    port = random.randrange(8000,8100)
    print "Listening: %s" % port
    resource = File('web')
    factory = Site(resource)
    reactor.callLater(25, rrun)
    reactor.listenTCP(port, factory)



reactor.callLater(1, rrun)
reactor.run()
