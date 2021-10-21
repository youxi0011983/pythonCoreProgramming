#!/usr/bin/python
# -*- coding:UTF-8 -*-

def displayNumType(num):
    print(num, 'is')
    if isinstance(num, (int, float, complex)):
        print("a number of type: ", type(num).__name__)
    else:
        print("not a number at all!!!")


if __name__ == '__main__':
    displayNumType(-69)
    displayNumType(98.6)
    displayNumType(-5.2 + 1.9j)
    displayNumType('xxx')

    year = int(input("Enter year: "))
    if year % 4 == 0 and ( year % 100 != 0 or year % 400 == 0):
        print("%s is leap year" % year)
    else:
        print("%s is not leap year" % year)
