#!/usr/bin/python
# -*- coding:UTF-8 -*-

import errno
import os
import socket
import stat
import tempfile


class NetworkError(IOError):
    pass


class FileError(IOError):
    pass


def updArgs(args, newarg=None):
    if isinstance(args, IOError):
        myargs = []
        myargs.extend([arg for arg in args])
    else:
        myargs = list(args)

    if newarg:
        myargs.append(newarg)

    return tuple(myargs)


def fileArgs(file, mode, args):
    if args[0] == errno.EACCES and 'access' in dir(os):
        perms = ''
        permd = {'r': os.R_OK, 'w': os.W_OK, 'x': os.X_OK}
        pkeys = permd.keys()
        pkeys.sort()
        pkeys.reverse()

        for eachPerm in 'rwx':
            if os.access(file, permd[eachPerm]):
                perms += eachPerm
            else:
                perms += '-'

        if isinstance(args, IOError):
            myargs = []
            myargs.extend([arg for arg in args])
        else:
            myargs = list(args)
        myargs[1] = "'%s' %s(perms:'%s;)" % (mode, myargs[1], perms)

        myargs.append(args.filename)
    else:
        myargs = args
    return tuple(myargs)


def myconnect(sock, host, port):
    try:
        sock.connect((host, port))
    except socket.error as args:
        myargs = updArgs(args)  # conv inst2tuple
        if len(myargs) == 1:  # no #s on some errs
            myargs = (errno.ENXIO, myargs[0])

        raise NetworkError(updArgs(myargs, host + ': ' + str(port)))


def myopen(file, mode='r'):
    try:
        fo = open(file, mode)
    except IOError as args:
        raise FileError(fileArgs(file, mode, args))

    return fo


def testfile():
    file = tempfile.mktemp()
    f = open(file, 'w')
    f.close()

    for eachTest in ((0, 'r'), (stat.S_IXUSR, 'r'), (stat.S_IRUSR, 'w'), (0o500, 'w')):
        try:
            os.chmod(file, eachTest[0])
            f = myopen(file, eachTest[1])
        except FileError as args:
            print("%s:%s" % (args.__class__.__name__, args))
    else:
        print(file, "opend ok...perm ignored")
        f.close()
    os.chmod(file, 0o777)  # enable all perms
    os.unlink(file)


def testnet():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    for eachHost in ('deli', 'www'):
        try:
            myconnect(s, 'deli', 8080)
        except NetworkError as args:
            print("%s: %s" % (args.__class__.__name__, args))


if __name__ == '__main__':
    testfile()
    testnet()
