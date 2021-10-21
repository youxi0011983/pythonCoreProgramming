#!/usr/bin/python
# -*- coding:UTF-8 -*-

from random import choice


class RandSeq(object):
    def __init__(self, seq):
        self.data = seq

    def __iter__(self):
        return self

    def __next__(self):
        return choice(self.data)