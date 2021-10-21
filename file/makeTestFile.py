#!/usr/bin/python
# -*- coding:UTF-8 -*-

# makeTextFile.py -- create text file
import os

ls = os.linesep

# get filename
while True:
    fname = input('Enter file name: ')
    if os.path.exists(fname):
        print("Error '%s' already exists" % fname)
    else:
        break

# get file content(text) lines
all = []
print("\nEnter line('.'by itself to quit).\n")

# loop until user terminates input
while True:
    entry = input('> ')
    if entry == '.':
        break
    else:
        all.append(entry)

# write lines to file with proper line-ending
try:
    fobj = open(fname, mode='w')
    fobj.writelines(['%s%s' % (x, ls) for x in all])
except IOError as e:
    print('file open error:', e)
finally:
    if 'fobj' in locals():
        fobj.close()
fobj.close()
print("DONE!")