#!/usr/bin/python
# -*- coding:UTF-8 -*-
PATH = './'

if __name__ == '__main__':
    filename = input('Enter file name: ')
    fileFullPath = PATH + filename
    try:
        fobj = open(fileFullPath, mode='r')
        for eachLine in fobj:
            print(eachLine)
    except IOError as e:
        print('file open error:', e)
    finally:
        if 'fobj' in locals():
            fobj.close()
    fobj.close()
