#!/usr/bin/python
# -*- coding:UTF-8 -*-

from twisted.internet import protocol, reactor

HOST = 'localhost'
PORT = 21567


class TSClntProtocal(protocol.Protocol):
    def sendData(self):
        data: bytes = input('>').encode()
        if data:
            print('...sending %s...' % data)
            self.transport.write(data)
        else:
            self.transport.loseConnection()

    def connectionMade(self):
        self.sendData()

    def dataReceived(self, data: bytes):
        print(data)
        self.sendData()


class TSClntFactory(protocol.ClientFactory):
    protocol = TSClntProtocal
    clientConnectionLost = clientConnectionFailed = lambda self, connecotr, reason: reactor.stop()


reactor.connectTCP(HOST, PORT, TSClntFactory())
reactor.run()
