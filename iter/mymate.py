#!/usr/bin/python
# -*- coding:UTF-8 -*-

from time import ctime

if __name__ == '__main__':
    print('*** Welcome to MetaClasses!')
    print('\tMetaclass declaration first.')


    class MetaC(type):
        def __init__(cls, name, bases, attrd):
            super(MetaC, cls).__init__(name, bases, attrd)
            print('*** Created class %r at: %s' % (name, ctime()))


    print('\tClass "Foo" declaration next.')


    class Foo(object):
        __metaclass__ = MetaC

        def __init__(self):
            print('*** Instantiated class %r at: %s' % (self.__class__.__name__, ctime()))


    print('\tClass "Foo" instantiation next.')
    f = Foo()
    print('\tDOME')
