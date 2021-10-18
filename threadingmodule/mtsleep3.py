#!/usr/bin/python
# -*- coding:UTF-8 -*-

import threading
from time import ctime, sleep
from random import randint

loops = [randint(1, 20) for i in range(3)]


def loop(nloop, nsec):
    print('start loop ', nloop, ' at:', ctime())
    sleep(nsec)
    print('loop ', nloop, ' done at:', ctime())


def main():
    print('starting at:', ctime())
    threads = []
    nloops = range(len(loops))

    for i in nloops:
        t = threading.Thread(target=loop, args=(i, loops[i]))
        threads.append(t)

    for i in nloops:
        threads[i].start()

    for i in nloops:
        threads[i].join()

    print('all Done at:', ctime())


if __name__ == '__main__':
    main()
