#!/usr/bin/python
# -*- coding:UTF-8 -*-

# 'readTextFile.py -- read and display text file'

# get filename
fname = input("Enter filename: ")
print()

# attempt to open file for reading
try:
    fobj = open(fname, 'r')
except IOError as e:
    print("*** file open error: ", e)
else:
    # display content to screen
    for eachLine in fobj:
        print(eachLine)
    fobj.close()
