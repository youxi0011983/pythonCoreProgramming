#!/usr/bin/python
# -*- coding:UTF-8 -*-

db = {}


def newuser():
    prompt = 'login desired: '
    while True:
        name = input(prompt)
        if name in db.keys():
            prompt = 'name taken, try another: '
            continue
        else:
            break
    pwd = input('passwd: ')
    db[name] = pwd


def olduser():
    name = input('login: ')
    pwd = input('passwd: ')
    passwd = db.get(name)
    if passwd == pwd:
        print('Welcome back', name)
    else:
        print('login incorrect')


def viewuser():
    print(db)


def showmenu():
    prompt = """
    (N)ew User Login
    (E)xisting User Login
    (v)iew user and passwd
    (Q)uit
    Enter choice: """
    done = False
    while not done:
        chosen = False
        while not chosen:
            try:
                choice = input(prompt).strip()[0].lower()
            except (EOFError, KeyboardInterrupt) as e:
                choice = 'q'
            print('\nYou picked: [%s]' % choice)
            if choice not in 'neqv':
                print('invalid option, try again')
            else:
                chosen = True
        if choice == 'q': done = True
        if choice == 'n': newuser()
        if choice == 'e': olduser()
        if choice == 'v': viewuser()


if __name__ == '__main__':
    showmenu()
