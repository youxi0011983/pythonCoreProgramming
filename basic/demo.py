#!/usr/bin/python
# -*- coding:UTF-8 -*-


if __name__ == '__main__':
    s = 'abcde'
    # i=-1
    for i in range(-1, -len(s), -1):
        print(s[:i])
