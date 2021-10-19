#!/usr/bin/python
# -*- coding:UTF-8 -*-

import tkinter

if __name__ == '__main__':
    top = tkinter.Tk()
    # label = tkinter.Label(top,text="Hello world!")
    # label.pack()
    quit = tkinter.Button(top, text='Hello world!', command=top.quit())
    quit.pack()
    tkinter.mainloop()
