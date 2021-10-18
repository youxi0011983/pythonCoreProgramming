#!/usr/bin/python
# -*- coding:UTF-8 -*-

import threading
from time import ctime, sleep
from random import randint

from past.builtins import apply

loops = [randint(1, 20) for i in range(2)]


class ThreadFunc(object):

    def __init__(self, func, args, name=''):
        self.name = name
        self.func = func
        self.args = args

    def __call__(self):
        self.func(*self.args)


def loop(nloop, nsec):
    print('start loop ', nloop, ' at:', ctime())
    sleep(nsec)
    print('loop ', nloop, ' done at:', ctime())


def switch(*args):
    print("This is switch")
    sleep(5)
    print("close switch")


def main():
    print('Starting at:', ctime())
    threads = []
    nloops = range(len(loops))
    for i in nloops:
        t = threading.Thread(
            # target=ThreadFunc(loop, (i, loops[i]), loop.__name__))
            target=ThreadFunc(switch, (i, loops[i]), switch.__name__))
        threads.append(t)

    for i in nloops:
        threads[i].start()

    for i in nloops:
        threads[i].join()
    print('all DONE at:', ctime())


if __name__ == '__main__':
    main()
