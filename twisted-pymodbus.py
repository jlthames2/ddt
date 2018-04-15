#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pymodbus.server.async import ModbusServerFactory
from pymodbus.transaction import ModbusSocketFramer
from pymodbus.device import ModbusDeviceIdentification
from pymodbus.datastore import ModbusSequentialDataBlock
from pymodbus.datastore import ModbusSlaveContext, ModbusServerContext
import random
from twisted.internet import reactor


def rrun(factory):
    reactor.removeAll()
    port = random.randrange(500, 599)
    print "Listening @ %s" % port
    reactor.listenTCP(port, factory)
    reactor.callLater(10, rrun, factory)


store = ModbusSlaveContext(
    di = ModbusSequentialDataBlock(0, [17]*100),
    co = ModbusSequentialDataBlock(0, [17]*100),
    hr = ModbusSequentialDataBlock(0, [17]*100),
    ir = ModbusSequentialDataBlock(0, [17]*100))
context = ModbusServerContext(slaves=store, single=True)


identity = ModbusDeviceIdentification()
identity.VendorName  = 'Pymodbus'
identity.ProductCode = 'PM'
identity.VendorUrl   = 'http://github.com/bashwork/pymodbus/'
identity.ProductName = 'Pymodbus Server'
identity.ModelName   = 'Pymodbus Server'
identity.MajorMinorRevision = '1.0'

framer  = ModbusSocketFramer
factory = ModbusServerFactory(context, framer, identity)

print "Starting Reactor...."
reactor.callLater(2, rrun, factory)
reactor.run()
