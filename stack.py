#!/usr/bin/python
# -*- coding:UTF-8 -*-

stack = []


def pushit():
    stack.append(input('Enter new string: ').strip())


def popit():
    if len(stack) == 0:
        print('Cannot pop from an empty stack!')
    else:
        print('Removed[', repr(stack.pop()), ']')


def viewstack():
    print(stack)  # class str() internally


CMDs = {'u': pushit, 'o': popit, 'v': viewstack}


def showmenu():
    pr = """
    p(U)sh
    p(O)p
    (V)iew
    (Q)uit
    
    Enter choice: """

    while True:
        while True:
            try:
                choice = input(pr).strip()[0].lower()
            except(EOFError, KeyboardInterrupt, IndexError) as e:
                choice = 'q'

            print("\nYou picked:[%s]"% choice)
            if choice not in 'uovq':
                print('invalid option,try again')
            else:
                break
        if choice == 'q':
            break
        CMDs[choice]()


if __name__ == '__main__':
    showmenu()
