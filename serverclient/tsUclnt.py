#!/usr/bin/python
# -*- coding:UTF-8 -*-

from socket import *

HOST = 'localhost'
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

udpCliSock = socket(AF_INET, SOCK_DGRAM)

try:
    while True:
        data = input('>')
        if not data:
            break
        udpCliSock.sendto(data.encode(), ADDR)
        data, ADDR = udpCliSock.recvfrom(BUFSIZ)
        if not data:
            break
        print(data)
finally:
    udpCliSock.close()
