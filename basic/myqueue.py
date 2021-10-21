#!/usr/bin/python
# -*- coding:UTF-8 -*-

queue = []


def enQ():
    queue.append(input('Enter new string: ').strip())


def deQ():
    if len(queue) == 0:
        print('Cannot pop from an empty queue!')
    else:
        print('Removed[', repr(queue.pop()), ']')


def viewQ():
    print(queue)  # class str() internally


CMDs = {'e': enQ, 'd': deQ, 'v': viewQ}


def showmenu():
    pr = """
    (E)nqueue
    (D)equeue
    (V)iew
    (Q)uit
    
    Enter choice: """

    while True:
        while True:
            try:
                choice = input(pr).strip()[0].lower()
            except(EOFError, KeyboardInterrupt, IndexError) as e:
                choice = 'q'

            print("\nYou picked:[%s]" % choice)
            if choice not in 'devq':
                print('invalid option,try again')
            else:
                break
        if choice == 'q':
            break
        CMDs[choice]()


if __name__ == '__main__':
    showmenu()
