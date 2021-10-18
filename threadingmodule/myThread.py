#!/usr/bin/python
# -*- coding:UTF-8 -*-

import threading
from time import ctime, sleep
from random import randint

loops = [randint(1, 20) for i in range(2)]


class MyThread(threading.Thread):
    def __init__(self, func, args, name=''):
        threading.Thread.__init__(self)
        self.name = name
        self.func = func
        self.args = args

    def run(self):
        print('Staring', self.name, 'at', ctime())
        self.res = self.func(*self.args)
        print(self.name, 'finished at:', ctime())

    def getResult(self):
        return self.res


def loop(nloop, nsec):
    print('start loop ', nloop, ' at:', ctime())
    sleep(nsec)
    print('loop ', nloop, ' done at:', ctime())


def main():
    print('Starting at:', ctime())
    threads = []
    nloops = range(len(loops))
    for i in nloops:
        t = MyThread(loop, (i, loops[i]), loop.__name__)
        threads.append(t)

    for i in nloops:
        threads[i].start()

    for i in nloops:
        threads[i].join()

    print('all DONE at:', ctime())


if __name__ == '__main__':
    main()
