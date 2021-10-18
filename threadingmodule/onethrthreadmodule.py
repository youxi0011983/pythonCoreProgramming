#!/usr/bin/python
# -*- coding:UTF-8 -*-

import threading
from time import sleep, ctime


class LoopClass(threading.Thread):
    def __init__(self, name, time):
        threading.Thread.__init__(self)
        self.name = name
        self.time = time

    def run(self):
        print('start loop %s at:' % self.name, ctime())
        sleep(self.time)
        print('loop %s done at:' % self.name, ctime())


def main():
    print('starting at:', ctime())
    # 创建线程
    loop0 = LoopClass("loop0", 4)
    loop1 = LoopClass("loop1", 2)
    # 开启线程
    loop0.start()
    loop1.start()
    loop0.join()
    loop1.join()
    sleep(6)
    print('all DONE at:', ctime())


if __name__ == '__main__':
    main()
