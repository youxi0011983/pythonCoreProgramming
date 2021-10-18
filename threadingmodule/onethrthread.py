#!/usr/bin/python
# -*- coding:UTF-8 -*-

import _thread
from time import sleep, ctime


def loop0():
    print('start loop 0 at:', ctime())
    sleep(4)
    print('loop 0 done at:', ctime())


def loop1():
    print('start loop 1 at:', ctime())
    sleep(2)
    print('loop 1 done at:', ctime())


def main():
    print('starting at:', ctime())
    try:
        _thread.start_new_thread(loop0, ())
        _thread.start_new_thread(loop1, ())
    except:
        print("Error: 无法启动线程")
    sleep(6)
    print('all DONE at:', ctime())


if __name__ == '__main__':
    main()
