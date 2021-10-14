#!/usr/bin/python
# -*- coding:UTF-8 -*-

import ftplib
import os
import socket

HOST = 'ftp.jaist.ac.jp'
DIRN = 'pub/Linux/debian/doc'
FILE = '00-INDEX'


def main():
    try:
        f = ftplib.FTP(HOST)
    except (socket.error, socket.gaierror) as e:
        print('ERROR: cannot reach "%s"' % HOST)
        return

    print('*** connected to host "%s"' % HOST)

    try:
        f.login()
    except ftplib.error_perm:
        print('ERROR: cannot login anonymously')
        f.quit()
        return
    print('*** Logged in a "anonymous"')

    try:
        f.cwd(DIRN)
    except ftplib.error_perm:
        print('ERROR: cannot CD to "%s"' % DIRN)
        f.quit()
        return
    print('*** Changed to "%s" folder' % DIRN)

    try:
        file = open(FILE, 'wb')
        f.retrbinary('RETR %s' % FILE, file.write)
    except ftplib.error_perm:
        print('ERROR: cannot read file "%s"' % FILE)
        file.close()
        os.unlink(FILE)
    else:
        print('*** Downloaded "%s"to CMD' % FILE)
    f.quit()
    return


if __name__ == '__main__':
    main()
