#!/usr/bin/python
# -*- coding:UTF-8 -*-

import tkinter

if __name__ == '__main__':
    top = tkinter.Tk()
    hello = tkinter.Label(top,text="Hello world!")
    hello.pack()
    quit = tkinter.Button(top, text='Hello world!', command=top.quit,bg='red',fg='white')
    quit.pack(fill=tkinter.X,expand=1)
    tkinter.mainloop()