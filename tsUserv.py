#!/usr/bin/python
# -*- coding:UTF-8 -*-

from socket import *
from time import ctime

HOST = ''
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

udpSerSock = socket(AF_INET, SOCK_DGRAM)
udpSerSock.bind(ADDR)

try:
    while True:
        print('waiting for message...')
        data, addr = udpSerSock.recvfrom(BUFSIZ)
        udpSerSock.sendto(('[%s] %s' % (ctime(), data.decode())).encode(), addr)
        print('...received from and returned tc:', addr)
except KeyboardInterrupt as e:
    print(e)
    udpSerSock.close()

