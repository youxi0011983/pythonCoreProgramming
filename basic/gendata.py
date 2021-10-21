#!/usr/bin/python
# -*- coding:UTF-8 -*-
import time
from random import randint, choice
from string import ascii_lowercase
# from sys import maxsize
from time import ctime

maxsize= 1634088472
maxsize= 1634088472
maxsize= 1634088472

doms = ('com', 'edu', 'net', 'org', 'gov')

for i in range(randint(5, 10)):
    dtint = randint(0, maxsize - 1)
    dtstr = ctime(dtint)
    shorter = randint(4, 7)
    em = ''
    for j in range(shorter):
        em += choice(ascii_lowercase)

    longer = randint(shorter, 12)
    dn = ''
    for j in range(longer):
        dn += choice(ascii_lowercase)

    print('%s::%s@%s.%s::%d-%d-%d' % (dtstr, em, dn, choice(doms), dtint, shorter, longer))
